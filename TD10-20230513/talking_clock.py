#!/usr/bin/python3

import threading
import time

__daemon_stop_event__ = threading.Event()

def start_daemon():
    def daemon_clock():
        while not __daemon_stop_event__.is_set():
            print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
            time.sleep(5)
    daemon = threading.Thread(target=daemon_clock)
    daemon.setDaemon(True)
    daemon.start()

def stop_daemon():
    __daemon_stop_event__.set()