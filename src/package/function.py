"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Packet Launcher :: ARP (Address Resolution Protocol)
 ------
 @ function.py
    * function python code -> my utility function's code
"""

# MagicArrow/src/function.py


""" isHexData function
        check that is hex data
        if hex data : return 1
        else : return 0
"""
def isHexData(_data):
    result = 0
    tempKey = 0
    hexData = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if _data in hexData:
        result = 1
        return result
    else:
        result = 0
        return result

    return result

""" isHardwareAddress function
        check that is hardware address (mac address)
        if hardware address : return 1
        else : return 0
"""
def isHardwareAddress(_hardwareAddress):
    result = 1 # if hardware address : 1,   else : 0
    length = len(_hardwareAddress)

    if length != 17:
        result = 0
        return result

    for i in range(1, length + 1):
        if (i % 3) == 0:
            if _hardwareAddress[i - 1] != ':':
                result = 0
                return result
        elif isHexData(_hardwareAddress[i - 1]) == 0:
            result = 0
            return result

    return result

def isProtocolAddress(_protocolAddress):
    result = 1 # if protocol address : 1,   else : 0
    length = len(_protocolAddress)

    if length < 7 | length > 15:
        result = 0
        return result

    for i in range (1, length + 1):
        

    return 0