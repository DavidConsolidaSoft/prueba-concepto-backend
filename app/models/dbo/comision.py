# Generado automáticamente
# Tabla: dbo.comision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Comision(Base):
    __tablename__ = "comision"
    __table_args__ = {"schema": "dbo"}

    p1 = Column(Numeric(16, 6), nullable=False)
    l1 = Column(Integer, nullable=False)
    p2 = Column(Numeric(16, 6), nullable=False)
    l2 = Column(Integer, nullable=False)
    p3 = Column(Numeric(16, 6), nullable=False)
    l3 = Column(Integer, nullable=False)
    p4 = Column(Numeric(16, 6), nullable=False)
    l4 = Column(Integer, nullable=False)
    p5 = Column(Numeric(16, 6), nullable=False)
    l5 = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    comision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tipovendedor = Column(Integer, nullable=False)
    efectivo = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Comision(comision={self.comision})>"