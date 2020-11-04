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

        HIVE_COMMAND_MAIN_OPTION = "?" # HIVE KEY = 1
        HIVE_COMMAND_MAIN_OPTION_SET = "set" # HIVE KEY = 10
        HIVE_COMMAND_MAIN_OPTION_SERVICES = "services" # HIVE KEY = 20
        HIVE_COMMAND_MAIN_OPTION_SHOW = "show" # HIVE KEY = 30
        HIVE_COMMAND_MAIN_OPTION_EXIT = "exit" # HIVE KEY = 40

        HIVE_COMMAND_SET_OPTION = "?" # HIVE KEY = 100
        HIVE_COMMAND_SET_OPTION_ESMA = "ethernet-source-mac-address" # HIVE KEY = 11
        HIVE_COMMAND_SET_OPTION_EDMA = "ethernet-destination-mac-address" # HIVE KEY = 12
        HIVE_COMMAND_SET_OPTION_EPT = "ethernet-protocol-type" # HIVE KEY = 13
        HIVE_COMMAND_SET_OPTION_OC = "operation-code" # HIVE KEY = 14
        HIVE_COMMAND_SET_OPTION_SHA = "sender-hardware-address" # HIVE KEY = 15
        HIVE_COMMAND_SET_OPTION_SPA = "sender-protocol-address" # HIVE KEY = 16
        HIVE_COMMAND_SET_OPTION_THA = "target-hardware-address" # HIVE KEY = 17
        HIVE_COMMAND_SET_OPTION_TPA = "target-protocol-address" # HIVE KEY = 18
        HIVE_COMMAND_SET_OPTION_RATE = "rate" # HIVE KEY = 19
        HIVE_COMMAND_SET_OPTION_QUIT = "quit" # HIVE KEY = 109

        HIVE_COMMAND_SERVICES_OPTION = "?" # HIVE KEY = 200
        HIVE_COMMAND_SERVICES_OPTION_START = "start" # HIVE KEY = 21
        HIVE_COMMAND_SERVICES_OPTION_STOP = "stop" # HIVE KEY = 22
        HIVE_COMMAND_SERVICES_OPTION_QUIT = "quit" # HIVE KEY = 209

        HIVE_COMMAND_SHOW_OPTION = "?" # HIVE KEY = 300
        HIVE_COMMAND_SHOW_OPTION_CONFIG = "configuration" # HIVE KEY = 31
        HIVE_COMMAND_SHOW_OPTION_STATUS = "status" # HIVE KEY = 32
        HIVE_COMMAND_SHOW_OPTION_VERSION = "version" # HIVE KEY = 33
        HIVE_COMMAND_SHOW_OPTION_QUIT = "quit" # HIVE KEY = 309

        while True:
            # main cui engine code
            self.print_main_command_line() # print main command line

            HIVE_MAIN_COMMAND = input()

            # main mode
            if HIVE_MAIN_COMMAND ==  HIVE_COMMAND_MAIN_OPTION: # print main option
                HIVE_KEY = 1
                self.print_main_option()

            # set mode
            elif HIVE_COMMAND == HIVE_COMMAND_MAIN_OPTION_SET: # select set command
                while True:
                    HIVE_KEY = 10
                    HIVE_COMMAND_SET_COMMAND = input()
                    if HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION: # print set option
                        HIVE_KEY = 101
                        self.print_set_option()
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_ESMA: # set ethernet source mac address
                        HIVE_KEY = 11
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_EDMA: # set ethernet destination mac address
                        HIVE_KEY = 12
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_EPT: # set ethernet protocol type
                        HIVE_KEY = 13
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_OC: # set operation code
                        HIVE_KEY = 14
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_SHA: # set sender hardware address
                        HIVE_KEY = 15
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_SPA: # set sender protocol address
                        HIVE_KEY = 16
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_THA: # set target hardware address
                        HIVE_KEY = 17
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_TPA: # set target hardware address
                        HIVE_KEY = 18
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_RATE: # set rate
                        HIVE_KEY = 19
                    elif HIVE_COMMAND_SET_COMMAND == HIVE_COMMAND_SET_OPTION_QUIT: # quit
                        HIVE_KEY = 109
                        break

            # services mode
            elif HIVE_COMMAND == HIVE_COMMAND_MAIN_OPTION_SERVICES:
                while True:
                    HIVE_KEY = 20
                    HIVE_COMMAND_SERVICES_COMMAND = input()
                    if HIVE_COMMAND_SERVICES_COMMAND == HIVE_COMMAND_SERVICES_OPTION: # print services option
                        HIVE_KEY = 201
                        self.print_services_option()
                    elif HIVE_COMMAND_SERVICES_COMMAND == HIVE_COMMAND_SERVICES_OPTION_START: # start services
                        HIVE_KEY = 21
                    elif HIVE_COMMAND_SERVICES_COMMAND == HIVE_COMMAND_SERVICES_OPTION_STOP: # stop services
                        HIVE_KEY = 22
                    elif HIVE_COMMAND_SERVICES_COMMAND == HIVE_COMMAND_SERVICES_OPTION_QUIT: # quit
                        HIVE_KEY = 209
                        break

            # show mode
            elif HIVE_COMMAND == HIVE_COMMAND_MAIN_OPTION_SHOW:
                while True:
                    HIVE_KEY = 30
                    HIVE_COMMAND_SHOW_COMMAND = input()
                    if HIVE_COMMAND_SHOW_COMMAND == HIVE_COMMAND_SHOW_OPTION: # print show option
                        HIVE_KEY = 301
                        self.print_show_option()
                    elif HIVE_COMMAND_SHOW_COMMAND == HIVE_COMMAND_SHOW_OPTION_CONFIG: # show arp packet config
                        HIVE_KEY = 31
                    elif HIVE_COMMAND_SHOW_COMMAND == HIVE_COMMAND_SHOW_OPTION_STATUS: # show services status
                        HIVE_KEY = 32
                    elif HIVE_COMMAND_SHOW_COMMAND == HIVE_COMMAND_SHOW_OPTION_VERSION: # show software version
                        HIVE_KEY = 33
                    elif HIVE_COMMAND_SHOW_COMMAND == HIVE_COMMAND_SHOW_OPTION_QUIT: # quit
                        HIVE_KEY = 309
                        break

            # exit mode
            elif HIVE_COMMAND == HIVE_COMMAND_MAIN_OPTION_EXIT:
                HIVE_KEY = 40
                break

            # else
            else:
                continue


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
            version
    """
    def print_show_option(self):
        SHOW_OPTION = "configuration : show arp configuration \n" \
                      "status : show services status \n" \
                      "version : show software version \n" \
                      ""
        print(SHOW_OPTION)
        return
