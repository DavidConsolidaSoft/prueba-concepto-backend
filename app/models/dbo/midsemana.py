# Generado automáticamente
# Tabla: dbo.midsemana
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Midsemana(Base):
    __tablename__ = "midsemana"
    __table_args__ = {"schema": "dbo"}

    Domingo = Column(String(1))
    Lunes = Column(String(1))
    Martes = Column(String(1))
    Miercoles = Column(String(1))
    Jueves = Column(String(1))
    Viernes = Column(String(1))
    Sabado = Column(String(1))
    midsemana = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Midsemana(midsemana={self.midsemana})>"