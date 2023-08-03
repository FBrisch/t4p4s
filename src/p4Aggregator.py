from hlir16.hlir_attrs import attrs_hdr_metadata_insts, attrs_top_level
from hlir16.hlirx_regroup import attrs_regroup_path_expressions, attrs_regroup_structs, regroup_attrs
from hlir16.p4node import P4Node, deep_copy
from parserCombiner import ParserCombiner
from rewrite_p4 import printHLIR


class P4Aggregator:
    def __init__(self,p4program1,p4program2):
        self.p4program1 = p4program1
        self.p4program2 = p4program2
        self.resultingProgram = deep_copy(p4program1)
    
    def run(self):
        printHLIR(self.p4program1)
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

        printHLIR(self.resultingProgram)
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
                if headerInstance.name != 'all_metadatas' and headerInstance.type.path.name ==header.name and not found:
                    newInstances.append(headerInstance)
                    found = True
        self.resultingProgram.header_instances.vec = newInstances

        
