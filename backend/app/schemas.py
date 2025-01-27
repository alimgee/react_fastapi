from pydantic import BaseModel
from datetime import datetime

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
