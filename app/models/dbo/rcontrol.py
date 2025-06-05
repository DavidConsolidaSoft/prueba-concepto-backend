# Generado automáticamente
# Tabla: dbo.rcontrol
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rcontrol(Base):
    __tablename__ = "rcontrol"
    __table_args__ = {"schema": "dbo"}

    variable = Column(String(25), nullable=False)
    valor = Column(Boolean, nullable=False)
    ncondicion = Column(String(100), nullable=False)
    rcontrol = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dia = Column(Integer)
    caja = Column(Integer)

    def __repr__(self):
        return "<Rcontrol(rcontrol={self.rcontrol})>"