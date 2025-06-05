# Generado automáticamente
# Tabla: dbo.kcodbarra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, String


class Kcodbarra(Base):
    __tablename__ = "kcodbarra"
    __table_args__ = {"schema": "dbo"}

    codigo = Column(String(50),primary_key=True, nullable=False)
    codbarra = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Kcodbarra(codigo={self.codigo})>"