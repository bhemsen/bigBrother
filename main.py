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
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)
 

t1 = FuncThread(db.insertTemperetureAndHumidity, instance)
t2 = FuncThread(db.cleanUp, "7")
t3 = FuncThread(db.getAllowdRFIDS, ())

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


db.close()