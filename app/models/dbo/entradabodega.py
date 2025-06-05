# Generado automáticamente
# Tabla: dbo.entradabodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Entradabodega(Base):
    __tablename__ = "entradabodega"
    __table_args__ = {"schema": "dbo"}

    entradabodega = Column(Integer, primary_key=True, nullable=False)
    numedocu = Column(String(9), nullable=False)
    rf = Column(DateTime)
    n = Column(String(50), nullable=False)
    rnum = Column(String(9), nullable=False)
    icdbarra = Column(String(25), nullable=False)
    npre = Column(String(40), nullable=False)
    rc = Column(Numeric(15, 6), nullable=False)
    np = Column(String(50), nullable=False)
    rp = Column(Numeric(15, 6), nullable=False)
    rt = Column(Numeric(19, 4), nullable=False)
    notas = Column(String(80), nullable=False)

    def __repr__(self):
        return "<Entradabodega(entradabodega={self.entradabodega})>"