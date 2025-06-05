# Generado automáticamente
# Tabla: dbo.tipoprov
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipoprov(Base):
    __tablename__ = "tipoprov"
    __table_args__ = {"schema": "dbo"}

    ntipoprov = Column(String(40), nullable=False)
    activo = Column(Boolean, nullable=False)
    tipoprov = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    preferido = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Tipoprov(tipoprov={self.tipoprov})>"