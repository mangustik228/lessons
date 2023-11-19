import random
from loguru import logger
import redis
from string import ascii_letters

client = redis.Redis(host="localhost", port=6380, db=0)


for i in range(5):
    client.incr("new_key")


client.delete("new_key")

client.set("key_1", "value_1", ex=5)
client.set('key_2', "value_2", ex=5)
client.set('key_3', "value_3", ex=5)

for _ in range(20):
    key = ''.join(random.sample(ascii_letters, random.randint(1, 20)))
    client.set(key, 1, ex=20)

result = [i.decode('utf-8') for i in client.keys()]
logger.info(result)
