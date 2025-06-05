# Generado automáticamente
# Tabla: dbo.fixed
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Fixed(Base):
    __tablename__ = "fixed"
    __table_args__ = {"schema": "dbo"}

    nproducto = Column(String(50), nullable=False)
    otroname = Column(String(150), nullable=False)
    activo = Column(Boolean, nullable=False)
    controla = Column(Boolean, nullable=False)
    bonificado = Column(Boolean, nullable=False)
    vineta = Column(Boolean, nullable=False)
    enventa = Column(Boolean, nullable=False)
    incluir = Column(Boolean, nullable=False)
    fabricar = Column(Boolean, nullable=False)
    exento = Column(Boolean, nullable=False)
    desccontad = Column(Boolean, nullable=False)
    parte = Column(Boolean, nullable=False)
    servicios = Column(Boolean, nullable=False)
    costo = Column(Numeric(15, 7), nullable=False)
    cantidadre = Column(Numeric(15, 6), nullable=False)
    minimo = Column(Numeric(15, 6), nullable=False)
    cantidadco = Column(Numeric(15, 6), nullable=False)
    compramini = Column(Numeric(15, 6), nullable=False)
    compramaxi = Column(Numeric(15, 6), nullable=False)
    promedio = Column(Numeric(15, 6), nullable=False)
    promlicita = Column(Numeric(15, 6), nullable=False)
    promedioex = Column(Numeric(15, 6), nullable=False)
    promlicit2 = Column(Numeric(15, 6), nullable=False)
    codbarra = Column(String(25),primary_key=True, nullable=False)
    icdbarra = Column(String(25), nullable=False)

    def __repr__(self):
        return "<Fixed(nproducto={self.nproducto})>"