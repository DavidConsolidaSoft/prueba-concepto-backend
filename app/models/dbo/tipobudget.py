# Generado automáticamente
# Tabla: dbo.tipobudget
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipobudget(Base):
    __tablename__ = "tipobudget"
    __table_args__ = {"schema": "dbo"}

    tipobudget = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    producto = Column(Boolean, nullable=False)
    vendedor = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    depto = Column(Boolean, nullable=False)
    municip = Column(Boolean, nullable=False)
    ntipobudget = Column(String(20), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    Activo = Column(Boolean, nullable=False)
    Empresa = Column(Integer, nullable=False)
    Usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipobudget(tipobudget={self.tipobudget})>"