import time
from datetime import timedelta

import redis
from loguru import logger

redis_client = redis.Redis(host="localhost", port=6379, db=0)


redis_client.set("key-1", "hello", timedelta(seconds=5))
redis_client.set("key-2", 5, timedelta(seconds=8))
redis_client.set("key-3", "world", timedelta(seconds=1))
logger.debug('set values. go to sleep...')
time.sleep(2)
for i in range(1, 4):
    result = redis_client.get(f"key-{i}")
    logger.debug(type(result))
    logger.debug(result)

redis_client.close()
