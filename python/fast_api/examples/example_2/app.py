import fastapi
from faker import Faker

faker = Faker('ru_RU')
lst_users = []
fake_db = {}
for i in range(1,35):
    lst_users.append(
        {'id':i,
        'first_name':faker.first_name(),
        'second_name':faker.middle_name(),
        'surname':faker.last_name(),
        'company':faker.company()}
    ) 
fake_db['users'] = lst_users
api = fastapi.FastAPI()



# Если передать get параметры, то будет другое отображение: 
# /users?limit=25&skip=5
@api.get('/users/')
def get_users(skip: int=0, limit: int=10):
    return fake_db['users'][skip:skip+limit]


@api.get('/')
def empty_request():
    return 'hello world'