"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Packet Launcher :: ARP (Address Resolution Protocol)
 ------
 @ main.py
    * main python code file
"""

# MagicArrow/src/main.py

from scapy.layers.inet import IP, ICMP
import cui as cui

cuiEngine = cui.Cui()
cuiEngine.print_rights()



# packet = IP(dst = "")/ICMP()
# packet.show()




