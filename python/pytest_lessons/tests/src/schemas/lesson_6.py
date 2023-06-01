from typing import Literal
from pydantic import BaseModel, Field, validator
from enum import Enum

class _Links(BaseModel):
    previous: bool | None
    current: str
    next: str 
    
class _Pagination(BaseModel):
    total: int 
    pages: int 
    page: int 
    limit: int 
    links: _Links

class _Meta(BaseModel):
    pagination: _Pagination

class _Item(BaseModel):
    id: int 
    name: str 
    email: str 
    gender: Literal["female", "male"]
    status: Literal["inactive", "active"]

class ResponseLesson(BaseModel):
    meta: _Meta
    data: list[_Item]