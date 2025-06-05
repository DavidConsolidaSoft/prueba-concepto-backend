# Generado automáticamente
# Tabla: dbo.UnidadVenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Unidadventa(Base):
    __tablename__ = "UnidadVenta"
    __table_args__ = {"schema": "dbo"}

    UnidadBase = Column(Integer, nullable=False)
    UVenta = Column(Integer, nullable=False)
    Factor = Column(Numeric(16, 6), nullable=False)
    Activo = Column(Boolean, nullable=False)
    UnidadVenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Unidadventa(UnidadVenta={self.UnidadVenta})>"