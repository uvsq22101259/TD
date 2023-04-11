from threading import Thread
from time import sleep
from random import randint

# moyenne = 0
# tab = [ randint(0,10000000) for i in range(10)]
# def speak(sentence: str):
#     pass

# def average(index):
#     global tab, moyenne
#     print(moyenne)
#     moyenne += tab[index]




# threads = []
# for i in range(len(tab)):
#     t = Thread(target=average, args=[i])
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()
# moyenne//= len(tab)
# print(moyenne)

tab = [ randint(0,10000000) for i in range(100)]

