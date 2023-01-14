import fastapi
import database
import pydantic_models
import config
from faker import Faker 
import random

fake = Faker('ru_RU')
fake_db = {}
user_lst = []
for i in range(1, 26):
    user_lst.append(
        {'id':i,
        'name':fake.name(),
        'date':fake.date(),
        'company':fake.company(),
        'balance':random.randint(0,100_000) + random.random()
        }
    )
fake_db['users'] = user_lst
fake_db['users'].append({
    'id':26,
    'name':'Vasya',
    'date':'2019-07-25',
    'company':'without job',
    'balance':'25'
})
api = fastapi.FastAPI()


@api.get('/')
def index():
    return {'response':'this is response from server'}

@api.get('/about_us')
def about():
    return {'About':'This is page about us'}

@api.get('/static/path')
def hello():
    return 'hello'

@api.get('/user/{name}')
def get_nick(name):
    return {'nick':name}

@api.get('/userid/{user_id:int}')
def user_id(user_id):
    return {'user_id_int':user_id}

@api.get('/userid/{user_id}')
def user_id2(user_id):
    return {'user_id_str':user_id}

@api.get('/get_info_by_user_id/{id:int}')
def get_info_by_user_id(id):
    return fake_db['users'][id-1]


@api.get('/get_total_balance')
def get_total_balance():
    total_balance = 0.0
    for user in fake_db['users']:
        total_balance += user['balance']
    return total_balance

@api.get('/get_total_balance_pydantic')
def get_total_balance_pydantic():
    total_balance = 0.0
    for user in fake_db['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance 
