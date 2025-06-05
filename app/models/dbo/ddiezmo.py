# Generado automáticamente
# Tabla: dbo.dDiezmo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ddiezmo(Base):
    __tablename__ = "dDiezmo"
    __table_args__ = {"schema": "dbo"}

    dDiezmo = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    ctrocosto = Column(Integer, nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    diezmo = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)
    numedocu = Column(String(9), nullable=False)
    remesa = Column(String(15), nullable=False)

    def __repr__(self):
        return "<Ddiezmo(dDiezmo={self.dDiezmo})>"