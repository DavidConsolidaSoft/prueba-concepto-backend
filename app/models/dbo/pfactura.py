# Generado automáticamente
# Tabla: dbo.pfactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Pfactura(Base):
    __tablename__ = "pfactura"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    cancelada = Column(Boolean, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    numedocu = Column(String(9), nullable=False)
    pedido = Column(String(10), nullable=False)
    comentario = Column(String(80), nullable=False)
    expcomen = Column(String(80), nullable=False)
    notas = Column(String(200), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechacanc = Column(DateTime)
    clientes = Column(String(25), nullable=False)
    bodega = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    transpte = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    tipovta = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    tipomov = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    factoriva = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    factura = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    fechafact = Column(DateTime)
    fexenta = Column(Numeric(16, 6), nullable=False)
    fafecta = Column(Numeric(16, 6), nullable=False)
    fviva = Column(Numeric(16, 6), nullable=False)
    fmontfact = Column(Numeric(16, 6), nullable=False)
    fpdesc = Column(Numeric(16, 6), nullable=False)
    fvdesc = Column(Numeric(16, 6), nullable=False)
    pfactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    fnumedocu = Column(String(9), nullable=False)
    validez = Column(String(55), nullable=False)
    tdeliver = Column(String(55), nullable=False)
    notas1 = Column(String(250), nullable=False)
    notas2 = Column(String(250), nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    caja = Column(Integer, nullable=False)
    basesiniva = Column(Integer, nullable=False)
    SINIVA = Column(Integer, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    clientes2 = Column(String(25), nullable=False)
    fecha1 = Column(DateTime, nullable=False)
    fecha2 = Column(DateTime, nullable=False)
    pais = Column(Integer, nullable=False)
    archivada = Column(Boolean, nullable=False)
    Faltandatos = Column(Boolean, nullable=False)
    AprobadoAutoriza = Column(Integer, nullable=False)
    conNotas = Column(Boolean, nullable=False)
    sinExistencias = Column(Boolean, nullable=False)
    Facturado = Column(Boolean, nullable=False)
    FacturaParcial = Column(Boolean, nullable=False)
    Modificado = Column(Boolean, nullable=False)
    ModifAutoriza = Column(Integer, nullable=False)
    conDescuento = Column(Boolean, nullable=False)
    descAutoriza = Column(Integer, nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="pfactura_set")  # Comentado automáticamente
    # tipomov_rel = relationship("Tipomov", back_populates="pfactura_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Pfactura(pfactura={self.pfactura})>"