// Autogenerated file (from src/hardware_indep/tables.h.py: via hardware_indep/tables.h.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#pragma once

#include "stateful_memory.h"
#include "actions.h"

#define ENTRY(tname)    tname ## _entry_t
#define ENTRYBASE       ENTRY(base_table)

typedef base_table_action_t ENTRYBASE;

typedef struct {
    actions_e                     id;
    eth_dstMac_filter_0_action_params_t params;
} ENTRY(eth_dstMac_filter_0);

typedef struct {
    actions_e                     id;
    eth_srcMac_filter_0_action_params_t params;
} ENTRY(eth_srcMac_filter_0);

typedef struct {
    actions_e                     id;
    eth_proto_filter_0_action_params_t params;
} ENTRY(eth_proto_filter_0);

typedef struct {
    actions_e                     id;
    ip_proto_filter_0_action_params_t params;
} ENTRY(ip_proto_filter_0);

typedef struct {
    actions_e                     id;
    ip_dstIP_filter_0_action_params_t params;
} ENTRY(ip_dstIP_filter_0);

typedef struct {
    actions_e                     id;
    ip_srcIP_filter_0_action_params_t params;
} ENTRY(ip_srcIP_filter_0);

typedef struct {
    actions_e                     id;
    tcp_srcPort_filter_0_action_params_t params;
} ENTRY(tcp_srcPort_filter_0);

typedef struct {
    actions_e                     id;
    tcp_dstPort_filter_0_action_params_t params;
} ENTRY(tcp_dstPort_filter_0);

typedef struct {
    actions_e                     id;
    udp_srcPort_filter_0_action_params_t params;
} ENTRY(udp_srcPort_filter_0);

typedef struct {
    actions_e                     id;
    udp_dstPort_filter_0_action_params_t params;
} ENTRY(udp_dstPort_filter_0);

typedef struct {
    actions_e                     id;
    tbl_firewall210_action_params_t params;
} ENTRY(tbl_firewall210);

typedef struct {
    actions_e                     id;
    tbl_act_action_params_t params;
} ENTRY(tbl_act);

typedef struct {
    actions_e                     id;
    tbl_act_0_action_params_t params;
} ENTRY(tbl_act_0);

typedef struct {
    actions_e                     id;
    tbl_firewall212_action_params_t params;
} ENTRY(tbl_firewall212);

typedef struct {
    actions_e                     id;
    tbl_act_1_action_params_t params;
} ENTRY(tbl_act_1);

typedef struct {
    actions_e                     id;
    tbl_act_2_action_params_t params;
} ENTRY(tbl_act_2);

typedef struct {
    actions_e                     id;
    tbl_firewall212_0_action_params_t params;
} ENTRY(tbl_firewall212_0);

typedef struct {
    actions_e                     id;
    tbl_firewall212_1_action_params_t params;
} ENTRY(tbl_firewall212_1);

typedef struct {
    actions_e                     id;
    tbl_act_3_action_params_t params;
} ENTRY(tbl_act_3);

typedef struct {
    actions_e                     id;
    tbl_act_4_action_params_t params;
} ENTRY(tbl_act_4);

typedef struct {
    actions_e                     id;
    tbl_firewall212_2_action_params_t params;
} ENTRY(tbl_firewall212_2);

typedef struct {
    actions_e                     id;
    tbl_firewall213_action_params_t params;
} ENTRY(tbl_firewall213);

typedef struct {
    actions_e                     id;
    tbl_act_5_action_params_t params;
} ENTRY(tbl_act_5);

typedef struct {
    actions_e                     id;
    tbl_act_6_action_params_t params;
} ENTRY(tbl_act_6);

typedef struct {
    actions_e                     id;
    tbl_firewall215_action_params_t params;
} ENTRY(tbl_firewall215);

typedef struct {
    actions_e                     id;
    tbl_act_7_action_params_t params;
} ENTRY(tbl_act_7);

typedef struct {
    actions_e                     id;
    tbl_act_8_action_params_t params;
} ENTRY(tbl_act_8);

typedef struct {
    actions_e                     id;
    tbl_firewall215_0_action_params_t params;
} ENTRY(tbl_firewall215_0);

typedef struct {
    actions_e                     id;
    tbl_firewall215_1_action_params_t params;
} ENTRY(tbl_firewall215_1);

typedef struct {
    actions_e                     id;
    tbl_act_9_action_params_t params;
} ENTRY(tbl_act_9);

typedef struct {
    actions_e                     id;
    tbl_act_10_action_params_t params;
} ENTRY(tbl_act_10);

typedef struct {
    actions_e                     id;
    tbl_firewall215_2_action_params_t params;
} ENTRY(tbl_firewall215_2);

typedef struct {
    actions_e                     id;
    tbl_firewall216_action_params_t params;
} ENTRY(tbl_firewall216);

typedef struct {
    actions_e                     id;
    tbl_act_11_action_params_t params;
} ENTRY(tbl_act_11);

typedef struct {
    actions_e                     id;
    tbl_act_12_action_params_t params;
} ENTRY(tbl_act_12);

typedef struct {
    actions_e                     id;
    tbl_firewall218_action_params_t params;
} ENTRY(tbl_firewall218);

typedef struct {
    actions_e                     id;
    tbl_act_13_action_params_t params;
} ENTRY(tbl_act_13);

typedef struct {
    actions_e                     id;
    tbl_act_14_action_params_t params;
} ENTRY(tbl_act_14);

typedef struct {
    actions_e                     id;
    tbl_firewall218_0_action_params_t params;
} ENTRY(tbl_firewall218_0);

typedef struct {
    actions_e                     id;
    tbl_firewall219_action_params_t params;
} ENTRY(tbl_firewall219);

typedef struct {
    actions_e                     id;
    tbl_act_15_action_params_t params;
} ENTRY(tbl_act_15);

typedef struct {
    actions_e                     id;
    tbl_act_16_action_params_t params;
} ENTRY(tbl_act_16);

typedef struct {
    actions_e                     id;
    tbl_act_17_action_params_t params;
} ENTRY(tbl_act_17);

typedef struct {
    actions_e                     id;
    tbl_act_18_action_params_t params;
} ENTRY(tbl_act_18);

typedef struct {
    actions_e                     id;
    tbl_firewall222_action_params_t params;
} ENTRY(tbl_firewall222);

typedef struct {
    actions_e                     id;
    tbl_firewall222_0_action_params_t params;
} ENTRY(tbl_firewall222_0);

typedef struct {
    actions_e                     id;
    tbl_firewall223_action_params_t params;
} ENTRY(tbl_firewall223);

typedef struct {
    actions_e                     id;
    tbl_firewall229_action_params_t params;
} ENTRY(tbl_firewall229);

typedef enum {
    TABLE_eth_dstMac_filter_0,
    TABLE_eth_srcMac_filter_0,
    TABLE_eth_proto_filter_0,
    TABLE_ip_proto_filter_0,
    TABLE_ip_dstIP_filter_0,
    TABLE_ip_srcIP_filter_0,
    TABLE_tcp_srcPort_filter_0,
    TABLE_tcp_dstPort_filter_0,
    TABLE_udp_srcPort_filter_0,
    TABLE_udp_dstPort_filter_0,
    TABLE_tbl_firewall210,
    TABLE_tbl_act,
    TABLE_tbl_act_0,
    TABLE_tbl_firewall212,
    TABLE_tbl_act_1,
    TABLE_tbl_act_2,
    TABLE_tbl_firewall212_0,
    TABLE_tbl_firewall212_1,
    TABLE_tbl_act_3,
    TABLE_tbl_act_4,
    TABLE_tbl_firewall212_2,
    TABLE_tbl_firewall213,
    TABLE_tbl_act_5,
    TABLE_tbl_act_6,
    TABLE_tbl_firewall215,
    TABLE_tbl_act_7,
    TABLE_tbl_act_8,
    TABLE_tbl_firewall215_0,
    TABLE_tbl_firewall215_1,
    TABLE_tbl_act_9,
    TABLE_tbl_act_10,
    TABLE_tbl_firewall215_2,
    TABLE_tbl_firewall216,
    TABLE_tbl_act_11,
    TABLE_tbl_act_12,
    TABLE_tbl_firewall218,
    TABLE_tbl_act_13,
    TABLE_tbl_act_14,
    TABLE_tbl_firewall218_0,
    TABLE_tbl_firewall219,
    TABLE_tbl_act_15,
    TABLE_tbl_act_16,
    TABLE_tbl_act_17,
    TABLE_tbl_act_18,
    TABLE_tbl_firewall222,
    TABLE_tbl_firewall222_0,
    TABLE_tbl_firewall223,
    TABLE_tbl_firewall229,
    TABLE_,
} table_name_e;

void exact_add_promote  (table_name_e tableid, uint8_t* key,                ENTRYBASE* entry, bool is_const_entry, bool should_print);
void lpm_add_promote    (table_name_e tableid, uint8_t* key, uint8_t depth, ENTRYBASE* entry, bool is_const_entry, bool should_print);
void ternary_add_promote(table_name_e tableid, uint8_t* key, uint8_t* mask, ENTRYBASE* entry, bool is_const_entry, bool should_print);
void table_setdefault_promote(table_name_e tableid, ENTRYBASE* entry, bool show_info);

//=============================================================================

// Computes the location of the validity field of the entry.
bool* entry_validity_ptr(ENTRYBASE* entry, lookup_table_t* t);
