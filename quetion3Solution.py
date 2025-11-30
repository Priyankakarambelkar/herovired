from http import client
from pymongo import MongoClient
import configparser
from io import StringIO
# create and write to input.txt

with open('file.txt', 'w') as f:
    f.write("[Database]\nhost = localhost\nport = 3306\nusername = admin\npassword = secret\n[Server]\naddress = 192.168.0.1\nport = 8080")

config_dict = {}


# Read the file and create dictionary
with open('file.txt','r') as file:
    config = configparser.ConfigParser()
    config.read_file(file)
    config_dict = {section: dict(config.items(section)) for section in config.sections()}


print(config_dict)

client = MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]
collection = db["my_gfg_collection"]

rec_id1 = collection.insert_one(config_dict)

# Display inserted documents
print("\nInserted records:")
for record in collection.find():
    print(record)

