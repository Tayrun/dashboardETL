from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from fastapi.responses import HTMLResponse

class DimSensor(Base):
    __tablename__ = 'DimSensor'
    Id = Column(Integer, primary_key=True)
    Nombre = Column(String(255))
    Tipo = Column(String(255))
    Unidad = Column(String(50))

class DimTerminal(Base):
    __tablename__ = 'DimTerminal'
    Id = Column(Integer, primary_key=True)
    Nombre = Column(String(255))
    Ubicacion = Column(String(255))
    EmbalseNombre = Column(String(255))

class LecturaHecho(Base):
    __tablename__ = 'LecturaHecho'
    Id = Column(Integer, primary_key=True)
    TiempoId = Column(Integer, ForeignKey('DimTiempo.Id'))
    UsuarioId = Column(Integer, ForeignKey('DimUsuario.Id'))
    TerminalId = Column(Integer, ForeignKey('DimTerminal.Id'))
    DispositivoId = Column(Integer, ForeignKey('DimDispositivo.Id'))
    SensorId = Column(Integer, ForeignKey('DimSensor.Id'))
    ValorLectura = Column(Float)