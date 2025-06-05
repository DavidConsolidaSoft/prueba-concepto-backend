# Generado automáticamente
# Tabla: dbo.controlcitas
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Controlcitas(Base):
    __tablename__ = "controlcitas"
    __table_args__ = {"schema": "dbo"}

    mitiempo = Column(Integer)
    midsemana = Column(Integer)
    clientes = Column(String(25))
    vendedor = Column(Integer)
    Notas = Column(String(500))
    diasemana = Column(Integer)
    dia = Column(DateTime)
    hora1 = Column(String(8))
    hora2 = Column(String(8))
    controlcitas = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    horasefectivas = Column(Numeric(18, 6))
    producto = Column(Integer)
    recordar = Column(Integer)
    drecordar = Column(DateTime)
    ordentrabajo = Column(Integer)
    rupfase = Column(Integer)
    rupsolicitud = Column(Integer)
    ruptipoproceso = Column(Integer)
    monto = Column(Numeric(10, 2))
    actividad = Column(Integer)

    def __repr__(self):
        return "<Controlcitas(controlcitas={self.controlcitas})>"