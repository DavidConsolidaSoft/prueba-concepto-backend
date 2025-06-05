# Generado automáticamente
# Tabla: dbo.dte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dte(Base):
    __tablename__ = "dte"
    __table_args__ = {"schema": "dbo"}

    ncatalogo = Column(String(50), nullable=False)
    catalogo = Column(String(50), nullable=False)
    scatalogo = Column(String(50), nullable=False)
    descripcion = Column(String(200), nullable=False)
    dte = Column(Integer, primary_key=True, nullable=False)
    tabla = Column(String(60))
    zona = Column(String(20))
    depto = Column(Integer)
    municip = Column(Integer)

    def __repr__(self):
        return "<Dte(dte={self.dte})>"