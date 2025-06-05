# Generado automáticamente
# Tabla: dbo.contrato
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Contrato(Base):
    __tablename__ = "contrato"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    cancelada = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    numedocu = Column(String(9), nullable=False)
    pedido = Column(String(10), nullable=False)
    notas = Column(String(200), nullable=False)
    fecha = Column(DateTime, nullable=False)
    fechacanc = Column(DateTime)
    clientes = Column(String(25), nullable=False)
    bodega = Column(Integer, nullable=False)
    prodprec = Column(Integer, nullable=False)
    iva = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tipomov = Column(Integer, nullable=False)
    factoriva = Column(Numeric(16, 6), nullable=False)
    factorinteres = Column(Numeric(16, 6), nullable=False)
    factormora = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    contrato = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cargo = Column(Numeric(16, 6), nullable=False)
    abono = Column(Numeric(16, 6), nullable=False)
    pprima = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    letras = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    basesiniva = Column(Boolean, nullable=False)

    # Relaciones
    # tipomov_rel = relationship("Tipomov", back_populates="contrato_set")  # Comentado automáticamente
    # vendedor_rel = relationship("Vendedor", back_populates="contrato_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Contrato(contrato={self.contrato})>"