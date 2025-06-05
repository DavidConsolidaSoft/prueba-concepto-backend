# Generado automáticamente
# Tabla: dbo.marca
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Marca(Base):
    __tablename__ = "marca"
    __table_args__ = {"schema": "dbo"}

    nmarca = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    marca = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Marca(marca={self.marca})>"