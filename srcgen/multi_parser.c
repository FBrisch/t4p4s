// Autogenerated file (from src/hardware_indep/multi_parser.c.py: via hardware_indep/multi_parser.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include "parser_stages.h"
#include "hdr_fld.h"
#include "hdr_fld_sprintf.h"

#if T4P4S_MULTI_IDX == 0
    void print_parsed_hdr_ethernet(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void print_parsed_hdr_udp(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    void print_parsed_hdr_arp(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void print_parsed_hdr_icmp(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    void print_parsed_hdr_ipv4(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void print_parsed_hdr_tcp(packet_descriptor_t* pd, header_descriptor_t* hdr, header_instance_e hdrinst) {
        #ifdef T4P4S_DEBUG
            char fields_txt[4096];
            if (hdr->size > 0)    sprintf_hdr(fields_txt, pd, hdr);
            debug("   :: Parsed header" T4LIT(#%d) " " T4LIT(%s,header) "/" T4LIT(%d) "B%s%s\n",
            hdr_infos[hdrinst].idx + 1, hdr_infos[hdrinst].name, hdr->size,
            hdr->size == 0 ? "" : ": ",
            hdr->size == 0 ? "" : fields_txt);
        #endif
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    int parser_extract_ethernet(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(ethernet);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (112 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "ethernet", 112, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_ethernet(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    int parser_extract_udp(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(udp);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (64 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "udp", 64, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_udp(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    int parser_extract_arp(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(arp);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (64 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "arp", 64, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_arp(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    int parser_extract_icmp(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(icmp);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (64 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "icmp", 64, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_icmp(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    int parser_extract_ipv4(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(ipv4);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (160 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "ipv4", 160, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_ipv4(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    int parser_extract_tcp(int vwlen, STDPARAMS) {
        parser_state_t* local_vars = pstate;
        header_instance_e hdrinst = HDR(tcp);
        header_descriptor_t* hdr = &(pd->headers[hdrinst]);
        hdr->was_enabled_at_initial_parse = true;
        hdr->size = (160 + vwlen) / 8;
        if (unlikely(pd->parsed_size + hdr->size > pd->wrapper->pkt_len)) {
            cannot_parse_hdr("", "tcp", 160, vwlen, STDPARAMS_IN);
            return PARSED_AFTER_END_OF_PACKET;
        }
        hdr->pointer = pd->extract_ptr;
        print_parsed_hdr_tcp(pd, hdr, hdrinst);
        pd->parsed_size += hdr->size;
        pd->extract_ptr += hdr->size;
        return hdr->size;
    }
#endif // T4P4S_MULTI_IDX == 1

