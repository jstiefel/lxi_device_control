# ============================================================================
# Name        : cpx400sp.py
# Author      : Julian Stiefel (jstiefel@ethz.ch)
# Version     : 1.0.0
# Created on  : 25.08.2020
# Copyright   :
# Description : A class to implement some basic device specific SCPI commands
#               for the Aim TTi CPX400SP PSU
# ============================================================================

import sys

sys.path.append(".")
from tcp_socket import TCP_Socket

class CPX400SP:
    def __init__(self, ip, port):
        try:
            self.cpx = TCP_Socket(ip, port)
            print('Device created')
        except:
            print('Failed to create device')

    def __del__(self):
        del self.cpx

    def get_identification(self):
        response = self.cpx.ask('*IDN?')
        return response

    def set_voltage(self, v):
        command = 'V1 ' + str(v)
        self.cpx.send(command)

    def get_voltage(self):
        voltage = self.cpx.ask('V1O?')
        return voltage

    def set_current(self, i):
        command = 'I1 ' + str(i)
        self.cpx.send(command)

    def get_current(self):
        current = self.cpx.ask('I1O?')
        return current
        