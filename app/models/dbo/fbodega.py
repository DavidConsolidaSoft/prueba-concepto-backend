# Generado automáticamente
# Tabla: dbo.fbodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Fbodega(Base):
    __tablename__ = "fbodega"
    __table_args__ = {"schema": "dbo"}

    nfbodega = Column(String(25), nullable=False)
    activo = Column(Boolean, nullable=False)
    fbodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Fbodega(fbodega={self.fbodega})>"