from pymongo import MongoClient
from config.config import settings
from utils.functions import generate_fake_data

client = MongoClient(settings.dsn)
collection = client["test_db_2"]["test_update"]
# generate_fake_data(collection)


result = collection.find().limit(2)
print(list(result))

# Update_value
current_value = {"name": "Игнатий"}
new_data = {"$set": {"name": "Ivan"}}
collection.update_one(current_value, new_data)


# Update another value
current_value = {"surname": "Колокольцев"}
new_data = {"$set": {"age": 99}}
collection.update_one(current_value, new_data)

# Drop value
current_value = {"surname": "Зуева"}
new_data = {"$pop": {"language": 1}}
# collection.update_one(current_value, new_data)
print(list(collection.find().limit(3)))
