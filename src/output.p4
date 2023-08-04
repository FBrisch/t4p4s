#include <v1model.p4>

header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

header arp_t {
    bit<16> htype;
    bit<16> ptype;
    bit<8> hlen;
    bit<8> plen;
    bit<16> oper;
}

header ipv4_t {
    bit<4> version;
    bit<4> ihl;
    bit<8> diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3> flags;
    bit<13> fragOffset;
    bit<8> ttl;
    bit<8> protocol;
    bit<16> hdrChecksum;
    bit<32> srcAddr;
    bit<32> dstAddr;
}

header icmp_t {
    bit<8> type;
    bit<8> code;
    bit<16> checksum;
    bit<16> identifier;
    bit<16> sequence_number;
}

header tcp_t {
    bit<16> _srcPort0;
    bit<16> _dstPort1;
    bit<32> _seqNo2;
    bit<32> _ackNo3;
    bit<4> _dataOffset4;
    bit<4> _res5;
    bit<1> _flags_cwr6;
    bit<1> _flags_ece7;
    bit<1> _flags_urg8;
    bit<1> _flags_ack9;
    bit<1> _flags_psh10;
    bit<1> _flags_rst11;
    bit<1> _flags_syn12;
    bit<1> _flags_fin13;
    bit<16> _window14;
    bit<16> _checksum15;
    bit<16> _urgentPtr16;
}

header udp_t {
    bit<16> srcPort;
    bit<16> dstPort;
    bit<16> plength;
    bit<16> checksum;
}

struct headers {
    ethernet_t ethernet;
    arp_t arp;
    ipv4_t ipv4;
    icmp_t icmp;
    tcp_t tcp;
    udp_t udp;
}

struct metadata {
}

parser ParserImpl( packet_in packet, out headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    state parse_arp {
        extract_header(
          hdr.arp
        );
        transition select(hdr.oper.oper){
          1:accept;
          default:accept;
        }
    }
    state parse_icmp {
        extract_header(
          hdr.icmp
        );
        transition accept;
    }
    state parse_tcp {
        extract_header(
          hdr.tcp
        );
        transition accept;
    }
    state parse_udp {
        extract_header(
          hdr.udp
        );
        transition accept;
    }
    state parse_ipv4 {
        extract_header(
          hdr.ipv4
        );
        transition select(hdr.protocol.protocol){
          1:parse_icmp;
          6:parse_tcp;
          17:parse_udp;
          default:accept;
        }
    }
    state start {
        extract_header(
          hdr.ethernet
        );
        transition select(hdr.etherType.etherType){
          2054:parse_arp;
          2048:parse_ipv4;
          default:accept;
        }
    }
}

control ingress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    action NoAction_1() {
    }
    action NoAction_2() {
    }
    action NoAction_3() {
    }
    action NoAction_4() {
    }
    action NoAction_5() {
    }
    action NoAction_6() {
    }
    action NoAction_7() {
    }
    action NoAction_8() {
    }
    action NoAction_9() {
    }
    action NoAction_10() {
    }
    action drop() {
        mark_to_drop(standard_metadata);
    }
    action drop_1() {
        mark_to_drop(standard_metadata);
    }
    action drop_2() {
        mark_to_drop(standard_metadata);
    }
    action drop_3() {
        mark_to_drop(standard_metadata);
    }
    action drop_4() {
        mark_to_drop(standard_metadata);
    }
    action drop_5() {
        mark_to_drop(standard_metadata);
    }
    action drop_6() {
        mark_to_drop(standard_metadata);
    }
    action drop_7() {
        mark_to_drop(standard_metadata);
    }
    action drop_8() {
        mark_to_drop(standard_metadata);
    }
    action drop_9() {
        mark_to_drop(standard_metadata);
    }
    action act() {
        tmp = True;
    }
    action act_0() {
        tmp = False;
    }
    action firewall212() {
        tmp_0 = True;
    }
    action act_1() {
        tmp_1 = True;
    }
    action act_2() {
        tmp_1 = False;
    }
    action firewall212_0() {
        tmp_0 = tmp_1;
    }
    action firewall212_1() {
        tmp_2 = True;
    }
    action act_3() {
        tmp_3 = True;
    }
    action act_4() {
        tmp_3 = False;
    }
    action firewall212_2() {
        tmp_2 = tmp_3;
    }
    action firewall213() {
        dropped_0 = 1;
    }
    action act_5() {
        tmp_4 = True;
    }
    action act_6() {
        tmp_4 = False;
    }
    action firewall215() {
        tmp_5 = True;
    }
    action act_7() {
        tmp_6 = True;
    }
    action act_8() {
        tmp_6 = False;
    }
    action firewall215_0() {
        tmp_5 = tmp_6;
    }
    action firewall215_1() {
        tmp_7 = True;
    }
    action act_9() {
        tmp_8 = True;
    }
    action act_10() {
        tmp_8 = False;
    }
    action firewall215_2() {
        tmp_7 = tmp_8;
    }
    action firewall216() {
        dropped_0 = 1;
    }
    action act_11() {
        tmp_9 = True;
    }
    action act_12() {
        tmp_9 = False;
    }
    action firewall218() {
        tmp_10 = True;
    }
    action act_13() {
        tmp_11 = True;
    }
    action act_14() {
        tmp_11 = False;
    }
    action firewall218_0() {
        tmp_10 = tmp_11;
    }
    action firewall219() {
        dropped_0 = 1;
    }
    action act_15() {
        tmp_12 = True;
    }
    action act_16() {
        tmp_12 = False;
    }
    action act_17() {
        tmp_14 = True;
    }
    action act_18() {
        tmp_14 = False;
    }
    action firewall222() {
        tmp_13 = tmp_14;
    }
    action firewall222_0() {
        tmp_13 = False;
    }
    action firewall223() {
        dropped_0 = 1;
    }
    action firewall229() {
        standard_metadata.egress_port = standard_metadata.egress_port + 1 && 1;
    }
    action firewall210() {
        dropped_0 = 0;
    }
    table eth_dstMac_filter_0 {
        key = {
            hdr.ethernet.dstAddr: exact;
        }
        actions = {
            drop;
            NoAction_1;
        }
        size = 1024;
        default_action = NoAction_1();
    }
    table eth_srcMac_filter_0 {
        key = {
            hdr.ethernet.srcAddr: exact;
        }
        actions = {
            drop_1;
            NoAction_2;
        }
        size = 1024;
        default_action = NoAction_2();
    }
    table eth_proto_filter_0 {
        key = {
            hdr.ethernet.etherType: exact;
        }
        actions = {
            drop_2;
            NoAction_3;
        }
        size = 1024;
        default_action = NoAction_3();
    }
    table ip_proto_filter_0 {
        key = {
            hdr.ipv4.protocol: exact;
        }
        actions = {
            drop_3;
            NoAction_4;
        }
        size = 1024;
        default_action = NoAction_4();
    }
    table ip_dstIP_filter_0 {
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            drop_4;
            NoAction_5;
        }
        size = 1024;
        default_action = NoAction_5();
    }
    table ip_srcIP_filter_0 {
        key = {
            hdr.ipv4.srcAddr: lpm;
        }
        actions = {
            drop_5;
            NoAction_6;
        }
        size = 1024;
        default_action = NoAction_6();
    }
    table tcp_srcPort_filter_0 {
        key = {
            hdr.tcp._srcPort0: exact;
        }
        actions = {
            drop_6;
            NoAction_7;
        }
        size = 1024;
        default_action = NoAction_7();
    }
    table tcp_dstPort_filter_0 {
        key = {
            hdr.tcp._dstPort1: exact;
        }
        actions = {
            drop_7;
            NoAction_8;
        }
        size = 1024;
        default_action = NoAction_8();
    }
    table udp_srcPort_filter_0 {
        key = {
            hdr.udp.srcPort: exact;
        }
        actions = {
            drop_8;
            NoAction_9;
        }
        size = 1024;
        default_action = NoAction_9();
    }
    table udp_dstPort_filter_0 {
        key = {
            hdr.udp.dstPort: exact;
        }
        actions = {
            drop_9;
            NoAction_10;
        }
        size = 1024;
        default_action = NoAction_10();
    }
    table tbl_firewall210 {
        key = {
        }
        actions = {
            firewall210;
        }
        default_action = firewall210();
    }
    table tbl_act {
        key = {
        }
        actions = {
            act;
        }
        default_action = act();
    }
    table tbl_act_0 {
        key = {
        }
        actions = {
            act_0;
        }
        default_action = act_0();
    }
    table tbl_firewall212 {
        key = {
        }
        actions = {
            firewall212;
        }
        default_action = firewall212();
    }
    table tbl_act_1 {
        key = {
        }
        actions = {
            act_1;
        }
        default_action = act_1();
    }
    table tbl_act_2 {
        key = {
        }
        actions = {
            act_2;
        }
        default_action = act_2();
    }
    table tbl_firewall212_0 {
        key = {
        }
        actions = {
            firewall212_0;
        }
        default_action = firewall212_0();
    }
    table tbl_firewall212_1 {
        key = {
        }
        actions = {
            firewall212_1;
        }
        default_action = firewall212_1();
    }
    table tbl_act_3 {
        key = {
        }
        actions = {
            act_3;
        }
        default_action = act_3();
    }
    table tbl_act_4 {
        key = {
        }
        actions = {
            act_4;
        }
        default_action = act_4();
    }
    table tbl_firewall212_2 {
        key = {
        }
        actions = {
            firewall212_2;
        }
        default_action = firewall212_2();
    }
    table tbl_firewall213 {
        key = {
        }
        actions = {
            firewall213;
        }
        default_action = firewall213();
    }
    table tbl_act_5 {
        key = {
        }
        actions = {
            act_5;
        }
        default_action = act_5();
    }
    table tbl_act_6 {
        key = {
        }
        actions = {
            act_6;
        }
        default_action = act_6();
    }
    table tbl_firewall215 {
        key = {
        }
        actions = {
            firewall215;
        }
        default_action = firewall215();
    }
    table tbl_act_7 {
        key = {
        }
        actions = {
            act_7;
        }
        default_action = act_7();
    }
    table tbl_act_8 {
        key = {
        }
        actions = {
            act_8;
        }
        default_action = act_8();
    }
    table tbl_firewall215_0 {
        key = {
        }
        actions = {
            firewall215_0;
        }
        default_action = firewall215_0();
    }
    table tbl_firewall215_1 {
        key = {
        }
        actions = {
            firewall215_1;
        }
        default_action = firewall215_1();
    }
    table tbl_act_9 {
        key = {
        }
        actions = {
            act_9;
        }
        default_action = act_9();
    }
    table tbl_act_10 {
        key = {
        }
        actions = {
            act_10;
        }
        default_action = act_10();
    }
    table tbl_firewall215_2 {
        key = {
        }
        actions = {
            firewall215_2;
        }
        default_action = firewall215_2();
    }
    table tbl_firewall216 {
        key = {
        }
        actions = {
            firewall216;
        }
        default_action = firewall216();
    }
    table tbl_act_11 {
        key = {
        }
        actions = {
            act_11;
        }
        default_action = act_11();
    }
    table tbl_act_12 {
        key = {
        }
        actions = {
            act_12;
        }
        default_action = act_12();
    }
    table tbl_firewall218 {
        key = {
        }
        actions = {
            firewall218;
        }
        default_action = firewall218();
    }
    table tbl_act_13 {
        key = {
        }
        actions = {
            act_13;
        }
        default_action = act_13();
    }
    table tbl_act_14 {
        key = {
        }
        actions = {
            act_14;
        }
        default_action = act_14();
    }
    table tbl_firewall218_0 {
        key = {
        }
        actions = {
            firewall218_0;
        }
        default_action = firewall218_0();
    }
    table tbl_firewall219 {
        key = {
        }
        actions = {
            firewall219;
        }
        default_action = firewall219();
    }
    table tbl_act_15 {
        key = {
        }
        actions = {
            act_15;
        }
        default_action = act_15();
    }
    table tbl_act_16 {
        key = {
        }
        actions = {
            act_16;
        }
        default_action = act_16();
    }
    table tbl_act_17 {
        key = {
        }
        actions = {
            act_17;
        }
        default_action = act_17();
    }
    table tbl_act_18 {
        key = {
        }
        actions = {
            act_18;
        }
        default_action = act_18();
    }
    table tbl_firewall222 {
        key = {
        }
        actions = {
            firewall222;
        }
        default_action = firewall222();
    }
    table tbl_firewall222_0 {
        key = {
        }
        actions = {
            firewall222_0;
        }
        default_action = firewall222_0();
    }
    table tbl_firewall223 {
        key = {
        }
        actions = {
            firewall223;
        }
        default_action = firewall223();
    }
    table tbl_firewall229 {
        key = {
        }
        actions = {
            firewall229;
        }
        default_action = firewall229();
    }
    apply {
        tbl_firewall210.apply();
        if(hdr.ethernet.isValid()){
            if(eth_srcMac_filter_0.apply().hit){
                tbl_act.apply();
            }
            else{
                tbl_act_0.apply();
            }
            if(tmp){
                tbl_firewall212.apply();
            }
            else{
                if(eth_dstMac_filter_0.apply().hit){
                    tbl_act_1.apply();
                }
                else{
                    tbl_act_2.apply();
                }
                tbl_firewall212_0.apply();
            }
            if(tmp_0){
                tbl_firewall212_1.apply();
            }
            else{
                if(eth_proto_filter_0.apply().hit){
                    tbl_act_3.apply();
                }
                else{
                    tbl_act_4.apply();
                }
                tbl_firewall212_2.apply();
            }
            if(tmp_2){
                tbl_firewall213.apply();
            }
            if(hdr.ipv4.isValid() && dropped_0 == 0){
                if(ip_srcIP_filter_0.apply().hit){
                    tbl_act_5.apply();
                }
                else{
                    tbl_act_6.apply();
                }
                if(tmp_4){
                    tbl_firewall215.apply();
                }
                else{
                    if(ip_dstIP_filter_0.apply().hit){
                        tbl_act_7.apply();
                    }
                    else{
                        tbl_act_8.apply();
                    }
                    tbl_firewall215_0.apply();
                }
                if(tmp_5){
                    tbl_firewall215_1.apply();
                }
                else{
                    if(ip_proto_filter_0.apply().hit){
                        tbl_act_9.apply();
                    }
                    else{
                        tbl_act_10.apply();
                    }
                    tbl_firewall215_2.apply();
                }
                if(tmp_7){
                    tbl_firewall216.apply();
                }
                if(hdr.tcp.isValid() && dropped_0 == 0){
                    if(tcp_srcPort_filter_0.apply().hit){
                        tbl_act_11.apply();
                    }
                    else{
                        tbl_act_12.apply();
                    }
                    if(tmp_9){
                        tbl_firewall218.apply();
                    }
                    else{
                        if(tcp_dstPort_filter_0.apply().hit){
                            tbl_act_13.apply();
                        }
                        else{
                            tbl_act_14.apply();
                        }
                        tbl_firewall218_0.apply();
                    }
                    if(tmp_10){
                        tbl_firewall219.apply();
                    }
                }
                else{
                    if(hdr.udp.isValid() && dropped_0 == 0){
                        if(udp_srcPort_filter_0.apply().hit){
                            tbl_act_15.apply();
                        }
                        else{
                            tbl_act_16.apply();
                        }
                        if(tmp_12){
                            if(udp_dstPort_filter_0.apply().hit){
                                tbl_act_17.apply();
                            }
                            else{
                                tbl_act_18.apply();
                            }
                            tbl_firewall222.apply();
                        }
                        else{
                            tbl_firewall222_0.apply();
                        }
                        if(tmp_13){
                            tbl_firewall223.apply();
                        }
                    }
                }
            }
            if(dropped_0 != 1){
                tbl_firewall229.apply();
            }
        }
    }
}

control DeparserImpl( packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.arp);
        packet.emit(hdr.ipv4);
        packet.emit(hdr.udp);
        packet.emit(hdr.tcp);
        packet.emit(hdr.icmp);
    }
}

control egress(inout headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    apply {
    }
}

control verifyChecksum(inout headers hdr, inout metadata meta) {
    apply {
    }
}

control computeChecksum(inout headers hdr, inout metadata meta) {
    apply {
    }
}