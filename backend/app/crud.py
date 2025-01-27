from sqlalchemy.orm import Session
from app import models, schemas

def get_news(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.News).offset(skip).limit(limit).all()

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news
