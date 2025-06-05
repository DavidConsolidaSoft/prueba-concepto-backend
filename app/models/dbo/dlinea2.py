# Generado automáticamente
# Tabla: dbo.dlinea2
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dlinea2(Base):
    __tablename__ = "dlinea2"
    __table_args__ = {"schema": "dbo"}

    dlinea2 = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dlinea1 = Column(Integer, nullable=False)
    rusuario = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    hora1 = Column(DateTime)
    hora2 = Column(DateTime)
    Notas = Column(String(200))
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dlinea2(dlinea2={self.dlinea2})>"