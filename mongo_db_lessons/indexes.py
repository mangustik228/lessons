from config.config import settings
from pymongo import MongoClient
from utils.functions import generate_fake_data

client = MongoClient(settings.dsn)
collection = client["test_db"]["indexes_collection"]

print(list(collection.find()))

# create index
collection.create_index("name")
print(f'{collection.index_information() = }')

# create uniquie index
collection.create_index("surname", unique=True)
print(f'{collection.index_information() = }')

# add index
collection.drop_index("name_1")  # Надо посмотреть как называеться индекс
print(f'{collection.index_information() = }')

collection.insert_one({"name": "Vasiliy", "surname": "Боярская"})
