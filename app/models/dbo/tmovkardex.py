# Generado automáticamente
# Tabla: dbo.tmovkardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tmovkardex(Base):
    __tablename__ = "tmovkardex"
    __table_args__ = {"schema": "dbo"}

    id = Column(String(1), nullable=False)
    fecha = Column(DateTime, nullable=False)
    ntipomov = Column(String(40), nullable=False)
    numedocu = Column(String(9), nullable=False)
    lote = Column(Numeric(16, 6), nullable=False)
    bodega = Column(Numeric(16, 6), nullable=False)
    entrada = Column(Numeric(16, 6), nullable=False)
    salida = Column(Numeric(16, 6), nullable=False)
    saldo = Column(Numeric(16, 6), nullable=False)
    valor = Column(Numeric(16, 6), nullable=False)
    costouni = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    costoseg = Column(Numeric(16, 6), nullable=False)
    ordenador = Column(String(1), nullable=False)
    tmovkardex = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Tmovkardex(tmovkardex={self.tmovkardex})>"