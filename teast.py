import Database
from Database import Database
import ast

key = [1,2,3,4,5,6,7,8,9]

db = Database("localhost", "webadmin", "password", "sensoro")

result = db.getAllowdRFIDS()
for i in range(len(result)-1):
    allowedKey = ast.literal_eval(result[i][0])
    securityLevel = result[i][2]
    name = result[i][1]
    if allowedKey == key:
        if securityLevel == 1:
            access = "granted"
            db.logEntry(name , key, access)

        else: 
            print('blabla')