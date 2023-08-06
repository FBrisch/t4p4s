// Autogenerated file (from src/hardware_indep/parser.c.py: via hardware_indep/parser.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include "dpdk_lib.h"
#include "util_packet.h"
#include "gen_include.h"
#include "parser_stages.h"

#ifdef T4P4S_STATS
    extern t4p4s_stats_t t4p4s_stats_global;
    extern t4p4s_stats_t t4p4s_stats_per_packet;
#endif

void gen_parse_drop_msg(int apparent_hdr_len, const char* hdrname, int max_stkhdr_count) {
    if (apparent_hdr_len == PARSED_AFTER_END_OF_PACKET) {
        debug("   " T4LIT(XX,status) " " T4LIT(Dropping packet,status) ": tried to parse " T4LIT(%s,header) " but it overshot the end of the packet\n", hdrname);
        } else if (apparent_hdr_len == PARSED_OVER_STACK_SIZE) {
        debug("   " T4LIT(XX,status) " " T4LIT(Dropping packet,status) ": cannot have more than " T4LIT(%d) " headers in stack " T4LIT(%s,header) "\n", max_stkhdr_count, hdrname);
        } else {
        debug("   " T4LIT(XX,status) " " T4LIT(Dropping packet,status) ": its length is negative (%d)\n", apparent_hdr_len);
    }
}

void drop_packet(STDPARAMS) {
    MODIFY(dst_pkt(pd), EGRESS_META_FLD, src_32(EGRESS_DROP_VALUE), ENDIAN_KEEP);
}

#ifdef T4P4S_DEBUG
    char transition_cond[1024];
    
    void set_transition_txt(const char* transition_txt) {
        strcpy(transition_cond, transition_txt);
    }
    #else
    void set_transition_txt(const char* transition_txt) {
        // do nothing
    }
#endif

void check_hdr_valid(packet_descriptor_t* pd, field_instance_e fld, const char* unspec) {
    #ifdef T4P4S_DEBUG
        header_instance_e hdr = fld_infos[fld].header_instance;
        if (unlikely(!is_header_valid(hdr, pd))) {
            const char* hdrname = hdr_infos[hdr].name;
            const char* fldname = field_names[fld];
            debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(%s,field) ", returning \"unspecified\" value " T4LIT(%s) "\n", hdrname, fldname, unspec);
        }
    #endif
}

void init_parser_state(parser_state_t* pstate) {
    set_transition_txt("");
}

void cannot_parse_hdr(const char* varwidth_txt, const char* hdr_name, int hdrlen, int vwlen, STDPARAMS) {
    #ifdef T4P4S_DEBUG
        int total_bytes = (hdrlen + vwlen) / 8;
        if (pd->parsed_size == pd->wrapper->pkt_len) {
            debug("    " T4LIT(!,warning) " Missing %sheader " T4LIT(%s,header) "/" T4LIT(%d) "+" T4LIT(%d) "B at offset " T4LIT(%d) "\n",
            varwidth_txt, hdr_name, (hdrlen+7) / 8, (vwlen+7) / 8, pd->parsed_size);
            } else {
            debug("    " T4LIT(!,warning) " Trying to parse %sheader " T4LIT(%s,header) "/" T4LIT(%d) "+" T4LIT(%d) "B at offset " T4LIT(%d) ", " T4LIT(missing %d bytes,warning) "\n",
            varwidth_txt, hdr_name, (hdrlen+7) / 8, (vwlen+7) / 8, pd->parsed_size, pd->parsed_size + total_bytes - pd->wrapper->pkt_len);
        }
    #endif
}

void parser_state_ParserImpl_parse_arp(STDPARAMS);
void parser_state_ParserImpl_parse_icmp(STDPARAMS);
void parser_state_ParserImpl_parse_tcp(STDPARAMS);
void parser_state_ParserImpl_parse_udp(STDPARAMS);
void parser_state_ParserImpl_parse_ipv4(STDPARAMS);
void parser_state_ParserImpl_start(STDPARAMS);
void parser_state_ParserImpl_accept(STDPARAMS);
void parser_state_ParserImpl_reject(STDPARAMS);

void print_missed_transition_conditions(const char*const* texts, int idx) {
    #ifdef T4P4S_SHOW_MISSED_TRANSITION_CONDITIONS
        for (int i = 0; i < idx; ++i) {
            if (!strcmp("", texts[i]))    continue;
            debug("   %%%% Transition condition " T4LIT(not met,status) ": %s\n", texts[i]);
        }
    #endif
}

void parser_state_ParserImpl_parse_arp_next_state(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    parser_state_t parameters = *pstate;
    if (unlikely(!is_header_valid(HDR(arp), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(oper,field) ", returning \"unspecified\" value " T4LIT(0xf4f3 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(arp)].name);
 }
 uint16_t Member647542_arp__oper = (GET32_def(src_pkt(pd), FLD(arp,oper), 0xf4f3 /* pseudorandom 16 bit value */));
 const char*const transition_texts[] = {
     " <== " T4LIT(arp,header) "." T4LIT(oper,field) "/" T4LIT(16) "b=" T4LIT(1)  " ",
     "" /* no transition condition */,
 };
if (Member647542_arp__oper == 1) { // select case #1
    print_missed_transition_conditions(transition_texts, 0);
    set_transition_txt(transition_texts[0]);
    parser_state_ParserImpl_accept(STDPARAMS_IN);
    } else if (true /* default */) { // select case #2
    print_missed_transition_conditions(transition_texts, 1);
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}
    
}

void parser_state_ParserImpl_parse_ipv4_next_state(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    parser_state_t parameters = *pstate;
    if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(protocol,field) ", returning \"unspecified\" value " T4LIT(0xe8 /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 uint8_t Member647573_ipv4__protocol = (GET32_def(src_pkt(pd), FLD(ipv4,protocol), 0xe8 /* pseudorandom 8 bit value */));
 const char*const transition_texts[] = {
     " <== " T4LIT(ipv4,header) "." T4LIT(protocol,field) "/" T4LIT(8) "b=" T4LIT(1)  " ",
     " <== " T4LIT(ipv4,header) "." T4LIT(protocol,field) "/" T4LIT(8) "b=" T4LIT(6)  " ",
     " <== " T4LIT(ipv4,header) "." T4LIT(protocol,field) "/" T4LIT(8) "b=" T4LIT(17) "=" T4LIT(0x11,bytes) " ",
     "" /* no transition condition */,
 };
if (Member647573_ipv4__protocol == 1) { // select case #1
    print_missed_transition_conditions(transition_texts, 0);
    set_transition_txt(transition_texts[0]);
    parser_state_ParserImpl_parse_icmp(STDPARAMS_IN);
    } else if (Member647573_ipv4__protocol == 6) { // select case #2
    print_missed_transition_conditions(transition_texts, 1);
    set_transition_txt(transition_texts[1]);
    parser_state_ParserImpl_parse_tcp(STDPARAMS_IN);
    } else if (Member647573_ipv4__protocol == 17) { // select case #3
    print_missed_transition_conditions(transition_texts, 2);
    set_transition_txt(transition_texts[2]);
    parser_state_ParserImpl_parse_udp(STDPARAMS_IN);
    } else if (true /* default */) { // select case #4
    print_missed_transition_conditions(transition_texts, 3);
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}
    
}

void parser_state_ParserImpl_start_next_state(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    parser_state_t parameters = *pstate;
    if (unlikely(!is_header_valid(HDR(ethernet), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(etherType,field) ", returning \"unspecified\" value " T4LIT(0xf4f3 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ethernet)].name);
 }
 uint16_t Member647507_ethernet__etherType = (GET32_def(src_pkt(pd), FLD(ethernet,etherType), 0xf4f3 /* pseudorandom 16 bit value */));
 const char*const transition_texts[] = {
     " <== " T4LIT(ethernet,header) "." T4LIT(etherType,field) "/" T4LIT(16) "b=" T4LIT(2054) "=" T4LIT(0x0806,bytes) " ",
     " <== " T4LIT(ethernet,header) "." T4LIT(etherType,field) "/" T4LIT(16) "b=" T4LIT(2048) "=" T4LIT(0x0800,bytes) " ",
     "" /* no transition condition */,
 };
if (Member647507_ethernet__etherType == 0x806) { // select case #1
    print_missed_transition_conditions(transition_texts, 0);
    set_transition_txt(transition_texts[0]);
    parser_state_ParserImpl_parse_arp(STDPARAMS_IN);
    } else if (Member647507_ethernet__etherType == 0x800) { // select case #2
    print_missed_transition_conditions(transition_texts, 1);
    set_transition_txt(transition_texts[1]);
    parser_state_ParserImpl_parse_ipv4(STDPARAMS_IN);
    } else if (true /* default */) { // select case #3
    print_missed_transition_conditions(transition_texts, 2);
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}
    
}

bool parser_state_ParserImpl_parse_arp_000_extract_arp(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0024 = 0;
    int arp_len = parser_extract_arp(vwlen_0024, STDPARAMS_IN);
    if (unlikely(arp_len < 0)) {
        gen_parse_drop_msg(arp_len, "arp", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

bool parser_state_ParserImpl_parse_icmp_000_extract_icmp(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0025 = 0;
    int icmp_len = parser_extract_icmp(vwlen_0025, STDPARAMS_IN);
    if (unlikely(icmp_len < 0)) {
        gen_parse_drop_msg(icmp_len, "icmp", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

bool parser_state_ParserImpl_parse_tcp_000_extract_tcp(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0026 = 0;
    int tcp_len = parser_extract_tcp(vwlen_0026, STDPARAMS_IN);
    if (unlikely(tcp_len < 0)) {
        gen_parse_drop_msg(tcp_len, "tcp", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

bool parser_state_ParserImpl_parse_udp_000_extract_udp(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0027 = 0;
    int udp_len = parser_extract_udp(vwlen_0027, STDPARAMS_IN);
    if (unlikely(udp_len < 0)) {
        gen_parse_drop_msg(udp_len, "udp", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

bool parser_state_ParserImpl_parse_ipv4_000_extract_ipv4(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0028 = 0;
    int ipv4_len = parser_extract_ipv4(vwlen_0028, STDPARAMS_IN);
    if (unlikely(ipv4_len < 0)) {
        gen_parse_drop_msg(ipv4_len, "ipv4", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

bool parser_state_ParserImpl_start_000_extract_ethernet(STDPARAMS) {
    parser_state_t* local_vars = pstate;
    int vwlen_0029 = 0;
    int ethernet_len = parser_extract_ethernet(vwlen_0029, STDPARAMS_IN);
    if (unlikely(ethernet_len < 0)) {
        gen_parse_drop_msg(ethernet_len, "ethernet", -1 /* ignored */);
        drop_packet(STDPARAMS_IN);
        return false;
    }
    return true;
}

int get_active_hdr_count(STDPARAMS) {
    int retval = 0;
    for (int i = 0; i < 6; ++i) {
        retval += is_header_valid(i, pd) ? 1 : 0;
    }
    return retval;
}

void print_parsing_success(STDPARAMS) {
    #ifdef T4P4S_DEBUG
        int hdr_count = get_active_hdr_count(STDPARAMS_IN);
        if (pd->payload_size > 0) {
            dbg_bytes(pd->data + pd->parsed_size, pd->payload_size, " " T4LIT(%%%%%%%%,success) " Packet is " T4LIT(accepted,success) ", " T4LIT(%d) "B in " T4LIT(%d) " header%s, " T4LIT(%d) "B of payload: ", pd->parsed_size, hdr_count, hdr_count != 1 ? "s" : "", pd->payload_size);
            } else {
            debug(" " T4LIT(%%%%%%%%,success) " Packet is " T4LIT(accepted,success) ", " T4LIT(%d) "B in " T4LIT(%d) " header%s, " T4LIT(empty payload) "\n", pd->parsed_size, hdr_count, hdr_count != 1 ? "s" : "");
        }
        
        if (hdr_count == 0) {
            debug("   " T4LIT(!! No headers were found,warning) " during parsing, the packet solely consists of payload\n");
        }
    #endif
}

void parser_state_ParserImpl_parse_arp(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,parse_arp) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,parse_arp) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(parse_arp,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_parse_arp_000_extract_arp(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_parse_arp_next_state(STDPARAMS_IN);
}

void parser_state_ParserImpl_parse_icmp(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,parse_icmp) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,parse_icmp) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(parse_icmp,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_parse_icmp_000_extract_icmp(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}

void parser_state_ParserImpl_parse_tcp(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,parse_tcp) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,parse_tcp) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(parse_tcp,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_parse_tcp_000_extract_tcp(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}

void parser_state_ParserImpl_parse_udp(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,parse_udp) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,parse_udp) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(parse_udp,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_parse_udp_000_extract_udp(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_accept(STDPARAMS_IN);
}

void parser_state_ParserImpl_parse_ipv4(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,parse_ipv4) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,parse_ipv4) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(parse_ipv4,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_parse_ipv4_000_extract_ipv4(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_parse_ipv4_next_state(STDPARAMS_IN);
}

void parser_state_ParserImpl_start(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,start) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,start) = true;
    #endif
    
    debug(" %%%%%%%% Parser state " T4LIT(start,parserstate) "%s\n", transition_cond);
    set_transition_txt("");
    bool success0 = parser_state_ParserImpl_start_000_extract_ethernet(STDPARAMS_IN);
    if (unlikely(!success0)) {
        debug("    " T4LIT(!,error) " Parsing " T4LIT(failed,error) ", " T4LIT(dropping,status) " packet\n");
        return;
    }
    parser_state_ParserImpl_start_next_state(STDPARAMS_IN);
}

void parser_state_ParserImpl_accept(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,accept) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,accept) = true;
    #endif
    
    pd->payload_size = packet_size(pd) - (pd->extract_ptr - (void*)pd->data);
    print_parsing_success(STDPARAMS_IN);
}

void parser_state_ParserImpl_reject(STDPARAMS) {
    #ifdef T4P4S_STATS
        t4p4s_stats_global.T4STAT(parser,state,reject) = true;
        t4p4s_stats_per_packet.T4STAT(parser,state,reject) = true;
    #endif
    
    debug(" " T4LIT(XXXX,status) " Parser state " T4LIT(reject,parserstate) " %s\n", transition_cond);
    debug("   " T4LIT(XX,status) " Packet is " T4LIT(dropped,status) "\n");
    drop_packet(STDPARAMS_IN);
}

