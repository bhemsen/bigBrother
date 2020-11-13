import asyncio
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


def asyncRun():
    asyncio.run(db.insertTemperetureAndHumidity(instance))
    asyncio.run(db.cleanUp("7"))


asyncRun()

db.getAllowdRFIDS()
db.close()
