# Generado automáticamente
# Tabla: dbo.recordar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Recordar(Base):
    __tablename__ = "recordar"
    __table_args__ = {"schema": "dbo"}

    nrecordar = Column(String(25))
    hrecordar = Column(Numeric(18, 6))
    recordar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Recordar(recordar={self.recordar})>"