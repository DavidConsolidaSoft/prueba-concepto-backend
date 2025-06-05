# Generado automáticamente
# Tabla: dbo.banco
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Banco(Base):
    __tablename__ = "banco"
    __table_args__ = {"schema": "dbo"}

    nbanco = Column(String(55), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    banco = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    simbanco = Column(String(4), nullable=False)
    condpago = Column(Integer, nullable=False)
    TARJETA = Column(Boolean, nullable=False)
    sqlPLANILLA = Column(String(250), nullable=False)
    largocuenta = Column(Integer, nullable=False)
    campo1 = Column(Integer, nullable=False)
    campo2 = Column(Integer, nullable=False)
    campo3 = Column(Integer, nullable=False)
    campo4 = Column(Integer, nullable=False)
    campo5 = Column(Integer, nullable=False)
    campo6 = Column(Integer, nullable=False)
    campo7 = Column(Integer, nullable=False)
    gastoAdmon = Column(Boolean, nullable=False)
    gastoFinan = Column(Boolean, nullable=False)
    gastoVenta = Column(Boolean, nullable=False)
    esbanco = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Banco(banco={self.banco})>"