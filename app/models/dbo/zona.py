# Generado automáticamente
# Tabla: dbo.zona
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Zona(Base):
    __tablename__ = "zona"
    __table_args__ = {"schema": "dbo"}

    zona = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nzona = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Zona(zona={self.zona})>"