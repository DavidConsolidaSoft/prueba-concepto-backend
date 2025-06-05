# Generado automáticamente
# Tabla: dbo.dcargaAnticipo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dcargaanticipo(Base):
    __tablename__ = "dcargaAnticipo"
    __table_args__ = {"schema": "dbo"}

    CargaAnticipo = Column(Integer, nullable=False)
    GastoAnticipo = Column(Integer, nullable=False)
    cargo = Column(Numeric(18, 6), nullable=False)
    dcargaAnticipo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fecha = Column(DateTime)

    def __repr__(self):
        return "<Dcargaanticipo(dcargaAnticipo={self.dcargaAnticipo})>"