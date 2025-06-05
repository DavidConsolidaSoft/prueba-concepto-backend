# Generado automáticamente
# Tabla: dbo.prodform
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Prodform(Base):
    __tablename__ = "prodform"
    __table_args__ = {"schema": "dbo"}

    nprodform = Column(String(120), nullable=False)
    ncprodform = Column(String(55), nullable=False)
    especific = Column(String(25), nullable=False)
    registrosani = Column(String(15), nullable=False)
    fecini1 = Column(DateTime)
    vence1 = Column(DateTime)
    estado1 = Column(String(50), nullable=False)
    responsable1 = Column(String(50), nullable=False)
    direccion1 = Column(String(50), nullable=False)
    telefono1 = Column(String(25), nullable=False)
    registromarca = Column(String(15), nullable=False)
    fecini2 = Column(DateTime)
    vence2 = Column(DateTime)
    estado2 = Column(String(50), nullable=False)
    responsable2 = Column(String(50), nullable=False)
    direccion2 = Column(String(50), nullable=False)
    telefono = Column(String(15), nullable=False)
    activo = Column(Boolean, nullable=False)
    formato = Column(Integer, nullable=False)
    producto = Column(Integer, nullable=False)
    prodform = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # producto_rel = relationship("Producto", back_populates="prodform_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Prodform(prodform={self.prodform})>"