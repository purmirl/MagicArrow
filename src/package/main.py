"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;
 Magic Arrow Project (Packet Launcher) by PeTrA. 2020~
 MagicArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 ------
 @ main.py
    * MagicArrow/src/package/main.py
    * main function code file
"""

from package import cui as cui

""" @main function
"""
def main():

    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engin()
    return

""" @call main
"""
if __name__ == "__main__":
    main()



