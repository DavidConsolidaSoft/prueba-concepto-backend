# Generado automáticamente
# Tabla: dbo.partida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Partida(Base):
    __tablename__ = "partida"
    __table_args__ = {"schema": "dbo"}

    nopartida = Column(String(9), nullable=False)
    nocheque = Column(String(15), nullable=False)
    nofacturas = Column(String(250), nullable=False)
    noquedan = Column(String(15), nullable=False)
    concepto = Column(String(250))
    referencia = Column(String(15), nullable=False)
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
    partida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
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
    OPERADORTRES = Column(String(1), nullable=False)
    OPERADOR = Column(String(1), nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    sucursal = Column(Integer, nullable=False)
    notaremision = Column(String(9), nullable=False)
    impremision = Column(Boolean, nullable=False)
    cerrada = Column(Boolean, nullable=False)
    cprovision = Column(String(250), nullable=False)
    ProvisionImpresa = Column(Boolean, nullable=False)
    cargo = Column(Numeric(18, 6), nullable=False)
    liquidadora = Column(Boolean, nullable=False)
    cajachica = Column(Boolean, nullable=False)
    mifecha = Column(DateTime)

    # Relaciones
    # periodo_rel = relationship("Periodo", back_populates="partida_set")  # Comentado automáticamente
    # tipopart_rel = relationship("Tipopart", back_populates="partida_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Partida(partida={self.partida})>"