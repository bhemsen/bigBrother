import threading
import time

import Database
from Database import Database



#initialize database connection
db = Database("localhost", "webadmin", "password", "sensoro")



#initialize threading
class FirstThread(threading.Thread):
 
    def run(self):
        exec(open('test2.py').read())
        print('firt')
    

class SecondThread(threading.Thread):
 
    def run(self):
        print('data send second Thread')
    

class ThirdThread(threading.Thread):
 
    def run(self):
        print('data send third Thread')


def runThread1():
    t1.run()
    t1.join()
    time.sleep(15)


def runThread2():
    t2.run()
    t2.join()
    time.sleep(30)


def runThread3():
    t3.run()
    t3.join()
    time.sleep(5)

try:
    t1 = FirstThread()
    t2 = SecondThread()
    t3 = ThirdThread()

    t1.start()
    t2.start()
    t3.start()


    while True:
        runThread1()
        runThread2()
        runThread3()

    db.close()


except KeyboardInterrupt:
    print("Abbruch")