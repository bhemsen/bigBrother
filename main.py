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
        db.insertTemperetureAndHumidity(instance)

class SecondThread(threading.Thread):
 
    def run(self):
        db.cleanUp("7")

class ThirdThread(threading.Thread):
 
    def run(self):
        db.getAllowdRFIDS()


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