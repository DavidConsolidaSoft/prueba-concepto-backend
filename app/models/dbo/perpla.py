# Generado automáticamente
# Tabla: dbo.perpla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Perpla(Base):
    __tablename__ = "perpla"
    __table_args__ = {"schema": "dbo"}

    nperpla = Column(String(50), nullable=False)
    nopla = Column(Numeric(6, 4), nullable=False)
    activo = Column(Boolean, nullable=False)
    perpla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Perpla(perpla={self.perpla})>"