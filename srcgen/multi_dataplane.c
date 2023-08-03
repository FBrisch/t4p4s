// Autogenerated file (from src/hardware_indep/multi_dataplane.c.py: via hardware_indep/multi_dataplane.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include "dataplane_impl.h"
#include "gen_model.h"

#include "dpdk_smem.h"

#if T4P4S_MULTI_IDX == 0
    apply_result_t ipv4_lpm_0_apply(STDPARAMS) {
        #ifdef T4P4S_DEBUG
            char key_txt[4096];
            int key_txt_idx = 0;
        #endif
        uint8_t key[4];
        table_ipv4_lpm_0_key(pd, key  KEYTXTPARAMS_IN);
        ENTRY(ipv4_lpm_0)* entry = (ENTRY(ipv4_lpm_0)*)lpm_lookup(tables[TABLE_ipv4_lpm_0], key);
        bool is_hit = entry->id != action_NoAction_1;
        if (likely(is_hit)) {
            ENTRY(ipv4_lpm_0)* default_entry = ipv4_lpm_0_get_default_entry(STDPARAMS_IN);
            is_hit = entry != default_entry;
        }
        #ifdef T4P4S_DEBUG
            ipv4_lpm_0_apply_show_hit_with_key(is_hit, entry  KEYTXTPARAM_IN, STDPARAMS_IN);
        #endif
        #ifdef T4P4S_STATS
            t4p4s_stats_global.T4STAT(table,hit,ipv4_lpm_0) = is_hit || t4p4s_stats_global.T4STAT(table,hit,ipv4_lpm_0);
            t4p4s_stats_global.T4STAT(table,miss,ipv4_lpm_0) = !is_hit || t4p4s_stats_global.T4STAT(table,miss,ipv4_lpm_0);
            t4p4s_stats_per_packet.T4STAT(table,hit,ipv4_lpm_0) = is_hit || t4p4s_stats_per_packet.T4STAT(table,hit,ipv4_lpm_0);
            t4p4s_stats_per_packet.T4STAT(table,miss,ipv4_lpm_0) = !is_hit || t4p4s_stats_per_packet.T4STAT(table,miss,ipv4_lpm_0);
        #endif
        ipv4_lpm_0_stats(entry->id, STDPARAMS_IN);
        switch (entry->id) {
            case action_set_nhop:
                action_code_set_nhop(entry->params.set_nhop_params, SHORT_STDPARAMS_IN);
            return (apply_result_t) { is_hit, entry->id };
            case action__drop:
                action_code__drop(entry->params._drop_params, SHORT_STDPARAMS_IN);
            return (apply_result_t) { is_hit, entry->id };
            case action_NoAction_1:
                return (apply_result_t) { is_hit, entry->id };
            
            default: return (apply_result_t) {}; // unreachable
        }
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    apply_result_t nexthops_0_apply(STDPARAMS) {
        #ifdef T4P4S_DEBUG
            char key_txt[4096];
            int key_txt_idx = 0;
        #endif
        uint8_t key[4];
        table_nexthops_0_key(pd, key  KEYTXTPARAMS_IN);
        ENTRY(nexthops_0)* entry = (ENTRY(nexthops_0)*)exact_lookup(tables[TABLE_nexthops_0], key);
        bool is_hit = entry->id != action_NoAction_2;
        if (likely(is_hit)) {
            ENTRY(nexthops_0)* default_entry = nexthops_0_get_default_entry(STDPARAMS_IN);
            is_hit = entry != default_entry;
        }
        #ifdef T4P4S_DEBUG
            nexthops_0_apply_show_hit_with_key(is_hit, entry  KEYTXTPARAM_IN, STDPARAMS_IN);
        #endif
        #ifdef T4P4S_STATS
            t4p4s_stats_global.T4STAT(table,hit,nexthops_0) = is_hit || t4p4s_stats_global.T4STAT(table,hit,nexthops_0);
            t4p4s_stats_global.T4STAT(table,miss,nexthops_0) = !is_hit || t4p4s_stats_global.T4STAT(table,miss,nexthops_0);
            t4p4s_stats_per_packet.T4STAT(table,hit,nexthops_0) = is_hit || t4p4s_stats_per_packet.T4STAT(table,hit,nexthops_0);
            t4p4s_stats_per_packet.T4STAT(table,miss,nexthops_0) = !is_hit || t4p4s_stats_per_packet.T4STAT(table,miss,nexthops_0);
        #endif
        nexthops_0_stats(entry->id, STDPARAMS_IN);
        switch (entry->id) {
            case action_forward:
                action_code_forward(entry->params.forward_params, SHORT_STDPARAMS_IN);
            return (apply_result_t) { is_hit, entry->id };
            case action__drop_1:
                action_code__drop_1(entry->params._drop_1_params, SHORT_STDPARAMS_IN);
            return (apply_result_t) { is_hit, entry->id };
            case action_NoAction_2:
                return (apply_result_t) { is_hit, entry->id };
            
            default: return (apply_result_t) {}; // unreachable
        }
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    void control_stage_ingress_0(control_locals_ingress_t* local_vars, STDPARAMS) {
ipv4_lpm_0_apply(STDPARAMS_IN)
;
;
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void control_stage_ingress_1(control_locals_ingress_t* local_vars, STDPARAMS) {
nexthops_0_apply(STDPARAMS_IN)
;
;
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    void control_stage_DeparserImpl_0(control_locals_DeparserImpl_t* local_vars, STDPARAMS) {
pd->header_reorder[pd->deparse_hdrinst_count] = HDR(ethernet);
++pd->deparse_hdrinst_count;
/* done calling gen_emit */
;
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void control_stage_DeparserImpl_1(control_locals_DeparserImpl_t* local_vars, STDPARAMS) {
pd->header_reorder[pd->deparse_hdrinst_count] = HDR(ipv4);
++pd->deparse_hdrinst_count;
/* done calling gen_emit */
;
    }
#endif // T4P4S_MULTI_IDX == 1

#if T4P4S_MULTI_IDX == 0
    void control_stage_verifyChecksum_0(control_locals_verifyChecksum_t* local_vars, STDPARAMS) {

 
 if (likely(is_header_valid(HDR(ipv4), pd))) {
     
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(versionIhl,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(diffserv,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(totalLen,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(identification,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(fragOffset,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(ttl,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(protocol,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(srcAddr,field) ", returning \"unspecified\" value " T4LIT(0x6c2fc190 /* pseudorandom 32 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(dstAddr,field) ", returning \"unspecified\" value " T4LIT(0x6c2fc190 /* pseudorandom 32 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 tuple_0_t struct_tuple_0_272560 = (tuple_0_t) {.f0 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,versionIhl), 0xed /* pseudorandom 8 bit value */),.f1 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,diffserv), 0xed /* pseudorandom 8 bit value */),.f2 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,totalLen), 0x2dc0 /* pseudorandom 16 bit value */),.f3 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,identification), 0x2dc0 /* pseudorandom 16 bit value */),.f4 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,fragOffset), 0x2dc0 /* pseudorandom 16 bit value */),.f5 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,ttl), 0xed /* pseudorandom 8 bit value */),.f6 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,protocol), 0xed /* pseudorandom 8 bit value */),.f7 = (uint32_t)GET32_def(src_pkt(pd), FLD(ipv4,srcAddr), 0x6c2fc190 /* pseudorandom 32 bit value */),.f8 = (uint32_t)GET32_def(src_pkt(pd), FLD(ipv4,dstAddr), 0x6c2fc190 /* pseudorandom 32 bit value */),};
SHORT_EXTERNCALL2(verify_checksum,tuple_0,u16)(is_header_valid(HDR(ipv4), pd), &struct_tuple_0_272560, (uint16_t)get_handle_fld(pd, FLD(ipv4, hdrChecksum), "parameter").pointer, enum_HashAlgorithm_csum16, SHORT_STDPARAMS_IN);
;
 }
    }
#endif // T4P4S_MULTI_IDX == 0

#if T4P4S_MULTI_IDX == 1
    void control_stage_computeChecksum_0(control_locals_computeChecksum_t* local_vars, STDPARAMS) {

 
 if (likely(is_header_valid(HDR(ipv4), pd))) {
     
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(versionIhl,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(diffserv,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(totalLen,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(identification,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(fragOffset,field) ", returning \"unspecified\" value " T4LIT(0x2dc0 /* pseudorandom 16 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(ttl,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(protocol,field) ", returning \"unspecified\" value " T4LIT(0xed /* pseudorandom 8 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(srcAddr,field) ", returning \"unspecified\" value " T4LIT(0x6c2fc190 /* pseudorandom 32 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 if (unlikely(!is_header_valid(HDR(ipv4), pd))) {
     debug("   " T4LIT(!!,warning) " Access to field in invalid header " T4LIT(%s,warning) "." T4LIT(dstAddr,field) ", returning \"unspecified\" value " T4LIT(0x6c2fc190 /* pseudorandom 32 bit value */) "\n", hdr_infos[HDR(ipv4)].name);
 }
 tuple_0_t struct_tuple_0_272653 = (tuple_0_t) {.f0 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,versionIhl), 0xed /* pseudorandom 8 bit value */),.f1 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,diffserv), 0xed /* pseudorandom 8 bit value */),.f2 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,totalLen), 0x2dc0 /* pseudorandom 16 bit value */),.f3 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,identification), 0x2dc0 /* pseudorandom 16 bit value */),.f4 = (uint16_t)GET32_def(src_pkt(pd), FLD(ipv4,fragOffset), 0x2dc0 /* pseudorandom 16 bit value */),.f5 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,ttl), 0xed /* pseudorandom 8 bit value */),.f6 = (uint8_t)GET32_def(src_pkt(pd), FLD(ipv4,protocol), 0xed /* pseudorandom 8 bit value */),.f7 = (uint32_t)GET32_def(src_pkt(pd), FLD(ipv4,srcAddr), 0x6c2fc190 /* pseudorandom 32 bit value */),.f8 = (uint32_t)GET32_def(src_pkt(pd), FLD(ipv4,dstAddr), 0x6c2fc190 /* pseudorandom 32 bit value */),};
SHORT_EXTERNCALL2(update_checksum,tuple_0,u16)(is_header_valid(HDR(ipv4), pd), &struct_tuple_0_272653, (uint16_t)get_handle_fld(pd, FLD(ipv4, hdrChecksum), "parameter").pointer, enum_HashAlgorithm_csum16, SHORT_STDPARAMS_IN);
;
 }
    }
#endif // T4P4S_MULTI_IDX == 1
