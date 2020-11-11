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
from package import cui as cui



def main():

    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engin()

    return

# main code start point
main()

# main conde end point



# packet = IP(dst = "")/ICMP()
# packet.show()




