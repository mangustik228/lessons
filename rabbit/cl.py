from loguru import logger
import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, db=0)

message = {
    "title": "new msg-2",
    "content": "new content-2"
}

redis_client.hset

logger.info('send message')
