# Generado automáticamente
# Tabla: dbo.planwork
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Planwork(Base):
    __tablename__ = "planwork"
    __table_args__ = {"schema": "dbo"}

    dia = Column(Integer)
    fecha = Column(DateTime)
    equipo = Column(Integer)
    rupfase = Column(Integer)
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    planwork = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Planwork(planwork={self.planwork})>"