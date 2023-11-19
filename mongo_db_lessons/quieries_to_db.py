from pymongo import MongoClient
from config.config import settings


client = MongoClient(settings.dsn)

collection = client["test_db"]["first_collection"]

result_one = collection.find_one({"_id": 1})
result_none = collection.find_one({"_id": 2})
result_all = collection.find()
print(f"{result_one = }", end="\n\n")
print(f"{result_none = }", end="\n\n")
print(f"{list(result_all) = }", end="\n\n")

query = {"value": 357}
filter_ = {"_id": False, "value": True}
result_filter = collection.find(query, filter_)
print(f"{list(result_filter) = }", end="\n\n")
