# Generado automáticamente
# Tabla: dbo.dprestamo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dprestamo(Base):
    __tablename__ = "dprestamo"
    __table_args__ = {"schema": "dbo"}

    planilla = Column(Integer)
    cuotanum = Column(Numeric(5, 0), nullable=False)
    fpagocuota = Column(DateTime, nullable=False)
    montocuota = Column(Numeric(18, 6), nullable=False)
    activo = Column(Boolean, nullable=False)
    prestemp = Column(Integer)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    dprestamo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer)
    pagado = Column(Boolean)
    noincluir = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Dprestamo(dprestamo={self.dprestamo})>"