# Generado automáticamente
# Tabla: dbo.sectorlaboral
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Sectorlaboral(Base):
    __tablename__ = "sectorlaboral"
    __table_args__ = {"schema": "dbo"}

    nsectorlaboral = Column(String(100), nullable=False)
    simbolo = Column(String(25), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    sectorlaboral = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Sectorlaboral(sectorlaboral={self.sectorlaboral})>"