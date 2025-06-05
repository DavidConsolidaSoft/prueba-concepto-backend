# Generado automáticamente
# Tabla: dbo.cargosocomp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Cargosocomp(Base):
    __tablename__ = "cargosocomp"
    __table_args__ = {"schema": "dbo"}

    ocompra = Column(Integer, nullable=False)
    cargoscomp = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    monto = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    cargosocomp = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)

    def __repr__(self):
        return "<Cargosocomp(cargosocomp={self.cargosocomp})>"