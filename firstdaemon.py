from threading import *
from datetime import datetime
from time import sleep
def affich_date():
    print(str(datetime.now()))
    sleep(5)


daemon = Thread(target=affich_date)
daemon.setDaemon(True)
daemon.start()

