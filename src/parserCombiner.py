from dataclasses import dataclass

from hlir16.p4node import deep_copy, deep_copy_with_details

@dataclass
class StateInParser:
    state1 : str 
    state2: str = None

class ParserCombiner:
    

    def __init__(self,parser1,parser2,header1,header2):
        self.parser1 = parser1
        self.parser2 = parser2
        self.headerDict1 = {}
        self.headerDict2 = {}
        self.stateDict1 = {}
        self.stateDict2 = {}
        self.headerNameTranslationDictionary = {}
        self.addedNodes = []
        for header in header1:
            self.headerDict1[header.name] = header
        for header in header2:
            self.headerDict2[header.name] = header
            
        for state in parser1.states:
            self.stateDict1[state.name] = state
        for state in parser2.states:
            self.stateDict2[state.name] = state
        
        self.resultingHeaders = []
        self.resultingStates = {}
    


    def runIteration(self):
        firstStateToIterate1 = self.stateDict1["start"]
        firstStateToIterate2 = self.stateDict2["start"]

        #self.resultingStates[self.parser1.states[0].name] = deep_copy(self.parser1.states[0])
        self.iterateOverStates(self.stateDict1["start"],self.stateDict2["start"])

        for state in self.parser1.states:
            if state.name in ["accept","reject"]:
                stateToInsert = deep_copy(state)
                self.resultingStates[state.name]= deep_copy(stateToInsert)
                self.resultingStates[state.name].Node_ID = stateToInsert.Node_ID
                self.addedNodes.append(stateToInsert)
        
        self.mergeMetadata()

        

    def iterateOverStates(self,state1,state2):
        if self.sumExtractedHeaderLength(state1) != self.sumExtractedHeaderLength(state2):
            print(f"could not combine states {state1.name} and {state2.name} due to extracted header width not matching({self.sumExtractedHeaderLength(state1)},{self.sumExtractedHeaderLength(state2)})")
            exit(1)
        if self.getExtractedHeader(state1) is not None:
            self.addedNodes.append(self.getExtractedHeader(state1))
            self.resultingHeaders.append(self.getExtractedHeader(state1))
            self.headerNameTranslationDictionary[self.getExtractedHeader(state2).name] = self.getExtractedHeader(state1).name
        
        mergedSelect,resultingSelectStatement = self.mergeSelects(state1.selectExpression,state2.selectExpression)

        for key,case in mergedSelect.items():
            if(case.state1 not in ["accept","reject"] and case.state2 not in ["accept","reject"]):
                if case.state1 == None:
                    self.addDistinctTree(case.state2,True)
                elif case.state2 == None:
                    self.addDistinctTree(case.state1,False)
                else:
                    self.iterateOverStates(self.stateDict1[case.state1],self.stateDict2[case.state2])
                    
            else:
                if(case.state1 != case.state2):
                    print("mismatch between accept/reject state and different state")
                    exit(-1)

        #assemble resulting select in state1 here
        #preliminary output
        #print(f"resulting state for {state1.name} and {state2.name}")
        #print(f"extracting {self.sumExtractedHeaderLength(state1)} bytes")
        #for key,case in mergedSelect.items():
        #   print(f"{key} - {case.state1},{case.state2}")
        #if resultingSelectStatement.node_type == "PathExpression":
        #    print("transition to " + resultingSelectStatement.path.name)
        #else:
        #    for case in resultingSelectStatement.selectCases:
        #        print(case < 3)
        resultingState = deep_copy(state1)
        resultingState.selectExpression = resultingSelectStatement
        self.resultingStates[resultingState.name]= deep_copy_with_details(resultingState)
        self.resultingStates[resultingState.name].Node_ID = resultingState.Node_ID
        self.addedNodes.append(self.resultingStates[resultingState.name])
        self.resultingStates[resultingState.name].is_skipped = False
        #hier koennen wir header name redirection machen, zumindest das dictionary muss hier gebaut werden
        

     
    def mergeSelects(self,selectStatement1,selectStatement2):

        selectDict = {}
        resultingSelectStatement = deep_copy(selectStatement1)
        #check if selects have same offset 
        if (selectStatement2.node_type != "PathExpression" and selectStatement1.node_type != "PathExpression"):
            if not selectStatement1.select.components[0].fld_ref.offset == selectStatement2.select.components[0].fld_ref.offset:
                print(f"couldnt combine select Statements, offset didnt match({selectStatement1.components[0].fld_ref.offset},{selectStatement2.components[0].fld_ref.offset})")
                exit(-1)
            #check if selects have same length
            if not selectStatement1.select.components[0].fld_ref.size == selectStatement2.select.components[0].fld_ref.size:
                print(f"couldnt combine select Statements, checked length didnt match({selectStatement1.components[0].fld_ref.size},{selectStatement2.components[0].fld_ref.size})")
                exit(-1)

        #merge select
        if selectStatement1.node_type == "PathExpression": # handle simple transitions without select
            selectDict[-1] = StateInParser(selectStatement1.path.name)
        else:
            for case in selectStatement1.selectCases:       #this only works with numbers for now
                if(case.keyset.node_type == 'DefaultExpression'):
                    selectDict[-1] = StateInParser(case.state.path.name)
                else:
                    selectDict[case.keyset.value] = StateInParser(case.state.path.name)
                    #self.resultingStates[case.state.path.name] = self.stateDict1[case.state.path.name]

        if selectStatement2.node_type == "PathExpression":
            if(-1 in selectDict):
                selectDict[-1].state2 = selectStatement2.path.name
            else:
                selectDict[-1] = StateInParser(selectStatement2.path.name)
        else:
            for case in selectStatement2.selectCases:
                if(case.keyset.node_type == 'DefaultExpression'):
                    selectDict[-1].state2 = case.state.path.name
                else:
                    if case.keyset.value not in selectDict:       #no collision between selects
                        selectDict[case.keyset.value] = StateInParser(None,case.state.path.name)
                        #selectStatement1.selectCases.add(case) #skip actual code manipulation for now
                        #self.resultingStates[case.state.path.name] = self.stateDict2[case.state.path.name]
                    else:
                        selectDict[case.keyset.value].state2 = case.state.path.name

        if resultingSelectStatement.node_type == "PathExpression" and len(selectDict) == 1:
            #both statements are simple transition, resulting statement can just be statement1
            return selectDict,resultingSelectStatement
        else:

            resultingSelectStatement.selectCases = deep_copy(selectStatement1.selectCases)
            resultingSelectStatement.selectCases.set_vec([]) 
            for key,value in selectDict.items():
                if key == -1:
                    if value.state1 != None:
                        resultingSelectStatement.selectCases.append(self.findSelectCase(selectStatement1,-1))
                    else:
                        resultingSelectStatement.selectCases.append(self.findSelectCase(selectStatement2,-1))
                elif value.state1 == None:
                    resultingSelectStatement.selectCases.append(self.findSelectCase(selectStatement2,key))
                elif value.state2 == None:
                    resultingSelectStatement.selectCases.append(self.findSelectCase(selectStatement1,key))
                else:
                    resultingSelectStatement.selectCases.append(self.findSelectCase(selectStatement1,key))

        return selectDict,resultingSelectStatement


    def addDistinctTree(self,statename, treeIsInTree2):
        currentState = {}

        if statename in ["accept","reject"]:
            return
        
        if treeIsInTree2:
            currentState = self.stateDict2[statename]
        else:
            currentState = self.stateDict1[statename]
        
        extractedHeader = self.getExtractedHeader(currentState)
        if extractedHeader is not None:
            self.addedNodes.append(extractedHeader)
            self.resultingHeaders.append(extractedHeader)
        self.resultingStates[statename] = deep_copy(currentState)
        self.resultingStates[statename].Node_ID = currentState.Node_ID
        self.addedNodes.append(self.resultingStates[statename])
        if currentState.selectExpression.node_type == "PathExpression":
            self.addDistinctTree(currentState.selectExpression.path.name,treeIsInTree2)
        else:
            for case in currentState.selectExpression.selectCases:
                self.addDistinctTree(case.state.path.name,treeIsInTree2)


    def sumExtractedHeaderLength(self,state):
        sumHeaderLength = 0
        stateComponents = state.components
        for comp in stateComponents:
            if(comp.node_type == 'MethodCallStatement' and comp.call == "extract_header"):
                sumHeaderLength += comp.header.byte_width
        return sumHeaderLength
    
    def getExtractedHeaderName(self,state):
         for comp in state.components:
            if(comp.call == "extract_header"):
                return comp.header.name


    def getExtractedHeader(self,state):
         for comp in state.components:
            if(comp.call == "extract_header"):
                return comp.header


    def findSelectCase(self,selectStatement,value):
        for case in selectStatement.selectCases:
                if(case.keyset.node_type == 'DefaultExpression'):
                    if value == -1:
                        return case
                else:
                    if case.keyset.value == value:       #no collision between selects
                       return case
        return None
    
    def mergeMetadata(self):
        metadatapresent = []
        metadata1 = self.headerDict1["all_metadatas_t"]
        metadata2 = self.headerDict2["all_metadatas_t"]
        resultingMetadata = self.headerDict1["all_metadatas_t"]


        for field in metadata1.fields:
            metadatapresent.append(field.name)

        for field in metadata2.fields:
            if field.name not in metadatapresent:
                resultingMetadata.fields.append(field)
                metadatapresent.append(field.name)
        self.addedNodes.append(resultingMetadata)
        self.resultingHeaders.append(resultingMetadata)