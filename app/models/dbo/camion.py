# Generado automáticamente
# Tabla: dbo.camion
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Camion(Base):
    __tablename__ = "camion"
    __table_args__ = {"schema": "dbo"}

    ncamion = Column(String(35), nullable=False)
    chasis = Column(String(25), nullable=False)
    motor = Column(String(25), nullable=False)
    notas = Column(String(120), nullable=False)
    mantenimiento = Column(Boolean, nullable=False)
    caracteristica = Column(String(60), nullable=False)
    camion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    propio = Column(Boolean, nullable=False)
    ejes = Column(Integer, nullable=False)
    marca = Column(String(25), nullable=False)
    year = Column(String(5), nullable=False)
    nacionalidad = Column(Integer, nullable=False)
    placa = Column(String(10))
    motorista = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    transpte = Column(Integer, nullable=False)
    tipovehiculo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Camion(camion={self.camion})>"