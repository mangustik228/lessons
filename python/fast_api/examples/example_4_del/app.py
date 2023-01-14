from pydantic_models import User, fake_db
import fastapi 
from fastapi import Request

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

@api.get('/users')
def get_info_users(skip:int = 0, limit:int = 10):
    return fake_db['users'][skip:skip+limit]



@api.get('/user/{user_id:int}')
def get_info_user(user_id):
    for user in fake_db['users']:
        if user['id'] == user_id:
            return user 
    return 'Nothing'

@api.post('/user/create')
def create_user(user: User):
    fake_db['users'].append(dict(user))
    return {'create new user': user}


@api.put('/user/{user_id:int}')
def update_user(user_id:int, user: User = fastapi.Body()):
    '''
    `fastapi.Body()` - явно указывает что переменную брать из тела запроса
    '''
    for index, us in enumerate(fake_db['users']):
        if us['id'] == user_id:
            fake_db['users'][index] = dict(user) 
            return {'Sucsefull update':user}
    return {'Don\'t finded user': user}

@api.delete('/user/{user_id}')
def delete_user(user_id:int = fastapi.Path()):
    '''
    `fastapi.Path()` - явно указывает что переменную брать из пути
    '''
    for index, u in enumerate(fake_db['users']):
        if u['id'] == user_id:
            del fake_db['users'][index]
            return {'delete_user': u}