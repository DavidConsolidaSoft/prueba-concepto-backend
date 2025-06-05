# Generado automáticamente
# Tabla: dbo.comisiontienda
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Comisiontienda(Base):
    __tablename__ = "comisiontienda"
    __table_args__ = {"schema": "dbo"}

    comisiontienda = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tienda = Column(Integer, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    valores = Column(Numeric(16, 6), nullable=False)
    vcomision = Column(Numeric(16, 6), nullable=False)
    rangospagados = Column(Integer, nullable=False)
    anio = Column(Integer)
    empresa = Column(Integer)
    mes = Column(Integer)
    comision = Column(Numeric(14, 2))
    fecha = Column(DateTime)

    def __repr__(self):
        return "<Comisiontienda(comisiontienda={self.comisiontienda})>"