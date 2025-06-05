# Generado automáticamente
# Tabla: dbo.CategoriaBien
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Categoriabien(Base):
    __tablename__ = "CategoriaBien"
    __table_args__ = {"schema": "dbo"}

    nCategoriaBien = Column(String(50), nullable=False)
    Codigo = Column(String(2), nullable=False)
    activo = Column(Boolean, nullable=False)
    CategoriaBien = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Categoriabien(CategoriaBien={self.CategoriaBien})>"