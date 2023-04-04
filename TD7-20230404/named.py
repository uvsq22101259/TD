#!/usr/bin/python3

import multiprocessing as mp
import os
import random

def write_to_pipe_hello_world(path):
    with open(path, "w") as f:
        f.write("Hello you!")

def write_to_pipe_int_pair(path):
    with open(path, "w") as f:
        f.write("%d %d" %(random.randint(0, 99), random.randint(0, 99)))

PATH = '__pipe__'

if __name__ == '__main__':
    os.mkfifo(PATH)
    p = mp.Process(target=write_to_pipe_hello_world, args=[PATH])
    p.start()
    with open(PATH) as f:
        print(f.read())
    p.join()

    p = mp.Process(target=write_to_pipe_int_pair, args=[PATH])
    p.start()
    with open(PATH) as f:
        pair = f.read()
        val1 = int(pair.split(' ')[0])
        val2 = int(pair.split(' ')[1])
    print("Val 1: %d -- Val 2: %d" % (val1, val2))
    p.join()

    os.unlink(PATH)
