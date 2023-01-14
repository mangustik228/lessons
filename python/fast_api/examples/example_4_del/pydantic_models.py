from pydantic import BaseModel
from faker import Faker 

faker = Faker('ru_RU')
fake_db = {}
users_lst = []
for i in range(1,25):
    users_lst.append({'id': i, **faker.simple_profile()})
fake_db['users'] = users_lst

class User(BaseModel):
    id: int
    username: str
    name: str
    sex: str
    address: str
    mail: str
    birthdate: str