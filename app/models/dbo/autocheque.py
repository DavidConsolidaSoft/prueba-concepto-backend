# Generado automáticamente
# Tabla: dbo.autocheque
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Autocheque(Base):
    __tablename__ = "autocheque"
    __table_args__ = {"schema": "dbo"}

    autocheque = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    partida = Column(Integer, nullable=False)
    chpartida = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    abono = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Autocheque(autocheque={self.autocheque})>"