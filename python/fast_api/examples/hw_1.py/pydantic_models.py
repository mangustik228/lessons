import pydantic

class User(pydantic.BaseModel):
    id:int 
    name:str 
    balance:float