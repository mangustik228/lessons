from fastapi import FastAPI, Depends 
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')
app = FastAPI()

class User(BaseModel):
    username: str 
    email: str | None = None 
    full_name: str | None = None
    disabled: bool | None = None 

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="a@gmail.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_schema)):
    user = fake_decode_token(token)
    return user 


@app.get('/users/me')
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user