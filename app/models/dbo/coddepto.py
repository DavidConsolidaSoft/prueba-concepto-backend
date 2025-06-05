# Generado automáticamente
# Tabla: dbo.coddepto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Coddepto(Base):
    __tablename__ = "coddepto"
    __table_args__ = {"schema": "dbo"}

    ncoddepto = Column(String(25))
    depto = Column(Integer)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    coddepto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Coddepto(coddepto={self.coddepto})>"