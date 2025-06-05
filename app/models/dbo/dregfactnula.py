# Generado automáticamente
# Tabla: dbo.dregfactnula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Dregfactnula(Base):
    __tablename__ = "dregfactnula"
    __table_args__ = {"schema": "dbo"}

    dregfactnula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    dregciclo = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dregfactnula(dregfactnula={self.dregfactnula})>"