import os

proc = os.fork()
if proc == 0:
    print(proc)


