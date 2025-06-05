# Generado automáticamente
# Tabla: dbo.dcompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dcompra(Base):
    __tablename__ = "dcompra"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    reservado = Column(Numeric(18, 6), nullable=False)
    bonificado = Column(Numeric(18, 6), nullable=False)
    hcantidad = Column(Numeric(18, 6), nullable=False)
    hreservado = Column(Numeric(18, 6), nullable=False)
    hbonificado = Column(Numeric(18, 6), nullable=False)
    precio = Column(Numeric(18, 6), nullable=False)
    preciolista = Column(Numeric(18, 6), nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    costo = Column(Numeric(18, 6), nullable=False)
    tax = Column(Numeric(18, 6), nullable=False)
    cprecio = Column(Numeric(18, 6))
    vtax = Column(Numeric(18, 6))
    gasto = Column(Numeric(18, 6))
    kardex = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    dcompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pdesc = Column(Numeric(18, 6), nullable=False)
    vdesc = Column(Numeric(18, 6), nullable=False)
    vgdesc = Column(Numeric(18, 6), nullable=False)
    fovial = Column(Numeric(18, 6), nullable=False)
    ncmonto = Column(Numeric(18, 6), nullable=False)
    ncafecta = Column(Numeric(18, 6), nullable=False)
    ncexenta = Column(Numeric(18, 6), nullable=False)
    ncviva = Column(Numeric(18, 6), nullable=False)
    nula = Column(Boolean, nullable=False)
    resolucion1 = Column(String(15))
    resolucion2 = Column(String(15))
    resolFecha = Column(DateTime)
    linea = Column(Integer, nullable=False)
    cotrans = Column(Numeric(18, 6), nullable=False)
    resolucion = Column(String(15), nullable=False)
    ptax = Column(Numeric(18, 6), nullable=False)
    tipoescala = Column(Integer, nullable=False)
    costoprom = Column(Numeric(16, 6))
    gratificado = Column(Numeric(9, 2), nullable=False)
    nolote = Column(String(20))
    fecvence = Column(DateTime)
    producto = Column(Integer, nullable=False)
    lote = Column(Integer)
    bodega = Column(Integer, nullable=False)
    precio1 = Column(Numeric(12, 6))
    precio2 = Column(Numeric(12, 6))
    precio3 = Column(Numeric(12, 6))
    precio4 = Column(Numeric(12, 6))
    precio5 = Column(Numeric(12, 6))
    dordentrabajo = Column(Integer)

    # Relaciones
    # kardex_rel = relationship("Kardex", back_populates="dcompra_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dcompra(dcompra={self.dcompra})>"