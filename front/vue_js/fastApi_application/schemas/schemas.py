from pydantic import BaseModel


class UserGet(BaseModel):
    id: int | None
    name: str 
    age: int | None 
