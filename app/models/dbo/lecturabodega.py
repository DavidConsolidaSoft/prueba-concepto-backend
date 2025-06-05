# Generado automáticamente
# Tabla: dbo.lecturabodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Lecturabodega(Base):
    __tablename__ = "lecturabodega"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    bodega = Column(Integer, nullable=False)
    Producto = Column(Integer, nullable=False)
    valor = Column(Numeric(18, 6), nullable=False)
    lecturavara = Column(Numeric(18, 6), nullable=False)
    galones = Column(Numeric(18, 6), nullable=False)
    LecturaBodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Lecturabodega(LecturaBodega={self.LecturaBodega})>"