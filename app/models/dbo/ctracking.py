# Generado automáticamente
# Tabla: dbo.ctracking
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ctracking(Base):
    __tablename__ = "ctracking"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    getcompra = Column(Boolean, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    nctracking = Column(String(35), nullable=False)
    ctracking = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ctracking(ctracking={self.ctracking})>"