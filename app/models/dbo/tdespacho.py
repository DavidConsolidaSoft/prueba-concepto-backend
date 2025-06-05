# Generado automáticamente
# Tabla: dbo.tdespacho
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tdespacho(Base):
    __tablename__ = "tdespacho"
    __table_args__ = {"schema": "dbo"}

    numedocu = Column(String(10), nullable=False)
    fecha = Column(DateTime, nullable=False)
    transpte = Column(Integer, nullable=False)
    motorista = Column(String(45), nullable=False)
    placa = Column(String(12), nullable=False)
    tdespacho = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    valorfleteton = Column(Numeric(16, 6), nullable=False)
    valorfleteviaje = Column(Numeric(16, 6), nullable=False)
    bultos = Column(String(15), nullable=False)
    kmsalida = Column(Numeric(16, 6), nullable=False)
    kmretorno = Column(Numeric(16, 6), nullable=False)
    kmrecorrido = Column(Numeric(16, 6), nullable=False)
    descripcion = Column(String(50), nullable=False)
    capacidadcont = Column(String(10), nullable=False)
    deposito = Column(Numeric(16, 6), nullable=False)
    peso = Column(Numeric(16, 6), nullable=False)
    destino = Column(String(50), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    notas = Column(String(120), nullable=False)
    bodega = Column(Integer, nullable=False)
    cerrado = Column(Boolean, nullable=False)
    caja = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tdespacho(tdespacho={self.tdespacho})>"