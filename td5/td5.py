# from subprocess import Popen, PIPE
# with open("example1.sh", "r") as file :
#     texte = file.readlines()
#     ligne = "ls | grep .py | xargs wc -l"
#     print(ligne)
#     process = Popen(ligne,stdout=PIPE, stderr=PIPE, shell = True)
#     stdout, stderr = process.communicate()
#     stdout = stdout.decode("utf-8") # format b'' vers str.
#     stderr = stderr.decode("utf-8") # idem
#     print(stdout+stderr)

from multiprocessing import Process
import os
from random import randint
from time import sleep
from math import sqrt

# def hello(name):
#     print(f"{name} says hello world !!")

# if __name__ == '__main__':
#     p = Process(target= hello, args= ("elie",))
#     p.start()
#     hello("papa elie")
#     p.join()


# def my_pid():
#     print(f"“Mon PID est {os.getpid()} et celui de mon pere est {os.getppid()} ")

# if __name__ == '__main__':
#     p = Process(target= my_pid)
#     p.start()
#     print(f"“Mon PID est {os.getpid()} et celui de mon fils est {p.pid}")
#     p.join()



# def comunique(name):
#     name.send("hey daddy")
#     name.close()

# if __name__ == '__main__':
#     parent,child = Pipe(duplex = False)
#     p = Process(target= comunique, args= (child,))
#     p.start()
#     print(parent.recv())
#     p.join()


  
# pid greater than 0 represents
# the parent process 
# r, w = os.pipe()

# pid = os.fork()

# if pid > 0 :
#     print("I am parent process:")
#     print("Process ID:", os.getpid())
#     print("Child's process ID:", pid)
#     print("hello world")
#     os.close(w)
#     r = os.fdopen(r,"r")
#     print("text =" , r.read())
#     r.close()

  
# # pid equal to 0 represents
# # the created child process
# else :
#     print("\nI am child process:")
#     print("Process ID:", os.getpid())
#     print("hello world")
#     os.close(r)
#     w = os.fdopen(w,"w")
#     w.write(str(randint(1,30)))
# p = 1
# for  i in range(10):
#     if  p :
#         p = os.fork()
        

# if not p :

#     print(os.getpid())

# if p :
#     for i in range(10):
#         print("mon fils :", os.wait())

# i <- 2
# tant que i <= sqrt(n) faire
# si n modulo i = 0 alors
# retourne FAUX
# i <- i + 1
# retourne VRAI


def primalité(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            print( f" {n} : {False} ")
            return
        i += 1
    print(f" {n} : {True} ")
    return

for  i in range(2,11):
    if __name__ == '__main__':
        p = Process(target= primalité, args= (i,))
        p.start()
        p.join()
