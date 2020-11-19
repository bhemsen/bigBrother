from sensoro.functions.days import days
from Database import Database

db = Database("localhost", "webadmin", "password", "sensoro")

db.cleanUp(str(days))