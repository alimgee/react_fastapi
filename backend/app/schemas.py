from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role: str

    class Config:
        orm_mode = True

class NewsBase(BaseModel):
    title: str
    content: str
    link: str
    date: datetime
    provider: str

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
