# Generado automáticamente
# Tabla: dbo.nmicontrol
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Nmicontrol(Base):
    __tablename__ = "nmicontrol"
    __table_args__ = {"schema": "dbo"}

    nmicontrol = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    clave = Column(String(50))
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    nconn = Column(Integer, nullable=False)
    naut = Column(Integer, nullable=False)
    ntiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Nmicontrol(nmicontrol={self.nmicontrol})>"