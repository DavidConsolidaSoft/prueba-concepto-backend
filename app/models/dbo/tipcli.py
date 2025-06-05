# Generado automáticamente
# Tabla: dbo.tipcli
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class TipCli(Base):
    __tablename__ = "tipcli"
    __table_args__ = {"schema": "dbo"}

    ntipcli = Column(String(200), nullable=False)
    activo = Column(Boolean, nullable=False)
    tipcli = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    clave = Column(String(20), nullable=False)
    cliencatego = Column(Integer)
    agrupar = Column(Boolean, nullable=False)
    agencia = Column(Boolean, nullable=False)
    gobierno = Column(Boolean, nullable=False)
    pdesc = Column(Integer, nullable=False)
    desc1 = Column(Integer, nullable=False)
    desc2 = Column(Integer, nullable=False)
    desc3 = Column(Integer, nullable=False)
    desc4 = Column(Integer, nullable=False)
    desc5 = Column(Integer, nullable=False)
    tipomiembro = Column(Integer, nullable=False)
    aplicadescuento = Column(Boolean, nullable=False)
    tipopago = Column(Integer, nullable=False)
    d1 = Column(Boolean, nullable=False)
    d2 = Column(Boolean, nullable=False)
    d3 = Column(Boolean, nullable=False)
    d4 = Column(Boolean, nullable=False)
    d5 = Column(Boolean, nullable=False)
    d6 = Column(Boolean, nullable=False)
    d7 = Column(Boolean, nullable=False)
    tproddesc = Column(Integer, nullable=False)
    restricciones = Column(Integer, nullable=False)
    miembrofamiliar = Column(Boolean, nullable=False)
    titularcuenta = Column(Boolean, nullable=False)
    miembrohonorario = Column(Boolean, nullable=False)
    agregadomilitar = Column(Boolean, nullable=False)
    cortesia = Column(Boolean, nullable=False)
    visitante = Column(Boolean, nullable=False)
    empleado = Column(Boolean, nullable=False)
    efectivo = Column(Numeric(18, 6), nullable=False)
    tarjeta = Column(Numeric(18, 6), nullable=False)
    credito = Column(Numeric(18, 6), nullable=False)
    mesa = Column(Boolean, nullable=False)
    esmilitar = Column(Boolean, nullable=False)
    pdesc1 = Column(Numeric(5, 2), nullable=False)
    pdesc2 = Column(Numeric(5, 2), nullable=False)
    pdesc3 = Column(Numeric(5, 2), nullable=False)
    pdesc4 = Column(Numeric(5, 2), nullable=False)
    pdesc5 = Column(Numeric(5, 2), nullable=False)
    aPlicadesc = Column(Boolean, nullable=False)
    cuota = Column(Float, nullable=False)
    siPariente = Column(Boolean, nullable=False)
    siPluma = Column(Boolean, nullable=False)
    tienecredito = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Tipcli(tipcli={self.tipcli})>"