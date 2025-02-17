
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/common_enums.h.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/common_enums.h.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/common_enums.h.py: via hardware_indep/common_enums.h.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

generated_code += add_code(" // SPDX-License-Identifier: Apache-2.0", lineno = 1)
generated_code += add_code(" // Copyright 2019 Eotvos Lorand University, Budapest, Hungary", lineno = 2)

generated_code += add_code("")
from utils.codegen import format_type ## src/hardware_indep/common_enums.h.py:5
from compiler_common import unique_everseen ## src/hardware_indep/common_enums.h.py:6

generated_code += add_code("")
generated_code += add_code(" #pragma once", lineno = 7)

generated_code += add_code("")
generated_code += add_code(" #include <stdbool.h>", lineno = 9)
generated_code += add_code(" #include <stdint.h>", lineno = 10)

generated_code += add_code("")
def short_name(name): ## src/hardware_indep/common_enums.h.py:13
    return name[:-2] if name.endswith('_t') else name ## src/hardware_indep/common_enums.h.py:14
for ee in hlir.errors + hlir.enums: ## src/hardware_indep/common_enums.h.py:17
    name = short_name(ee.c_name) ## src/hardware_indep/common_enums.h.py:18
    generated_code += add_code(' #define T4P4S_TYPE_{}'.format(name), lineno = 18)
for data in hlir.news.data: ## src/hardware_indep/common_enums.h.py:21
    generated_code += add_code(' #define T4P4S_TYPE_{}'.format(data.name), lineno = 21)
for ee in hlir.errors + hlir.enums: ## src/hardware_indep/common_enums.h.py:25
    kind = 'enum' if ee.node_type == 'Type_Enum' else 'error' ## src/hardware_indep/common_enums.h.py:26
    name = short_name(ee.c_name) ## src/hardware_indep/common_enums.h.py:27
    generated_code += add_code(" typedef enum {", lineno = 27)
    for m in ee.members: ## src/hardware_indep/common_enums.h.py:29
        generated_code += add_code('     {},'.format(m.c_name), indent_level = 1, lineno = 29)
    generated_code += add_code(' }} {}_t;'.format(name), lineno = 30)
    generated_code += add_code("", lineno = 31)
    generated_code += add_code(' extern const char* {}_value_names_{}[{}];'.format(kind, ee.name, len(ee.members)), lineno = 32)
    generated_code += add_code("", lineno = 33)
generated_code += add_code("", lineno = 34)
