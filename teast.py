import Database
from Database import Database
import ast

key = [1,2,3,4,5,6,7,8,9]
key = [4,4,4,4,4,4,4,4]



def compareKeyWithDatabaseKeys(key):
    db = Database("localhost", "webadmin", "password", "sensoro")
    result = db.getAllowdRFIDS()

    for i in range(len(result)-1):
        allowedKey = ast.literal_eval(result[i][0])
        securityLevel = result[i][2]
        name = result[i][1]
        print(allowedKey)
        if allowedKey == key:
            if securityLevel == 2:
                entry(name)
                access = "granted"
                db.logEntry(name , key, access)
                return

            else:
                noentry(name)
                access = "denied"
                db.logEntry(name , key, access)
                return

    unknown()
    name = "unknown"
    access = "denied"
    db.logEntry(name , key, access)


for i in range(10):
    compareKeyWithDatabaseKeys(key)
    print(i)