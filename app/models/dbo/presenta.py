# Generado automáticamente
# Tabla: dbo.presenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Presenta(Base):
    __tablename__ = "presenta"
    __table_args__ = {"schema": "dbo"}

    npresenta = Column(String(40), nullable=False)
    preferido = Column(Boolean, nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    umedida = Column(Integer, nullable=False)
    presenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Presenta(presenta={self.presenta})>"