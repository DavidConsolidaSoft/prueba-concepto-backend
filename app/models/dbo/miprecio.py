# Generado automáticamente
# Tabla: dbo.miprecio
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Miprecio(Base):
    __tablename__ = "miprecio"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    dprodprec = Column(Integer)
    producto = Column(Integer)
    prodprec = Column(Integer)
    tprecio = Column(Numeric(18, 6))
    fprecio = Column(Numeric(18, 6))

    def __repr__(self):
        return "<Miprecio(dprodprec={self.dprodprec})>"