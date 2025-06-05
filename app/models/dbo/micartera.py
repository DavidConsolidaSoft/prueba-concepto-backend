# Generado automáticamente
# Tabla: dbo.miCartera
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Micartera(Base):
    __tablename__ = "miCartera"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    VENDEDOR = Column(String(50))
    CODIGOCLIENTE = Column(String(25))
    CLIENTE = Column(String(50))
    FECHA = Column(DateTime)
    DOCUMENTO = Column(String(9))
    monto = Column(Numeric(18, 6))
    saldonormal = Column(Numeric(18, 6))
    saldo30 = Column(Numeric(18, 6))
    saldo60 = Column(Numeric(18, 6))
    saldo90 = Column(Numeric(18, 6))
    saldo120 = Column(Numeric(18, 6))
    saldom120 = Column(Numeric(18, 6))
    saldo = Column(Numeric(18, 6))
    Telefono = Column(String(25))
    Municip = Column(String(50))
    Direccion = Column(String(200))
    LimiteCredito = Column(Numeric(18, 6))
    vencida = Column(Integer)

    def __repr__(self):
        return "<Micartera(VENDEDOR={self.VENDEDOR})>"