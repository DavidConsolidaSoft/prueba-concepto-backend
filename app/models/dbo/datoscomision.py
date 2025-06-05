# Generado automáticamente
# Tabla: dbo.datosComision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Datoscomision(Base):
    __tablename__ = "datosComision"
    __table_args__ = {"schema": "dbo"}

    datoscomision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    codigo = Column(Integer, nullable=False)
    casaprod = Column(Integer, nullable=False)
    comision = Column(Numeric(18, 6), nullable=False)
    factorcomision = Column(Numeric(18, 6), nullable=False)
    porcnologro = Column(Numeric(18, 6), nullable=False)
    AntiguedadCobro = Column(Numeric(18, 6), nullable=False)
    FactorLogro = Column(Numeric(18, 6), nullable=False)
    Logrocuota = Column(Numeric(18, 6), nullable=False)
    MontoVendido = Column(Numeric(18, 6), nullable=False)
    cuotaVendedor = Column(Numeric(18, 6), nullable=False)
    MontoCobrado = Column(Numeric(18, 6), nullable=False)
    ComisionFija = Column(Boolean, nullable=False)
    periodocomision = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Datoscomision(datoscomision={self.datoscomision})>"