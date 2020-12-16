"""
 Copyright 2020 PeTrA. All rights reserved.
"""

import time
from threading import Thread

def function(_thread_name):
    count_number = 0
    while True:
        print("count number : ", count_number)
        count_number = count_number + 1

        time.sleep(2)

thread_01 = Thread(target = function, args = ("purmirl", ))
thread_01.start()