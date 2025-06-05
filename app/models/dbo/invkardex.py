# Generado automáticamente
# Tabla: dbo.invkardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Invkardex(Base):
    __tablename__ = "invkardex"
    __table_args__ = {"schema": "dbo"}

    mes = Column(DateTime)
    costoprom = Column(Numeric(18, 6), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    INVFIN = Column(Numeric(16, 6), nullable=False)
    QINVFIN = Column(Numeric(16, 6), nullable=False)
    kardex = Column(Integer,primary_key=True, nullable=False)
    producto = Column(Integer)

    def __repr__(self):
        return "<Invkardex(mes={self.mes})>"