import json
import random
import uuid
from loguru import logger
from redis import Redis
from mimesis import Person
from pydantic import BaseModel, Field


client = Redis("localhost", 6379, 0)


def random_age():
    return random.randint(1, 80)


def get_random_uuid(prefix):
    return lambda: prefix + "_" + str(uuid.uuid4())


class BasePerson(BaseModel):
    age: int = Field(..., default_factory=random_age)
    name: str = Field(..., default_factory=Person('ru').name)
    surname: str = Field(..., default_factory=Person("ru").surname)


class Person(BasePerson):
    key: str = Field(..., default_factory=get_random_uuid("person"))


lst_persons = [Person() for i in range(50)]

for person in lst_persons:
    client.set(person.key, person.model_dump_json(), ex=20)

for person_uuid in client.scan_iter("person_*"):
    person = BasePerson.model_validate_json(client.get(person_uuid))
    print(person)


# print(lst_persons)


# class Person(BaseModel):
#     id: int | None
#     age: int
#     name: str
#     surname: str


# data = [
#     {
#         "id": i,
#         "age": random.randint(1, 35),
#         "name": Person('ru').name(),
#         "surname": Person("ru").surname()
#     } for i in range(15)]


# for datum in data:
#     client.lpush(f"person-{datum.pop('id')}", json.dumps(datum))

# result = client.lrange("person-3", 0, 15)

# result = [json.loads(i) for i in result]


# logger.info(result)

# client.delete("ozon")
# client.rpush("ozon", 1)
# client.rpush("ozon", 2)
# client.rpush("ozon", 3)
# client.rpush("ozon", 4)
# client.rpush("ozon", 5, 6, 7, 8, 9, 10)
# result = client.lrange("ozon", 0, 100)
# print(client.llen("ozon"))
# print(client.llen("wb"))
# print(result)
# print(client.lindex("ozon", 5))

# client.close()
