from fastapi import FastAPI 
from pydantic import BaseModel

USERS = []


class DegreeType(BaseModel):
    beginner: "beginner"
    junior: "junior"


class Degree(BaseModel):
    id: int 
    name: DegreeType


class User(BaseModel):
    id: int 
    name: str 
    degree: list[Degree]


app = FastAPI()


@app.get('/')
def hello_world():
    return "hello world"


@app.post('/users')
def post_users(users: list[User]):
    USERS.extend(users)
    return {"status": 200,
            "data": users}