# Generado automáticamente
# Tabla: dbo.controlperiodo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class ControlPeriodo(Base):
    __tablename__ = "controlperiodo"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime)
    cerrado = Column(Boolean)
    controlPeriodo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    caja = Column(Integer)
    sincro = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Controlperiodo(controlPeriodo={self.controlPeriodo})>"