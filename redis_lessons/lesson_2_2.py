import random
import redis
from string import ascii_letters

client = redis.Redis("localhost", 6380, db=0)

for _ in range(100):
    client.set(
        "".join(random.sample(ascii_letters, random.randint(1, 5))),
        1,
        ex=20
    )

for item in client.scan_iter("*z"):
    print(item)

client.close()
