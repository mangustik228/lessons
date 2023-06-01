import json


def test_just_test(calculate: callable):
    result = calculate(1, 2)
    assert 1 == 1 


def test_create_and_delete_file(create_user_and_delete_user):
    with open(create_user_and_delete_user, 'r') as file:
        data = json.load(file)
     