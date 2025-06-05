# Generado automáticamente
# Tabla: dbo.AddingsProveedor
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Addingsproveedor(Base):
    __tablename__ = "AddingsProveedor"
    __table_args__ = {"schema": "dbo"}

    proveedor = Column(Integer)
    ccuenta = Column(Integer)
    serie = Column(String(50), nullable=False)
    resolucion = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    AddingsProveedor = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Addingsproveedor(AddingsProveedor={self.AddingsProveedor})>"