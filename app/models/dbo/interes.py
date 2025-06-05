# Generado automáticamente
# Tabla: dbo.interes
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Interes(Base):
    __tablename__ = "interes"
    __table_args__ = {"schema": "dbo"}

    ninteres = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    operador = Column(String(8), nullable=False)
    fechainici = Column(DateTime)
    fechafinal = Column(DateTime)
    interessimple = Column(Boolean, nullable=False)
    interescompuesto = Column(Boolean, nullable=False)
    interesmoratorio = Column(Boolean, nullable=False)
    interes = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Interes(interes={self.interes})>"