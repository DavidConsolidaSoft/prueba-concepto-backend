# Generado automáticamente
# Tabla: dbo.pagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Pagos(Base):
    __tablename__ = "pagos"
    __table_args__ = {"schema": "dbo"}

    tipomov = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
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
    pagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
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
    caja = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    tipopago = Column(Integer, nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    rutacobro = Column(Integer, nullable=False)
    ENFIRME = Column(Boolean, nullable=False)
    docunico = Column(String(9), nullable=False)
    bodega = Column(Integer, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    autopago = Column(Boolean, nullable=False)
    factura = Column(Integer, nullable=False)
    referenciapagos = Column(Integer, nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="pagos_set")  # Comentado automáticamente
    # tipomov_rel = relationship("Tipomov", back_populates="pagos_set")  # Comentado automáticamente
    # vendedor_rel = relationship("Vendedor", back_populates="pagos_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Pagos(pagos={self.pagos})>"