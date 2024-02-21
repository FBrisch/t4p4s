from hlir16.hlir_attrs import attrs_hdr_metadata_insts, attrs_top_level
from hlir16.hlirx_regroup import attrs_regroup_path_expressions, attrs_regroup_structs, regroup_attrs
from hlir16.p4node import P4Node, deep_copy
from parserCombiner import ParserCombiner
from rewrite_p4 import printHLIR
from filemod import writer

class P4Aggregator:

    prefix1 = "NF1_"
    prefix2 = "NF2_"
    def __init__(self,p4program1,p4program2,p4inject):
        self.p4program1 = p4program1
        self.p4program2 = p4program2
        self.p4inject = p4inject
        self.resultingProgram = deep_copy(p4program1)
    
    def run(self):
        parser1 = self.p4program1.parsers[0]
        parser2 = self.p4program2.parsers[0]
        headers1 = self.p4program1.headers
        headers2 = self.p4program2.headers
        combiner = ParserCombiner(parser1,parser2,headers1,headers2)
        combiner.runIteration()
        for node in combiner.addedNodes:
            self.addNodeToAllNodes(node)

        self.resultingProgram.parsers[0].states.vec = [f for f in combiner.resultingStates.values()]
        
        self.resultingProgram.headers.vec = combiner.resultingHeaders
        for header in self.resultingProgram.headers.vec:
            header.is_skipped = False
            header.is_local = False
        self.mergeHeaderInstances(combiner.resultingHeaders)


        #newMetadata = self.mergeMetadata(next(x for x in self.p4program1.headers if x.name == 'all_metadatas_t'),next(x for x in self.p4program2.headers if x.name == 'all_metadatas_t'))
        #self.resultingProgram.headers.vec.append(newMetadata)
        #self.resultingProgram.header_instances.vec.append(newMetadata)

        newControls = []

        for control1 in self.p4program1.controls:
            for control2 in self.p4program2.controls:
                if control1.name == control2.name:
                    newControls.append(self.mergeControl(control1,control2,combiner.headerNameTranslationDictionary))
        self.resultingProgram.controls.vec = newControls    
        

        #writer("output.p4",printHLIR(self.resultingProgram),method="w")
        #self.resultingProgram.header_instances.vec = combiner.resultingHeaders
        
        #self.resultingProgram.groups.pathexprs.append(self.p4program2.groups.pathexprs)
        #attrs_top_level(self.resultingProgram,"test","test")
        #regroup_attrs(self.resultingProgram)
        #attrs_regroup_path_expressions(self.resultingProgram)
        #attrs_hdr_metadata_insts(self.resultingProgram)
        #attrs_regroup_structs(self.resultingProgram)
        #print(self.p4program2.parsers[0].states < 3)
        #print("--------------------------------------------")
        #print(self.resultingProgram.parsers[0].states < 3)
        #print(vec)

    def getResult(self):
        return self.resultingProgram
    
    def printParser(self):
        print("states")
        self.resultingProgram.parsers[0].states

    def addNodeToAllNodes(self,node):
        self.resultingProgram.all_nodes.vec.append(node)
        for node2 in self.p4program2.all_nodes:
            if node in node2.node_parents:
                self.resultingProgram.all_nodes.vec.append(node)

    def mergeHeaderInstances(self,headers):
        newInstances = []
        
        for header in headers:
            found = False
            for headerInstance in self.p4program1.header_instances.vec + self.p4program2.header_instances.vec:
                if headerInstance.name != 'all_metadatas' and headerInstance.type.path.name == header.name and not found:
                    
                    newInstances.append(headerInstance)
                    found = True
        self.resultingProgram.header_instances.vec = newInstances

    def mergeControl(self,control1,control2,headers):
        IngressNames = ['MyIngress']
        DeparserNames = ['DeparserImpl','MyDeparser']
        newControl1 = control1.body
        newControl2 = control2.body
        resultingControl = deep_copy(control1)
        index1 = 0
        index2 = 0
        if control1.name in DeparserNames:
            # resultComponents = []
            # for header2,header1 in headers.items():
            #     while index2 < len(control2.body.components.vec) and control2.body.components[index2].methodCall.arguments[0].expression.type.name != header2:
            #         resultComponents.append(control2.body.components[index2])
            #         index2 = index2 + 1
            #     index2 = index2 + 1
            #     while index1 < len(control1.body.components.vec) and control1.body.components[index1].methodCall.arguments[0].expression.type.name != header1:
            #         resultComponents.append(control1.body.components[index1])
            #         index1 = index1 + 1
            #     resultComponents.append(control1.body.components[index1])
            #     index1 = index1 + 1
            # while index2 < len(control2.body.components.vec):
            #     resultComponents.append(control2.body.components[index2])
            #     index2 = index2 + 1
            # while index1 < len(control1.body.components.vec):
            #     resultComponents.append(control1.body.components[index1])
            #     index1 = index1 + 1
            # resultingControl.body.components = resultComponents
            print('Deparser')
        
        else:
            for decl in resultingControl.controlLocals:
                if decl.node_type == "Declaration_Variable":
                    decl.name = self.prefix1 + decl.name
            for action in resultingControl.actions:
                action.name = self.prefix1 + action.name


            for table in resultingControl.tables:
                table.short_name = self.prefix1 + table.short_name
            if control1.name in IngressNames:
                resultingControl.tables.append(self.p4inject.controls[1].tables[0])
            for decl in control2.controlLocals:
                if decl.node_type == "Declaration_Variable":
                    decl.name = self.prefix2 + decl.name
                    resultingControl.controlLocals.append(decl)
            if control1.name in IngressNames:
                resultingControl.controlLocals = resultingControl.controlLocals + [self.p4inject.controls[1].controlLocals[0],self.p4inject.controls[1].controlLocals[4],self.p4inject.controls[1].controlLocals[5],self.p4inject.controls[1].controlLocals[6]]
            for action in control2.actions:
                    action.name = self.prefix2 + action.name
                    resultingControl.actions.append(action)
            if control1.name in IngressNames:
                resultingControl.actions = resultingControl.actions + [self.p4inject.controls[1].actions[3],self.p4inject.controls[1].actions[4],self.p4inject.controls[1].actions[5],self.p4inject.controls[1].actions[6]]
                
            for table in control2.tables:
                table.short_name = self.prefix2 + table.short_name
                resultingControl.tables.append(table)
            #for controlBlock in control2.body.components:
                #controlBlock.name == self.prefix2 + controlBlock.name
                #resultingControl.body.components.append(controlBlock)
            
            if control1.name in IngressNames:
                newControl = self.p4inject.controls[1].body.components.vec
                newControl[0].ifTrue.components[1].ifTrue.components[1].ifTrue =  P4Node(init={
                                    'node_type' : 'BlockStatement',
                                    'components' : P4Node({
                                        'node_type':'Array'
                                    },vec=[newControl[0].ifTrue.components[1].ifTrue.components[1].ifTrue] + newControl1.components.vec )})
                newControl[0].ifTrue.components[1].ifFalse.components[1].ifTrue =  P4Node(init={
                                    'node_type' : 'BlockStatement',
                                    'components' : P4Node({
                                        'node_type':'Array'
                                    },vec=[newControl[0].ifTrue.components[1].ifFalse.components[1].ifTrue] + newControl2.components.vec )})
                resultingControl.body.components.vec = [P4Node(init={
                    'node_type' : 'BlockStatement',
                    'components' : P4Node({
                        'node_type':'Array'
                    },vec=newControl)
                        })]
        return resultingControl
        
    def mergeMetadata(self,metadata1,metadata2):
        newMetadata = []
        for data in metadata1.fields:
            if not any(ele.name == data.name for ele in newMetadata):
                newMetadata.append(data)
        for data in metadata2.fields:
            if not any(ele.name == data.name for ele in newMetadata):
                newMetadata.append(data)
        metadata1.fields.vec = newMetadata
        return metadata1
