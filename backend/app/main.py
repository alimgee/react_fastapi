from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, crud  # Adjusted import for package
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    return crud.create_news(db=db, news=news)

@app.get("/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_news(db=db, skip=skip, limit=limit)
