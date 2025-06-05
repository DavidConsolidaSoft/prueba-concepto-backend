# Generado automáticamente
# Tabla: dbo.descmax
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Descmax(Base):
    __tablename__ = "descmax"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    porcmax = Column(Numeric(16, 6), nullable=False)
    descmax = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Descmax(descmax={self.descmax})>"