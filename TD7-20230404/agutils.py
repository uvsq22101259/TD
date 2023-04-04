#!/usr/bin/python3

import os

def createID():
    return os.getpid()

def createMessage():
    return "Hello, my PID is %d" % (os.getpid())