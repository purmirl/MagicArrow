"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : scapy-Python3

 Packet Launcher :: ARP (Address Resolution Protocol)
"""

# PythonProjectStructure/src/main.py;

from scapy.all import *

packet = IP(dst = "8.8.8.8")/ICMP()
packet.show()



