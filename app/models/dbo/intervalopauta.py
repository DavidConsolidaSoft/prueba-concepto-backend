# Generado automáticamente
# Tabla: dbo.IntervaloPauta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Intervalopauta(Base):
    __tablename__ = "IntervaloPauta"
    __table_args__ = {"schema": "dbo"}

    nIntervaloPauta = Column(String(35), nullable=False)
    Lunes = Column(Boolean, nullable=False)
    Martes = Column(Boolean, nullable=False)
    Miercoles = Column(Boolean, nullable=False)
    Jueves = Column(Boolean, nullable=False)
    viernes = Column(Boolean, nullable=False)
    sabado = Column(Boolean, nullable=False)
    domingo = Column(Boolean, nullable=False)
    IntervaloPauta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Intervalopauta(IntervaloPauta={self.IntervaloPauta})>"