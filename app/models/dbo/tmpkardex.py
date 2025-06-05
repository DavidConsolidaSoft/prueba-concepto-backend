# Generado automáticamente
# Tabla: dbo.tmpkardex
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Tmpkardex(Base):
    __tablename__ = "tmpkardex"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    qinvfin = Column(Numeric(18, 6), nullable=False)
    invfin = Column(Numeric(18, 6), nullable=False)
    costoprom = Column(Numeric(18, 6), nullable=False)
    qcompra = Column(Numeric(18, 6), nullable=False)
    qotrosing = Column(Numeric(18, 6), nullable=False)
    qingreso = Column(Numeric(18, 6), nullable=False)
    qsalida = Column(Numeric(18, 6), nullable=False)
    qventa = Column(Numeric(18, 6), nullable=False)
    qdevol = Column(Numeric(18, 6), nullable=False)
    qbonif = Column(Numeric(18, 6), nullable=False)
    compra = Column(Numeric(18, 6), nullable=False)
    otrosing = Column(Numeric(18, 6), nullable=False)
    ingreso = Column(Numeric(18, 6), nullable=False)
    salida = Column(Numeric(18, 6), nullable=False)
    venta = Column(Numeric(18, 6), nullable=False)
    devol = Column(Numeric(18, 6), nullable=False)
    bonif = Column(Numeric(18, 6), nullable=False)
    invini = Column(Numeric(18, 6), nullable=False)
    qinvini = Column(Numeric(18, 6), nullable=False)
    PRODUCTO = Column(Integer, nullable=False)
    mes = Column(DateTime)
    KARDEX = Column(Integer)

    def __repr__(self):
        return "<Tmpkardex(qinvfin={self.qinvfin})>"