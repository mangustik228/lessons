from random import randint
from pymongo import MongoClient
from config.config import settings

client = MongoClient(settings.dsn)

collection = client["test_db"]["first_collection"]


collection.insert_one({"_id": 1, "value": "this is first value"})
collection.insert_one({"_id": randint(5, 500), "value": randint(5, 500)})


many_values = [
    {"_id": randint(500, 1000), "value": "hello world"} for _ in range(5)
]

result = collection.insert_many(many_values)

print(result)
