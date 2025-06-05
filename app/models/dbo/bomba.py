# Generado automáticamente
# Tabla: dbo.bomba
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Bomba(Base):
    __tablename__ = "bomba"
    __table_args__ = {"schema": "dbo"}

    nbomba = Column(String(20), nullable=False)
    bodega = Column(Integer, nullable=False)
    Bomba = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Bomba(Bomba={self.Bomba})>"