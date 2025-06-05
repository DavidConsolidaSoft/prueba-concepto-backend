# Generado automáticamente
# Tabla: dbo.tipoBodega
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipobodega(Base):
    __tablename__ = "tipoBodega"
    __table_args__ = {"schema": "dbo"}

    ntipoBodega = Column(String(35), nullable=False)
    activo = Column(Boolean)
    tipoBodega = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Tipobodega(tipoBodega={self.tipoBodega})>"