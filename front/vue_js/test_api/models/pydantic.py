from typing import Literal
from pydantic import BaseModel


class CvTypesSchema(BaseModel):
    title: str = "Заголовок"
    subtitle: str = "Подзаголовок"
    avatar: str = "Аватар"
    text: str = "Текст"


class CvPostRequest(BaseModel):
    type_: Literal['Заголовок', 'Подзаголовок', 'Аватар', 'Текст']
    data: str | bytes
    user_id: int


class TextData(BaseModel):
    title: str
    text: str


class TextResponse(BaseModel):
    status: Literal["ok"]
    user_id: int
    data: list[TextData]
