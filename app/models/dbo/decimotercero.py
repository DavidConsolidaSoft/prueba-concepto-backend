# Generado automáticamente
# Tabla: dbo.decimotercero
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Decimotercero(Base):
    __tablename__ = "decimotercero"
    __table_args__ = {"schema": "dbo"}

    tipopla = Column(Integer, nullable=False)
    empleado = Column(Integer, nullable=False)
    finicio = Column(DateTime, nullable=False)
    ffin = Column(DateTime, nullable=False)
    sueldo = Column(Numeric(18, 6), nullable=False)
    spromedio = Column(Numeric(18, 6), nullable=False)
    comision = Column(Numeric(18, 6), nullable=False)
    cpromedio = Column(Numeric(18, 6), nullable=False)
    pagos = Column(Integer, nullable=False)
    fcontrato = Column(DateTime, nullable=False)
    fmaxima = Column(DateTime, nullable=False)
    dias = Column(Integer, nullable=False)
    facotr = Column(Numeric(18, 6), nullable=False)
    valor = Column(Numeric(18, 6), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    decimotercero = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Decimotercero(decimotercero={self.decimotercero})>"