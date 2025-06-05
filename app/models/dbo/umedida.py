# Generado automáticamente
# Tabla: dbo.umedida
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class UMedida(Base):
    __tablename__ = "umedida"
    __table_args__ = {"schema": "dbo"}

    numedida = Column(String(40), nullable=False)
    simumedida = Column(String(4), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    umedida = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    i = Column(Integer, nullable=False)
    unidad = Column(Boolean, nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    factorut = Column(Numeric(18, 6), nullable=False)
    ancho = Column(Numeric(18, 6), nullable=False)
    largo = Column(Numeric(18, 6), nullable=False)
    alto = Column(Numeric(18, 6), nullable=False)
    factorm3 = Column(Numeric(18, 6), nullable=False)
    peso = Column(Numeric(18, 6), nullable=False)
    peso2 = Column(Numeric(18, 6), nullable=False)
    esfactor = Column(Boolean, nullable=False)
    ubase = Column(Integer, nullable=False)
    fbase = Column(Numeric(12, 2), nullable=False)

    def __repr__(self):
        return "<Umedida(umedida={self.umedida})>"