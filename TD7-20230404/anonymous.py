#!/usr/bin/python3

import multiprocessing as mp
import os
import random

def write_to_pipe_hello_world(out):
    os.close(rp)
    with os.fdopen(out, "w") as f:
        f.write("Hello you!")

def write_to_pipe_int_pair(out):
    os.close(rp)
    with os.fdopen(out, "w") as f:
        f.write("%d %d" %(random.randint(0, 99), random.randint(0, 99)))

if __name__ == '__main__':
    rp, wp = os.pipe()
    p = mp.Process(target=write_to_pipe_hello_world, args=[wp])
    p.start()
    os.close(wp)
    with os.fdopen(rp) as f:
        print(f.read())
    p.join()

    rp, wp = os.pipe()
    p = mp.Process(target=write_to_pipe_int_pair, args=[wp])
    p.start()
    os.close(wp)
    with os.fdopen(rp) as f:
        pair = f.read()
        val1 = int(pair.split(' ')[0])
        val2 = int(pair.split(' ')[1])
    print("Val 1: %d -- Val 2: %d" % (val1, val2))
    p.join()
