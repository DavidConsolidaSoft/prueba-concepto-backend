# Generado automáticamente
# Tabla: dbo.rangospagados
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Rangospagados(Base):
    __tablename__ = "rangospagados"
    __table_args__ = {"schema": "dbo"}

    rangospagados = Column(Integer, primary_key=True, nullable=False)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    impresa = Column(Boolean, nullable=False)
    pcomision = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Rangospagados(rangospagados={self.rangospagados})>"