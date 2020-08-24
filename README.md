# LXI device control

This repo hosts C++ and Python scripts for communication with lab instrumentation and data acquisitation systems using LXI over Ethernet. Tested on Ubuntu 18.04. You can use them as a template and add further communication commands.

New concept: Communicating manually over TCP sockets, which corresponds to LXI standard (?) -> yes, TCP/IP follows LXI.

## About

LAN eXtensions for Instrumentation (LXI) defines a standard for a communication protocol used by several lab instrumentation and data acquisition manufacturers. The communication is established over Ethernet by using [several communication protocols](https://www.lxistandard.org/About/LXI-Protocols.aspx), which follow the LXI standard. For TCP/IP these are the [VXI-11 and HiSLIP protocol](https://www.lxistandard.org/About/VXI-11-and-LXI.aspx). These protocols provide mechanisms to send ASCII commands to the device (SCPI). I.e., they provide an interface to the device, while the particular commands which need to be send to the device are still defined by the manufacturer (usually the same for all interfaces like USB, ethernet, RS232 etc.) and need to be looked up in the corresponding documentation. Therefore, in this repo, templates are created for each device. By using the corresponding commands, these can easily be adapted to other LXI devices.

Different LXI libraries exist. This repo uses [lxi-tools](https://github.com/lxi-tools) for C++ and [Python VXI-11](https://github.com/python-ivi/python-vxi11). It should be mentioned that in the future VXI-11 will be replaced by the newer HiSLIP. But this will be implemented in the underlying libraries. Another library worth mentioning is the VISA API, which offers much more functionality and is supported by several vendors.

## Using lxi-tools from terminal

```
lxi discover -m
lxi scpi --address 192.168.1.131 -p 9221 -r "*IDN?"
lxi scpi --address 192.168.1.131 -p 9221 -r "V1 20"
```

## Tested devices

- Aim TTi CPX400SP (Sidenote: USB firmware error in descriptors (https://github.com/libusb/libusb/issues/767))
    - Commands: http://"IP"/cmd_set.htm
    - Instructions: http://resources.aimtti.com/manuals/CPX400S+SA+SP_Instruction_Manual-Iss9.pdf
    - limited VXI-11 interface, using TCP instead
    - LXI seems to only include operations for device discovery, which do not help us too much. Use of raw TCP instead, which is not LXI?! Is this a joke? Writing a TCP socket communication myself.
    - 
    ```
    TCP Sockets: The instrument uses 2 sockets on TCP port 9221 for instrument control and monitoring.  Text commands are sent to this port as defined in ‘Remote Commands’ and any replies are returned via the same port.  Any string must be one or more complete commands. Commands may be separated with either semicolons “;” or line feeds. No terminator is required since the TCP frame contains complete commands though commands may be sent with a terminator if desired (it will be ignored).  Each command over TCP behaves as if it is terminated with a command terminator (ASCII character 0AH, line feed).
    ```

## Build and run

```
gcc -o test testcpx400sp.cc -llxi
./test
```

```
mkdir build
cd build
cmake ../
cmake --build . 
```


## Dependencies

```
sudo apt-get install liblxi-dev
pip install python-vxi11
```

### Python

### C++