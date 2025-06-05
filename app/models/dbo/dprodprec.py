# Generado automáticamente
# Tabla: dbo.dprodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class DProdPrec(Base):
    __tablename__ = "dprodprec"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    pfecha = Column(DateTime)
    pminimo = Column(Numeric(16, 6), nullable=False)
    precioa = Column(Numeric(16, 6), nullable=False)
    preciob = Column(Numeric(16, 6), nullable=False)
    precioc = Column(Numeric(16, 6), nullable=False)
    cantidada = Column(Integer, nullable=False)
    cantidadb = Column(Integer, nullable=False)
    cantidadc = Column(Integer, nullable=False)
    mprecio = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    fprecio = Column(Numeric(16, 6), nullable=False)
    cfecha = Column(DateTime)
    factor = Column(Numeric(16, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    dprodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tprecio = Column(Numeric(16, 6), nullable=False)
    TIPCLI = Column(Integer, nullable=False)
    Margen = Column(Numeric(18, 6))
    MargenMinimo = Column(Numeric(18, 6))
    vineta = Column(Numeric(18, 6), nullable=False)
    pprecio = Column(Numeric(18, 6), nullable=False)
    fPrecioPromo = Column(Numeric(18, 6), nullable=False)
    tPrecioPromo = Column(Numeric(18, 6), nullable=False)
    pfechaini = Column(DateTime)
    pfechafin = Column(DateTime)
    precio1 = Column(Numeric(18, 6), nullable=False)
    precio2 = Column(Numeric(18, 6), nullable=False)
    precio3 = Column(Numeric(18, 6), nullable=False)
    precio4 = Column(Numeric(18, 6), nullable=False)
    precio5 = Column(Numeric(18, 6), nullable=False)
    precio6 = Column(Numeric(18, 6), nullable=False)
    precio7 = Column(Numeric(18, 6), nullable=False)
    precio8 = Column(Numeric(18, 6), nullable=False)
    precioagregado = Column(Numeric(18, 6), nullable=False)
    parte = Column(Boolean, nullable=False)
    cargofull = Column(Numeric(18, 6), nullable=False)
    qlinea = Column(Integer, nullable=False)
    preciomax = Column(Numeric(18, 6), nullable=False)

    # Relaciones
    # producto_rel = relationship("Producto", back_populates="dprodprec_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dprodprec(dprodprec={self.dprodprec})>"