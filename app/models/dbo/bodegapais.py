# Generado automáticamente
# Tabla: dbo.BodegaPais
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, BigInteger
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Bodegapais(Base):
    __tablename__ = "BodegaPais"
    __table_args__ = {"schema": "dbo"}

    bodegapais = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    pais = Column(Integer, nullable=False)
    Orden = Column(String(1), nullable=False)
    bodega = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Bodegapais(bodegapais={self.bodegapais})>"