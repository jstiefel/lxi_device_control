# ============================================================================
# Name        : cpx400sp_example.py
# Author      : Julian Stiefel (jstiefel@ethz.ch)
# Version     : 1.0.0
# Created on  : 25.08.2020
# Copyright   :
# Description : This is an example script on how to control the Aim TTi
#               CPX400SP.
# ============================================================================

import sys
import time

sys.path.append(".")
from cpx400sp import CPX400SP

def main():
        
    cpx = CPX400SP('192.168.1.131', 9221)
    print(cpx.get_identification())

    iterations = 0
    
    while iterations < 1000:
        cpx.set_voltage(10)
        cpx.set_current(1)
        print("Measured voltage is: {}".format(cpx.get_voltage()))
        print("Measured current is: {}".format(cpx.get_current()))
        time.sleep(2)
        cpx.set_voltage(20)
        cpx.set_current(2)
        print("Measured voltage is: {}".format(cpx.get_voltage()))
        print("Measured current is: {}".format(cpx.get_current()))
        iterations = iterations + 1
        time.sleep(2)

    del cpx

if __name__ == "__main__":
    main()
