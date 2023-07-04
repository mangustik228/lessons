from datetime import datetime
from pydantic import BaseModel


class SSeler(BaseModel):
    id: int
    title: str
    created_at: datetime
    legal_adress: str | None

    class Config:
        orm_mode = True
