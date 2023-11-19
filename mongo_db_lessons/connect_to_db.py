from pymongo import MongoClient
from config.config import settings


client = MongoClient(settings.dsn)


collection = client["test_db"]["first_collection"]

# client.test_db.second_collection.insert_one({"_id": 1, "value": "value_1"})


one_value = client.test_db.second_collection.find_one({"_id": 1})
second_value = client.test_db.second_collection.find_one({"_id": 2})

# client.test_db.second_collection.insert_one({"_id": 2, "value": "value_2"})

all_value = client.test_db.second_colletion.find()

print(one_value)
print(second_value)
print(all_value)
print(list(all_value))

for value in all_value:
    print(value)
