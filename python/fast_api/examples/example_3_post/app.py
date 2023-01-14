import fastapi
from fastapi import Request
from faker import Faker 
from pydantic_models import User

faker = Faker('ru_RU')
fake_db = {}
users_lst = []
for i in range(1,25):
    users_lst.append({'id': i, **faker.simple_profile()})
fake_db['users'] = users_lst


api = fastapi.FastAPI()

@api.get('/')
@api.post('/')
@api.put('/')
@api.delete('/')
def index(request: Request):
    return {'Request': [
                request.method,
                request.headers
                ]
            }

@api.get('/users/')
def users(skip:int = 0, limit:int = 10):
    return fake_db['users'][skip:skip+limit]

@api.post('/users/create')
def post_users(user: User):
    fake_db['users'].append(user)
    return {'User Created!': user}

@api.put('/user/{user_id:int}')
def update_user(user_id: int, user: User = fastapi.Body()):
    # return fastapi.Body()
    for index, old_user in enumerate(fake_db['users']):
        if old_user['id'] == user_id:
            fake_db['users'][index] = user
        return fake_db['users'][index]


@api.get('/user/{user_id:int}')
def get_info_user(user_id:int):
    for user in fake_db['users']:
        if user['id'] == user_id:
            return user