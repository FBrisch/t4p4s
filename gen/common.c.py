
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/common.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/common.c.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/common.c.py: via hardware_indep/common.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

generated_code += add_code(" // SPDX-License-Identifier: Apache-2.0", lineno = 1)
generated_code += add_code(" // Copyright 2021 Eotvos Lorand University, Budapest, Hungary", lineno = 2)

generated_code += add_code("")
from utils.codegen import format_type ## src/hardware_indep/common.c.py:5

generated_code += add_code("")
generated_code += add_code(" #include \"common.h\"", lineno = 6)
generated_code += add_code(" #include \"util_debug.h\"", lineno = 7)
generated_code += add_code("", lineno = 8)

generated_code += add_code("")
generated_code += add_code(" void do_assignment(header_instance_e dst_hdr, header_instance_e src_hdr, SHORT_STDPARAMS) {", lineno = 10)
generated_code += add_code("     if (likely(is_header_valid(src_hdr, pd))) {", indent_level = 1, lineno = 11)
generated_code += add_code("         if (unlikely(!is_header_valid(dst_hdr, pd))) {", indent_level = 2, lineno = 12)
generated_code += add_code("             activate_hdr(dst_hdr, pd);", indent_level = 3, lineno = 13)
generated_code += add_code("         }", indent_level = 2, lineno = 14)
generated_code += add_code("         int copy_len = hdr_infos[src_hdr].byte_width + pd->headers[src_hdr].vw_size / 8;", indent_level = 2, lineno = 15)
generated_code += add_code("         memcpy(pd->headers[dst_hdr].pointer, pd->headers[src_hdr].pointer, copy_len);", indent_level = 2, lineno = 16)
generated_code += add_code("         dbg_bytes(pd->headers[dst_hdr].pointer, copy_len, \"    \" T4LIT(=,field) \" Set \" T4LIT(%s,header) \"/\" T4LIT(%dB) \" = \" T4LIT(%s,header) \" = \",", indent_level = 2, lineno = 17)
generated_code += add_code("                   hdr_infos[dst_hdr].name, hdr_infos[src_hdr].byte_width, hdr_infos[src_hdr].name);", indent_level = 2, lineno = 18)
generated_code += add_code("     } else {", indent_level = 2, lineno = 19)
generated_code += add_code("         debug(\"    \" T4LIT(=,status) \" Set header \" T4LIT(%s,header) \"/\" T4LIT(%dB) \" = \" T4LIT(invalid,status) \" from \" T4LIT(%s,header) \"/\" T4LIT(%dB) \"\\n\",", indent_level = 2, lineno = 20)
generated_code += add_code("               hdr_infos[dst_hdr].name, hdr_infos[dst_hdr].byte_width, hdr_infos[src_hdr].name, hdr_infos[src_hdr].byte_width);", indent_level = 2, lineno = 21)
generated_code += add_code("         deactivate_hdr(dst_hdr, pd);", indent_level = 2, lineno = 22)
generated_code += add_code("     }", indent_level = 1, lineno = 23)
generated_code += add_code(" }", lineno = 24)
generated_code += add_code("", lineno = 25)

generated_code += add_code("")
generated_code += add_code(" void debug_validity_info_msg(bool is_valid, const uint8_t*const ptr, header_instance_e hdr, SHORT_STDPARAMS) {", lineno = 27)
generated_code += add_code("     bool is_ok = is_header_valid(hdr, pd) == is_valid;", indent_level = 1, lineno = 28)
generated_code += add_code("     const char* status_txt = is_valid ? T4LIT(valid,success) : T4LIT(invalid,status);", indent_level = 1, lineno = 29)
generated_code += add_code("     if (is_ok) {", indent_level = 1, lineno = 30)
generated_code += add_code("        debug(\"   :: Set header \" T4LIT(%s,header) \"/\" T4LIT(%d) \"+\" T4LIT(%d) \"B = %s\\n\",", indent_level = 2, lineno = 31)
generated_code += add_code("              hdr_infos[hdr].name, pd->headers[hdr].size, pd->headers[hdr].vw_size/8, status_txt);", indent_level = 2, lineno = 32)
generated_code += add_code("     } else {", indent_level = 2, lineno = 33)
generated_code += add_code("        debug(\"   \" T4LIT(!!,warning) \" Trying to set header \" T4LIT(%s,header) \" to %s but it is already %s\\n\", hdr_infos[hdr].name, status_txt, status_txt);", indent_level = 2, lineno = 34)
generated_code += add_code("     }", indent_level = 1, lineno = 35)
generated_code += add_code(" }", lineno = 36)
generated_code += add_code("", lineno = 37)

generated_code += add_code("")
generated_code += add_code(" void set_hdr_valid(header_instance_e hdr, SHORT_STDPARAMS) {", lineno = 40)
generated_code += add_code("     if (likely(!is_header_valid(hdr, pd))) {", indent_level = 1, lineno = 41)
generated_code += add_code("        activate_hdr(hdr, pd);", indent_level = 2, lineno = 42)
generated_code += add_code("        pd->is_deparse_reordering = true;", indent_level = 2, lineno = 43)
generated_code += add_code("     }", indent_level = 1, lineno = 44)
generated_code += add_code("     debug_validity_info_msg(true, pd->headers[hdr].pointer, hdr, SHORT_STDPARAMS_IN);", indent_level = 1, lineno = 45)
generated_code += add_code(" }", lineno = 46)
generated_code += add_code("", lineno = 47)

generated_code += add_code("")
generated_code += add_code(" void set_hdr_invalid(header_instance_e hdr, SHORT_STDPARAMS) {", lineno = 49)
generated_code += add_code("     if (likely(is_header_valid(hdr, pd))) {", indent_level = 1, lineno = 50)
generated_code += add_code("        pd->headers[hdr].pointer = NULL;", indent_level = 2, lineno = 51)
generated_code += add_code("        pd->is_deparse_reordering = true;", indent_level = 2, lineno = 52)
generated_code += add_code("     }", indent_level = 1, lineno = 53)
generated_code += add_code("     debug_validity_info_msg(false, pd->headers[hdr].pointer, hdr, SHORT_STDPARAMS_IN);", indent_level = 1, lineno = 54)
generated_code += add_code(" }", lineno = 55)
generated_code += add_code("", lineno = 56)

generated_code += add_code("")
def remove_prefix(txt, prefix): ## src/hardware_indep/common.c.py:60
    return txt[len(prefix):] if txt.startswith(prefix) else txt ## src/hardware_indep/common.c.py:61
def remove_suffix(txt, suffix): ## src/hardware_indep/common.c.py:63
    return txt[:-len(suffix)] if txt.endswith(suffix) else txt ## src/hardware_indep/common.c.py:64
def short_name(name): ## src/hardware_indep/common.c.py:66
    return remove_suffix(name, '_t') ## src/hardware_indep/common.c.py:67
for ee in hlir.errors + hlir.enums: ## src/hardware_indep/common.c.py:69
    kind = 'enum' if ee.node_type == 'Type_Enum' else 'error' ## src/hardware_indep/common.c.py:70
    name = short_name(ee.c_name) ## src/hardware_indep/common.c.py:71
    generated_code += add_code(' const char* {}_value_names_{}[{}] = {{'.format(kind, ee.name, len(ee.members)), lineno = 71)
    for m in ee.members: ## src/hardware_indep/common.c.py:73
        name = remove_prefix(m.c_name, f'{kind}_{ee.name}_') ## src/hardware_indep/common.c.py:74
        generated_code += add_code('     "{}",'.format(name), indent_level = 1, lineno = 74)
    generated_code += add_code(" };", lineno = 75)
    generated_code += add_code("", lineno = 76)
generated_code += add_code("", lineno = 77)
