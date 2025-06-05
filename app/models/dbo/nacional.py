# Generado automáticamente
# Tabla: dbo.nacional
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Nacional(Base):
    __tablename__ = "nacional"
    __table_args__ = {"schema": "dbo"}

    nnacional = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    nacional = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    codigoPais = Column(String(5))

    def __repr__(self):
        return "<Nacional(nacional={self.nacional})>"