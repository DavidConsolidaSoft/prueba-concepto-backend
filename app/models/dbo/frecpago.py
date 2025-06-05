# Generado automáticamente
# Tabla: dbo.frecpago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Frecpago(Base):
    __tablename__ = "frecpago"
    __table_args__ = {"schema": "dbo"}

    nfrecpago = Column(String(50), nullable=False)
    primera = Column(Boolean, nullable=False)
    uno = Column(Numeric(5, 2))
    segunda = Column(Boolean, nullable=False)
    dos = Column(Numeric(5, 2), nullable=False)
    todas = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    frecpago = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Frecpago(nfrecpago={self.nfrecpago})>"