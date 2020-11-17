import threading
import time
import RPi.GPIO as GPIO
import dht11
import Database
from Database import Database

# initialize GPIOS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#read data using pin 14
instance = dht11.DHT11(pin = 4)

#initialize database connection
db = Database("localhost", "webadmin", "password", "sensoro")



#initialize threading
class FirstThread(threading.Thread):
 
    def run(self):
        while True:
            db.insertTemperetureAndHumidity(instance)
            time.sleep(15)

class SecondThread(threading.Thread):
 
    def run(self):
        while True:
            db.cleanUp("7")
            time.sleep(2000000)

class ThirdThread(threading.Thread):
 
    def run(self):
        while True:
            db.getAllowdRFIDS()
            time.sleep(2)

t1 = FirstThread()
t2 = SecondThread()
t3 = ThirdThread()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


db.close()