from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import LecturaHecho, DimSensor, DimTerminal

app = FastAPI()

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/lecturas")
def get_lecturas(db: Session = Depends(get_db)):
    # Obtener las últimas 50 lecturas con información del sensor y terminal
    lecturas = (
        db.query(LecturaHecho, DimSensor.Nombre.label("sensor_nombre"), DimTerminal.Nombre.label("terminal_nombre"))
        .join(DimSensor, LecturaHecho.SensorId == DimSensor.Id)
        .join(DimTerminal, LecturaHecho.TerminalId == DimTerminal.Id)
        .order_by(LecturaHecho.Id.desc())
        .limit(50)
        .all()
    )

    results = [
        {
            "id": l.LecturaHecho.Id,
            "valor": float(l.LecturaHecho.ValorLectura),
            "sensor": l.sensor_nombre,
            "terminal": l.terminal_nombre
        }
        for l in lecturas
    ]

    return results