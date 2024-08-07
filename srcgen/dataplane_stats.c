// Autogenerated file (from src/hardware_indep/dataplane_stats.c.py: via hardware_indep/dataplane_stats.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include "dataplane_impl.h"

void eth_dstMac_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,eth_dstMac_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,eth_dstMac_filter_0) = true;
        if (action_drop == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_dstMac_filter_0,drop) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_dstMac_filter_0,drop) = true;
        }
        if (action_NoAction_1 == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_dstMac_filter_0,NoAction_1) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_dstMac_filter_0,NoAction_1) = true;
        }
    #endif
}

void eth_srcMac_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,eth_srcMac_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,eth_srcMac_filter_0) = true;
        if (action_drop_1 == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_srcMac_filter_0,drop_1) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_srcMac_filter_0,drop_1) = true;
        }
        if (action_NoAction_2 == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_srcMac_filter_0,NoAction_2) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_srcMac_filter_0,NoAction_2) = true;
        }
    #endif
}

void eth_proto_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,eth_proto_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,eth_proto_filter_0) = true;
        if (action_drop_2 == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_proto_filter_0,drop_2) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_proto_filter_0,drop_2) = true;
        }
        if (action_NoAction_3 == action_id) {
            t4p4s_stats_global.T4STAT(action,eth_proto_filter_0,NoAction_3) = true;
            t4p4s_stats_per_packet.T4STAT(action,eth_proto_filter_0,NoAction_3) = true;
        }
    #endif
}

void ip_proto_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,ip_proto_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,ip_proto_filter_0) = true;
        if (action_drop_3 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_proto_filter_0,drop_3) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_proto_filter_0,drop_3) = true;
        }
        if (action_NoAction_4 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_proto_filter_0,NoAction_4) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_proto_filter_0,NoAction_4) = true;
        }
    #endif
}

void ip_dstIP_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,ip_dstIP_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,ip_dstIP_filter_0) = true;
        if (action_drop_4 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_dstIP_filter_0,drop_4) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_dstIP_filter_0,drop_4) = true;
        }
        if (action_NoAction_5 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_dstIP_filter_0,NoAction_5) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_dstIP_filter_0,NoAction_5) = true;
        }
    #endif
}

void ip_srcIP_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,ip_srcIP_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,ip_srcIP_filter_0) = true;
        if (action_drop_5 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_srcIP_filter_0,drop_5) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_srcIP_filter_0,drop_5) = true;
        }
        if (action_NoAction_6 == action_id) {
            t4p4s_stats_global.T4STAT(action,ip_srcIP_filter_0,NoAction_6) = true;
            t4p4s_stats_per_packet.T4STAT(action,ip_srcIP_filter_0,NoAction_6) = true;
        }
    #endif
}

void tcp_srcPort_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tcp_srcPort_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tcp_srcPort_filter_0) = true;
        if (action_drop_6 == action_id) {
            t4p4s_stats_global.T4STAT(action,tcp_srcPort_filter_0,drop_6) = true;
            t4p4s_stats_per_packet.T4STAT(action,tcp_srcPort_filter_0,drop_6) = true;
        }
        if (action_NoAction_7 == action_id) {
            t4p4s_stats_global.T4STAT(action,tcp_srcPort_filter_0,NoAction_7) = true;
            t4p4s_stats_per_packet.T4STAT(action,tcp_srcPort_filter_0,NoAction_7) = true;
        }
    #endif
}

void tcp_dstPort_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tcp_dstPort_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tcp_dstPort_filter_0) = true;
        if (action_drop_7 == action_id) {
            t4p4s_stats_global.T4STAT(action,tcp_dstPort_filter_0,drop_7) = true;
            t4p4s_stats_per_packet.T4STAT(action,tcp_dstPort_filter_0,drop_7) = true;
        }
        if (action_NoAction_8 == action_id) {
            t4p4s_stats_global.T4STAT(action,tcp_dstPort_filter_0,NoAction_8) = true;
            t4p4s_stats_per_packet.T4STAT(action,tcp_dstPort_filter_0,NoAction_8) = true;
        }
    #endif
}

void udp_srcPort_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,udp_srcPort_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,udp_srcPort_filter_0) = true;
        if (action_drop_8 == action_id) {
            t4p4s_stats_global.T4STAT(action,udp_srcPort_filter_0,drop_8) = true;
            t4p4s_stats_per_packet.T4STAT(action,udp_srcPort_filter_0,drop_8) = true;
        }
        if (action_NoAction_9 == action_id) {
            t4p4s_stats_global.T4STAT(action,udp_srcPort_filter_0,NoAction_9) = true;
            t4p4s_stats_per_packet.T4STAT(action,udp_srcPort_filter_0,NoAction_9) = true;
        }
    #endif
}

void udp_dstPort_filter_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,udp_dstPort_filter_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,udp_dstPort_filter_0) = true;
        if (action_drop_9 == action_id) {
            t4p4s_stats_global.T4STAT(action,udp_dstPort_filter_0,drop_9) = true;
            t4p4s_stats_per_packet.T4STAT(action,udp_dstPort_filter_0,drop_9) = true;
        }
        if (action_NoAction_10 == action_id) {
            t4p4s_stats_global.T4STAT(action,udp_dstPort_filter_0,NoAction_10) = true;
            t4p4s_stats_per_packet.T4STAT(action,udp_dstPort_filter_0,NoAction_10) = true;
        }
    #endif
}

void tbl_firewall210_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall210) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall210) = true;
        if (action_firewall210 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall210,firewall210) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall210,firewall210) = true;
        }
    #endif
}

void tbl_act_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act) = true;
        if (action_act == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act,act) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act,act) = true;
        }
    #endif
}

void tbl_act_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_0) = true;
        if (action_act_0 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_0,act_0) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_0,act_0) = true;
        }
    #endif
}

void tbl_firewall212_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall212) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall212) = true;
        if (action_firewall212 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall212,firewall212) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall212,firewall212) = true;
        }
    #endif
}

void tbl_act_1_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_1) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_1) = true;
        if (action_act_1 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_1,act_1) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_1,act_1) = true;
        }
    #endif
}

void tbl_act_2_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_2) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_2) = true;
        if (action_act_2 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_2,act_2) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_2,act_2) = true;
        }
    #endif
}

void tbl_firewall212_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall212_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall212_0) = true;
        if (action_firewall212_0 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall212_0,firewall212_0) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall212_0,firewall212_0) = true;
        }
    #endif
}

void tbl_firewall212_1_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall212_1) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall212_1) = true;
        if (action_firewall212_1 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall212_1,firewall212_1) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall212_1,firewall212_1) = true;
        }
    #endif
}

void tbl_act_3_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_3) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_3) = true;
        if (action_act_3 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_3,act_3) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_3,act_3) = true;
        }
    #endif
}

void tbl_act_4_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_4) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_4) = true;
        if (action_act_4 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_4,act_4) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_4,act_4) = true;
        }
    #endif
}

void tbl_firewall212_2_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall212_2) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall212_2) = true;
        if (action_firewall212_2 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall212_2,firewall212_2) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall212_2,firewall212_2) = true;
        }
    #endif
}

void tbl_firewall213_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall213) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall213) = true;
        if (action_firewall213 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall213,firewall213) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall213,firewall213) = true;
        }
    #endif
}

void tbl_act_5_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_5) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_5) = true;
        if (action_act_5 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_5,act_5) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_5,act_5) = true;
        }
    #endif
}

void tbl_act_6_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_6) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_6) = true;
        if (action_act_6 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_6,act_6) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_6,act_6) = true;
        }
    #endif
}

void tbl_firewall215_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall215) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall215) = true;
        if (action_firewall215 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall215,firewall215) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall215,firewall215) = true;
        }
    #endif
}

void tbl_act_7_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_7) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_7) = true;
        if (action_act_7 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_7,act_7) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_7,act_7) = true;
        }
    #endif
}

void tbl_act_8_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_8) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_8) = true;
        if (action_act_8 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_8,act_8) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_8,act_8) = true;
        }
    #endif
}

void tbl_firewall215_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall215_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall215_0) = true;
        if (action_firewall215_0 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall215_0,firewall215_0) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall215_0,firewall215_0) = true;
        }
    #endif
}

void tbl_firewall215_1_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall215_1) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall215_1) = true;
        if (action_firewall215_1 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall215_1,firewall215_1) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall215_1,firewall215_1) = true;
        }
    #endif
}

void tbl_act_9_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_9) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_9) = true;
        if (action_act_9 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_9,act_9) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_9,act_9) = true;
        }
    #endif
}

void tbl_act_10_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_10) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_10) = true;
        if (action_act_10 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_10,act_10) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_10,act_10) = true;
        }
    #endif
}

void tbl_firewall215_2_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall215_2) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall215_2) = true;
        if (action_firewall215_2 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall215_2,firewall215_2) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall215_2,firewall215_2) = true;
        }
    #endif
}

void tbl_firewall216_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall216) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall216) = true;
        if (action_firewall216 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall216,firewall216) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall216,firewall216) = true;
        }
    #endif
}

void tbl_act_11_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_11) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_11) = true;
        if (action_act_11 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_11,act_11) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_11,act_11) = true;
        }
    #endif
}

void tbl_act_12_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_12) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_12) = true;
        if (action_act_12 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_12,act_12) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_12,act_12) = true;
        }
    #endif
}

void tbl_firewall218_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall218) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall218) = true;
        if (action_firewall218 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall218,firewall218) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall218,firewall218) = true;
        }
    #endif
}

void tbl_act_13_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_13) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_13) = true;
        if (action_act_13 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_13,act_13) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_13,act_13) = true;
        }
    #endif
}

void tbl_act_14_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_14) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_14) = true;
        if (action_act_14 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_14,act_14) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_14,act_14) = true;
        }
    #endif
}

void tbl_firewall218_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall218_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall218_0) = true;
        if (action_firewall218_0 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall218_0,firewall218_0) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall218_0,firewall218_0) = true;
        }
    #endif
}

void tbl_firewall219_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall219) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall219) = true;
        if (action_firewall219 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall219,firewall219) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall219,firewall219) = true;
        }
    #endif
}

void tbl_act_15_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_15) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_15) = true;
        if (action_act_15 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_15,act_15) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_15,act_15) = true;
        }
    #endif
}

void tbl_act_16_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_16) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_16) = true;
        if (action_act_16 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_16,act_16) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_16,act_16) = true;
        }
    #endif
}

void tbl_act_17_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_17) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_17) = true;
        if (action_act_17 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_17,act_17) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_17,act_17) = true;
        }
    #endif
}

void tbl_act_18_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_act_18) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_act_18) = true;
        if (action_act_18 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_act_18,act_18) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_act_18,act_18) = true;
        }
    #endif
}

void tbl_firewall222_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall222) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall222) = true;
        if (action_firewall222 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall222,firewall222) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall222,firewall222) = true;
        }
    #endif
}

void tbl_firewall222_0_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall222_0) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall222_0) = true;
        if (action_firewall222_0 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall222_0,firewall222_0) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall222_0,firewall222_0) = true;
        }
    #endif
}

void tbl_firewall223_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall223) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall223) = true;
        if (action_firewall223 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall223,firewall223) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall223,firewall223) = true;
        }
    #endif
}

void tbl_firewall229_stats(int action_id, STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(table,apply,tbl_firewall229) = true;
        t4p4s_stats_per_packet.T4STAT(table,apply,tbl_firewall229) = true;
        if (action_firewall229 == action_id) {
            t4p4s_stats_global.T4STAT(action,tbl_firewall229,firewall229) = true;
            t4p4s_stats_per_packet.T4STAT(action,tbl_firewall229,firewall229) = true;
        }
    #endif
}

