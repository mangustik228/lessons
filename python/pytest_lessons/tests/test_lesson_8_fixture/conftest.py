import os
import pytest
from random import randrange
import json 

fp = "tests/src/lesson_6.json"

DATA = {
    "id":5,
    "name":"Vasiliy"
}

@pytest.fixture
def create_user_and_delete_user():
    with open(fp, 'w') as file:
        json.dump(DATA, file)
    print(f'Создал бд')
    yield fp 
    os.remove(fp) 
    print(f'Удалил бд')
        

def _calculate(a, b):
    return a + b 


@pytest.fixture
def calculate():
    '''Передать функцию, чтоб вызвать в тесте'''
    return _calculate
