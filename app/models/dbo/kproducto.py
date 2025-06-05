# Generado automáticamente
# Tabla: dbo.kproducto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer
from sqlalchemy import Column, SmallInteger
from sqlalchemy import Column, String


class Kproducto(Base):
    __tablename__ = "kproducto"
    __table_args__ = {"schema": "dbo"}

    tprecio = Column(Float, nullable=False)
    fprecio = Column(Float, nullable=False)
    precio = Column(SmallInteger, nullable=False)
    nprodprec = Column(String(100), nullable=False)
    codigo = Column(String(50), nullable=False)
    nproducto = Column(String(150), nullable=False)
    prodprec = Column(Integer)
    producto = Column(Integer,primary_key=True)

    def __repr__(self):
        return "<Kproducto(tprecio={self.tprecio})>"