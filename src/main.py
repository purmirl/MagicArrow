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
from scapy.layers.inet import IP, ICMP

class Main():
    def __init__(self):
        return

    def print_rights(self):
        print("Copyright 2020 PeTrA. All rights reserved.")
        print("MagicArrow 1.0")
        return


mainFunction = Main()
mainFunction.print_rights()

# packet = IP(dst = "")/ICMP()
# packet.show()




