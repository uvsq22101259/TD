from threading import Thread
from time import sleep
from random import randint
from sys import argv


def somme(index):
    global result, nbr_boucle
    for  i in range(index,index + nbr_boucle):
        if i < n:
            result += tab[i]

def maximum(index):
    offset = index +nbr_boucle
    if offset > n:
        offset = n
    result.append(max(tab[index:offset]))


def minimum(index):
    offset = index +nbr_boucle
    if offset > n:
        offset = n
    result.append(min(tab[index:offset]))


_,m,n,opcode = argv
m,n = int(m), int(n)
nbr_boucle = n // m +1
tab = [ randint(0,100) for i in range(n)]
print(tab)
threads = []

if opcode == "+":
    result = int()
    for i in range(0,n,nbr_boucle):
        t = Thread(target=somme, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(result)

elif opcode == "/":
    result = int()
    for i in range(0,n,nbr_boucle):
        t = Thread(target=somme, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(result / n)

elif opcode == "M":
    result = []
    for i in range(0,n,nbr_boucle):
        t = Thread(target=maximum, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(max(result))

elif opcode == "m":
    result = []
    for i in range(0,n,nbr_boucle):
        t = Thread(target=minimum, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(min(result))