# Generado automáticamente
# Tabla: dbo.CostoTipo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Costotipo(Base):
    __tablename__ = "CostoTipo"
    __table_args__ = {"schema": "dbo"}

    nCostoTipo = Column(String(50), nullable=False)
    Codigo = Column(String(2), nullable=False)
    activo = Column(Boolean, nullable=False)
    CostoTipo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Costotipo(CostoTipo={self.CostoTipo})>"