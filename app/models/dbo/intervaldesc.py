# Generado automáticamente
# Tabla: dbo.IntervalDesc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Intervaldesc(Base):
    __tablename__ = "IntervalDesc"
    __table_args__ = {"schema": "dbo"}

    IntervalDesc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    interval1 = Column(Integer)
    interval2 = Column(Integer)
    interval3 = Column(Integer)
    interval4 = Column(Integer)
    interval5 = Column(Integer)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    diasgracia = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Intervaldesc(IntervalDesc={self.IntervalDesc})>"