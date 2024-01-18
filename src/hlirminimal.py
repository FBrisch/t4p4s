
from compiler_load_p4 import load_from_p4, load_hlir


filename='basic_part1withMods.p4'
cache_dir_name='t4p4s/cache'

testCompilerArgs = {'p4_file': filename,
                    'multi': 2, 'p4v': 16, 'p4c_path': None,
                    'compiler_files_dir': 't4p4s/src/hardware_indep',
                    'generated_dir': 'srcgen',
                    'desugar_info': 'comment',
                    'verbose': False,
                    'hint': ['nohint'],
                    'recompile': True,
                    'beautify': False,
                    'use_real_random': False,
                    'p4dbg': False,
                    'p4opt': [],
                    'p4incdir':[],'filename':filename}

hlir = load_from_p4(testCompilerArgs, cache_dir_name)
print("p4:")
print('NF1_meter.read(meterValue);')
print("hlir")
print(hlir.controls.vec[1].body.components.vec[1].ifTrue.components.vec[0])

print('---------------------')
print('this looks like a table apply:')
print(hlir.controls.vec[1].body.components.vec[1].ifTrue.components.vec[0].methodCall.method)

print('output for meter calls:')
