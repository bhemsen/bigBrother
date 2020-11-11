import mysql.connector
import time
from mysql.connector import Error
#import Python_DHT

#sensor = Python_DHT.DHT11
#pin = 4


db = mysql.connector.connect(
    host="192.168.178.21",
    user="webadmin",
    passwd="W05sqSOOuaFdh2XmvKYN",
    database="sensoro"
)

curser = db.cursor(prepared=True)
sql_insert_query = "INSERT INTO temperature values(0, CURRENT_DATE(), NOW(), %s)"

temperature = '2'
while True:

    #temperature = Python_DHT.read_retry(sensor, pin)
    temperature += '1'

    try:
        curser.execute(sql_insert_query, (temperature,), True)
        db.commit()
        print ("Data committed")
        
    except mysql.connector.Error as error:
        print("parameterized query failed {}".format(error))
        db.rollback()    
    time.sleep(5)

curser.close()
db.close()
