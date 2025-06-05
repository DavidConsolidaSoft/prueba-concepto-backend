# Generado automáticamente
# Tabla: dbo.tocompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tocompra(Base):
    __tablename__ = "tocompra"
    __table_args__ = {"schema": "dbo"}

    ocompra = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tocompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    numedocu = Column(String(9), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tocompra(tocompra={self.tocompra})>"