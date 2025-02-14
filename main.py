#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, '/home/pi/bigBrother/sensoro/functions')
#import functions
from threading import Thread
import time
import RPi.GPIO as GPIO
import dht11
import Database
from Database import Database
from sensoro.functions.days import days
from sensoro.functions.temp import maxTemperature




# initialize GPIOS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#read data using pin 14
instance = dht11.DHT11(pin = 4)

#initialize database connection
db = Database("localhost", "webadmin", "password", "sensoro")





#initialize threading

class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.daemon = True
        self.start()
    def run(self):
        while self.running:
            db.insertTemperetureAndHumidity(instance)

    def stop(self):
        self.running = False
            

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.daemon = True
        self.start()
    def run(self):
        while self.running:
            db.cleanUp(str(days))

    def stop(self):
        self.running = False

class myClassC(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.daemon = True
        self.start()
    def run(self):
            exec(open('./RFID_auslesen_LCD.py').read())
        
    def stop(self):
        self.running = False

if __name__ == "__main__":
    
    try:
        myClassA()
        myClassB()
     #   myClassC()
        while True:
            pass


    except KeyboardInterrupt:
        print("Abbruch")
        myClassA().stop()
        myClassB().stop()
      #  myClassC().stop()
    
    db.close()

