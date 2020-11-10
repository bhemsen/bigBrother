import mysql.connector
import time


db = mysql.connector.connect(
    host="192.168.178.21",
    user="webadmin",
    passwd="W05sqSOOuaFdh2XmvKYN",
    database="sensoro"
)

curser = db.cursor()


while True:
    try:
        curser.execute ("""INSERT INTO temperature values(0, CURRENT_DATE(), NOW(), 22)""")
        db.commit()
        print ("Data committed")
    except:
        print ("Error")
        db.rollback()    
    time.sleep(30)

db.close()
