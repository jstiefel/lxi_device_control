//============================================================================
// Name        : cpx400sp.cc
// Author      : Julian Stiefel (jstiefel@ethz.ch)
// Version     : 1.0.0
// Created on  : 24.08.2020
// Copyright   :
// Description : LXI communication with Aim TTi CPX400SP PSU
//============================================================================

#include "../include/lxi_device_control/cpx400sp.h"

using namespace std;

int main(int argc, char **argv) {
    char response[65536];
    int device, length, timeout = 1000;

    // Initialize LXI library
    lxi_init();

    // Connect to LXI device
    device = lxi_connect("192.168.1.131", 9221, "inst0", timeout, RAW);

    // Send SCPI command
    lxi_send(device, "*IDN?", strlen("*IDN?"), timeout);

    // Wait for response
    lxi_receive(device, response, sizeof(response), timeout);

    printf("%s\n", response);

    // Disconnect
    lxi_disconnect(device);

    return 0;
}