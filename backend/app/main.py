from fastapi import FastAPI,Depends
from .database import engine,get_db
from . import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/class/{course}-{number}")
def get_class(number: int,course: str, db: Session = Depends(get_db)):
    #all_classes=db.query(models.Post).filter(models.Post.code==number).filter(models.Post.subject==course).all()
    #return {"all classes": all_classes}
    
    all_classes=db.query(models.Post).filter(models.Post.code==number).filter(models.Post.subject==course).group_by(models.Post.prof)
    return {"all classes": all_classes}