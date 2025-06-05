# Generado automáticamente
# Tabla: dbo.parentes
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Parentes(Base):
    __tablename__ = "parentes"
    __table_args__ = {"schema": "dbo"}

    nparentes = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    parentes = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Parentes(parentes={self.parentes})>"