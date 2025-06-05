# Generado automáticamente
# Tabla: dbo.TIPOPLAZA
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipoplaza(Base):
    __tablename__ = "TIPOPLAZA"
    __table_args__ = {"schema": "dbo"}

    TIPOPLAZA = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    DESCRIPCION = Column(String(80))
    activo = Column(Boolean)
    temporal = Column(Boolean)
    permanente = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Tipoplaza(TIPOPLAZA={self.TIPOPLAZA})>"