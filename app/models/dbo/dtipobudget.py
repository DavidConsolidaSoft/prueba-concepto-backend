# Generado automáticamente
# Tabla: dbo.dtipobudget
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Dtipobudget(Base):
    __tablename__ = "dtipobudget"
    __table_args__ = {"schema": "dbo"}

    dtipobudget = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tipobudget = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    clientes = Column(String(25), nullable=False)
    depto = Column(Integer, nullable=False)
    municip = Column(Integer, nullable=False)
    budget = Column(Numeric(18, 6), nullable=False)
    mes = Column(DateTime)
    horatiempo = Column(DateTime, nullable=False)
    Activo = Column(Boolean, nullable=False)
    Empresa = Column(Integer, nullable=False)
    Usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dtipobudget(dtipobudget={self.dtipobudget})>"