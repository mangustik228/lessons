import copy 
from database import crud
import pydantic_models as pyd 
import config 
import fastapi 
from fastapi import FastAPI, Query, Body 
from time import sleep 

api = FastAPI()


@api.get('/just_sleep')
def just_sleep():
    sleep(15)
    return 'Я поспал'

@api.get("/user/{user_id}")
def read_user(user_id: str, query: str = None):
    if query:
        return {"item_id": user_id, "query": query}
    return {"item_id":user_id}

@api.put('/user/{user_id}')
def update_user(user_id: int, user: pyd.User_to_update = fastapi.Body()):
    return crud.update_user(user).to_dict()


@api.delete('/user/{user_id}')
@crud.db_session
def delete_user(user_id: int = fastapi.Path()):
    crud.get_user_by_id(user_id).delete()
    return f'Юзер {user_id} успешно удален' 

@api.post('/user/create')
def create_user(user:pyd.User_to_create):
    nick = user.nick if user.nick else None 
    return crud\
        .create_user(tg_id=user.tg_id,nick=nick)\
        .to_dict()


@api.get('/get_info_by_user_id/{user_id:int}')
@crud.db_session
def get_info_by_user_id(user_id):
    return crud.get_user_info(crud.User[user_id])



@api.get('/get_user_balance_by_id/{user_id:int}')
@crud.db_session
def get_user_balance_by_id(user_id):
    crud.update_wallet_balance(crud.User[user_id].wallet)
    return crud.User[user_id].wallet.balance

@api.get('/get_total_balance')
@crud.db_session
def get_total_balance():
    balance = 0.0
    crud.update_all_wallets()
    for user in crud.User.select()[:]:
        balance += user.wallet.balance
    return balance 

@api.get("/users")
@crud.db_session 
def get_users(skip: int=0, limit: int=10):
    users = []
    for user in crud.User.select()[skip:skip+limit]:
        users.append(user.to_dict())
    return users

@api.get('/get_info_by_tg_id/{tg_id:int}')
@crud.db_session 
def get_info_by_tg_id(tg_id):
    return crud.get_user_by_tg_id(tg_id).to_dict()