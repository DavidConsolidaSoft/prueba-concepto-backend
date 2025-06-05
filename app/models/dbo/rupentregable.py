# Generado automáticamente
# Tabla: dbo.RupEntregable
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rupentregable(Base):
    __tablename__ = "RupEntregable"
    __table_args__ = {"schema": "dbo"}

    RupOT = Column(Integer, nullable=False)
    RupEntResponsable = Column(Integer, nullable=False)
    nRupEntregable = Column(String(35))
    ParaCuandoEnt = Column(DateTime)
    Activo = Column(Boolean, nullable=False)
    RupEntregable = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupentregable(RupEntregable={self.RupEntregable})>"