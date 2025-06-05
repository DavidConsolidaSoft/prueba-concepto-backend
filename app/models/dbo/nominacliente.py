# Generado automáticamente
# Tabla: dbo.nominacliente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Nominacliente(Base):
    __tablename__ = "nominacliente"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    cliencatego = Column(Integer, nullable=False)
    nominacliente = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    invcliente = Column(Integer, nullable=False)
    consumo = Column(Numeric(18, 6), nullable=False)
    cuotas = Column(Numeric(18, 6), nullable=False)
    pago = Column(Numeric(18, 6), nullable=False)
    liquidado = Column(Boolean, nullable=False)
    presentada = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    fechapago = Column(DateTime)
    clientes = Column(String(25))
    nopago = Column(String(9), nullable=False)
    nofactura = Column(String(9), nullable=False)
    pagos = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Nominacliente(fecha={self.fecha})>"