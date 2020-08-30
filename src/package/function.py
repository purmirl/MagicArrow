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

def isHexData(_data):
    tempKey = 0
    hexData = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if _data in hexData:
        return 1
    else:
        return 0
    return 0

