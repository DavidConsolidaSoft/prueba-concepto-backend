# Generado automáticamente
# Tabla: dbo.ordenFormula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Ordenformula(Base):
    __tablename__ = "ordenFormula"
    __table_args__ = {"schema": "dbo"}

    ordenFormula = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    cantidad = Column(Numeric(18, 6), nullable=False)
    porcprecio = Column(Numeric(18, 6), nullable=False)
    porccosto = Column(Numeric(18, 6), nullable=False)
    concentracion = Column(Numeric(18, 6), nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    ordentrabajo = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Ordenformula(ordenFormula={self.ordenFormula})>"