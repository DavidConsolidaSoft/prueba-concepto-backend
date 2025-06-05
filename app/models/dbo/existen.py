# Generado automáticamente
# Tabla: dbo.existen
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Existen(Base):
    __tablename__ = "existen"
    __table_args__ = {"schema": "dbo"}

    icdbarra = Column(String(25), nullable=False)
    nproducto = Column(String(50), nullable=False)
    cantidad = Column(Numeric(15, 6), nullable=False)
    ncategori = Column(String(40), nullable=False)
    ntipoprod = Column(String(40), nullable=False)
    tipoprod = Column(Integer,primary_key=True, nullable=False)

    def __repr__(self):
        return "<Existen(icdbarra={self.icdbarra})>"