// Autogenerated file (from src/hardware_indep/controlplane.h.py: via hardware_indep/controlplane.h.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#pragma once

#include "dpdk_lib.h"
#include "tables.h"

void make_ipv4_lpm_0_set_default_table_entry(ipv4_lpm_0_action_t* action, const char* action_name, p4_action_parameter_t** action_params);
void make_nexthops_0_set_default_table_entry(nexthops_0_action_t* action, const char* action_name, p4_action_parameter_t** action_params);
