from config.config import settings
from pymongo import MongoClient
from utils.functions import generate_fake_data

client = MongoClient(settings.dsn)


collection = client["test_db"]["delete_doc"]
# generate_fake_data(collection, print_=True)


# Delete document
value = collection.delete_one({"surname": {"$regex": r'Дубова'}})
result_all = collection.find()
print(value.deleted_count)  # Deleted
print(list(result_all))
