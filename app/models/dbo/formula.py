# Generado automáticamente
# Tabla: dbo.formula
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Formula(Base):
    __tablename__ = "formula"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    porcprecio = Column(Numeric(16, 6), nullable=False)
    porccosto = Column(Numeric(16, 6), nullable=False)
    mformula = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    formula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    descripcion = Column(String(50), nullable=False)
    concentracion = Column(Numeric(18, 6), nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    umedida = Column(Integer, nullable=False)
    presenta = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Formula(formula={self.formula})>"