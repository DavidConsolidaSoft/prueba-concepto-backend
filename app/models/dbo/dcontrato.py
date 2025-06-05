# Generado automáticamente
# Tabla: dbo.dcontrato
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dcontrato(Base):
    __tablename__ = "dcontrato"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    bonificado = Column(Numeric(16, 6), nullable=False)
    gratificado = Column(Numeric(16, 6), nullable=False)
    hcantidad = Column(Numeric(16, 6), nullable=False)
    hreservado = Column(Numeric(16, 6), nullable=False)
    hbonificado = Column(Numeric(16, 6), nullable=False)
    hgratificado = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    preciolista = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    texto = Column(String(10), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    vgdesc = Column(Numeric(16, 6), nullable=False)
    factorinteres = Column(Numeric(16, 6), nullable=False)
    factormora = Column(Numeric(16, 6), nullable=False)
    contrato = Column(Integer, nullable=False)
    dcontrato = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    kardex = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    pprima = Column(Numeric(16, 6), nullable=False)
    letras = Column(Numeric(16, 6), nullable=False)
    nula = Column(Boolean, nullable=False)

    # Relaciones
    # contrato_rel = relationship("Contrato", back_populates="dcontrato_set")  # Comentado automáticamente
    # kardex_rel = relationship("Kardex", back_populates="dcontrato_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dcontrato(dcontrato={self.dcontrato})>"