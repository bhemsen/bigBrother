import mysql.connector
import time
from mysql.connector import Error

class Database:
    #this parameters needs to be strings
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        
        self.db = mysql.connector.connect(
            host= self.host,
            user= self.user,
            passwd= self.passwd,
            database= self.database
            )

        self.cursor = self.db.cursor(prepared=True)

    
    def insertTemperetureAndHumidity(self, dht11Instance):
        sql = "INSERT INTO temperature values(0, CURRENT_DATE(), NOW(), %s, %s)"

        while True:
            result = dht11Instance.read()
            while not result.is_valid():  # read until valid values
                result = dht11Instance.read()
            
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            
            temperature = str(result.temperature)
            humidity = str(result.humidity)
            
            try:
                self.cursor.execute(sql, (temperature,humidity,), True)
                self.db.commit()
                print ("Data committed")
            
            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))
                self.db.rollback()   
                time.sleep(15)

    #days needs to be a string   
    def cleanUp(self, days):
        sql = "DELETE FROM temperature WHERE DATEDIFF(day, NOW()) <= %s"
        self.days = days

        while True:
            try:
                self.cursor.execute(sql, days, True)
                self.db.commit()
                print ("Data deleted")
                    
            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))
                self.db.rollback()    
                time.sleep(2500000)

        
    def getAllowdRFIDS(self):
        data = []
        sql = "SELECT rfid,name,securityLevel FROM rfid WHERE securityLevel = 1 OR securityLevel = 2"
        try:
            self.cursor.execute(sql)
            print ("data recieved")
            
            result = self.cursor.fetchall()

            for row in result:
                row = list(row)
                data.append(row)
            return data

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.db.rollback()   


    def addNewRFID(self, data):
        self.data = str(data)
        sql = "INSERT INTO `rfid` (`ID`, `name`, `securityLevel`, `rfid`) VALUES (NULL, %s, %s, %s)"
        name = input("Name: ")
        securityLevel = 0

        while not (securityLevel == "1" or securityLevel == "2"):
            securityLevel = str(input("2 für Leitende Mitarbeiter, 1 für Angestellte : "))
    
        try:
            self.cursor.execute(sql, (name, securityLevel, self.data,))
            self.db.commit()
            print('Daten wurden gesetzt')

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            self.db.rollback() 




    def close(self):
        self.cursor.close()
        self.db.close()

        

