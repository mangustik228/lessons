from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    name: str
    sex: str
    address: str
    mail: str
    birthdate: str