#!/usr/bin/python3

import multiprocessing as mp
import os
import random
import time

NUM_PROCESS = 10
ACK_MESSAGE = 'ACK'

def request_reply(pipe_in, pipe_out):
    with os.fdopen(pipe_out, "w") as f:
        time.sleep(random.randint(0, 5))
        number = random.randint(1, 999)
        print("I(%d) sent a request %d!" % (os.getpid(), number))
        f.write("%d\n%d\n" % (os.getpid(), number))

    with os.fdopen(pipe_in) as f:
        ack = f.readline()[:-1]
        if ack == ACK_MESSAGE:
            print("I(%d) received the ack!" % (os.getpid()))
        else:
            raise IOError

if __name__ == '__main__':
    r_main, w_main = os.pipe()
    process_list = []
    w_list = {}
    for i in range(NUM_PROCESS):
        r, w = os.pipe()
        process_list.append(mp.Process(target=request_reply, args=[r, w_main]))
        process_list[-1].start()
        w_list[process_list[-1].pid] = w

    os.close(w_main)
    with os.fdopen(r_main) as f:
        for _ in range(NUM_PROCESS):
            pid = int(f.readline()[:-1])
            string = f.readline()[:-1]

            print("%d sent '%s', will ack this!" % (pid, string))

            with os.fdopen(w_list[pid], "w") as fw:
                fw.write("%s\n" % (ACK_MESSAGE))

    for p in process_list:
        p.join() 
