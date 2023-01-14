import pydantic

class User(pydantic.BaseModel):
    id: int 
    name: str
    date: str
    company: str
    balance: float