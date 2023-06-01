from pydantic import BaseModel, validator 

class Post(BaseModel):
    id: int 
    title: str 
    name: str | None 
