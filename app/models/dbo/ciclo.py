# Generado automáticamente
# Tabla: dbo.ciclo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ciclo(Base):
    __tablename__ = "ciclo"
    __table_args__ = {"schema": "dbo"}

    mes = Column(String(2), nullable=False)
    ano = Column(String(2), nullable=False)
    cerrado = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    ciclo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ciclo(ciclo={self.ciclo})>"