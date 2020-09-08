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


class launcher():
    def __init__(self, _operationCode, _senderHardwareAddress, _senderProtocolAddress, _targetHardwareAddress, _targetProtocolAddress, _rate):
        self.operationCode = _operationCode
        self.senderHardwareAddress = _senderHardwareAddress
        self.senderProtocolAddress = _senderProtocolAddress
        self.targetHardwareAddress = _targetHardwareAddress
        self.targetProtocolAddress = _targetProtocolAddress
        self.rate = _rate
        return

    def launcherStart(self):

        return