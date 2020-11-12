import mysql.connector
import time
from mysql.connector import Error

def cleanUp():
       
    db = mysql.connector.connect(
        host="localhost",
        user="webadmin",
        passwd="password",
        database="sensoro"
    )
    sql = "DELETE FROM temperature WHERE DATEDIFF(day, NOW()) <= %s"

    curser = db.cursor(prepared=True)
    days = '7'


    while True:
        try:
            curser.execute(sql, days, True)
            db.commit()
            print ("Data deleted")
            
        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            db.rollback()    
        time.sleep(2500000)

    curser.close()
    db.close()

cleanUp()