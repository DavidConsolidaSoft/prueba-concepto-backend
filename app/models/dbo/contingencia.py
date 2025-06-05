# Generado automáticamente
# Tabla: dbo.contingencia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Contingencia(Base):
    __tablename__ = "contingencia"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer)
    uuid = Column(String(45),primary_key=True)
    serie = Column(String(15))
    numero = Column(String(15))
    empresa = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Contingencia(factura={self.factura})>"