# Generado automáticamente
# Tabla: dbo.nivel
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Nivel(Base):
    __tablename__ = "nivel"
    __table_args__ = {"schema": "dbo"}

    nnivel = Column(String(15), nullable=False)
    tipo = Column(Integer, nullable=False)
    nota = Column(String(50), nullable=False)
    nivel = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Nivel(nivel={self.nivel})>"