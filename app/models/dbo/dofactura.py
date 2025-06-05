# Generado automáticamente
# Tabla: dbo.dofactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dofactura(Base):
    __tablename__ = "dofactura"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    gratificado = Column(Numeric(16, 6), nullable=False)
    bonificado = Column(Numeric(16, 6), nullable=False)
    hcantidad = Column(Numeric(16, 6), nullable=False)
    hreservado = Column(Numeric(16, 6), nullable=False)
    hgratificado = Column(Numeric(16, 6), nullable=False)
    hbonificado = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    preciolista = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    texto = Column(String(10), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    vgdesc = Column(Numeric(16, 6), nullable=False)
    ofactura = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    dofactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    ncmonto = Column(Numeric(16, 6), nullable=False)
    ncafecta = Column(Numeric(16, 6), nullable=False)
    ncexenta = Column(Numeric(16, 6), nullable=False)
    ncviva = Column(Numeric(16, 6), nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    nombre = Column(String(1000), nullable=False)
    nula = Column(Boolean, nullable=False)
    talonario = Column(Integer)
    mes = Column(DateTime)
    apliquemora = Column(Boolean, nullable=False)
    unidadVenta = Column(Integer, nullable=False)
    PrecioUVenta = Column(Numeric(16, 6), nullable=False)
    CantidadUVenta = Column(Numeric(16, 6), nullable=False)
    ReservadoUVenta = Column(Numeric(16, 6), nullable=False)
    BonificadoUVenta = Column(Numeric(16, 6), nullable=False)
    GratificadoUVenta = Column(Numeric(16, 6), nullable=False)
    Cotrans = Column(Numeric(16, 8), nullable=False)
    vendedor = Column(Integer, nullable=False)
    prioridad = Column(Integer, nullable=False)
    estado = Column(Integer, nullable=False)
    factalm = Column(Integer, nullable=False)
    dregciclo = Column(Integer, nullable=False)
    dgratif = Column(Numeric(18, 6), nullable=False)
    gratif = Column(Numeric(18, 6), nullable=False)
    vineta = Column(Boolean, nullable=False)
    bomba = Column(Integer, nullable=False)
    concaja = Column(Boolean, nullable=False)
    bonifreservado = Column(Boolean, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    pcomision = Column(Numeric(5, 2), nullable=False)
    uvendidas = Column(Numeric(16, 8), nullable=False)
    vinculado = Column(Boolean, nullable=False)
    fraccion = Column(Numeric(18, 6), nullable=False)
    nbonif = Column(Integer, nullable=False)
    resolucion1 = Column(String(15))
    resolfecha = Column(DateTime)
    linea = Column(Integer, nullable=False)
    oPrecio = Column(Numeric(18, 6), nullable=False)
    tipoescala = Column(Integer, nullable=False)
    UConfirmada = Column(Numeric(18, 6), nullable=False)
    Ufacturada = Column(Numeric(18, 6), nullable=False)
    cambodega = Column(Integer, nullable=False)
    condicion1 = Column(Boolean, nullable=False)
    ocompra = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    confirmado = Column(Boolean, nullable=False)

    # Relaciones
    # ofactura_rel = relationship("Ofactura", back_populates="dofactura_set")  # Comentado automáticamente
    # producto_rel = relationship("Producto", back_populates="dofactura_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dofactura(dofactura={self.dofactura})>"