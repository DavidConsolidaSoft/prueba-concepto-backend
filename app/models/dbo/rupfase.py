# Generado automáticamente
# Tabla: dbo.RupFase
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Rupfase(Base):
    __tablename__ = "RupFase"
    __table_args__ = {"schema": "dbo"}

    nRupFase = Column(String(80))
    Orden = Column(String(5), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupFase = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    Preparacion = Column(Boolean, nullable=False)
    MaterialEmpaque = Column(Boolean, nullable=False)
    MateriaPrima = Column(Boolean, nullable=False)
    Adicion = Column(Boolean, nullable=False)
    Devolucion = Column(Boolean, nullable=False)
    Produccion = Column(Boolean, nullable=False)
    Revision = Column(Boolean, nullable=False)
    productoTerminado = Column(Boolean, nullable=False)
    repuesto = Column(Boolean, nullable=False)
    TALLER = Column(Boolean, nullable=False)
    informe = Column(String(35), nullable=False)
    imprimeInforme = Column(Boolean, nullable=False)
    nivel = Column(Integer)

    def __repr__(self):
        return "<Rupfase(RupFase={self.RupFase})>"