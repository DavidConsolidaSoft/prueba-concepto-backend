# Generado automáticamente
# Tabla: dbo.Incapacidad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Incapacidad(Base):
    __tablename__ = "Incapacidad"
    __table_args__ = {"schema": "dbo"}

    Incapacidad = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    inicio = Column(DateTime)
    fin = Column(DateTime)
    nIncapacidad = Column(String(80))
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    TipoIncapacidad = Column(Integer)
    Planilla = Column(Integer)
    empleado = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    ndias = Column(Integer)
    montopago = Column(Numeric(18, 6))
    fechareg = Column(DateTime)
    notas = Column(String(150))

    def __repr__(self):
        return "<Incapacidad(Incapacidad={self.Incapacidad})>"