# Generado automáticamente
# Tabla: dbo.RupTipoProceso
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ruptipoproceso(Base):
    __tablename__ = "RupTipoProceso"
    __table_args__ = {"schema": "dbo"}

    nRupTipoProceso = Column(String(25), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupTipoProceso = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nivel = Column(String(6))
    rupactividad = Column(Integer)
    rupot = Column(Integer)
    cantidad = Column(Numeric(9, 2))
    insumo = Column(String(50))
    producto = Column(String(50))

    def __repr__(self):
        return "<Ruptipoproceso(RupTipoProceso={self.RupTipoProceso})>"