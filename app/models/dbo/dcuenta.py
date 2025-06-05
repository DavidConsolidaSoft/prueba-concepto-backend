# Generado automáticamente
# Tabla: dbo.dcuenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dcuenta(Base):
    __tablename__ = "dcuenta"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    debe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    adebe = Column(Numeric(16, 6), nullable=False)
    ahaber = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    apdebe = Column(Numeric(16, 6), nullable=False)
    aphaber = Column(Numeric(16, 6), nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    periodo = Column(Integer, nullable=False)
    dcuenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fecha = Column(DateTime, nullable=False)
    tienemov = Column(Boolean, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Dcuenta(dcuenta={self.dcuenta})>"