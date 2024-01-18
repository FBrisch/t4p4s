/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

const bit<16> TYPE_IPV4 = 0x800;

/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<32> vlan;
    bit<16>   etherType;
}

header ipv4_t {
    bit<4>    version;
    bit<4>    ihl;
    bit<8>    diffserv;
    bit<16>   totalLen;
    bit<16>   identification;
    bit<3>    flags;
    bit<13>   fragOffset;
    bit<8>    ttl;
    bit<8>    protocol;
    bit<16>   hdrChecksum;
    ip4Addr_t srcAddr;
    ip4Addr_t dstAddr;
}

// New header type for transfering needed data
header dissaggregation_header_t {
    egressSpec_t port;
    bit<7> padding;
}


struct metadata {
    bit<1> tunnelID;
    egressSpec_t port; 
}

struct headers {
    ethernet_t   ethernet;
    ipv4_t       ipv4;
    dissaggregation_header_t  dissaggregation_header; // New header for transfering needed data
}

/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        packet.extract(hdr.ethernet);
        packet.extract(hdr.ipv4);
        transition accept;
    }


}

/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

control MyVerifyChecksum(inout headers hdr, inout metadata meta) {   
    apply {  }
}


/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {
    action drop() {
        mark_to_drop(standard_metadata);
    }
    
    bit<32> meterValue;
    direct_meter<bit<32>>(MeterType.packets) NF1_meter;
    direct_meter<bit<32>>(MeterType.packets) NF2_meter;
        
    action chg_addr(egressSpec_t port, macAddr_t dstAddr) {
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        standard_metadata.egress_spec = 2;
        meta.port = port;
    }
    
    table ipv4_lpm1 {
        key = {
            hdr.ipv4.dstAddr: lpm;
        }
        actions = {
            chg_addr;
            drop;
            NoAction;
        }
        size = 1024;
        default_action = drop();
    }

    action set_tunnelid(bit<1> tunnelid){
        meta.tunnelID = tunnelid;
    }

    table tunnelident {
        key = {
            hdr.ethernet.vlan: exact;
        }
        actions = {
            set_tunnelid;
            drop;
        }
        size = 1024;
        default_action = drop();
    }

    
    apply {
        tunnelident.apply();
      if(meta.tunnelID == 1){
        NF1_meter.read(meterValue);
        if(meterValue == 0){
            ipv4_lpm1.apply();
        }else{
            drop();
        }
      }else{
        NF2_meter.read(meterValue);
        if(meterValue == 0){
            /pipeline 2
        }else{
            drop();
        }
      }
    }
}

/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {
    apply {  }
}

/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/

control MyComputeChecksum(inout headers  hdr, inout metadata meta) {
     apply { }
}

/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.ipv4);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/

V1Switch(
MyParser(),
MyVerifyChecksum(),
MyIngress(),
MyEgress(),
MyComputeChecksum(),
MyDeparser()
) main;
