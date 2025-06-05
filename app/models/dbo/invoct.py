# Generado automáticamente
# Tabla: dbo.invoct
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Invoct(Base):
    __tablename__ = "invoct"
    __table_args__ = {"schema": "dbo"}

    mes = Column(DateTime)
    kardex = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    cuarentena = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    costoprom = Column(Numeric(18, 6), nullable=False)
    invkardex = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    invini = Column(Numeric(16, 6), nullable=False)
    qinvini = Column(Numeric(16, 6), nullable=False)
    compra = Column(Numeric(16, 6), nullable=False)
    qcompra = Column(Numeric(16, 6), nullable=False)
    otrosing = Column(Numeric(16, 6), nullable=False)
    qotrosing = Column(Numeric(16, 6), nullable=False)
    INGRESO = Column(Numeric(16, 6), nullable=False)
    SALIDA = Column(Numeric(16, 6), nullable=False)
    BONIF = Column(Numeric(16, 6), nullable=False)
    DEVOL = Column(Numeric(16, 6), nullable=False)
    VENTA = Column(Numeric(16, 6), nullable=False)
    INVFIN = Column(Numeric(16, 6), nullable=False)
    QINGRESO = Column(Numeric(16, 6), nullable=False)
    QSALIDA = Column(Numeric(16, 6), nullable=False)
    QBONIF = Column(Numeric(16, 6), nullable=False)
    QDEVOL = Column(Numeric(16, 6), nullable=False)
    QVENTA = Column(Numeric(16, 6), nullable=False)
    QINVFIN = Column(Numeric(16, 6), nullable=False)
    final = Column(Numeric(18, 6), nullable=False)
    producto = Column(Integer,primary_key=True)

    def __repr__(self):
        return "<Invoct(mes={self.mes})>"