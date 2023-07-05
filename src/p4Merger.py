from hlir16.hlir_attrs import attrs_hdr_metadata_insts
from hlir16.hlirx_regroup import regroup_attrs
from hlir16.p4node import P4Node, deep_copy
from parserCombiner import ParserCombiner


class P4Merger:
    def __init__(self,p4program1,p4program2):
        self.p4program1 = p4program1
        self.p4program2 = p4program2
        self.resultingProgram = deep_copy(p4program1)
    
    def run(self):
        parser1 = self.p4program1.parsers[0]
        parser2 = self.p4program2.parsers[0]
        headers1 = self.p4program1.headers
        headers2 = self.p4program2.headers
        combiner = ParserCombiner(parser1,parser2,headers1,headers2)
        combiner.runIteration()

        self.resultingProgram.parsers[0].states.vec = [f for f in combiner.resultingStates.values()]
        
        self.resultingProgram.headers.vec = combiner.resultingHeaders
        self.resultingProgram.header_instances.vec = combiner.resultingHeaders
        #regroup_attrs(self.resultingProgram)
        #attrs_hdr_metadata_insts(self.resultingProgram)
        #print(self.p4program2.parsers[0].states < 3)
        #print("--------------------------------------------")
        #print(self.resultingProgram.parsers[0].states < 3)
        #print(vec)

    def getResult(self):
        return self.resultingProgram
    
    def printParser(self):
        print("states")
        self.resultingProgram.parsers[0].states