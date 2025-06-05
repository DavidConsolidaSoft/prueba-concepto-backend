# Generado automáticamente
# Tabla: dbo.RupSolicitud
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rupsolicitud(Base):
    __tablename__ = "RupSolicitud"
    __table_args__ = {"schema": "dbo"}

    Clientes = Column(String(25), nullable=False)
    nRupSolicitud = Column(String(50))
    fechaSolicitud = Column(DateTime)
    ParaCuando = Column(DateTime)
    RupResponsable = Column(Integer, nullable=False)
    Precio = Column(Numeric(16, 6), nullable=False)
    PrecioReal = Column(Numeric(16, 6), nullable=False)
    Observaciones = Column(String(150), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupSolicitud = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupsolicitud(RupSolicitud={self.RupSolicitud})>"