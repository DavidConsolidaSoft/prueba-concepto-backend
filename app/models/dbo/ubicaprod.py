# Generado automáticamente
# Tabla: dbo.ubicaProd
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class UbicaProd(Base):
    __tablename__ = "ubicaProd"
    __table_args__ = {"schema": "dbo"}

    uProd = Column(String(4))
    producto = Column(Integer)
    caja = Column(Integer)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    ubicaProd = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Ubicaprod(ubicaProd={self.ubicaProd})>"