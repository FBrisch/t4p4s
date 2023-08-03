
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/common.h.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/common.h.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/common.h.py: via hardware_indep/common.h.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

generated_code += add_code(" // SPDX-License-Identifier: Apache-2.0", lineno = 1)
generated_code += add_code(" // Copyright 2019 Eotvos Lorand University, Budapest, Hungary", lineno = 2)

generated_code += add_code("")
from utils.codegen import format_type ## src/hardware_indep/common.h.py:5
from compiler_common import unique_everseen ## src/hardware_indep/common.h.py:6

generated_code += add_code("")
generated_code += add_code(" #pragma once", lineno = 7)

generated_code += add_code("")
generated_code += add_code(" #include <stdbool.h>", lineno = 9)
generated_code += add_code(" #include <stdint.h>", lineno = 10)
generated_code += add_code(" #include \"parser.h\"", lineno = 11)
generated_code += add_code(" #include \"stats.h\"", lineno = 12)

generated_code += add_code("")
generated_code += add_code(" #include \"dataplane.h\"", lineno = 14)
generated_code += add_code(" #include \"util_packet.h\"", lineno = 15)

generated_code += add_code("")
generated_code += add_code(" #define T4P4S_BROADCAST_PORT 100", lineno = 18)

generated_code += add_code("")
generated_code += add_code(' #define NB_TABLES {}'.format(len(hlir.tables)), lineno = 21)

generated_code += add_code("")
for typedef in hlir.typedefs: ## src/hardware_indep/common.h.py:25
    generated_code += add_code(' typedef {} {};'.format(format_type(typedef.type), typedef.name), lineno = 25)
generated_code += add_code("", lineno = 26)