# Generado automáticamente
# Tabla: dbo.reloj
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Reloj(Base):
    __tablename__ = "reloj"
    __table_args__ = {"schema": "dbo"}

    reloj = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nreloj = Column(String(100), nullable=False)
    codreloj = Column(Integer, nullable=False)
    hecomoingreso = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Reloj(reloj={self.reloj})>"