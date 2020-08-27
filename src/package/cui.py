"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Magic Arrow Project by PeTrA. 2020
 MagicArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Packet Launcher :: ARP (Address Resolution Protocol)
 ------
 @ cui.py
    * character user interface python code file
"""

# MagicArrow/src/cui.py


class Cui():

    def __init__(self):
        return

    def cui_engin(self):
        self.print_rights() # print copyright
        HIVE_KEY = 0
        HIVE_COMMAND = 0
        HIVE_COMMAND_OPTION = "?"

        while True:
            # main cui engine code
            self.print_main_command_line() # print main command line
            HIVE_COMMAND = input()

            if HIVE_COMMAND == HIVE_COMMAND_OPTION:
                HIVE_KEY = 1

            if HIVE_COMMAND == "?":
                self.print_main_option()
             
            if HIVE_KEY == -1:
               break

        return

    def print_rights(self):
        print("Copyright 2020 PeTrA. All rights reserved.")
        print("MagicArrow 1.0")
        return

    def print_main_command_line(self):
        print("main@magicarrow:~# ")
        return

    # option line
    """ main option
            arp
            rate
            services
            show
    """
    def print_main_option(self):
        MAIN_OPTION = "arp : make arp packet \n " \
                      "rate : packet launch rate per 1 second \n " \
                      "services : program's operation services \n " \
                      "show : show program status"
        print(MAIN_OPTION)
        return

    """ arp option
            operation-code
    """
    def print_arp_option(self):
        ARP_OPTION = "operation-code : set arp operation code"
        print(ARP_OPTION)
        return

    """ arp operation code option
            sender-hardware-address
    """
    def print_arp_operationCode_option(self):
        ARP_OPERATIONCODE_OPTION = "sender-hardware-address"
        print(ARP_OPERATIONCODE_OPTION)
        return
