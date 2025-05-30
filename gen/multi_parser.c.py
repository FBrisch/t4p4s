
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/multi_parser.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/multi_parser.c.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/multi_parser.c.py: via hardware_indep/multi_parser.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

# SPDX-License-Identifier: Apache-2.0 ## src/hardware_indep/multi_parser.c.py:2
# Copyright 2021 Eotvos Lorand University, Budapest, Hungary ## src/hardware_indep/multi_parser.c.py:3

generated_code += add_code("")
from compiler_log_warnings_errors import addWarning ## src/hardware_indep/multi_parser.c.py:5
from utils.codegen import to_c_bool ## src/hardware_indep/multi_parser.c.py:6

generated_code += add_code("")
part_count = compiler_common.current_compilation['multi'] ## src/hardware_indep/multi_parser.c.py:8

generated_code += add_code("")
all_hdrs = sorted(hlir.header_instances.filterfalse(lambda hdr: hdr.urtype.is_metadata), key=lambda hdr: len(hdr.urtype.fields)) ## src/hardware_indep/multi_parser.c.py:10

generated_code += add_code("")
generated_code += add_code(" #include \"parser_stages.h\"", lineno = 11)
generated_code += add_code(" #include \"hdr_fld.h\"", lineno = 12)
generated_code += add_code(" #include \"hdr_fld_sprintf.h\"", lineno = 13)

generated_code += add_code("")
for part_idx, hdr in enumerate(all_hdrs): ## src/hardware_indep/multi_parser.c.py:16
    multi_idx = part_idx % part_count ## src/hardware_indep/multi_parser.c.py:17
    generated_code += add_code(' #if T4P4S_MULTI_IDX == {}'.format(multi_idx), lineno = 17)
    generated_code += add_code(' void print_parsed_hdr_{}(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {{'.format(hdr.name), indent_level = 1, lineno = 19)
    generated_code += add_code("     #ifdef T4P4S_DEBUG", indent_level = 2, lineno = 20)
    generated_code += add_code("         char fields_txt[4096];", indent_level = 3, lineno = 21)
    generated_code += add_code("         if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);", indent_level = 3, lineno = 22)
    generated_code += add_code("         debug(\"   :: Parsed header\" T4LIT(#%d) \" \" T4LIT(%s,header) \"/\" T4LIT(%d) \"B%s%s\\n\",", indent_level = 3, lineno = 23)
    generated_code += add_code("               hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,", indent_level = 3, lineno = 24)
    generated_code += add_code("               hdr->size == 0 ? \"\" : \": \",", indent_level = 3, lineno = 25)
    generated_code += add_code("               hdr->size == 0 ? \"\" : fields_txt);", indent_level = 3, lineno = 26)
    generated_code += add_code("     #endif", indent_level = 2, lineno = 27)
    generated_code += add_code(" }", indent_level = 1, lineno = 28)
    generated_code += add_code(' #endif // T4P4S_MULTI_IDX == {}'.format(multi_idx), lineno = 29)
    generated_code += add_code("", lineno = 30)
for part_idx, hdr in enumerate(all_hdrs): ## src/hardware_indep/multi_parser.c.py:33
    multi_idx = part_idx % part_count ## src/hardware_indep/multi_parser.c.py:34
    generated_code += add_code(' #if T4P4S_MULTI_IDX == {}'.format(multi_idx), lineno = 34)
    generated_code += add_code(' int parser_extract_{}(int vwlen, STDPARAMS) {{'.format(hdr.name), indent_level = 1, lineno = 36)
    generated_code += add_code("     parser_state_t* local_vars = pstate;", indent_level = 2, lineno = 37)
    hdrtype = hdr.urtype ## src/hardware_indep/multi_parser.c.py:40
    is_vw = hdrtype.is_vw ## src/hardware_indep/multi_parser.c.py:41
    base_size = hdr.urtype.size ## src/hardware_indep/multi_parser.c.py:42
    is_stack = 'stack' in hdr and hdr.stack is not None ## src/hardware_indep/multi_parser.c.py:44
    if is_stack: ## src/hardware_indep/multi_parser.c.py:46
        generated_code += add_code('     stk_next(STK({}), pd);'.format(hdr.stack.name), indent_level = 2, lineno = 46)
        generated_code += add_code('     header_instance_e hdrinst = stk_current(STK({}), pd);'.format(hdr.stack.name), indent_level = 2, lineno = 47)
    else: ## src/hardware_indep/multi_parser.c.py:49
        generated_code += add_code('     header_instance_e hdrinst = HDR({});'.format(hdr.name), indent_level = 2, lineno = 49)
    generated_code += add_code("     header_descriptor_t* hdr = &(pd->headers[hdrinst]);", indent_level = 2, lineno = 50)
    generated_code += add_code('     hdr->was_enabled_at_initial_parse = {};'.format(to_c_bool(not hdr.is_skipped)), indent_level = 2, lineno = 52)
    generated_code += add_code('     hdr->size = ({} + vwlen) / 8;'.format(base_size), indent_level = 2, lineno = 53)
    if is_vw: ## src/hardware_indep/multi_parser.c.py:55
        generated_code += add_code("     hdr->vw_size = vwlen;", indent_level = 2, lineno = 55)
    generated_code += add_code("     if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {", indent_level = 2, lineno = 57)
    generated_code += add_code('         cannot_parse_hdr("{}", "{}", {}, vwlen, STDPARAMS_IN);'.format("variable width " if is_vw else "", hdr.name, base_size), indent_level = 3, lineno = 58)
    generated_code += add_code("         return PARSED_AFTER_END_OF_PACKET;", indent_level = 3, lineno = 59)
    generated_code += add_code("     }", indent_level = 2, lineno = 60)
    if hdr.is_skipped: ## src/hardware_indep/multi_parser.c.py:63
        generated_code += add_code("     hdr->pointer = NULL;", indent_level = 2, lineno = 63)
        skip_size = hdrtype.size ## src/hardware_indep/multi_parser.c.py:65
        skip_pad_txt = '' ## src/hardware_indep/multi_parser.c.py:66
        if hdrtype.size % 8 != 0: ## src/hardware_indep/multi_parser.c.py:67
            padded_skip_size = ((skip_size+7) // 8) * 8 ## src/hardware_indep/multi_parser.c.py:68
            addWarning('Skipping bits', f'Only byte aligned skipping is supported, {skip_size}b is padded to {padded_skip_size//8}B') ## src/hardware_indep/multi_parser.c.py:69
            skip_size = padded_skip_size ## src/hardware_indep/multi_parser.c.py:70
            skip_pad_txt = '"->" T4LIT()' ## src/hardware_indep/multi_parser.c.py:71
        generated_code += add_code('     if (unlikely(pd->parsed_size + {} > pd->wrapper->pkt_len)) {{'.format(skip_size//8), indent_level = 2, lineno = 71)
        generated_code += add_code('         debug("   " T4LIT(!!,error) " Tried to skip " T4LIT(<{}>,header) "/" T4LIT(%d) "B but it is over packet size\\n", {} / 8);'.format(hdrtype.name, skip_size), indent_level = 3, lineno = 72)
        generated_code += add_code("         return PARSED_AFTER_END_OF_PACKET;", indent_level = 3, lineno = 73)
        generated_code += add_code("     } else {", indent_level = 3, lineno = 74)
        generated_code += add_code('         debug("   :: Skipping " T4LIT(<{}>,header) "/" T4LIT(%d) "B\\n", {} / 8);'.format(hdrtype.name, skip_size), indent_level = 3, lineno = 75)
        generated_code += add_code("     }", indent_level = 2, lineno = 76)
        generated_code += add_code('     pd->parsed_size += {};'.format(skip_size//8), indent_level = 2, lineno = 78)
    else: ## src/hardware_indep/multi_parser.c.py:80
        generated_code += add_code("     hdr->pointer = pd->extract_ptr;", indent_level = 2, lineno = 80)
        for fld in hdrtype.fields: ## src/hardware_indep/multi_parser.c.py:83
            if fld.preparsed and fld.size <= 32: ## src/hardware_indep/multi_parser.c.py:84
                generated_code += add_code('     pd->fields.FLD(hdr,{}) = GET32(src_pkt(pd), FLD({}, {}));'.format(name, hdr.name, name), indent_level = 2, lineno = 84)
                generated_code += add_code('     pd->fields.ATTRFLD(hdr,{}) = NOT_MODIFIED;'.format(name), indent_level = 2, lineno = 85)
        generated_code += add_code('     print_parsed_hdr_{}(pd, hdr, hdrinst);'.format(hdr.name), indent_level = 2, lineno = 87)
        generated_code += add_code("     pd->parsed_size += hdr->size;", indent_level = 2, lineno = 89)
    generated_code += add_code("     pd->extract_ptr += hdr->size;", indent_level = 2, lineno = 91)
    if hdr.is_skipped: ## src/hardware_indep/multi_parser.c.py:94
        generated_code += add_code('     return 0; // {} is skipped'.format(hdr.name), indent_level = 2, lineno = 94)
    else: ## src/hardware_indep/multi_parser.c.py:96
        generated_code += add_code("     return hdr->size;", indent_level = 2, lineno = 96)
    generated_code += add_code(" }", indent_level = 1, lineno = 97)
    generated_code += add_code(' #endif // T4P4S_MULTI_IDX == {}'.format(multi_idx), lineno = 98)
    generated_code += add_code("", lineno = 99)
