# Generado automáticamente
# Tabla: dbo.estilo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Estilo(Base):
    __tablename__ = "estilo"
    __table_args__ = {"schema": "dbo"}

    nestilo = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    estilo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Estilo(estilo={self.estilo})>"