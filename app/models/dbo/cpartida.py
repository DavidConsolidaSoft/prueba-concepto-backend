# Generado automáticamente
# Tabla: dbo.cpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Cpartida(Base):
    __tablename__ = "cpartida"
    __table_args__ = {"schema": "dbo"}

    nopartida = Column(String(9))
    nocheque = Column(String(15))
    nofacturas = Column(String(250))
    noquedan = Column(String(15))
    concepto = Column(String(75))
    referencia = Column(String(15))
    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    quedan = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    cheqimp = Column(Boolean, nullable=False)
    conciliado = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
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
    debe = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    cpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partida = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    CDEBE = Column(Numeric(18, 6), nullable=False)
    CHABER = Column(Numeric(18, 6), nullable=False)
    IMPRIMECHEQUE = Column(Boolean, nullable=False)
    CMONTO = Column(Numeric(18, 6), nullable=False)
    TASACAMBIOTRES = Column(Numeric(18, 6), nullable=False)
    pagado = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Cpartida(cpartida={self.cpartida})>"