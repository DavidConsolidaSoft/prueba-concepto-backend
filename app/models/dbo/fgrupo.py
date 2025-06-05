# Generado automáticamente
# Tabla: dbo.fgrupo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Fgrupo(Base):
    __tablename__ = "fgrupo"
    __table_args__ = {"schema": "dbo"}

    nfgrupo = Column(String(35), nullable=False)
    activo = Column(Boolean, nullable=False)
    fgrupo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Fgrupo(fgrupo={self.fgrupo})>"