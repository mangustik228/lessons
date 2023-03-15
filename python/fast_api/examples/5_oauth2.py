from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt 
from passlib.context import CryptContext


class Token(BaseModel):
    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    username: str | None = None 

class Admin(BaseModel):
    username: str 

class UserInDB(Admin):
    hashed_password: str 

api = FastAPI()
SECRET_KEY = '2cf98a6a1758bfae2045db1b42a1ab1efc9383d0ab37f592fad37bb163623688'
ALGORITHM = 'HS256'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
USERNAME = 'admin'
PASSWORD = '$2b$12$S30C/ZLLK2MUKRYZO3X52OeaPP2uBN2YSyHAL23nJWoaZebMSsbyO'
CREDENTIALS_EXCEPTION = lambda msg: HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=msg, 
        headers={"WWW-Authenticate":"Bearer"}
    )


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    if username == USERNAME:
        return UserInDB(username=username, hashed_password=PASSWORD)
    
def authenticate_user(username:str, password:str):
    user = get_user(username)
    if not user:
        return False 
    if not verify_password(password, user.hashed_password):
        return False
    return user 

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt 

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try: 
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username: str = payload.get("sub")
        if username is None: 
            raise CREDENTIALS_EXCEPTION('not validate credentials') 
        token_data = TokenData(username=username)
    except JWTError:
        raise CREDENTIALS_EXCEPTION('not validate credentials')  
    user = get_user(username=token_data.username)
    if user is None: 
        raise CREDENTIALS_EXCEPTION('not validate credentials') 
    return user 


@api.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        CREDENTIALS_EXCEPTION('incorrect username or password')
    access_token = create_access_token(
        data={"sub":user.username})
    return{"access_token":access_token, "token_type":"bearer"}


@api.get("/users/me", response_model=Admin)
async def read_users_me(current_user: Admin = Depends(get_current_user)):
    return current_user


