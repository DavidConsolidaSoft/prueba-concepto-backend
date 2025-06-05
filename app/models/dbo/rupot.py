# Generado automáticamente
# Tabla: dbo.RupOT
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rupot(Base):
    __tablename__ = "RupOT"
    __table_args__ = {"schema": "dbo"}

    RupSolicitud = Column(Integer, nullable=False)
    RupOTResponsable = Column(Integer, nullable=False)
    nRupOT = Column(String(35))
    ParaCuandoOT = Column(DateTime)
    Activo = Column(Boolean, nullable=False)
    RupOT = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    producto = Column(Integer)
    almacen = Column(Integer)
    cantidad = Column(Numeric(9, 2))
    fentrega = Column(DateTime)
    rupactividad = Column(Integer)

    def __repr__(self):
        return "<Rupot(RupOT={self.RupOT})>"