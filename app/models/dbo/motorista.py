# Generado automáticamente
# Tabla: dbo.motorista
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Motorista(Base):
    __tablename__ = "motorista"
    __table_args__ = {"schema": "dbo"}

    nmotorista = Column(String(35), nullable=False)
    ordenNumero = Column(String(15), nullable=False)
    notas = Column(String(120), nullable=False)
    motorista = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(150), nullable=False)
    licencia = Column(String(20), nullable=False)
    carnet = Column(String(15), nullable=False)
    nacionalidad = Column(Integer, nullable=False)
    empleado = Column(Integer, nullable=False)
    codaduanero = Column(String(15), nullable=False)

    def __repr__(self):
        return "<Motorista(motorista={self.motorista})>"