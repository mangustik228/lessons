from pymongo import MongoClient
from config.config import settings

client = MongoClient(settings.dsn)

collection = client["test_db"]["first_collection"]

# Search by regex
query = {"value": {"$regex": r'is'}}
result_regex = collection.find(query)
print(f'{list(result_regex) = }')


# Search with limit
result_all_with_limit = collection.find().limit(3)
print(f'{list(result_all_with_limit)= }')

# Search with sort by _id
result_sort_by_id = collection.find().sort("_id").limit(5)
print(f"{list(result_sort_by_id) = }")

# size of collection
result_count_documents = collection.count_documents({})
print(f"{result_count_documents = }")
