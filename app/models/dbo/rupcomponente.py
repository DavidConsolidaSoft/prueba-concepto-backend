# Generado automáticamente
# Tabla: dbo.RupComponente
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rupcomponente(Base):
    __tablename__ = "RupComponente"
    __table_args__ = {"schema": "dbo"}

    RupEntregable = Column(Integer, nullable=False)
    RupCompResponsable = Column(Integer, nullable=False)
    nRupComponente = Column(String(35))
    ParaCuandoComp = Column(DateTime)
    Activo = Column(Boolean, nullable=False)
    RupComponente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupcomponente(RupComponente={self.RupComponente})>"