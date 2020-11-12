import mysql.connector
import time
from mysql.connector import Error
import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 4)


db = mysql.connector.connect(
    host="localhost",
    user="webadmin",
    passwd="password",
    database="sensoro"
)

curser = db.cursor(prepared=True)
sql_insert_query = "INSERT INTO temperature values(0, CURRENT_DATE(), NOW(), %s, %s)"

while True:

    result = instance.read()

    while not result.is_valid():  # read until valid values
        result = instance.read()

    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)

    temperature = str(result.temperature)
    humidity = str(result.humidity)


    try:
        curser.execute(sql_insert_query, (temperature,humidity,), True)
        db.commit()
        print ("Data committed")
        
    except mysql.connector.Error as error:
        print("parameterized query failed {}".format(error))
        db.rollback()    
    time.sleep(15)

curser.close()
db.close()


