# Generado automáticamente
# Tabla: dbo.doventa
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Doventa(Base):
    __tablename__ = "doventa"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    bonificado = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    preciolist = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    tax = Column(Numeric(16, 6), nullable=False)
    cprecio = Column(Numeric(16, 6), nullable=False)
    vtax = Column(Numeric(16, 6), nullable=False)
    gasto = Column(Numeric(16, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    oventa = Column(Integer, nullable=False)
    venta = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    vgdesc = Column(Numeric(16, 6), nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    rcantidad = Column(Numeric(16, 6), nullable=False)
    rreservado = Column(Numeric(16, 6), nullable=False)
    rbonificado = Column(Numeric(16, 6), nullable=False)
    rprecio = Column(Numeric(16, 6), nullable=False)
    rmontfact = Column(Numeric(16, 6), nullable=False)
    rpdesc = Column(Numeric(16, 6), nullable=False)
    rvdesc = Column(Numeric(16, 6), nullable=False)
    ccantidad = Column(Numeric(16, 6), nullable=False)
    presenta = Column(Integer, nullable=False)
    doventa = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    unidades = Column(Numeric(16, 6), nullable=False)
    cbonificado = Column(Numeric(18, 6), nullable=False)
    linea = Column(Integer)
    fechaDespacho = Column(DateTime)
    fechaRecepcion = Column(DateTime)
    disponible = Column(Numeric(18, 6), nullable=False)
    kardex = Column(Integer, nullable=False)
    bodega1 = Column(Integer)
    oprecio = Column(Numeric(12, 2), nullable=False)
    pcomision = Column(Numeric(6, 2), nullable=False)
    derecinto = Column(Numeric(12, 2), nullable=False)
    detransito = Column(Numeric(12, 2), nullable=False)
    comprar = Column(Numeric(12, 2), nullable=False)
    autorizado = Column(Numeric(12, 2), nullable=False)
    nombre = Column(String(1000))
    nosujeto = Column(Numeric(12, 2), nullable=False)
    gratif = Column(Numeric(12, 2), nullable=False)

    def __repr__(self):
        return "<Doventa(activo={self.activo})>"