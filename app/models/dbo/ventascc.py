# Generado automáticamente
# Tabla: dbo.ventascc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ventascc(Base):
    __tablename__ = "ventascc"
    __table_args__ = {"schema": "dbo"}

    numedocu = Column(String(35))
    fecha = Column(DateTime, nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    exportacion = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    serie = Column(String(1), nullable=False)
    clientes = Column(String(25), nullable=False)
    iva = Column(Integer, nullable=False)
    periodoiva = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    ventascc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    factor = Column(Numeric(16, 6), nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    tipomov = Column(Integer, nullable=False)
    otro = Column(Numeric(16, 6), nullable=False)
    PEDIDO = Column(String(25), nullable=False)
    cotrans = Column(Numeric(18, 6), nullable=False)
    tipobodega = Column(Integer, nullable=False)
    CCREF = Column(String(50))
    docunico = Column(String(9), nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    nosujeto = Column(Numeric(18, 6), nullable=False)
    factura = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    importado = Column(Boolean, nullable=False)
    cuenta = Column(Integer)
    partida = Column(Integer)
    tarjeta = Column(Numeric(9, 2))
    CESC = Column(Numeric(9, 2), nullable=False)

    # Relaciones
    # clientes_rel = relationship("Clientes", back_populates="ventascc_set")  # Comentado automáticamente
    # periodoiva_rel = relationship("Periodoiva", back_populates="ventascc_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ventascc(ventascc={self.ventascc})>"