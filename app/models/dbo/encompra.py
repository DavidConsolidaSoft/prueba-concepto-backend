# Generado automáticamente
# Tabla: dbo.encompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Encompra(Base):
    __tablename__ = "encompra"
    __table_args__ = {"schema": "dbo"}

    nencompra = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    fecingreso = Column(DateTime)
    fecretiro = Column(DateTime)
    lencompra = Column(Boolean, nullable=False)
    lpagador = Column(Boolean, nullable=False)
    encompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Encompra(encompra={self.encompra})>"