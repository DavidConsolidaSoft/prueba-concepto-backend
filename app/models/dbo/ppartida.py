# Generado automáticamente
# Tabla: dbo.ppartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ppartida(Base):
    __tablename__ = "ppartida"
    __table_args__ = {"schema": "dbo"}

    nopartida = Column(String(9), nullable=False)
    nocheque = Column(String(15), nullable=False)
    nofacturas = Column(String(254), nullable=False)
    noquedan = Column(String(9), nullable=False)
    concepto = Column(String(100), nullable=False)
    referencia = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    quedan = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    cheqimp = Column(Boolean, nullable=False)
    conciliado = Column(Boolean, nullable=False)
    contabilid = Column(Boolean, nullable=False)
    automatico = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechapago = Column(DateTime)
    reffecha = Column(DateTime)
    tipopart = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    periodo = Column(Integer, nullable=False)
    ccuenta = Column(Integer, nullable=False)
    chpartida = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    debe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    ppartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    CDEBE = Column(Numeric(18, 6), nullable=False)
    CHABER = Column(Numeric(18, 6), nullable=False)
    CMONTO = Column(Numeric(18, 6), nullable=False)

    # Relaciones
    # periodo_rel = relationship("Periodo", back_populates="ppartida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ppartida(ppartida={self.ppartida})>"