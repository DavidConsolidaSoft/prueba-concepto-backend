# Generado automáticamente
# Tabla: dbo.dOrdenTrabajo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dordentrabajo(Base):
    __tablename__ = "dOrdenTrabajo"
    __table_args__ = {"schema": "dbo"}

    dOrdenTrabajo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ordenTrabajo = Column(Integer, nullable=False)
    rupfase = Column(Integer, nullable=False)
    ausuario = Column(Integer, nullable=False)
    susuario = Column(Integer, nullable=False)
    finicio = Column(DateTime, nullable=False)
    ffin = Column(DateTime)
    perdida = Column(Numeric(18, 6), nullable=False)
    devolucion = Column(Boolean, nullable=False)
    adicion = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    suspendida = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    Operadores = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    ingreso = Column(Boolean, nullable=False)
    salida = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    rupstatus = Column(Integer, nullable=False)
    costo = Column(Numeric(18, 6), nullable=False)
    dias = Column(Integer, nullable=False)
    horas = Column(Integer, nullable=False)
    Informe = Column(String(35), nullable=False)
    almacen = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dordentrabajo(dOrdenTrabajo={self.dOrdenTrabajo})>"