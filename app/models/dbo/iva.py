# Generado automáticamente
# Tabla: dbo.iva
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Iva(Base):
    __tablename__ = "iva"
    __table_args__ = {"schema": "dbo"}

    niva = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    operador = Column(String(1), nullable=False)
    fechainicio = Column(DateTime)
    fechafinal = Column(DateTime)
    ivalocal = Column(Boolean, nullable=False)
    ivaexport = Column(Boolean, nullable=False)
    ivaimport = Column(Boolean, nullable=False)
    iva = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    tipovta = Column(Integer, nullable=False)
    PERCEPCION = Column(Numeric(18, 6), nullable=False)
    pais = Column(Integer, nullable=False)
    fseguridad = Column(Numeric(2, 0), nullable=False)

    def __repr__(self):
        return "<Iva(iva={self.iva})>"