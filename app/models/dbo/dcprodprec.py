# Generado automáticamente
# Tabla: dbo.dcprodprec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dcprodprec(Base):
    __tablename__ = "dcprodprec"
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
    cprodprec = Column(Integer, nullable=False)
    dcprodprec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tprecio = Column(Numeric(16, 6), nullable=False)

    # Relaciones
    # producto_rel = relationship("Producto", back_populates="dcprodprec_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dcprodprec(dcprodprec={self.dcprodprec})>"