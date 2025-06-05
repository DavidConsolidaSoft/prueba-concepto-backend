# Generado automáticamente
# Tabla: dbo.ventascon
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ventascon(Base):
    __tablename__ = "ventascon"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    docini = Column(String(35))
    docfin = Column(String(35))
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    exportacion = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    serie = Column(String(1), nullable=False)
    iva = Column(Integer, nullable=False)
    periodoiva = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    ventascon = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    ncaja = Column(String(50), nullable=False)
    tipomov = Column(Integer, nullable=False)
    nueva = Column(Boolean, nullable=False)
    cotrans = Column(Numeric(18, 6), nullable=False)
    tipobodega = Column(Integer, nullable=False)
    ccref = Column(String(50), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    factura = Column(Integer, nullable=False)
    importado = Column(Boolean, nullable=False)
    total = Column(Numeric(18, 6), nullable=False)
    retencion = Column(Numeric(18, 6), nullable=False)
    cuenta = Column(Integer)
    partida = Column(Integer)
    tarjeta = Column(Integer)
    CESC = Column(Numeric(9, 2), nullable=False)

    # Relaciones
    # periodoiva_rel = relationship("Periodoiva", back_populates="ventascon_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ventascon(ventascon={self.ventascon})>"