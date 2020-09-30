"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Packet Launcher :: ARP (Address Resolution Protocol)
 ------
 @ launcher.py
    * launcher python code file --> engine code
"""

# MagicArrow/src/cui.py

from package.function import isHardwareAddress
from scapy.all import *

# please check!! arp packet structure
"""
    Hardware type (16bits) | Protocol Type (16bits)
    Hardware Length (8bits) | Protocol Length (8bits) | Operation Code (16bits)
    Sender Hardware Address (32bits)
    Sender Protocol Address (32bits)
    Target Hardware Address (32bits)
    Target Protocol Address (32bits)
"""
class launcher():
    def __init__(self, _operationCode, _senderHardwareAddress, _senderProtocolAddress, _targetHardwareAddress, _targetProtocolAddress, _rate):
        self.operationCode = _operationCode
        self.senderHardwareAddress = _senderHardwareAddress
        self.senderProtocolAddress = _senderProtocolAddress
        self.targetHardwareAddress = _targetHardwareAddress
        self.targetProtocolAddress = _targetProtocolAddress
        self.rate = _rate
        return
    # Scapy Usage : send arp packet
    # send(Ether(src = SOURCE_MAC, dst = DESTINATION_MAC) / ARP(op = OPERATION_CODE, hwsrc = SOURCE_HARDWARE_ADDRESS, hwdst = DESTINATION_HARDWARE_ADDRESS, psrc = SOURCE_PROTOCOL_ADDRESS, pdst = DESTINATION_HARDWARE_ADRESS), inter = RandNum(10, 40), loop = 0)
    def launcherStart(self):

        return