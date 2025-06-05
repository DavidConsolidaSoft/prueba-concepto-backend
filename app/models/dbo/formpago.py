# Generado automáticamente
# Tabla: dbo.formpago
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class FormPago(Base):
    __tablename__ = "formpago"
    __table_args__ = {"schema": "dbo"}

    nformpago = Column(String(50), nullable=False)
    frecuente = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    formpago = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    empresa = Column(Integer, nullable=False)
    HORATIEMPO = Column(DateTime, nullable=False)
    FIJO = Column(Boolean)
    OBRA = Column(Boolean)
    COMISION = Column(Boolean)

    def __repr__(self):
        return "<Formpago(formpago={self.formpago})>"