# Generado automáticamente
# Tabla: dbo.ctrocosto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Ctrocosto(Base):
    __tablename__ = "ctrocosto"
    __table_args__ = {"schema": "dbo"}

    noctrocosto = Column(String(25), nullable=False)
    nctrocosto = Column(String(50), nullable=False)
    ctrolong = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    ctrocosto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    provision = Column(Integer, nullable=False)
    Partida = Column(Integer, nullable=False)
    sucursal = Column(Integer, nullable=False)
    informeRetencion = Column(String(25), nullable=False)
    Nombre = Column(String(60), nullable=False)
    Nit = Column(String(18), nullable=False)
    Direccion = Column(String(255), nullable=False)
    telefono = Column(String(18), nullable=False)
    Celular = Column(String(18), nullable=False)
    email = Column(String(35), nullable=False)
    Notas = Column(String(255), nullable=False)
    hijos = Column(Integer, nullable=False)
    fechaIngreso = Column(DateTime, nullable=False)
    lider = Column(Integer, nullable=False)
    Nacionalidad = Column(Integer, nullable=False)
    Distrito = Column(Integer, nullable=False)
    Domiciliado = Column(Boolean, nullable=False)
    porc = Column(Numeric(5, 2))

    # Relaciones
    # ctrolong_rel = relationship("Ctrolong", back_populates="ctrocosto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Ctrocosto(ctrocosto={self.ctrocosto})>"