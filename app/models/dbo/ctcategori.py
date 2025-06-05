# Generado automáticamente
# Tabla: dbo.ctcategori
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ctcategori(Base):
    __tablename__ = "ctcategori"
    __table_args__ = {"schema": "dbo"}

    ncategori = Column(String(40), nullable=False)
    preferido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    ctcategori = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ctcategori(ctcategori={self.ctcategori})>"