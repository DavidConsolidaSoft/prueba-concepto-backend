# Generado automáticamente
# Tabla: dbo.AddingsClientes
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Addingsclientes(Base):
    __tablename__ = "AddingsClientes"
    __table_args__ = {"schema": "dbo"}

    tipomov = Column(Integer)
    caja = Column(Integer)
    serie = Column(String(50))
    resolucion = Column(String(50))
    fecha = Column(DateTime)
    activo = Column(Boolean, nullable=False)
    AddingsClientes = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    descrip = Column(String(15))

    def __repr__(self):
        return "<Addingsclientes(AddingsClientes={self.AddingsClientes})>"