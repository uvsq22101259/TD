#!/usr/bin/python3

import multiprocessing as mp
import os

NUM_PROCESS = 10

def broadcast(pipe_in):
    with os.fdopen(pipe_in) as f:
        print("I(%d) received '%s'!" % (os.getpid(), f.readline().split('\n')[0]))

if __name__ == '__main__':
    process_list = []
    w_list = []
    for i in range(NUM_PROCESS):
        r, w = os.pipe()
        w_list.append(w)
        process_list.append(mp.Process(target=broadcast, args=[r]))

    for p in process_list:
        p.start()

    for w in w_list:
        with os.fdopen(w, "w") as f:
            f.write('Hello you!\n')
    
    for p in process_list:
        p.join()
