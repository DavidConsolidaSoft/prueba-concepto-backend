# Generado automáticamente
# Tabla: dbo.consigna
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Consigna(Base):
    __tablename__ = "consigna"
    __table_args__ = {"schema": "dbo"}

    compra = Column(Integer, nullable=False)
    almacen = Column(Integer, nullable=False)
    consigna = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Consigna(consigna={self.consigna})>"