# Generado automáticamente
# Tabla: dbo.controlcarga
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Controlcarga(Base):
    __tablename__ = "controlcarga"
    __table_args__ = {"schema": "dbo"}

    Numedocu = Column(String(15), nullable=False)
    clientes = Column(String(25), nullable=False)
    vendedor = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    tipovta = Column(Integer, nullable=False)
    tipomov = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    enfirme = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    notas = Column(String(120), nullable=False)
    fecha = Column(DateTime, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    controlcarga = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    moneda = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    siniva = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Controlcarga(controlcarga={self.controlcarga})>"