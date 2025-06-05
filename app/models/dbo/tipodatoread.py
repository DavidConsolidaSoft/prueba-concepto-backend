# Generado automáticamente
# Tabla: dbo.tipodatoread
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Tipodatoread(Base):
    __tablename__ = "tipodatoread"
    __table_args__ = {"schema": "dbo"}

    tipodatotxt = Column(Integer, nullable=False)
    tipodato = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tipodatoread = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipodatoread(tipodatoread={self.tipodatoread})>"