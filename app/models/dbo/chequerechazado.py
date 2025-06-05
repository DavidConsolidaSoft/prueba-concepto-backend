# Generado automáticamente
# Tabla: dbo.chequeRechazado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Chequerechazado(Base):
    __tablename__ = "chequeRechazado"
    __table_args__ = {"schema": "dbo"}

    ChequeRechazado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nocheque = Column(String(15), nullable=False)
    vendedor = Column(Integer, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    chrechazado = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    fechaPago = Column(DateTime)
    Fecha = Column(DateTime, nullable=False)
    Fechacheque = Column(DateTime, nullable=False)
    FechaAnulacion = Column(DateTime)
    banco = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Chequerechazado(ChequeRechazado={self.ChequeRechazado})>"