#!/usr/bin/python3

from queue import Queue
import threading

__DAEMON_STOP_EVENT__ = threading.Event()
__PASCAL__ = {}
__QUEUE__ = Queue()

def __daemon_add__(name, value):
    __PASCAL__[name] = value

def __daemon_rm__(name):
    __PASCAL__.pop(name)

def __daemon_ask__(name):
    try:
        print("[PASCAL] Entry '%s' = '%f'" % (name, __PASCAL__[name]))
    except KeyError:
        print("[PASCAL] Entry '%s' is not recognized, please try again" % (name))

def __daemon_main__():
    while not __DAEMON_STOP_EVENT__.is_set():
        item = __QUEUE__.get()
        if item is not None:
            if item['operation'] == 'add':
                __daemon_add__(item['name'], item['value'])
            elif item['operation'] == 'rm':
                __daemon_rm__(item['name'])
            else:
                __daemon_ask__(item['name'])
        __QUEUE__.task_done()

def start_daemon():
    __DAEMON_STOP_EVENT__.clear()
    __PASCAL__.clear()
    daemon = threading.Thread(target=__daemon_main__)
    daemon.setDaemon(True)
    daemon.start()

def stop_daemon():
    __QUEUE__.join()
    __DAEMON_STOP_EVENT__.set()
    __QUEUE__.put(None)

def add_entry(name, value):
    __QUEUE__.put({
        'operation': 'add',
        'name': name,   
        'value': value
    })

def rm_entry(name):
    __QUEUE__.put({
        'operation': 'rm',
        'name': name
    })

def ask_entry(name):
    __QUEUE__.put({
        'operation': 'ask',
        'name': name
    })