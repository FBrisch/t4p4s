/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

#define SRH_SID_MAX 4
typedef bit<16> ether_type_t;
const ether_type_t ETHERTYPE_IPV4 = 16w0x0800;
const ether_type_t ETHERTYPE_ARP = 16w0x0806;
const ether_type_t ETHERTYPE_IPV6 = 16w0x86dd;
const ether_type_t ETHERTYPE_VLAN = 16w0x8100;

typedef bit<8> ip_protocol_t;
const ip_protocol_t IP_PROTOCOLS_ICMP = 1;
const ip_protocol_t IP_PROTOCOLS_TCP = 6;
const ip_protocol_t IP_PROTOCOLS_UDP = 17;
const ip_protocol_t IP_PROTOCOLS_ROUTE = 43; // Routing Header for IPv6
/********************** H E A D E R S  **********************************/
header ipv6_srh_h {
    bit<8> next_hdr;
    bit<8> hdr_ext_len;
    bit<8> routing_type;
    bit<8> seg_left;
    bit<8> last_entry;
    bit<8> flags;
    bit<12> tag;
    bit<4> gtpMessageType;
}

header ipv6_srh_segment_h {
    bit<128> sid;
}

struct metadata {
    bit<128> next_sid;
}

struct headers {
    ipv6_srh_h srh; 
    ipv6_srh_segment_h srh_sid_0; 
    ipv6_srh_segment_h srh_sid_1; 
    ipv6_srh_segment_h srh_sid_2; 
    ipv6_srh_segment_h srh_sid_3; 

}

/********************* P A R S E R  *************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        transition parse_srh;
    }
	
    state parse_srh {
        packet.extract(hdr.srh);
        transition parse_srh_sid_0;
    }
    #define PARSE_SRH_SID(curr, next)               \
    state parse_srh_sid_##curr {                \
        packet.extract(hdr.srh_sid_##curr);         \
        transition select(hdr.srh.last_entry) {  \
            curr : parse_srh_next_header;       \
            default : parse_srh_sid_##next;     \
        }                                       \
    }                                           \
    // switch_srv6.p4:SRH_SID_MAX 4
    PARSE_SRH_SID(0, 1)
    PARSE_SRH_SID(1, 2)
    PARSE_SRH_SID(2, 3)
    state parse_srh_sid_3 {
        packet.extract(hdr.srh_sid_3);
        transition select(hdr.srh.last_entry) {
            3 : parse_srh_next_header;
        }
    }
    state parse_srh_next_header {
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
        mark_to_drop();
    }
    
    bit<32> meterValue = 0;
    meter(2, MeterType.packets) segmentMeter;
    counter(2, CounterType.packets) c;
    action set_nextsid_1() {
        meta.next_sid = hdr.srh_sid_0.sid;
    }
    action set_nextsid_2() {
        meta.next_sid = hdr.srh_sid_1.sid;
    }
    action set_nextsid_3() {
        meta.next_sid = hdr.srh_sid_2.sid;
    }
    action set_nextsid_4() {
        meta.next_sid = hdr.srh_sid_3.sid;
    }
    
    table srv6_set_nextsid { // helper table
        key = {
            hdr.srh.seg_left : exact;
        }
        size = 8;
        actions = {
            NoAction;
            set_nextsid_1;
            set_nextsid_2;
            set_nextsid_3;
            set_nextsid_4;
        }
        const default_action = NoAction;
        //const entries = {
        //    (1 &&& 0xff) : set_nextsid_1();
        //    (2 &&& 0xff) : set_nextsid_2();
        //    (3 &&& 0xff) : set_nextsid_3();
        //    (4 &&& 0xff) : set_nextsid_4();
        //}
    }

    
    apply {
       if (hdr.srh.isValid()) {
            srv6_set_nextsid.apply();
            if(meta.next_sid == 1){
                //segmentMeter.execute_meter<bit<32>>(0,meterValue);
                if(meterValue == 0){
                    c.count(0);
                }else{
                    drop();
                }
            }else{
                //segmentMeter.execute_meter<bit<32>>(1,meterValue);
                if(meterValue == 0){
                    c.count(1);
                }else{
                    drop();
                }
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
