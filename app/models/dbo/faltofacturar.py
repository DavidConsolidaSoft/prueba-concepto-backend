# Generado automáticamente
# Tabla: dbo.faltofacturar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Faltofacturar(Base):
    __tablename__ = "faltofacturar"
    __table_args__ = {"schema": "dbo"}

    clientes = Column(String(25), nullable=False)
    vendedor = Column(Integer, nullable=False)
    kardex = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    cantidad = Column(Numeric(18, 6))
    precio = Column(Numeric(18, 6))
    faltofacturar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Faltofacturar(faltofacturar={self.faltofacturar})>"