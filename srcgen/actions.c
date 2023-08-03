// Autogenerated file (from src/hardware_indep/actions.c.py: via hardware_indep/actions.c.py), do not modify directly.
// Generator: T4P4S (https://github.com/P4ELTE/t4p4s/)

#include <unistd.h>

#include "dpdk_lib.h"
#include "actions.h"
#include "util_debug.h"
#include "util_packet.h"

extern ctrl_plane_backend bg;

#define STD_DIGEST_RECEIVER_ID 1024

const char* action_names[] = {
    "set_nhop",
    "_drop",
    "NoAction_1",
    "forward",
    "_drop_1",
    "NoAction_2",
};

const char* action_canonical_names[] = {
    ".set_nhop",
    "._drop",
    ".NoAction",
    ".forward",
    "._drop",
    ".NoAction",
};

const char* action_short_names[] = {
    "set_nhop",
    "._drop",
    ".NoAction",
    "forward",
    "._drop",
    ".NoAction",
};
