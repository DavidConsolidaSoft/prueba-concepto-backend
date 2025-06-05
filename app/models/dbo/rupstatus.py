# Generado automáticamente
# Tabla: dbo.RupStatus
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rupstatus(Base):
    __tablename__ = "RupStatus"
    __table_args__ = {"schema": "dbo"}

    nRupStatus = Column(String(25))
    Activo = Column(Boolean, nullable=False)
    RupStatus = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    suspendido = Column(Boolean, nullable=False)
    terminado = Column(Boolean, nullable=False)
    cancelado = Column(Boolean, nullable=False)
    enproceso = Column(Boolean, nullable=False)
    noiniciado = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Rupstatus(RupStatus={self.RupStatus})>"