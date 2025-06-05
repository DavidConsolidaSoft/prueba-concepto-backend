# Generado automáticamente
# Tabla: dbo.periodoactivo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Periodoactivo(Base):
    __tablename__ = "periodoactivo"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    periodoactivo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Periodoactivo(periodoactivo={self.periodoactivo})>"