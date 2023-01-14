from pydantic_models import User 
import fastapi
from faker import Faker 


faker = Faker('ru_RU')

api = fastapi.FastAPI()

fake_db = {
    'users':[
        {'id':1,
        'name':faker.first_name(),
        'middle_name':faker.middle_name(),
        'last_name':faker.last_name(),
        'balance':15300},
        {'id':2,
        'name':faker.first_name(),
        'surname':faker.last_name(),
        'balance':160.23},
        {'id':3,
        'name':faker.first_name(),
        'surname':faker.last_name(),
        'balance':'25000'},
    ]
}

@api.get('/get_full_balance')
def get_full_balance():
    total_balance = 0.0 
    for user in fake_db['users']:
        total_balance += User(**user).balance
    return total_balance 


@api.get('/hello')
def hello():
    return 'hello'


@api.get('/get_info_user_by_id/{user_id:int}')
def get_info_user_by_id(user_id):
    return fake_db['users'][user_id-1]


