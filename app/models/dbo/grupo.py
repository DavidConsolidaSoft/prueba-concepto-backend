# Generado automáticamente
# Tabla: dbo.grupo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Grupo(Base):
    __tablename__ = "grupo"
    __table_args__ = {"schema": "dbo"}

    ngrupo = Column(String(150), nullable=False)
    grupo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Grupo(grupo={self.grupo})>"