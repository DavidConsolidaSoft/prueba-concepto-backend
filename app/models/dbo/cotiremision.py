# Generado automáticamente
# Tabla: dbo.cotiremision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Cotiremision(Base):
    __tablename__ = "cotiremision"
    __table_args__ = {"schema": "dbo"}

    cotiremision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cambodega = Column(Integer)
    oventa = Column(Integer)
    aremisionar = Column(Numeric(18, 6))
    remisionado = Column(Numeric(18, 6))
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    doventa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Cotiremision(cotiremision={self.cotiremision})>"