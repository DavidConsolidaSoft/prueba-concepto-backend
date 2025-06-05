# Generado automáticamente
# Tabla: dbo.dpreciovineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dpreciovineta(Base):
    __tablename__ = "dpreciovineta"
    __table_args__ = {"schema": "dbo"}

    producto = Column(Integer, nullable=False)
    codigo = Column(String(12), nullable=False)
    precio1 = Column(Numeric(18, 6), nullable=False)
    precio2 = Column(Numeric(18, 6), nullable=False)
    precio3 = Column(Numeric(18, 6), nullable=False)
    preciovineta = Column(Integer, nullable=False)
    dpreciovineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    precio4 = Column(Numeric(18, 6), nullable=False)
    precio5 = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Dpreciovineta(dpreciovineta={self.dpreciovineta})>"