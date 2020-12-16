"""
 Copyright 2020 PeTrA. All rights reserved.
"""

import time
from threading import Thread

def function(_thread_name):
    print(_thread_name + " function start.")

    count_number = 0
    while True:
        if THREAD_KEY == -1:
            break
        print("count number : ", count_number)
        count_number = count_number + 1
        time.sleep(2)

    print(_thread_name + " function stop.")
    return

def main_function():
    global THREAD_KEY
    THREAD_KEY = 0

    thread_01 = Thread(target=function, args=("purmirl", ))
    thread_01.start()

    key = input()

    print("main_function key : ", key)
    if key == "0":
        THREAD_KEY = -1

    return

main_function()