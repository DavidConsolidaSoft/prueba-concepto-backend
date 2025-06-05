# Generado automáticamente
# Tabla: dbo.politing
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Politing(Base):
    __tablename__ = "politing"
    __table_args__ = {"schema": "dbo"}

    tipopla = Column(Integer)
    ingreso = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    poliing = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    emptipla = Column(Integer)
    empleado = Column(Integer)
    monto = Column(Numeric(19, 4))
    manual = Column(Boolean)
    devengado = Column(Boolean)

    def __repr__(self):
        return "<Politing(poliing={self.poliing})>"