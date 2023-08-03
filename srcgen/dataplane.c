// Autogenerated file (from src/hardware_indep/dataplane.c.py: via hardware_indep/dataplane.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include "gen_include.h"
#include "dataplane_impl.h"
#include "dataplane.h"
#include "dataplane_stages.h"
#include "hdr_fld.h"

#include "dpdk_smem.h"

void parser_state_ParserImpl_start(STDPARAMS);

void reset_vw_fields(SHORT_STDPARAMS) {
}

void reset_headers(SHORT_STDPARAMS) {
    pd->is_deparse_reordering = false;
    pd->headers[HDR(ethernet)].pointer = NULL;
    pd->headers[HDR(ipv4)].pointer = NULL;
    pd->headers[HDR(arp)].pointer = NULL;
    // reset metadatas
    memset(pd->headers[HDR(all_metadatas)].pointer, 0, hdr_infos[HDR(all_metadatas)].byte_width * sizeof(uint8_t));
    
    reset_vw_fields(SHORT_STDPARAMS_IN);
}

void init_header(header_instance_e hdrinst, const char* hdrname, SHORT_STDPARAMS) {
    pd->headers[hdrinst] = (header_descriptor_t) {
        .type = hdrinst,
        .size = hdr_infos[hdrinst].byte_width,
        .pointer = NULL,
        .vw_size = 0,
        #ifdef T4P4S_DEBUG
        .name = hdrname,
        #endif
    };
}

void init_metadata_header(SHORT_STDPARAMS) {
    pd->headers[HDR(all_metadatas)] = (header_descriptor_t) {
        .type = HDR(all_metadatas),
        .size = hdr_infos[HDR(all_metadatas)].byte_width * 8,
        .pointer = rte_malloc("all_metadatas_t", hdr_infos[HDR(all_metadatas)].byte_width * sizeof(uint8_t), 0),
        .vw_size = 0,
    };
}

void init_headers(SHORT_STDPARAMS) {
    init_header(HDR(ethernet), "ethernet", SHORT_STDPARAMS_IN);
    init_header(HDR(ipv4), "ipv4", SHORT_STDPARAMS_IN);
    init_header(HDR(arp), "arp", SHORT_STDPARAMS_IN);
    init_metadata_header(SHORT_STDPARAMS_IN);
}

void init_dataplane(SHORT_STDPARAMS) {
    init_headers(SHORT_STDPARAMS_IN);
    reset_headers(SHORT_STDPARAMS_IN);
    
    MODIFY(dst_pkt(pd), EGRESS_META_FLD, src_32(EGRESS_INIT_VALUE), ENDIAN_KEEP);
}

// skipping method generation for empty control egress
void control_ingress(STDPARAMS)  {
    control_locals_ingress_t local_vars_struct;
    pd->control_locals = (void*)&local_vars_struct;
    control_stage_ingress_0(&local_vars_struct, STDPARAMS_IN);
    control_stage_ingress_1(&local_vars_struct, STDPARAMS_IN);
}

void control_DeparserImpl(STDPARAMS)  {
    control_locals_DeparserImpl_t local_vars_struct;
    pd->control_locals = (void*)&local_vars_struct;
    control_stage_DeparserImpl_0(&local_vars_struct, STDPARAMS_IN);
    control_stage_DeparserImpl_1(&local_vars_struct, STDPARAMS_IN);
}

void control_verifyChecksum(STDPARAMS)  {
    control_locals_verifyChecksum_t local_vars_struct;
    pd->control_locals = (void*)&local_vars_struct;
    control_stage_verifyChecksum_0(&local_vars_struct, STDPARAMS_IN);
}

void control_computeChecksum(STDPARAMS)  {
    control_locals_computeChecksum_t local_vars_struct;
    pd->control_locals = (void*)&local_vars_struct;
    control_stage_computeChecksum_0(&local_vars_struct, STDPARAMS_IN);
}

void process_packet(STDPARAMS) {
parser_state_ParserImpl_start(STDPARAMS_IN);
if (unlikely(is_packet_dropped(pd)))   return;
control_verifyChecksum(STDPARAMS_IN);
control_ingress(STDPARAMS_IN);
// control egress is empty
control_computeChecksum(STDPARAMS_IN);
control_DeparserImpl(STDPARAMS_IN);
}

extern void deparse_packet(SHORT_STDPARAMS);

void handle_packet(uint32_t portid, int pkt_idx, STDPARAMS)
{
    reset_headers(SHORT_STDPARAMS_IN);
    set_handle_packet_metadata(pd, portid);
    
    dbg_bytes(pd->data, packet_size(pd), "Handling packet " T4LIT(#%03d) " (port " T4LIT(%d,port) ", " T4LIT(%02dB) "): ", pkt_idx, get_ingress_port(pd), packet_size(pd));
    
    pd->parsed_size = 0;
    pd->extract_ptr = pd->data;
    
    pd->deparse_hdrinst_count = 0;
    
    process_packet(STDPARAMS_IN);
    
    deparse_packet(SHORT_STDPARAMS_IN);
}
