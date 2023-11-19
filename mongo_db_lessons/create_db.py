from pymongo import MongoClient
from config.config import settings

CLIENT = MongoClient(settings.dsn)

# Получить кластеры(базы), которые существуют
clusters = CLIENT.list_database_names()
print(clusters)

# Создать бд или подключиться к существующей
db = CLIENT["test_db"]

# Создать коллекцию
collection = db.create_collection("first_collection")

clusters = CLIENT.list_database_names()
print(clusters)
