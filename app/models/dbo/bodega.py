# Generado automáticamente
# Tabla: dbo.bodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Bodega(Base):
    __tablename__ = "bodega"
    __table_args__ = {"schema": "dbo"}

    nbodega = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    preferido = Column(Boolean, nullable=False)
    bodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    serie = Column(String(1), nullable=False)
    tipobodega = Column(Integer, nullable=False)
    ruteo = Column(Boolean, nullable=False)
    general = Column(Boolean, nullable=False)
    SUCURSAL = Column(Integer)
    venta = Column(Boolean, nullable=False)
    devolucion = Column(Boolean, nullable=False)
    bipdescuento = Column(Boolean, nullable=False)
    remision = Column(Boolean, nullable=False)
    recarga = Column(Boolean, nullable=False)
    Supermercado = Column(Boolean, nullable=False)
    combustible = Column(Boolean, nullable=False)
    taller = Column(Integer, nullable=False)
    complementofactura = Column(Boolean)
    rutacamion = Column(Integer, nullable=False)
    bodegaproduccion = Column(Boolean, nullable=False)
    consignacion = Column(Boolean, nullable=False)
    servicios = Column(Boolean, nullable=False)
    entransito = Column(Boolean, nullable=False)
    noexcel = Column(Boolean, nullable=False)
    noprint = Column(Boolean, nullable=False)
    caja = Column(Integer, nullable=False)
    recintofiscal = Column(Boolean, nullable=False)
    showroom = Column(Boolean, nullable=False)
    puedofacturar = Column(Boolean, nullable=False)
    puedeSupervisor = Column(Boolean, nullable=False)
    plazos = Column(Boolean, nullable=False)
    cuotam3 = Column(Numeric(6, 2))
    cuotam3seg = Column(Numeric(6, 2))
    reservado = Column(Boolean, nullable=False)
    m_in = Column(Integer, nullable=False)
    h_in = Column(Integer, nullable=False)
    mout = Column(Integer, nullable=False)
    hout = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Bodega(bodega={self.bodega})>"