# Generado automáticamente
# Tabla: dbo.vcontabilidad
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer, String


class Vcontabilidad(Base):
    __tablename__ = "vcontabilidad"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    idalumno = Column(String(255))
    apellido1 = Column(String(255))
    apellido2 = Column(String(255))
    nombres = Column(String(255))
    idcategori = Column(String(255))
    DescripC = Column(String(255))
    email = Column(String(255))
    idcarrera = Column(String(255))
    Carrera = Column(String(255))
    calleaven = Column(String(255))
    numeroc = Column(String(255))
    colonibarr = Column(String(255))
    pasaje = Column(String(255))
    telefijo = Column(String(255))
    nombred = Column(String(255))
    nombremun = Column(String(255))

    def __repr__(self):
        return "<Vcontabilidad(idalumno={self.idalumno})>"