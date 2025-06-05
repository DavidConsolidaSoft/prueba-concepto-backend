# Generado automáticamente
# Tabla: dbo.compra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Compra(Base):
    __tablename__ = "compra"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    aplicaexistencia = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    tipomov = Column(Integer, nullable=False)
    numedocu = Column(String(45))
    pedido = Column(String(10), nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipovta = Column(Integer, nullable=False)
    encompra = Column(Integer, nullable=False)
    proveedor = Column(Integer, nullable=False)
    proveedor2 = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    cprodprec = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(18, 6), nullable=False)
    tasacambioseg = Column(Numeric(18, 6), nullable=False)
    tasacambiotres = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    tax = Column(Numeric(18, 6), nullable=False)
    descuentos = Column(Numeric(18, 6), nullable=False)
    descaplica = Column(Boolean, nullable=False)
    flete = Column(Numeric(18, 6), nullable=False)
    fob = Column(Numeric(18, 6), nullable=False)
    seguro = Column(Numeric(18, 6), nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    montcomp = Column(Numeric(18, 6), nullable=False)
    montgasto = Column(Numeric(18, 6), nullable=False)
    montbonif = Column(Numeric(18, 6), nullable=False)
    pdesc = Column(Numeric(18, 6), nullable=False)
    vdesc = Column(Numeric(18, 6), nullable=False)
    notas = Column(String(300))
    compra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    basesiniva = Column(Boolean, nullable=False)
    cargo = Column(Numeric(18, 6), nullable=False)
    abono = Column(Numeric(18, 6), nullable=False)
    nproveedor = Column(String(50), nullable=False)
    nocuenta = Column(String(25), nullable=False)
    registro = Column(String(15), nullable=False)
    noPoliza = Column(String(10), nullable=False)
    GASTOS = Column(Numeric(18, 6), nullable=False)
    Partida = Column(Integer, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    bodega = Column(Integer, nullable=False)
    taller = Column(Boolean, nullable=False)
    tiquetinicial = Column(Integer, nullable=False)
    tiquetfinal = Column(Integer, nullable=False)
    numtiquet = Column(Integer, nullable=False)
    canttiquet = Column(Integer, nullable=False)
    precioUnitario = Column(Numeric(18, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    cotrans = Column(Numeric(18, 6), nullable=False)
    preventa = Column(Boolean, nullable=False)
    poliza = Column(String(25), nullable=False)
    gestiontaller = Column(Integer)

    # Relaciones
    # iva_rel = relationship("Iva", back_populates="compra_set")  # Comentado automáticamente
    # tipomov_rel = relationship("Tipomov", back_populates="compra_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Compra(compra={self.compra})>"