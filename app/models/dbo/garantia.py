# Generado automáticamente
# Tabla: dbo.garantia
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Garantia(Base):
    __tablename__ = "garantia"
    __table_args__ = {"schema": "dbo"}

    ngarantia = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    vencimiento = Column(Integer, nullable=False)
    meses = Column(Boolean, nullable=False)
    garantia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Garantia(garantia={self.garantia})>"