
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/tables.h.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/tables.h.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/tables.h.py: via hardware_indep/tables.h.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

# SPDX-License-Identifier: Apache-2.0 ## src/hardware_indep/tables.h.py:2
# Copyright 2018 Eotvos Lorand University, Budapest, Hungary ## src/hardware_indep/tables.h.py:3

generated_code += add_code("")
generated_code += add_code(" #pragma once", lineno = 4)

generated_code += add_code("")
generated_code += add_code(" #include \"stateful_memory.h\"", lineno = 6)
generated_code += add_code(" #include \"actions.h\"", lineno = 7)

generated_code += add_code("")
generated_code += add_code(" #define ENTRY(tname)    tname ## _entry_t", lineno = 10)
generated_code += add_code(" #define ENTRYBASE       ENTRY(base_table)", lineno = 11)

generated_code += add_code("")
# Note: a table entry contains a (possibly invalid) action and a state ## src/hardware_indep/tables.h.py:15
#       the latter of which is not represented ## src/hardware_indep/tables.h.py:16
generated_code += add_code(" typedef base_table_action_t ENTRYBASE;", lineno = 16)
generated_code += add_code("", lineno = 17)

generated_code += add_code("")
for table in hlir.tables: ## src/hardware_indep/tables.h.py:21
    generated_code += add_code(" typedef struct {", lineno = 21)
    generated_code += add_code("     actions_e                     id;", indent_level = 1, lineno = 22)
    generated_code += add_code('     {}_action_params_t params;'.format(table.name), indent_level = 1, lineno = 23)
    generated_code += add_code(' }} ENTRY({});'.format(table.name), lineno = 24)
    generated_code += add_code("", lineno = 25)
generated_code += add_code(" typedef enum {", lineno = 28)
for table in hlir.tables: ## src/hardware_indep/tables.h.py:30
    generated_code += add_code('     TABLE_{},'.format(table.name), indent_level = 1, lineno = 30)
generated_code += add_code(" TABLE_,", indent_level = 1, lineno = 31)
generated_code += add_code(" } table_name_e;", lineno = 32)
generated_code += add_code("", lineno = 33)

generated_code += add_code("")
generated_code += add_code(" void exact_add_promote  (table_name_e tableid, uint8_t* key,                ENTRYBASE* entry, bool is_const_entry, bool should_print);", lineno = 36)
generated_code += add_code(" void lpm_add_promote    (table_name_e tableid, uint8_t* key, uint8_t depth, ENTRYBASE* entry, bool is_const_entry, bool should_print);", lineno = 37)
generated_code += add_code(" void ternary_add_promote(table_name_e tableid, uint8_t* key, uint8_t* mask, ENTRYBASE* entry, bool is_const_entry, bool should_print);", lineno = 38)
generated_code += add_code(" void table_setdefault_promote(table_name_e tableid, ENTRYBASE* entry, bool show_info);", lineno = 39)

generated_code += add_code("")
generated_code += add_code(" //=============================================================================", lineno = 41)

generated_code += add_code("")
generated_code += add_code(" // Computes the location of the validity field of the entry.", lineno = 43)
generated_code += add_code(" bool* entry_validity_ptr(ENTRYBASE* entry, lookup_table_t* t);", lineno = 44)
