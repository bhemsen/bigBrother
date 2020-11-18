import threading
import time

import Database
from Database import Database



#initialize database connection
db = Database("localhost", "webadmin", "password", "sensoro")
days = "7"
instance = 24


#initialize threading

def insertTempHum(instance):
    while True:
        try:
            exec(open('./writeDB.py').read())

        except KeyboardInterrupt:
            print("Abbruch")

def cleanUp(days):
    while True:
        try:
            exec(open('./test2.py').read())
            print('bis hier auch')

            time.sleep(30)

        except KeyboardInterrupt:
            print("Abbruch")

def runRFID():
    while True:
        try:
            exec(open('./test2.py').read())

            time.sleep(2)

        except KeyboardInterrupt:
            print("Abbruch")



if __name__ == "__main__":
    try:
        t = threading.Thread(target=insertTempHum, args=(instance,))
        t2 = threading.Thread(target=cleanUp, args=(days,))
        t3 = threading.Thread(target=runRFID,)
        t.start()
        print('test')
        t2.start()
        exec(open('./test2.py').read())



    except KeyboardInterrupt:
        print("Abbruch")