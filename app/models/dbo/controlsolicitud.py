# Generado automáticamente
# Tabla: dbo.ControlSolicitud
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Controlsolicitud(Base):
    __tablename__ = "ControlSolicitud"
    __table_args__ = {"schema": "dbo"}

    Clientes = Column(String(25), nullable=False)
    OrdenTrabajo = Column(Integer, nullable=False)
    nControlSolicitud = Column(String(50), nullable=False)
    fechaSolicitud = Column(DateTime)
    fechaEntrega = Column(DateTime)
    fechaInicial = Column(DateTime)
    fechaTermino = Column(DateTime)
    empleado = Column(Integer, nullable=False)
    PrecioBudget = Column(Numeric(16, 6), nullable=False)
    PrecioReal = Column(Numeric(16, 6), nullable=False)
    Observaciones = Column(String(45), nullable=False)
    Activo = Column(Boolean, nullable=False)
    ControlSolicitud = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controlsolicitud(ControlSolicitud={self.ControlSolicitud})>"