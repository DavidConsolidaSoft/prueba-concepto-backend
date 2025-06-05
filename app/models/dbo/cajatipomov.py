# Generado automáticamente
# Tabla: dbo.cajatipomov
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Cajatipomov(Base):
    __tablename__ = "cajatipomov"
    __table_args__ = {"schema": "dbo"}

    cajatipomov = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    caja = Column(Integer)
    tipomov = Column(Integer)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Cajatipomov(cajatipomov={self.cajatipomov})>"