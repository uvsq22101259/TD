from threading import Thread, Lock

def agr(cpt):
    for i in range(10):
        lock.acquire()
        cpt[0] +=1
        lock.release()



compteur = [0]
threadlist = []
lock = Lock()
for i in range(2):
    t = Thread(target= agr, args=[compteur])
    threadlist.append(t)

for t in threadlist:
    t.start()

for t in threadlist:
    t.join()

print(compteur)