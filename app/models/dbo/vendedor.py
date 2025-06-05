# Generado automáticamente
# Tabla: dbo.vendedor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Vendedor(Base):
    __tablename__ = "vendedor"
    __table_args__ = {"schema": "dbo"}

    nvendedor = Column(String(50), nullable=False)
    fecingreso = Column(DateTime)
    fecretiro = Column(DateTime)
    lvendedor = Column(Boolean, nullable=False)
    lcobrador = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    tipvende = Column(Integer, nullable=False)
    vendedor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    clientes = Column(String(25), nullable=False)
    bodega = Column(Integer, nullable=False)
    noCAJERO = Column(Boolean, nullable=False)
    prodprec = Column(Integer, nullable=False)
    fqmin = Column(Integer, nullable=False)
    fqmax = Column(Integer, nullable=False)
    cqmin = Column(Integer, nullable=False)
    cqmax = Column(Integer, nullable=False)
    fcorrel = Column(Integer, nullable=False)
    ccorrel = Column(Integer, nullable=False)
    tipomov = Column(Integer, nullable=False)
    pqmin = Column(Integer, nullable=False)
    pqmax = Column(Integer, nullable=False)
    pcorrel = Column(Integer, nullable=False)
    rqmin = Column(Integer, nullable=False)
    rqmax = Column(Integer, nullable=False)
    rcorrel = Column(Integer, nullable=False)
    controlcorrel = Column(Integer, nullable=False)
    zonavendedor = Column(Integer, nullable=False)
    fact1 = Column(Integer, nullable=False)
    fact2 = Column(Integer, nullable=False)
    ccf1 = Column(Integer, nullable=False)
    ccf2 = Column(Integer, nullable=False)
    FACT = Column(Integer, nullable=False)
    ccf = Column(Integer, nullable=False)
    Pagos1 = Column(Integer, nullable=False)
    Pagos2 = Column(Integer, nullable=False)
    Pagos = Column(Integer, nullable=False)
    recibo1 = Column(Integer, nullable=False)
    recibo2 = Column(Integer, nullable=False)
    recibo = Column(Integer, nullable=False)
    vcorreo = Column(String(100), nullable=False)
    cajero = Column(Boolean, nullable=False)
    cuota = Column(Numeric(18, 6), nullable=False)
    VENDEDOR1 = Column(Integer, nullable=False)
    Mesero = Column(Boolean, nullable=False)
    pedidomin = Column(Integer, nullable=False)
    pedidocorr = Column(Integer, nullable=False)
    pedidomax = Column(Integer, nullable=False)
    clave = Column(Integer, nullable=False)
    tipovendedor = Column(Integer, nullable=False)
    descrip = Column(String(35))
    idvend = Column(String(15))

    def __repr__(self):
        return "<Vendedor(vendedor={self.vendedor})>"