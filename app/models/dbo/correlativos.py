# Generado automáticamente
# Tabla: dbo.correlativos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Correlativos(Base):
    __tablename__ = "correlativos"
    __table_args__ = {"schema": "dbo"}

    correlativos = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    dato = Column(String(4))

    def __repr__(self):
        return "<Correlativos(correlativos={self.correlativos})>"