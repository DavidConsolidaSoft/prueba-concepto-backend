# Generado automáticamente
# Tabla: dbo.presociales
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Presociales(Base):
    __tablename__ = "presociales"
    __table_args__ = {"schema": "dbo"}

    empleado = Column(Integer, nullable=False)
    anios = Column(Integer, nullable=False)
    meses = Column(Integer, nullable=False)
    dias = Column(Integer, nullable=False)
    suelmen = Column(Numeric(18, 6), nullable=False)
    sueldiario = Column(Numeric(18, 6), nullable=False)
    suelmenprom = Column(Numeric(18, 6), nullable=False)
    sueldiarioprom = Column(Numeric(18, 6), nullable=False)
    diaspreaviso = Column(Integer, nullable=False)
    preaviso = Column(Numeric(18, 6), nullable=False)
    diascesantia = Column(Integer, nullable=False)
    cesantia = Column(Numeric(18, 6), nullable=False)
    diaspreavisoprop = Column(Integer, nullable=False)
    preavisoprop = Column(Numeric(18, 6), nullable=False)
    diascesantiaprop = Column(Integer, nullable=False)
    cesantiaprop = Column(Numeric(18, 6), nullable=False)
    diasvacacion = Column(Integer, nullable=False)
    vacacion = Column(Numeric(18, 6), nullable=False)
    diasdecimo3 = Column(Integer, nullable=False)
    decimo3 = Column(Numeric(18, 6), nullable=False)
    diasdecimo4 = Column(Integer, nullable=False)
    decimo4 = Column(Numeric(18, 6), nullable=False)
    diasbonovacacion = Column(Integer, nullable=False)
    bonovacacion = Column(Numeric(18, 6), nullable=False)
    diastrabajados = Column(Integer, nullable=False)
    trabajados = Column(Numeric(18, 6), nullable=False)
    diasbonoedu = Column(Integer, nullable=False)
    bonoedu = Column(Numeric(18, 6), nullable=False)
    total = Column(Numeric(18, 6), nullable=False)
    diasleyvacaciones = Column(Integer, nullable=False)
    techobonoedu = Column(Numeric(18, 6), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    presociales = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Presociales(presociales={self.presociales})>"