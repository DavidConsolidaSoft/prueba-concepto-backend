# Generado automáticamente
# Tabla: dbo.OcultaBodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Ocultabodega(Base):
    __tablename__ = "OcultaBodega"
    __table_args__ = {"schema": "dbo"}

    OcultaBodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    bodega = Column(Integer, nullable=False)
    caja = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ocultabodega(OcultaBodega={self.OcultaBodega})>"