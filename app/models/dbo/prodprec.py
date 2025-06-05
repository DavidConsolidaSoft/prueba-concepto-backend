# Generado automáticamente
# Tabla: dbo.prodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class ProdPrec(Base):
    __tablename__ = "prodprec"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nprodprec = Column(String(50), nullable=False)
    fechainicial = Column(DateTime)
    fechafinal = Column(DateTime)
    moneda = Column(Integer, nullable=False)
    prodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    condicion1 = Column(Boolean, nullable=False)
    Margen = Column(Numeric(18, 6))
    MargenMinimo = Column(Numeric(18, 6))
    Preferido = Column(Boolean)
    ruta = Column(Boolean, nullable=False)
    taller = Column(Boolean, nullable=False)
    PorcDescuento = Column(Numeric(18, 6), nullable=False)
    porcentaje = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Prodprec(prodprec={self.prodprec})>"