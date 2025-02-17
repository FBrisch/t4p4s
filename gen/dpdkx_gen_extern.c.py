
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/dpdkx_gen_extern.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/dpdkx_gen_extern.c.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/dpdkx_gen_extern.c.py: via hardware_indep/dpdkx_gen_extern.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

# SPDX-License-Identifier: Apache-2.0 ## src/hardware_indep/dpdkx_gen_extern.c.py:2
# Copyright 2021 Eotvos Lorand University, Budapest, Hungary ## src/hardware_indep/dpdkx_gen_extern.c.py:3

generated_code += add_code("")
from utils.codegen import format_type, get_detailed_extern_callinfos ## src/hardware_indep/dpdkx_gen_extern.c.py:5
from utils.extern import extern_has_tuple_params ## src/hardware_indep/dpdkx_gen_extern.c.py:6
from compiler_common import generate_var_name, get_short_type ## src/hardware_indep/dpdkx_gen_extern.c.py:7
from more_itertools import unique_everseen ## src/hardware_indep/dpdkx_gen_extern.c.py:8

generated_code += add_code("")
generated_code += add_code(" #include \"dpdk_lib.h\"", lineno = 9)
generated_code += add_code(" #include \"util_debug.h\"", lineno = 10)
generated_code += add_code(" #include \"dpdkx_gen_extern.h\"", lineno = 11)

generated_code += add_code("")
detailed_callinfos = get_detailed_extern_callinfos(hlir) ## src/hardware_indep/dpdkx_gen_extern.c.py:15

generated_code += add_code("")
def get_externtype(part, partypeinfolen, partype_suffix, varname): ## src/hardware_indep/dpdkx_gen_extern.c.py:18
    return f'EXTERNTYPE{partypeinfolen}({part}{partype_suffix})* {varname}' ## src/hardware_indep/dpdkx_gen_extern.c.py:19
for partypeinfolen, mname_parts, partype_suffix, params, params_as_buf, ret, mname_postfix, mname_postfix_as_buf, args, args_as_buf, refvars, arginfos, parinfos in sorted(unique_everseen(detailed_callinfos, key=lambda c: c[0:3])): ## src/hardware_indep/dpdkx_gen_extern.c.py:22
    if len(mname_parts) == 1: ## src/hardware_indep/dpdkx_gen_extern.c.py:23
        call = f'SHORT_EXTERNCALL{partypeinfolen + len(mname_parts)-1}' ## src/hardware_indep/dpdkx_gen_extern.c.py:24
    else: ## src/hardware_indep/dpdkx_gen_extern.c.py:25
        call = f'EXTERNCALL{partypeinfolen + len(mname_parts)-2}' ## src/hardware_indep/dpdkx_gen_extern.c.py:26
        extern_type_name = f'' ## src/hardware_indep/dpdkx_gen_extern.c.py:27
        varname = generate_var_name('extern') ## src/hardware_indep/dpdkx_gen_extern.c.py:28
        externtype = get_externtype(mname_parts[0], partypeinfolen, partype_suffix, varname) ## src/hardware_indep/dpdkx_gen_extern.c.py:29
        params = f'{externtype}, {params}' ## src/hardware_indep/dpdkx_gen_extern.c.py:30
        args_as_buf = f'{varname}, ' + args_as_buf ## src/hardware_indep/dpdkx_gen_extern.c.py:31
    return_stmt = 'return ' if not ret.startswith('void') else '' ## src/hardware_indep/dpdkx_gen_extern.c.py:33
    generated_code += add_code(' {} {}({}{})({}) {{'.format(ret, call, ",".join(mname_parts), partype_suffix, params), lineno = 33)
    generated_code += add_code('     {}EXTERNIMPL{}({}{})({});'.format(return_stmt, partypeinfolen + len(mname_parts)-1, ",".join(mname_parts), mname_postfix_as_buf, args_as_buf), indent_level = 1, lineno = 35)
    generated_code += add_code(" }", lineno = 36)
    generated_code += add_code("", lineno = 37)
