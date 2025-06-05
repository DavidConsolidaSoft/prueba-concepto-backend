# Generado automáticamente
# Tabla: dbo.contratoPagos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Contratopagos(Base):
    __tablename__ = "contratoPagos"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    invcliente = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    montfact = Column(Numeric(18, 6), nullable=False)
    contratoPagos = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    # Relaciones
    # factura_rel = relationship("Factura", back_populates="contratopagos_set")  # Comentado automáticamente
    # invcliente_rel = relationship("Invcliente", back_populates="contratopagos_set")  # Comentado automáticamente
    # pagos_rel = relationship("Pagos", back_populates="contratopagos_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Contratopagos(contratoPagos={self.contratoPagos})>"