# Generado automáticamente
# Tabla: dbo.lpartida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Lpartida(Base):
    __tablename__ = "lpartida"
    __table_args__ = {"schema": "dbo"}

    concepto = Column(String(75), nullable=False)
    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    automatico = Column(Boolean, nullable=False)
    numedocu = Column(String(9), nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipopart = Column(Integer, nullable=False)
    partida = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    debemont = Column(Numeric(16, 6), nullable=False)
    habermont = Column(Numeric(16, 6), nullable=False)
    fpartida = Column(Integer, nullable=False)
    lpartida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Lpartida(lpartida={self.lpartida})>"