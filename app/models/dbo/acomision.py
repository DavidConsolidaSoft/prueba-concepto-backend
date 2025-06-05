# Generado automáticamente
# Tabla: dbo.acomision
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Acomision(Base):
    __tablename__ = "acomision"
    __table_args__ = {"schema": "dbo"}

    miembro = Column(String(35), nullable=False)
    clientes = Column(String(25), nullable=False)
    ccopias = Column(Numeric(15, 6), nullable=False)
    cal1 = Column(Numeric(4, 2), nullable=False)
    compnivel1 = Column(Numeric(15, 6), nullable=False)
    comsdirectos = Column(Numeric(15, 6), nullable=False)
    calc2 = Column(Numeric(15, 6), nullable=False)
    compnivel2 = Column(Numeric(15, 6), nullable=False)
    comsdirectos2 = Column(Numeric(15, 6), nullable=False)
    pnivel = Column(Numeric(15, 6), nullable=False)
    snivel = Column(Numeric(15, 6), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    acomision = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Acomision(acomision={self.acomision})>"