# Generado automáticamente
# Tabla: dbo.proveedor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Proveedor(Base):
    __tablename__ = "proveedor"
    __table_args__ = {"schema": "dbo"}

    nproveedor = Column(String(50), nullable=False)
    municip = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    tipoprov = Column(Integer, nullable=False)
    contado = Column(Boolean, nullable=False)
    exento = Column(Boolean, nullable=False)
    nit = Column(String(21))
    registro = Column(String(15), nullable=False)
    giro = Column(String(50), nullable=False)
    contacto = Column(String(50), nullable=False)
    razonsoc = Column(String(50), nullable=False)
    sitioweb = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    notas = Column(String(50), nullable=False)
    direccion = Column(String(200), nullable=False)
    descuento = Column(Integer, nullable=False)
    promcomp = Column(Numeric(16, 6), nullable=False)
    prompago = Column(Numeric(16, 6), nullable=False)
    fechalim = Column(DateTime)
    recomendado = Column(String(120), nullable=False)
    activo = Column(Boolean, nullable=False)
    telefono1 = Column(String(15))
    telefono2 = Column(String(15), nullable=False)
    fax = Column(String(15))
    limitecredito = Column(Numeric(16, 6), nullable=False)
    hora = Column(DateTime)
    proveedor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    retencion = Column(Boolean, nullable=False)
    ivacero = Column(Boolean)
    percepcion = Column(Boolean, nullable=False)
    cuenta = Column(Integer, nullable=False)
    comisionmedios = Column(Numeric(18, 6), nullable=False)
    pais = Column(Integer, nullable=False)
    otroDocumento = Column(String(20), nullable=False)
    otroDoc = Column(String(15), nullable=False)
    diasEntrega = Column(Integer, nullable=False)
    infopago = Column(String(300), nullable=False)
    puertoEmbarque = Column(String(35), nullable=False)
    cuenta1 = Column(Integer)
    diasDespacho = Column(Integer, nullable=False)
    tipo = Column(Integer, nullable=False)
    clasificacion = Column(Integer, nullable=False)
    sector = Column(Integer, nullable=False)
    costo = Column(Integer, nullable=False)

    # Relaciones
    # municip_rel = relationship("Municip", back_populates="proveedor_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Proveedor(proveedor={self.proveedor})>"