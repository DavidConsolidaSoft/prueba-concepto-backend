# Generado automáticamente
# Tabla: dbo.politpla
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Politpla(Base):
    __tablename__ = "politpla"
    __table_args__ = {"schema": "dbo"}

    poldesc = Column(Integer)
    tipopla = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    politpla = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    emptipla = Column(Integer)
    empleado = Column(Integer)
    MONTO = Column(Numeric(19, 4))

    def __repr__(self):
        return "<Politpla(politpla={self.politpla})>"