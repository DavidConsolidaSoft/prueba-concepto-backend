# Generado automáticamente
# Tabla: dbo.ppagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ppagos(Base):
    __tablename__ = "ppagos"
    __table_args__ = {"schema": "dbo"}

    tipomov = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    encompra = Column(Integer, nullable=False)
    proveedor = Column(Integer, nullable=False)
    referencia = Column(String(15), nullable=False)
    notas = Column(String(120), nullable=False)
    fecha = Column(DateTime, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    difcambio = Column(Numeric(16, 6), nullable=False)
    mora = Column(Numeric(16, 6), nullable=False)
    ppagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    numedocu = Column(String(10), nullable=False)
    cargo = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    iva = Column(Integer, nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    condpago = Column(Integer, nullable=False)
    fovial = Column(Numeric(18, 6), nullable=False)
    importacion = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    tipobodega = Column(Integer, nullable=False)

    # Relaciones
    # tipomov_rel = relationship("Tipomov", back_populates="ppagos_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ppagos(ppagos={self.ppagos})>"