
# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

# Autogenerated file (from src/hardware_indep/stats.c.py:), do not modify directly.
# Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

import compiler_common
import re

def add_code(line, indent_level = 0, lineno = None, file = "src/hardware_indep/stats.c.py:"):
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


generated_code += "// Autogenerated file (from src/hardware_indep/stats.c.py: via hardware_indep/stats.c.py), do not modify directly.\n"
generated_code += "// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)\n"
generated_code += "\n"

generated_code += add_code(" // SPDX-License-Identifier: Apache-2.0", lineno = 1)
generated_code += add_code(" // Copyright 2020 Eotvos Lorand University, Budapest, Hungary", lineno = 2)

generated_code += add_code("")
from compiler_common import unique_everseen, to_c_bool ## src/hardware_indep/stats.c.py:5

generated_code += add_code("")
generated_code += add_code(" #include \"common.h\"", lineno = 6)
generated_code += add_code(" #include \"dpdk_lib.h\"", lineno = 7)

generated_code += add_code("")
generated_code += add_code(" extern char* action_short_names[];", lineno = 9)
generated_code += add_code(" extern char* action_names[];", lineno = 10)

generated_code += add_code("")
parser = hlir.parsers[0] ## src/hardware_indep/stats.c.py:13

generated_code += add_code("")
known_parser_state_names = ('start', 'accept', 'reject') ## src/hardware_indep/stats.c.py:15
_, parser_state_names = zip(*sorted((0 if s.name in known_parser_state_names else 1, s.name) for s in parser.states)) ## src/hardware_indep/stats.c.py:16

generated_code += add_code("")
generated_code += add_code(" #ifndef T4P4S_STATS", lineno = 17)
generated_code += add_code("     void t4p4s_print_global_stats()     { /* do nothing */ }", indent_level = 1, lineno = 18)
generated_code += add_code("     void t4p4s_print_per_packet_stats() { /* do nothing */ }", indent_level = 1, lineno = 19)
generated_code += add_code("     void t4p4s_init_global_stats()      { /* do nothing */ }", indent_level = 1, lineno = 20)
generated_code += add_code("     void t4p4s_init_per_packet_stats()  { /* do nothing */ }", indent_level = 1, lineno = 21)
generated_code += add_code("     void print_packet_stats(LCPARAMS)    { /* do nothing */ }", indent_level = 1, lineno = 22)
generated_code += add_code(" #else", indent_level = 1, lineno = 23)
generated_code += add_code("", indent_level = 1, lineno = 24)
generated_code += add_code(" t4p4s_stats_t t4p4s_stats_global;", indent_level = 1, lineno = 25)
generated_code += add_code(" t4p4s_stats_t t4p4s_stats_per_packet;", indent_level = 1, lineno = 26)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" char name_buf[128 * 1024];", indent_level = 1, lineno = 28)
generated_code += add_code(" int name_counter;", indent_level = 1, lineno = 29)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" char stats_buf[128 * 1024];", indent_level = 1, lineno = 31)
generated_code += add_code(" int stats_counter;", indent_level = 1, lineno = 32)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_init_stats(t4p4s_stats_t* t4p4s_stats) {", indent_level = 1, lineno = 34)
for name in parser_state_names: ## src/hardware_indep/stats.c.py:36
    generated_code += add_code('     t4p4s_stats->T4STAT(parser,state,{}) = false;'.format(name), indent_level = 2, lineno = 36)
for table in hlir.tables: ## src/hardware_indep/stats.c.py:39
    generated_code += add_code('     t4p4s_stats->T4STAT(table,apply,{}) = false;'.format(table.name), indent_level = 2, lineno = 39)
    if 'key' in table: ## src/hardware_indep/stats.c.py:42
        generated_code += add_code('     t4p4s_stats->T4STAT(table,hit,{}) = false;'.format(table.name), indent_level = 2, lineno = 42)
        generated_code += add_code('     t4p4s_stats->T4STAT(table,miss,{}) = false;'.format(table.name), indent_level = 2, lineno = 43)
    else: ## src/hardware_indep/stats.c.py:45
        generated_code += add_code('     t4p4s_stats->T4STAT(table,used,{}) = false;'.format(table.name), indent_level = 2, lineno = 45)
    for action_name in table.actions.map('expression.method.path.name'): ## src/hardware_indep/stats.c.py:48
        generated_code += add_code('     t4p4s_stats->T4STAT(action,{},{}) = false;'.format(table.name, action_name), indent_level = 2, lineno = 48)
generated_code += add_code(" }", indent_level = 1, lineno = 49)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_init_global_stats() {", indent_level = 1, lineno = 51)
generated_code += add_code("     t4p4s_init_stats(&t4p4s_stats_global);", indent_level = 2, lineno = 52)
generated_code += add_code(" }", indent_level = 1, lineno = 53)
generated_code += add_code("", indent_level = 1, lineno = 54)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_init_per_packet_stats() {", indent_level = 1, lineno = 56)
generated_code += add_code("     t4p4s_init_stats(&t4p4s_stats_per_packet);", indent_level = 2, lineno = 57)
generated_code += add_code(" }", indent_level = 1, lineno = 58)
generated_code += add_code("", indent_level = 1, lineno = 59)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_print_stats_parser_states(bool is_on, t4p4s_stats_t* t4p4s_stats, bool is_global) {", indent_level = 1, lineno = 61)
generated_code += add_code("     sprintf(stats_buf, \"%s\", \"\");", indent_level = 2, lineno = 62)
generated_code += add_code("     char* printout = stats_buf;", indent_level = 2, lineno = 63)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     stats_counter = 0;", indent_level = 2, lineno = 65)
generated_code += add_code("     bool is_used;", indent_level = 2, lineno = 66)
generated_code += add_code("     bool cond;", indent_level = 2, lineno = 67)
for name in parser_state_names: ## src/hardware_indep/stats.c.py:69
    generated_code += add_code('     is_used = t4p4s_stats->T4STAT(parser,state,{});'.format(name), indent_level = 2, lineno = 69)
    generated_code += add_code("     cond = !(is_used ^ is_on);", indent_level = 2, lineno = 70)
    generated_code += add_code("     if (cond) {", indent_level = 2, lineno = 71)
    generated_code += add_code('         printout += sprintf(printout, T4LIT({},parserstate) ", ");'.format(name), indent_level = 3, lineno = 72)
    generated_code += add_code("         ++stats_counter;", indent_level = 3, lineno = 73)
    generated_code += add_code("     }", indent_level = 2, lineno = 74)
generated_code += add_code("     if (stats_counter == 0 && !is_on)    return;", indent_level = 2, lineno = 76)
generated_code += add_code("     // do not complain if only \"reject\" is unused", indent_level = 2, lineno = 77)
generated_code += add_code("     if (stats_counter == 1 && !is_on && !t4p4s_stats->T4STAT(parser,state,reject))    return;", indent_level = 2, lineno = 78)
generated_code += add_code("     if (is_global) {", indent_level = 2, lineno = 79)
generated_code += add_code("         debug(\"- %4d %s parser states: %s\\n\", stats_counter, is_on ? \"used\" : \"unused\", stats_buf);", indent_level = 2, lineno = 80)
generated_code += add_code("     } else {", indent_level = 2, lineno = 81)
generated_code += add_code("         debug(\"- parser states: %s\\n\", stats_buf);", indent_level = 2, lineno = 82)
generated_code += add_code("     }", indent_level = 2, lineno = 83)
generated_code += add_code(" }", indent_level = 1, lineno = 84)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" enum t4p4s_table_stat_e { T4TABLE_APPLIED };", indent_level = 1, lineno = 86)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void print_part(char** printout_ptr, const char*const table_short_name, bool is_on, bool hidden, bool is_table_hit, bool is_table_miss, bool is_table_applied, bool is_hidden) {", indent_level = 1, lineno = 88)
generated_code += add_code("     bool is_hit  = (is_on == is_table_hit);", indent_level = 2, lineno = 89)
generated_code += add_code("     bool is_miss = (is_on == is_table_miss);", indent_level = 2, lineno = 90)
generated_code += add_code("     bool is_used = hidden ? is_table_applied : !(is_on ^ (is_hit || is_miss));", indent_level = 2, lineno = 91)
generated_code += add_code("     bool cond = !(is_used ^ is_on) && !(hidden ^ is_hidden);", indent_level = 2, lineno = 92)
generated_code += add_code("     if (!cond)   return;", indent_level = 2, lineno = 93)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     if (hidden || !is_on) {", indent_level = 2, lineno = 95)
generated_code += add_code("         *printout_ptr += sprintf(*printout_ptr, T4LIT(%s,table) \", \", table_short_name);", indent_level = 3, lineno = 96)
generated_code += add_code("     } else {", indent_level = 3, lineno = 97)
generated_code += add_code("         *printout_ptr += sprintf(*printout_ptr, T4LIT(%s,table) \"[%s%s], \", table_short_name, is_hit ? \"hit\" : \"\", is_miss ? \"miss\" : \"\");", indent_level = 3, lineno = 98)
generated_code += add_code("     }", indent_level = 2, lineno = 99)
generated_code += add_code("     ++stats_counter;", indent_level = 2, lineno = 100)
generated_code += add_code(" }", indent_level = 1, lineno = 101)
generated_code += add_code("", indent_level = 1, lineno = 102)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_print_stats_tables(bool is_on, bool hidden, enum t4p4s_table_stat_e stat, t4p4s_stats_t* t4p4s_stats, bool is_global) {", indent_level = 1, lineno = 104)
generated_code += add_code("     sprintf(stats_buf, \"%s\", \"\");", indent_level = 2, lineno = 105)
generated_code += add_code("     char* printout = stats_buf;", indent_level = 2, lineno = 106)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     stats_counter = 0;", indent_level = 2, lineno = 108)
for table in sorted(hlir.tables, key=lambda table: table.short_name): ## src/hardware_indep/stats.c.py:110
    name = table.name ## src/hardware_indep/stats.c.py:111
    generated_code += add_code(' print_part(&printout, "{}", is_on, hidden,'.format(table.short_name), indent_level = 2, lineno = 111)
    generated_code += add_code('            t4p4s_stats->T4STAT(table,hit,{}), t4p4s_stats->T4STAT(table,miss,{}), t4p4s_stats->T4STAT(table,apply,{}), {});'.format(name, name, name, to_c_bool(table.is_hidden)), indent_level = 2, lineno = 112)
generated_code += add_code("     if (stats_counter == 0 && !is_on)    return;", indent_level = 2, lineno = 114)
generated_code += add_code("     if (is_global) {", indent_level = 2, lineno = 115)
generated_code += add_code("         debug(\"- %4d %s %stables: %s\\n\", stats_counter, is_on ? \"applied\" : \"unapplied\", hidden ? \"hidden \" : \"\", stats_buf);", indent_level = 2, lineno = 116)
generated_code += add_code("     } else {", indent_level = 2, lineno = 117)
generated_code += add_code("         debug(\"- tables: %s\\n\", stats_buf);", indent_level = 2, lineno = 118)
generated_code += add_code("     }", indent_level = 2, lineno = 119)
generated_code += add_code(" }", indent_level = 1, lineno = 120)
generated_code += add_code("", indent_level = 1, lineno = 121)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" #define NO_ACTION_NAME \".NoAction\"", indent_level = 1, lineno = 123)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_print_stats_action(bool is_used, bool is_on, bool real_action, bool is_real_action, char** printout_ptr, int action_idx) {", indent_level = 1, lineno = 126)
generated_code += add_code("     if ((is_used ^ is_on) || (real_action ^ is_real_action))   return;", indent_level = 2, lineno = 127)
generated_code += add_code("     *printout_ptr += sprintf(*printout_ptr, \"%s\" T4LIT(%s,action), name_counter > 0 ? \", \" : \"\", real_action ? action_short_names[action_idx] : \"\");", indent_level = 2, lineno = 128)
generated_code += add_code("     ++name_counter;", indent_level = 2, lineno = 129)
generated_code += add_code("     ++stats_counter;", indent_level = 2, lineno = 130)
generated_code += add_code(" }", indent_level = 1, lineno = 131)
generated_code += add_code("", indent_level = 1, lineno = 132)

generated_code += add_code("", indent_level = 1)
ta_reorder = {(t, a): idx for idx, (t, a) in enumerate((t,a) for t in hlir.tables for a in unique_everseen(t.actions))} ## src/hardware_indep/stats.c.py:136

generated_code += add_code("", indent_level = 1)
for idx, (table, action) in enumerate((t, a) for t in sorted(hlir.tables, key=lambda table: table.short_name) for a in sorted(unique_everseen(t.actions), key=lambda a: a.action_object.short_name)): ## src/hardware_indep/stats.c.py:138
    ao = action.action_object ## src/hardware_indep/stats.c.py:139
    action_idx = ta_reorder[(table, action)] ## src/hardware_indep/stats.c.py:140
    is_hidden_ok = "" if table.is_hidden else "!" ## src/hardware_indep/stats.c.py:142
    generated_code += add_code(' void t4p4s_print_stats_{}_{}(char** printout_ptr, bool is_on, bool real_action, t4p4s_stats_t* t4p4s_stats) {{'.format(table.name, ao.name), indent_level = 1, lineno = 143)
    generated_code += add_code('     bool is_used         = t4p4s_stats->T4STAT(action,{},{});'.format(table.name, ao.name), indent_level = 2, lineno = 144)
    generated_code += add_code('     bool is_real_action  = strcmp(action_short_names[{}], NO_ACTION_NAME);'.format(action_idx), indent_level = 2, lineno = 145)
    generated_code += add_code('     t4p4s_print_stats_action(is_used, is_on, real_action, is_real_action, printout_ptr, {});'.format(action_idx), indent_level = 2, lineno = 146)
    generated_code += add_code(" }", indent_level = 1, lineno = 147)
    generated_code += add_code("", indent_level = 1, lineno = 148)
generated_code += add_code(" void print_table_name(char** printout_ptr, const char*const table_short_name, bool real_action) {", indent_level = 1, lineno = 150)
generated_code += add_code("     if (name_counter == 0)   return;", indent_level = 2, lineno = 151)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     if (real_action)    *printout_ptr += sprintf(*printout_ptr, \"         \" T4LIT(%s,table) \": %s\\n\", table_short_name, name_buf);", indent_level = 2, lineno = 153)
generated_code += add_code("     else                *printout_ptr += sprintf(*printout_ptr, T4LIT(%s,table) \", \", table_short_name);", indent_level = 2, lineno = 154)
generated_code += add_code(" }", indent_level = 1, lineno = 155)
generated_code += add_code("", indent_level = 1, lineno = 156)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void t4p4s_print_stats_table_actions(bool is_on, bool hidden, bool real_action, const char* action_type_txt, enum t4p4s_table_stat_e stat, t4p4s_stats_t* t4p4s_stats, bool is_global) {", indent_level = 1, lineno = 158)
generated_code += add_code("     sprintf(stats_buf, \"%s\", \"\");", indent_level = 2, lineno = 159)
generated_code += add_code("     char* printout = stats_buf;", indent_level = 2, lineno = 160)
generated_code += add_code("     char* printout_name;", indent_level = 2, lineno = 161)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     stats_counter = 0;", indent_level = 2, lineno = 163)
for table in sorted(hlir.tables, key=lambda table: table.short_name): ## src/hardware_indep/stats.c.py:165
    generated_code += add_code("     sprintf(name_buf, \"%s\", \"\");", indent_level = 2, lineno = 165)
    generated_code += add_code("     printout_name = name_buf;", indent_level = 2, lineno = 166)
    generated_code += add_code("     name_counter = 0;", indent_level = 2, lineno = 168)
    is_hidden_ok = "" if table.is_hidden else "!" ## src/hardware_indep/stats.c.py:170
    for action_name in unique_everseen(table.actions.map('expression.method.path.name')): ## src/hardware_indep/stats.c.py:171
        generated_code += add_code('     if ({}hidden)   t4p4s_print_stats_{}_{}(&printout_name, is_on, real_action, t4p4s_stats);'.format(is_hidden_ok, table.name, action_name), indent_level = 2, lineno = 171)
    generated_code += add_code('     print_table_name(&printout, "{}", real_action);'.format(table.short_name), indent_level = 2, lineno = 172)
    generated_code += add_code("", indent_level = 2, lineno = 173)
generated_code += add_code("     if (stats_counter == 0 && !is_on)    return;", indent_level = 2, lineno = 175)
generated_code += add_code("     if (is_global) {", indent_level = 2, lineno = 176)
generated_code += add_code("         debug(\"- %4d %s %s%s:%s%s%s\", stats_counter, is_on ? \"applied\" : \"unapplied\", hidden ? \"hidden \" : \"\", action_type_txt, real_action ? \"\\n\" : \" \", stats_buf, real_action ? \"\" : \"\\n\");", indent_level = 3, lineno = 177)
generated_code += add_code("     } else {", indent_level = 3, lineno = 178)
generated_code += add_code("         debug(\"- %s:%s%s%s\", action_type_txt, real_action ? \"\\n\" : \" \", stats_buf, real_action ? \"\" : \"\\n\");", indent_level = 3, lineno = 179)
generated_code += add_code("     }", indent_level = 2, lineno = 180)
generated_code += add_code(" }", indent_level = 1, lineno = 181)
generated_code += add_code("", indent_level = 1, lineno = 182)

generated_code += add_code("", indent_level = 1)
generated_code += add_code("     #ifdef T4P4S_DEBUG", indent_level = 1, lineno = 184)
generated_code += add_code("         extern volatile int packet_with_error_counter;", indent_level = 2, lineno = 185)
generated_code += add_code("         extern volatile int packet_counter;", indent_level = 2, lineno = 186)
generated_code += add_code("     #endif", indent_level = 1, lineno = 187)
generated_code += add_code("", indent_level = 1, lineno = 188)

generated_code += add_code("", indent_level = 1)
generated_code += add_code("     void t4p4s_print_stats_error_packets() {", indent_level = 1, lineno = 190)
generated_code += add_code("         #ifdef T4P4S_DEBUG", indent_level = 2, lineno = 191)
generated_code += add_code("             int all  = packet_counter;", indent_level = 3, lineno = 192)
generated_code += add_code("             int errs = packet_with_error_counter;", indent_level = 3, lineno = 193)
generated_code += add_code("             if (errs == 0) {", indent_level = 3, lineno = 194)
generated_code += add_code("                 debug(\"- \" T4LIT(%2d,success) \" OK packet%s\\n\", all, all != 1 ? \"s\" : \"\");", indent_level = 4, lineno = 195)
generated_code += add_code("             } else {", indent_level = 4, lineno = 196)
generated_code += add_code("                 debug(\"- \" T4LIT(%2d,error) \" error%s in packet processing, \" T4LIT(%2d,success) \" OK packet%s (\" T4LIT(%2d) \" packet%s in total)\\n\",", indent_level = 4, lineno = 197)
generated_code += add_code("                       errs, errs != 1 ? \"s\" : \"\", all - errs, all - errs != 1 ? \"s\" : \"\", all, all != 1 ? \"s\" : \"\");", indent_level = 4, lineno = 198)
generated_code += add_code("             }", indent_level = 3, lineno = 199)
generated_code += add_code("         #endif", indent_level = 2, lineno = 200)
generated_code += add_code("     }", indent_level = 1, lineno = 201)

generated_code += add_code("", indent_level = 1)
generated_code += add_code("     void t4p4s_print_stats(bool is_on, t4p4s_stats_t* t4p4s_stats, bool is_global) {", indent_level = 1, lineno = 203)
generated_code += add_code("         t4p4s_print_stats_parser_states(is_on, t4p4s_stats, is_global);", indent_level = 2, lineno = 204)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         t4p4s_print_stats_tables(is_on, false, T4TABLE_APPLIED, t4p4s_stats, is_global);", indent_level = 2, lineno = 206)
generated_code += add_code("         if (is_global) {", indent_level = 2, lineno = 207)
generated_code += add_code("             t4p4s_print_stats_tables(is_on, true, T4TABLE_APPLIED, t4p4s_stats, is_global);", indent_level = 3, lineno = 208)
generated_code += add_code("         }", indent_level = 2, lineno = 209)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("         t4p4s_print_stats_table_actions(is_on, false, true, \"real actions\", T4TABLE_APPLIED, t4p4s_stats, is_global);", indent_level = 2, lineno = 211)
generated_code += add_code("         t4p4s_print_stats_table_actions(is_on, false, false, \"no-actions\", T4TABLE_APPLIED, t4p4s_stats, is_global);", indent_level = 2, lineno = 212)
generated_code += add_code("     }", indent_level = 1, lineno = 213)
generated_code += add_code("", indent_level = 1, lineno = 214)

generated_code += add_code("", indent_level = 1)
generated_code += add_code("     void t4p4s_print_global_stats() {", indent_level = 1, lineno = 217)
generated_code += add_code("         debug(\"\\n\");", indent_level = 2, lineno = 218)
generated_code += add_code("         debug(\"Overall statistics:\\n\");", indent_level = 2, lineno = 219)
generated_code += add_code("         t4p4s_print_stats_error_packets();", indent_level = 2, lineno = 220)
generated_code += add_code("         t4p4s_print_stats(true, &t4p4s_stats_global, true);", indent_level = 2, lineno = 221)
generated_code += add_code("         debug(\"\\n\");", indent_level = 2, lineno = 222)
generated_code += add_code("         t4p4s_print_stats(false, &t4p4s_stats_global, true);", indent_level = 2, lineno = 223)
generated_code += add_code("     }", indent_level = 1, lineno = 224)
generated_code += add_code("", indent_level = 1, lineno = 225)

generated_code += add_code("", indent_level = 1)
generated_code += add_code("     void t4p4s_print_per_packet_stats() {", indent_level = 1, lineno = 227)
generated_code += add_code("         debug(\"Per packet statistics:\\n\");", indent_level = 2, lineno = 228)
generated_code += add_code("         t4p4s_print_stats(true, &t4p4s_stats_per_packet, false);", indent_level = 2, lineno = 229)

generated_code += add_code("", indent_level = 2)
generated_code += add_code("     }", indent_level = 1, lineno = 231)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" void print_packet_stats(LCPARAMS) {", indent_level = 1, lineno = 234)
generated_code += add_code("     COUNTER_ECHO(lcdata->conf->processed_packet_num,\"   :: Processed packet count: %d\\n\");", indent_level = 2, lineno = 235)
generated_code += add_code("     COUNTER_ECHO(lcdata->conf->doing_crypto_packet,\"   :: Crypto packets in progress: %d\\n\");", indent_level = 2, lineno = 236)
generated_code += add_code("     COUNTER_ECHO(lcdata->conf->fwd_packet,\"   :: Forwarded packet without encrypt: %d\\n\");", indent_level = 2, lineno = 237)
generated_code += add_code("     #if defined ASYNC_MODE && ASYNC_MODE != ASYNC_OFF", indent_level = 2, lineno = 238)
generated_code += add_code("          COUNTER_ECHO(lcdata->conf->sent_to_crypto_packet,\"   :: Sent to crypto packet: %d\\n\");", indent_level = 2, lineno = 239)
generated_code += add_code("          COUNTER_ECHO(lcdata->conf->async_packet,\"   :: Async handled packet: %d\\n\");", indent_level = 2, lineno = 240)
generated_code += add_code("          COUNTER_ECHO(lcdata->conf->async_drop_counter,\"   :: Dropped async packet: %d\\n\");", indent_level = 2, lineno = 241)
generated_code += add_code("     #endif", indent_level = 2, lineno = 242)
generated_code += add_code(" }", indent_level = 1, lineno = 243)
generated_code += add_code("", indent_level = 1, lineno = 244)

generated_code += add_code("", indent_level = 1)
generated_code += add_code(" #endif", lineno = 246)
generated_code += add_code("", lineno = 247)
