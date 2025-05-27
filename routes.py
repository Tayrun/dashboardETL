from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from . import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/lecturas/")
def obtener_lecturas(db: Session = Depends(get_db)):
    return db.query(models.LecturaHecho).all()
