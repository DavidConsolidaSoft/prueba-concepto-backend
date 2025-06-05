# Generado automáticamente
# Tabla: dbo.ingreso
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Ingreso(Base):
    __tablename__ = "ingreso"
    __table_args__ = {"schema": "dbo"}

    ningreso = Column(String(80))
    activo = Column(Boolean)
    comision = Column(Boolean)
    aguinaldo = Column(Boolean)
    vacacion = Column(Boolean)
    frecpago = Column(Integer)
    ingreso = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    VIATICOS = Column(Boolean)
    PROPORCIONAL = Column(Boolean, nullable=False)
    gratificacion = Column(Boolean)
    HEF = Column(Boolean)
    Alimentacion = Column(Boolean)

    def __repr__(self):
        return "<Ingreso(ingreso={self.ingreso})>"