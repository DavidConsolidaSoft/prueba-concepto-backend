# Generado automáticamente
# Tabla: dbo.dcontrolcarga
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dcontrolcarga(Base):
    __tablename__ = "dcontrolcarga"
    __table_args__ = {"schema": "dbo"}

    BLNumero = Column(String(15), nullable=False)
    camion = Column(Integer, nullable=False)
    tipoviaje = Column(Integer, nullable=False)
    motorista = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    munipickat = Column(Integer, nullable=False)
    munientrega = Column(Integer, nullable=False)
    notas = Column(String(120), nullable=False)
    fechaentrega = Column(DateTime)
    fechasalida = Column(DateTime)
    fechallegada = Column(DateTime)
    impresa = Column(Boolean, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    afecta = Column(Numeric(18, 6), nullable=False)
    exenta = Column(Numeric(18, 6), nullable=False)
    viva = Column(Numeric(18, 6), nullable=False)
    addcharge = Column(Numeric(18, 6), nullable=False)
    controlcarga = Column(Integer, nullable=False)
    dcontrolcarga = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Dcontrolcarga(dcontrolcarga={self.dcontrolcarga})>"