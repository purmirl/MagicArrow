"""
 MagicArrow
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
            set
            services
            show
            exit
    """
    def print_main_option(self):
        MAIN_OPTION = "set : set packet configuration \n " \
                      "services : program's operation services \n " \
                      "show : show program status \n" \
                      "exit : program exit \n" \
                      ""
        print(MAIN_OPTION)
        return

    """ set option
            ethernet-source-mac-address
            ethernet-destination-mac-address
            ethernet-protocol-type
            operation-code
            sender-hardware-address
            sender-protocol-address
            target-hardware-address
            target-protocol-address
            rate
    """
    def print_set_option(self):
        ARP_OPTION = "ethernet-source-mac-address : set ethernet source mac address (mac or default) \n" \
                     "ethernet-destination-mac-address : set ethernet destination mac address (mac or default) \n" \
                     "ethernet-protocol-type : set ethernet protocol type (arp, rarp) \n" \
                     "operation-code : set arp operation code \n" \
                     "sender-hardware-address : set sender hardware address (mac) \n" \
                     "sender-protocol-address : set sender protocol address (ip \n" \
                     "target-hardware-address : set target hardware address (mac) \n" \
                     "target-protocol-address : set target protocol address (ip) \n" \
                     "rate : packet launch rate per 1 second \n" \
                     ""
        print(ARP_OPTION)
        return

    """ services option
            start : packet launch start
            stop : packet launch stop
    """
    def print_services_option(self):
        SERVICES_OPTION = "start : packet launch start \n" \
                          "stop : packet launch stop \n" \
                          ""
        print(SERVICES_OPTION)
        return

    """ show option
            configuration
            status
    """
    def print_show_option(self):
        SHOW_OPTION = "configuration : show arp configuration \n" \
                      "status : show services status \n" \
                      ""
        print(SHOW_OPTION)
        return
