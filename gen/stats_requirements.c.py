
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/stats_requirements.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/stats_requirements.c.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/stats_requirements.c.py: via hardware_indep/stats_requirements.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

generated_code += add_code(" // SPDX-License-Identifier: Apache-2.0", lineno = 1)
generated_code += add_code(" // Copyright 2021 Eotvos Lorand University, Budapest, Hungary", lineno = 2)

generated_code += add_code("")
generated_code += add_code(" #include <string.h>", lineno = 4)

generated_code += add_code("")
generated_code += add_code(" #include \"common.h\"", lineno = 6)
generated_code += add_code(" #include \"dpdk_lib.h\"", lineno = 7)

generated_code += add_code("")
generated_code += add_code(" #ifndef T4P4S_STATS", lineno = 10)
generated_code += add_code(" #else", indent_level = 1, lineno = 11)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" extern t4p4s_stats_t t4p4s_stats_per_packet;", indent_level = 1, lineno = 13)

generated_code += add_code("", indent_level = 1)
reqconds = 'apply hit miss cond run parse NONE ERROR'.split(' ') ## src/hardware_indep/stats_requirements.c.py:17

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" typedef enum {", indent_level = 1, lineno = 18)
for cond in reqconds: ## src/hardware_indep/stats_requirements.c.py:20
    generated_code += add_code('     reqcond_{},'.format(cond), indent_level = 2, lineno = 20)
generated_code += add_code(" } reqcond_e;", indent_level = 1, lineno = 21)
generated_code += add_code("", indent_level = 1, lineno = 22)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" reqcond_e get_reqcond(const char* name) {", indent_level = 1, lineno = 24)
for cond in reqconds: ## src/hardware_indep/stats_requirements.c.py:26
    generated_code += add_code('     if (!strcmp("{}", name))    return reqcond_{};'.format(cond, cond), indent_level = 2, lineno = 26)
generated_code += add_code("     return reqcond_ERROR;", indent_level = 2, lineno = 27)
generated_code += add_code(" };", indent_level = 1, lineno = 28)
generated_code += add_code("", indent_level = 1, lineno = 29)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" const char* get_reqcond_txt(reqcond_e reqcond) {", indent_level = 1, lineno = 32)
for cond in reqconds: ## src/hardware_indep/stats_requirements.c.py:34
    generated_code += add_code('     if (reqcond_{} == reqcond)    return "{}";'.format(cond, cond), indent_level = 2, lineno = 34)
generated_code += add_code("     return \"unreachable code\";", indent_level = 2, lineno = 35)
generated_code += add_code(" };", indent_level = 1, lineno = 36)
generated_code += add_code("", indent_level = 1, lineno = 37)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" #define MAX_PART_COUNT 128", indent_level = 1, lineno = 40)
generated_code += add_code("", indent_level = 1, lineno = 41)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" const char*const prefix_skip_char(const char*const txt, char c) {", indent_level = 1, lineno = 43)
generated_code += add_code("     const char* ptr = txt;", indent_level = 2, lineno = 44)
generated_code += add_code("     while (*ptr == c)  ++ptr;", indent_level = 2, lineno = 45)
generated_code += add_code("     return ptr;", indent_level = 2, lineno = 46)
generated_code += add_code(" }", indent_level = 1, lineno = 47)
generated_code += add_code("", indent_level = 1, lineno = 48)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" int split(char* parts[MAX_PART_COUNT], const char* reqs, const char* separator) {", indent_level = 1, lineno = 50)
generated_code += add_code("     int count = 0;", indent_level = 2, lineno = 51)
generated_code += add_code("     char* tmp = strdup(reqs);", indent_level = 2, lineno = 52)
generated_code += add_code("     while ( (parts[count] = strsep(&tmp,separator)) != NULL )  ++count;", indent_level = 2, lineno = 53)
generated_code += add_code("     free(tmp);", indent_level = 2, lineno = 54)
generated_code += add_code("     return count;", indent_level = 2, lineno = 55)
generated_code += add_code(" }", indent_level = 1, lineno = 56)
generated_code += add_code("", indent_level = 1, lineno = 57)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" bool check_table_name(const char*const table_name) {", indent_level = 1, lineno = 60)
for table in hlir.tables: ## src/hardware_indep/stats_requirements.c.py:62
    generated_code += add_code('     if (!strcmp("{}", table_name))    return true;'.format(table.short_name), indent_level = 2, lineno = 62)
generated_code += add_code("     return false;", indent_level = 2, lineno = 63)
generated_code += add_code(" }", indent_level = 1, lineno = 64)
generated_code += add_code("", indent_level = 1, lineno = 65)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" bool check_table_requirement(const char*const table_name, reqcond_e reqcond, bool on) {", indent_level = 1, lineno = 68)
generated_code += add_code("     t4p4s_stats_t stat = t4p4s_stats_per_packet;", indent_level = 2, lineno = 69)
for table in hlir.tables: ## src/hardware_indep/stats_requirements.c.py:71
    name = table.name ## src/hardware_indep/stats_requirements.c.py:72
    sname = table.short_name ## src/hardware_indep/stats_requirements.c.py:73
    conds = 'apply' + (' hit miss' if 'key' in table else ' used') ## src/hardware_indep/stats_requirements.c.py:75
    for cond in conds.split(' '): ## src/hardware_indep/stats_requirements.c.py:76
        generated_code += add_code('     if (!strcmp("{}", table_name) && reqcond == reqcond_{} && (on == stat.T4STAT(table,{},{})))   return true;'.format(sname, cond, cond, name), indent_level = 2, lineno = 76)
generated_code += add_code("     return false;", indent_level = 2, lineno = 77)
generated_code += add_code(" }", indent_level = 1, lineno = 78)
generated_code += add_code("", indent_level = 1, lineno = 79)

generated_code += add_code("", indent_level = 1)
# TODO ## src/hardware_indep/stats_requirements.c.py:82
generated_code += add_code(" bool check_action_requirement(const char*const table_name, reqcond_e reqcond, bool on) {", indent_level = 1, lineno = 82)
generated_code += add_code("     return false;", indent_level = 2, lineno = 83)
generated_code += add_code(" }", indent_level = 1, lineno = 84)
generated_code += add_code("", indent_level = 1, lineno = 85)

generated_code += add_code("", indent_level = 1)
# TODO ## src/hardware_indep/stats_requirements.c.py:88
generated_code += add_code(" bool check_parser_requirement(const char*const table_name, reqcond_e reqcond, bool on) {", indent_level = 1, lineno = 88)
generated_code += add_code("     return false;", indent_level = 2, lineno = 89)
generated_code += add_code(" }", indent_level = 1, lineno = 90)
generated_code += add_code("", indent_level = 1, lineno = 91)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" bool check_cond(const char*const cond) {", indent_level = 1, lineno = 94)
generated_code += add_code("     const char*const ltrimmed_cond = prefix_skip_char(cond, ' ');", indent_level = 2, lineno = 95)
generated_code += add_code("     bool on = true;", indent_level = 2, lineno = 96)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     bool result = true;", indent_level = 2, lineno = 98)
generated_code += add_code("     reqcond_e reqcond = reqcond_NONE;", indent_level = 2, lineno = 99)
generated_code += add_code("     char* parts[MAX_PART_COUNT];", indent_level = 2, lineno = 100)
generated_code += add_code("     int part_count = split(parts, cond, \" \");", indent_level = 2, lineno = 101)
generated_code += add_code("     for (int i = 0; i < part_count; ++i) {", indent_level = 2, lineno = 102)
generated_code += add_code("         if (strlen(parts[i]) == 0)    continue;", indent_level = 2, lineno = 103)
for cond in reqconds: ## src/hardware_indep/stats_requirements.c.py:105
    generated_code += add_code('         if (!strcmp("{}", parts[i])) {{'.format(cond), indent_level = 2, lineno = 105)
    generated_code += add_code("             if (reqcond != reqcond_NONE) {", indent_level = 3, lineno = 106)
    generated_code += add_code('                 debug("    " T4LIT(!,warning) " More than one requirement (" T4LIT({},warning) " and " T4LIT(%s,warning) ") found in condition " T4LIT(%s,warning) "\\n",'.format(cond), indent_level = 4, lineno = 107)
    generated_code += add_code("                       parts[i], ltrimmed_cond);", indent_level = 4, lineno = 108)
    generated_code += add_code("                 result = false;", indent_level = 4, lineno = 109)
    generated_code += add_code("                 goto free_mem; // breaking out of outermost loop", indent_level = 4, lineno = 110)
    generated_code += add_code("             }", indent_level = 3, lineno = 111)
    generated_code += add_code("             reqcond = get_reqcond(parts[i]);", indent_level = 3, lineno = 112)
    generated_code += add_code("             continue;", indent_level = 3, lineno = 113)
    generated_code += add_code("         }", indent_level = 2, lineno = 114)
generated_code += add_code("         if (!strcmp(\"not\", parts[i])) {", indent_level = 2, lineno = 116)
generated_code += add_code("             if (!on) {", indent_level = 3, lineno = 117)
generated_code += add_code("                 debug(\"    \" T4LIT(!,warning) \" Condition contains multiple negation: \" T4LIT(%s,warning) \"\\n\", ltrimmed_cond);", indent_level = 4, lineno = 118)
generated_code += add_code("                 result = false;", indent_level = 4, lineno = 119)
generated_code += add_code("                 goto free_mem; // breaking out of outermost loop", indent_level = 4, lineno = 120)
generated_code += add_code("             }", indent_level = 3, lineno = 121)
generated_code += add_code("             on = false;", indent_level = 3, lineno = 122)
generated_code += add_code("             continue;", indent_level = 3, lineno = 123)
generated_code += add_code("         }", indent_level = 2, lineno = 124)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         // we have found a table name", indent_level = 2, lineno = 126)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         if (reqcond == reqcond_NONE) {", indent_level = 2, lineno = 128)
generated_code += add_code("             debug(\"    \" T4LIT(!,warning) \" Table \" T4LIT(%s,table) \" found, but no check (e.g. \" T4LIT(hit) \") given in condition \" T4LIT(%s,warning) \"\\n\", parts[i], ltrimmed_cond);", indent_level = 3, lineno = 129)
generated_code += add_code("             result = false;", indent_level = 3, lineno = 130)
generated_code += add_code("             goto free_mem; // breaking out of outermost loop", indent_level = 3, lineno = 131)
generated_code += add_code("         }", indent_level = 2, lineno = 132)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         result &= check_table_name(parts[i]);", indent_level = 2, lineno = 134)
generated_code += add_code("         if (!result) {", indent_level = 2, lineno = 135)
generated_code += add_code("             debug(\"    \" T4LIT(!,warning) \" Nonexistent table \" T4LIT(%s,table) \" given in condition \" T4LIT(%s,warning) \"\\n\", parts[i], ltrimmed_cond);", indent_level = 3, lineno = 136)
generated_code += add_code("             result = false;", indent_level = 3, lineno = 137)
generated_code += add_code("             goto free_mem; // breaking out of outermost loop", indent_level = 3, lineno = 138)
generated_code += add_code("         }", indent_level = 2, lineno = 139)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         result &= check_table_requirement(parts[i], reqcond, on);", indent_level = 2, lineno = 141)
generated_code += add_code("         if (!result) {", indent_level = 2, lineno = 142)
generated_code += add_code("             debug(\"    \" T4LIT(!,warning) \" Requirement \" T4LIT(%s%s) \" on table \" T4LIT(%s,table) \" failed in condition \" T4LIT(%s,warning) \"\\n\",", indent_level = 3, lineno = 143)
generated_code += add_code("                   on ? \"\" : \"not \", get_reqcond_txt(reqcond), parts[i], cond);", indent_level = 3, lineno = 144)
generated_code += add_code("             result = false;", indent_level = 3, lineno = 145)
generated_code += add_code("             goto free_mem; // breaking out of outermost loop", indent_level = 3, lineno = 146)
generated_code += add_code("         } else {", indent_level = 3, lineno = 147)
generated_code += add_code("             result = true;", indent_level = 3, lineno = 148)
generated_code += add_code("             goto free_mem; // condition holds, breaking out of outermost loop", indent_level = 3, lineno = 149)
generated_code += add_code("         }", indent_level = 2, lineno = 150)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     }", indent_level = 2, lineno = 152)

generated_code += add_code("", indent_level = 2)
generated_code += add_code(" debug(\"    \" T4LIT(!,warning) \" No table given in condition \" T4LIT(%s,warning) \"\\n\", cond);", indent_level = 2, lineno = 154)
generated_code += add_code(" result = false;", indent_level = 2, lineno = 155)

generated_code += add_code("", indent_level = 2)
generated_code += add_code(" free_mem:", indent_level = 2, lineno = 157)
generated_code += add_code("     free(parts[0]);", indent_level = 2, lineno = 158)
generated_code += add_code("     return result;", indent_level = 2, lineno = 159)
generated_code += add_code(" }", indent_level = 1, lineno = 160)
generated_code += add_code("", indent_level = 1, lineno = 161)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" bool check_controlflow_requirements(fake_cmd_t cmd) {", indent_level = 1, lineno = 163)
generated_code += add_code("     bool result = true;", indent_level = 2, lineno = 164)
generated_code += add_code("     const char* reqs = cmd.requirements[0];", indent_level = 2, lineno = 165)
generated_code += add_code("     char* conds[MAX_PART_COUNT];", indent_level = 2, lineno = 166)
generated_code += add_code("     int part_count = split(conds, reqs, \",\");", indent_level = 2, lineno = 167)
generated_code += add_code("     for (int i = 0; i < part_count; ++i) {", indent_level = 2, lineno = 168)
generated_code += add_code("         result &= check_cond(conds[i]);", indent_level = 2, lineno = 169)
generated_code += add_code("     }", indent_level = 2, lineno = 170)
generated_code += add_code("     free(conds[0]);", indent_level = 2, lineno = 171)
generated_code += add_code("     return result;", indent_level = 2, lineno = 172)
generated_code += add_code(" }", indent_level = 1, lineno = 173)
generated_code += add_code("", indent_level = 1, lineno = 174)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" #endif", lineno = 176)