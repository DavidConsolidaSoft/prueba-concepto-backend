# Generado automáticamente
# Tabla: dbo.oventa
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Oventa(Base):
    __tablename__ = "oventa"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    numedocu = Column(String(9), nullable=False)
    pedido = Column(String(10), nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipovta = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    proveedor = Column(Integer, nullable=False)
    proveedor2 = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    cprodprec = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    tax = Column(Numeric(16, 6), nullable=False)
    descuentos = Column(Numeric(16, 6), nullable=False)
    descaplica = Column(Boolean, nullable=False)
    flete = Column(Numeric(16, 6), nullable=False)
    fob = Column(Numeric(16, 6), nullable=False)
    seguro = Column(Numeric(16, 6), nullable=False)
    monto = Column(Numeric(16, 6), nullable=False)
    montcomp = Column(Numeric(16, 6), nullable=False)
    montgasto = Column(Numeric(16, 6), nullable=False)
    montbonif = Column(Numeric(16, 6), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    notas = Column(String(400))
    oventa = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    rfecha = Column(DateTime)
    rnumedocu = Column(String(9), nullable=False)
    venta = Column(Integer, nullable=False)
    rmontcomp = Column(Numeric(16, 6), nullable=False)
    pagada = Column(Boolean, nullable=False)
    pfecha = Column(DateTime)
    proyecto = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    fechaDespacho = Column(DateTime)
    fechaRecepcion = Column(DateTime)
    retencion = Column(Numeric(18, 6), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    clientes = Column(String(25), nullable=False)
    nclientes = Column(String(60), nullable=False)
    tipopedido = Column(Integer, nullable=False)
    datoscliente = Column(String(450), nullable=False)
    factura = Column(Integer, nullable=False)
    basesinimpuesto = Column(Boolean, nullable=False)
    nosujeto = Column(Numeric(12, 2), nullable=False)
    dgratif = Column(Numeric(12, 2), nullable=False)

    def __repr__(self):
        return "<Oventa(activo={self.activo})>"