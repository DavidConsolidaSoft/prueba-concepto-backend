# Generado automáticamente
# Tabla: dbo.comprafirme
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Comprafirme(Base):
    __tablename__ = "comprafirme"
    __table_args__ = {"schema": "dbo"}

    comprafirme = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    numedocu = Column(String(15))
    fecha = Column(DateTime)
    fechaOut = Column(DateTime)
    fechain = Column(DateTime)
    impresa = Column(Boolean)
    nula = Column(Boolean)
    notas = Column(String(250))
    notasPago = Column(String(350))
    flete = Column(Numeric(9, 2))
    seguro = Column(Numeric(9, 2))
    montgasto = Column(Numeric(9, 2))
    cartacredito = Column(String(15))
    poliza = Column(String(15))
    encompra = Column(Integer)
    embarque = Column(Integer)
    cembarque = Column(Integer)
    loadingcontainer = Column(String(120))
    billloading = Column(String(35))
    containerno = Column(String(35))
    marchamo = Column(String(35))
    loadingPort = Column(String(35))
    DischargePort = Column(String(35))
    DeliveryPort = Column(String(35))
    hechoen = Column(String(25))
    deliveryterms = Column(String(80))
    ctracking = Column(Integer)
    recinto = Column(Boolean)
    fecharecinto = Column(DateTime)
    metros3 = Column(Numeric(9, 2))
    metros3p = Column(Numeric(9, 2))
    impuesto = Column(Numeric(9, 2))
    impuestop = Column(Numeric(9, 2))
    arancel = Column(Numeric(9, 2))
    arancelp = Column(Numeric(9, 2))
    cif = Column(Numeric(9, 2))
    montoiva = Column(Numeric(9, 2))
    ndeposito = Column(Integer)
    recintofiscal = Column(Integer)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    horatiempo = Column(DateTime)
    Tipomov = Column(Integer)
    Gastos = Column(Numeric(9, 2))

    def __repr__(self):
        return "<Comprafirme(comprafirme={self.comprafirme})>"