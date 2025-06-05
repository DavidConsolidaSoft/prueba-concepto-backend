# Generado automáticamente
# Tabla: dbo.RazonFinan
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Razonfinan(Base):
    __tablename__ = "RazonFinan"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nRazonFinan = Column(String(100), nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    RazonFinan = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    proyectado = Column(Numeric(18, 6), nullable=False)
    grupo = Column(String(50), nullable=False)
    orden = Column(Integer, nullable=False)
    fecha = Column(DateTime)
    tipo = Column(String(9))

    def __repr__(self):
        return "<Razonfinan(RazonFinan={self.RazonFinan})>"