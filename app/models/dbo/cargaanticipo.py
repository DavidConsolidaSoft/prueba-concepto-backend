# Generado automáticamente
# Tabla: dbo.cargaAnticipo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Cargaanticipo(Base):
    __tablename__ = "cargaAnticipo"
    __table_args__ = {"schema": "dbo"}

    camion = Column(Integer, nullable=False)
    motorista = Column(Integer, nullable=False)
    empleado = Column(Integer, nullable=False)
    fecha = Column(DateTime)
    cargo = Column(Numeric(18, 6), nullable=False)
    anticipo = Column(Numeric(18, 6), nullable=False)
    autorizo = Column(Integer, nullable=False)
    liquido = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    cargaAnticipo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pagado = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    fecharetorno = Column(DateTime)
    fechasalida = Column(DateTime)
    clasecarga = Column(String(35), nullable=False)
    notas = Column(String(300))
    dplanilla = Column(Integer, nullable=False)
    destino = Column(String(100), nullable=False)
    dpfactura = Column(Integer, nullable=False)

    # Relaciones
    # camion_rel = relationship("Camion", back_populates="cargaanticipo_set")  # Comentado automáticamente
    # motorista_rel = relationship("Motorista", back_populates="cargaanticipo_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Cargaanticipo(cargaAnticipo={self.cargaAnticipo})>"