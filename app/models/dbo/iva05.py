# Generado automáticamente
# Tabla: dbo.iva05
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Float
from sqlalchemy import Column, String


class Iva05(Base):
    __tablename__ = "iva05"
    __table_args__ = {"schema": "dbo"}

    periodoiva = Column(Float)
    fecha = Column(DateTime)
    nocheque = Column(String(255))
    numedocu = Column(Float)
    proveedor = Column(Float)
    moneda = Column(Float)
    afecta  = Column(Float)
    importacion = Column(Float)
    viva = Column(Float)
    exenta = Column(Float)
    retencion = Column(Float)
    horatiempo = Column(DateTime)
    usario = Column(Float)
    otro = Column(Float)
    fovial = Column(Float)
    nproveedor = Column(String(255))
    nocuenta = Column(String(255),primary_key=True)
    tipobodega = Column(Float)
    percepcion = Column(Float)
    partida = Column(Float)
    pagos = Column(Float)
    compras = Column(Float)

    def __repr__(self):
        return "<Iva05(periodoiva={self.periodoiva})>"