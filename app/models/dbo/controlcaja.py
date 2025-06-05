# Generado automáticamente
# Tabla: dbo.controlcaja
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controlcaja(Base):
    __tablename__ = "controlcaja"
    __table_args__ = {"schema": "dbo"}

    controlcaja = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    producto = Column(Integer)
    fecha = Column(String(6))
    caja = Column(Integer)
    t1 = Column(Integer)
    t2 = Column(Integer)
    t3 = Column(Integer)
    t4 = Column(Integer)
    t5 = Column(Integer)
    t6 = Column(Integer)
    t7 = Column(Integer)
    t8 = Column(Integer)
    opagada = Column(Integer)
    docompra = Column(Integer)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controlcaja(controlcaja={self.controlcaja})>"