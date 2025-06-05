# Generado automáticamente
# Tabla: dbo.MiMensaje
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Mimensaje(Base):
    __tablename__ = "MiMensaje"
    __table_args__ = {"schema": "dbo"}

    MiMensaje = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nMiMensaje = Column(String(250), nullable=False)
    longitud = Column(Integer, nullable=False)
    Preferido = Column(Boolean, nullable=False)
    Activo = Column(Boolean, nullable=False)
    Empresa = Column(Integer, nullable=False)
    Usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Mimensaje(MiMensaje={self.MiMensaje})>"