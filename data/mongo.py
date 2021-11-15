'''
pip install pymongo

mongoserver installed and up and running C:\Program Files\MongoDB\Server\5.0\bin in mongod is server running

mongo application in bin is just client. these are the commands i used: 
show dbs
use pythondb
db.employees.find()
Start mongodb server  and run this program
'''
from pymongo import MongoClient  # import mongo client to connect
import pprint

# Creating instance of mongoclient
client = MongoClient()

# Creating database
db = client.pythondb
print("Database created -  pythondb")

employee = {"id": "101",
            "name": "Anusha",
            "profession": "Software Engineer",
            }

# Creating document
employees = db.employees
print("Created employees table")

# Inserting data
employees.insert_one(employee)
print("New employee is added")

# Fetching data
print("Check table data")
pprint.pprint(employees.find_one())

'''
enter into mongo shell
$ mongo  
> show dbs  
> use pythondb
> db.employees.find()  
'''
