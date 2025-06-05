# Generado automáticamente
# Tabla: dbo.controlCosto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Controlcosto(Base):
    __tablename__ = "controlCosto"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime)
    cerrado = Column(Boolean)
    ControlCosto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controlcosto(ControlCosto={self.ControlCosto})>"