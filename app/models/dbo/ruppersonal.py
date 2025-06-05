# Generado automáticamente
# Tabla: dbo.RupPersonal
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Ruppersonal(Base):
    __tablename__ = "RupPersonal"
    __table_args__ = {"schema": "dbo"}

    nRupPersonal = Column(String(50), nullable=False)
    fechaIngreso = Column(DateTime)
    fechaRetiro = Column(DateTime)
    HoraHombre = Column(Numeric(16, 6), nullable=False)
    Observaciones = Column(String(200))
    Renta = Column(Boolean, nullable=False)
    Factura = Column(Boolean, nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupPersonal = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Ruppersonal(RupPersonal={self.RupPersonal})>"