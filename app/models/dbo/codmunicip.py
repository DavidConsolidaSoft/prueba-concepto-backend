# Generado automáticamente
# Tabla: dbo.codmunicip
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Codmunicip(Base):
    __tablename__ = "codmunicip"
    __table_args__ = {"schema": "dbo"}

    ncodmunicip = Column(String(25))
    municip = Column(Integer)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    codmunicip = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Codmunicip(codmunicip={self.codmunicip})>"