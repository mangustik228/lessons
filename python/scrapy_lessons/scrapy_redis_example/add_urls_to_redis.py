import json
from redis import Redis
from app.utils import get_url

redis_client = Redis()


for i in range(1, 5):
    for j in range(1, 5):
        url = get_url(i, j)
        data = {
            "url": url,
            "meta": {
                "task_number": f"task_{i}_{j}"
            }
        }
        redis_client.lpush("queue", json.dumps(data))
