# Generado automáticamente
# Tabla: dbo.dcpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dcpartida(Base):
    __tablename__ = "dcpartida"
    __table_args__ = {"schema": "dbo"}

    orden = Column(String(1), nullable=False)
    banco = Column(Boolean, nullable=False)
    cheque = Column(Boolean, nullable=False)
    cheqnulo = Column(Boolean, nullable=False)
    aquien = Column(Boolean, nullable=False)
    cheqimp = Column(Boolean, nullable=False)
    concepto = Column(String(254), nullable=False)
    debe = Column(Numeric(16, 6), nullable=False)
    haber = Column(Numeric(16, 6), nullable=False)
    hdebe = Column(Numeric(16, 6), nullable=False)
    hhaber = Column(Numeric(16, 6), nullable=False)
    pdebe = Column(Numeric(16, 6), nullable=False)
    phaber = Column(Numeric(16, 6), nullable=False)
    hphaber = Column(Numeric(16, 6), nullable=False)
    hpdebe = Column(Numeric(16, 6), nullable=False)
    partida = Column(Integer, nullable=False)
    Cpartida = Column(Integer, nullable=False)
    Dpartida = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    dcpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    hconcepto = Column(String(254))
    Automatico = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Dcpartida(dcpartida={self.dcpartida})>"