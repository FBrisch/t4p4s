
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/dataplane_table_default_entry.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/dataplane_table_default_entry.c.py:"):
    global generated_code

    line_ends = {
        "line_comment": "\n",
        "inline_comment": "",
        "no_comment": "\n",
        "no_comment_inline": "",
    }

    sugar_style = compiler_common.file_sugar_style[-1]

    stripped_line = line.strip()
    no_sugar_on_line = stripped_line.startswith('//') or stripped_line.startswith('# ') or stripped_line == ""

    indent = compiler_common.file_indent_str * indent_level
    if 'inline' in compiler_common.file_sugar_style[-1]:
        indent = ''

    sugared = sugar(no_sugar_on_line, file, lineno, sugar_style)
    line_end = line_ends[sugar_style]
    return f'{indent}{stripped_line}{sugared}{line_end}'


def sugar(no_sugar_on_line, file, lineno, sugar_style):
    if True or no_sugar_on_line or file is None or lineno is None:
        return ""

    if sugar_style == 'line_comment':
        return f" // {file}{lineno}"
    if sugar_style == 'inline_comment':
        return f" /* {file}{lineno} */"
    return ""


generated_code += "// Autogenerated file (from src/hardware_indep/dataplane_table_default_entry.c.py: via hardware_indep/dataplane_table_default_entry.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

# SPDX-License-Identifier: Apache-2.0 ## src/hardware_indep/dataplane_table_default_entry.c.py:2
# Copyright 2016 Eotvos Lorand University, Budapest, Hungary ## src/hardware_indep/dataplane_table_default_entry.c.py:3

generated_code += add_code("")
from utils.codegen import format_declaration, format_statement, format_expr, format_type, gen_format_type, get_method_call_env ## src/hardware_indep/dataplane_table_default_entry.c.py:5
from compiler_log_warnings_errors import addError, addWarning ## src/hardware_indep/dataplane_table_default_entry.c.py:6
from compiler_common import types, generate_var_name, get_hdrfld_name, unique_everseen ## src/hardware_indep/dataplane_table_default_entry.c.py:7

generated_code += add_code("")
generated_code += add_code(" #include \"gen_include.h\"", lineno = 8)
generated_code += add_code(" #include \"dataplane_impl.h\"", lineno = 9)

generated_code += add_code("")
table_infos = [(table, table.short_name + ("/keyless" if table.key_bit_size == 0 else "") + ("/hidden" if table.is_hidden else "")) for table in hlir.tables] ## src/hardware_indep/dataplane_table_default_entry.c.py:12

generated_code += add_code("")
for table, table_info in table_infos: ## src/hardware_indep/dataplane_table_default_entry.c.py:14
    # note: default_val is set properly only on lcore 0 on each socket ## src/hardware_indep/dataplane_table_default_entry.c.py:15
    generated_code += add_code(' ENTRY({})* {}_get_default_entry(STDPARAMS) {{'.format(table.name, table.name), lineno = 15)
    generated_code += add_code('     return (ENTRY({})*)tables[TABLE_{}][0].default_val;'.format(table.name, table.name), indent_level = 1, lineno = 16)
    generated_code += add_code(" }", lineno = 17)
    generated_code += add_code("", lineno = 18)
