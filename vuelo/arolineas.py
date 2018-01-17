from pymongo import MongoClient
import csv

# DB connectivity
client = MongoClient('localhost', 27017)
db = client.get_database(name="daw")
print(client.database_names())

print(db.collection_names())
collection = db.get_collection(name="aerolineas")

for i in db.routes.find({'Airline': '3S','Source airport':{'$in':['FDF','PTP']}}):
    print(i)
dicci = {}
lista =[]


# Function to parse csv to dictionary

# Final insert statement
