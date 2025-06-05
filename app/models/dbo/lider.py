# Generado automáticamente
# Tabla: dbo.Lider
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Lider(Base):
    __tablename__ = "Lider"
    __table_args__ = {"schema": "dbo"}

    Lider = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nLider = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Lider(Lider={self.Lider})>"