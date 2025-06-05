# Generado automáticamente
# Tabla: dbo.equipoprocess
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Equipoprocess(Base):
    __tablename__ = "equipoprocess"
    __table_args__ = {"schema": "dbo"}

    equipo = Column(Integer)
    almacen = Column(Integer)
    clientes = Column(String(25))
    tiempo = Column(Numeric(6, 2))
    fecha = Column(DateTime)
    fechainicio = Column(DateTime)
    fechafin = Column(DateTime)
    estatus = Column(Integer)
    rupfase = Column(Integer)
    empresa = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    horatiempo = Column(DateTime, nullable=False)
    equipoprocess = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    rupstatus = Column(Integer)
    fentrega = Column(DateTime)
    hcuanto = Column(Integer)
    rupot = Column(Integer)
    mcuanto = Column(Integer)
    empleado = Column(Integer)
    orden = Column(String(6))
    f1 = Column(DateTime)

    def __repr__(self):
        return "<Equipoprocess(equipoprocess={self.equipoprocess})>"