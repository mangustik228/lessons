from fastapi import FastAPI, Depends, Body
import schemas
from models import session
import models
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello_world():
    return {'status':'ok'}


@app.get('/users', response_model=list[schemas.UserGet]|None)
def get_users():
    users=session.query(models.User).all()
    return [{
        "id":user.id,
        "name":user.name,
        "age":user.age
    } for user in users]


@app.post('/user')
def post_user(user:schemas.UserGet=Body()):
    user=models.User(**user.dict())
    session.add(user)
    session.commit()
    return {'status':'user created'}

@app.delete('/user')
def delete_user(user:schemas.UserGet=Body()):
    deleted_counted = session.query(models.User).filter_by(id=user.id, name=user.name).delete()
    session.commit()
    logger.info(f'Удален успешно с id')
    return {'status':f'user deleted {deleted_counted} шт'} if deleted_counted else {'status':'такого юзера не было'}

