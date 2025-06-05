# Generado automáticamente
# Tabla: dbo.tiposan
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tiposan(Base):
    __tablename__ = "tiposan"
    __table_args__ = {"schema": "dbo"}

    ntiposan = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    tiposan = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Tiposan(tiposan={self.tiposan})>"