# Generado automáticamente
# Tabla: dbo.controldia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controldia(Base):
    __tablename__ = "controldia"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime)
    cdia = Column(String(2))
    controldia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controldia(controldia={self.controldia})>"