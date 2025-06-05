# Generado automáticamente
# Tabla: dbo.pEntrega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Pentrega(Base):
    __tablename__ = "pEntrega"
    __table_args__ = {"schema": "dbo"}

    pEntrega = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    fecha = Column(DateTime, nullable=False)
    concepto = Column(Integer, nullable=False)
    Distrito = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Pentrega(pEntrega={self.pEntrega})>"