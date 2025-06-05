# Generado automáticamente
# Tabla: dbo.ccontrato
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ccontrato(Base):
    __tablename__ = "ccontrato"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    fecha = Column(DateTime, nullable=False)
    nula = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    vendedor = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    numedocu = Column(String(9), nullable=False)
    cancelada = Column(Boolean, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    pprima = Column(Numeric(18, 6), nullable=False)
    letras = Column(Integer, nullable=False)
    factorinteres = Column(Numeric(18, 6), nullable=False)
    abono = Column(Numeric(18, 6), nullable=False)
    cargo = Column(Numeric(18, 6), nullable=False)
    ccontrato = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    fechainicial = Column(DateTime, nullable=False)
    montocredito = Column(Numeric(18, 6), nullable=False)
    diaPago = Column(Integer, nullable=False)
    cuota = Column(Numeric(18, 6), nullable=False)
    tipomov = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ccontrato(clientes={self.clientes})>"