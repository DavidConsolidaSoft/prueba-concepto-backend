# Generado automáticamente
# Tabla: dbo.fproducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Fproducto(Base):
    __tablename__ = "fproducto"
    __table_args__ = {"schema": "dbo"}

    icdbarra = Column(String(15), nullable=False)
    nfproducto = Column(String(70), nullable=False)
    fbodega = Column(Integer, nullable=False)
    ftipoprod = Column(Integer, nullable=False)
    proveedor = Column(Integer, nullable=False)
    fgrupo = Column(Integer, nullable=False)
    umedida = Column(Integer, nullable=False)
    fmodelo = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    marca = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    costolocal = Column(Numeric(16, 6), nullable=False)
    costoseg = Column(Numeric(16, 6), nullable=False)
    vidautil = Column(Numeric(16, 6), nullable=False)
    gasto = Column(Numeric(16, 6), nullable=False)
    gastolocal = Column(Numeric(16, 6), nullable=False)
    gastoseg = Column(Numeric(16, 6), nullable=False)
    vrescate = Column(Numeric(16, 6), nullable=False)
    vrescatelocal = Column(Numeric(16, 6), nullable=False)
    vrescateseg = Column(Numeric(16, 6), nullable=False)
    cuota = Column(Numeric(16, 6), nullable=False)
    cuotalocal = Column(Numeric(16, 6), nullable=False)
    cuotaseg = Column(Numeric(16, 6), nullable=False)
    depreciado = Column(Boolean, nullable=False)
    cantidad = Column(Integer, nullable=False)
    noserie = Column(String(25), nullable=False)
    chasis = Column(String(25), nullable=False)
    documento = Column(String(25), nullable=False)
    fecha = Column(DateTime, nullable=False)
    comentario = Column(String(254), nullable=False)
    fproducto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    periodoaf = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Fproducto(fproducto={self.fproducto})>"