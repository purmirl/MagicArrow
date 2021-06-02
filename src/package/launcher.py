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

from package.function import is_hardware_address
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
    def __init__(self, _operation_code, _sender_hardware_address, _sender_protocol_address, _target_hardware_address,
                 _target_protocol_address, _rate):
        self.operation_code = _operation_code
        self.sender_hardware_address = _sender_hardware_address
        self.sender_protocol_address = _sender_protocol_address
        self.target_hardware_address = _target_hardware_address
        self.target_protocol_address = _target_protocol_address
        self.rate = _rate
        return
    # Scapy Usage : send arp packet
    # send(Ether(src = SOURCE_MAC, dst = DESTINATION_MAC) / ARP(op = OPERATION_CODE,
    # hwsrc = SOURCE_HARDWARE_ADDRESS, hwdst = DESTINATION_HARDWARE_ADDRESS,
    # psrc = SOURCE_PROTOCOL_ADDRESS, pdst = DESTINATION_HARDWARE_ADRESS),
    # inter = RandNum(10, 40), loop = 0)
    def launcher_start(self):
        
        return

    # thread
    def send_packet(self):

        return

    def set_operation_code(self, _operation_code):
        self.operation_code = _operation_code
        return

    def set_sender_hardware_address(self, _sender_hardware_address):
        self.sender_hardware_address = _sender_hardware_address
        return

    def set_sender_protocol_address(self, _sender_protocol_address):
        self.sender_protocol_address = _sender_protocol_address
        return

    def set_target_hardware_address(self, _target_hardware_address):
        self.target_hardware_address = _target_hardware_address
        return

    def set_target_protocol_address(self, _target_protocol_address):
        self.target_protocol_address = _target_protocol_address
        return

    def set_rate(self, _rate):
        self.rate = _rate
        return

    def get_operation_code(self):
        return self.operation_code

    def get_sender_hardware_address(self):
        return self.sender_hardware_address

    def get_sender_protocol_address(self):
        return self.sender_protocol_address

    def get_target_hardware_address(self):
        return self.target_hardware_address

    def get_target_protocol_address(self):
        return self.target_protocol_address

    def get_rate(self):
        return self.rate



