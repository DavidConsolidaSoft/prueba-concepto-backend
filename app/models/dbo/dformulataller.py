# Generado automáticamente
# Tabla: dbo.dformulataller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Dformulataller(Base):
    __tablename__ = "dformulataller"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    km3 = Column(Boolean, nullable=False)
    km5 = Column(Boolean, nullable=False)
    km6 = Column(Boolean, nullable=False)
    km9 = Column(Boolean, nullable=False)
    km10 = Column(Boolean, nullable=False)
    km12 = Column(Boolean, nullable=False)
    km15 = Column(Boolean, nullable=False)
    km18 = Column(Boolean, nullable=False)
    km20 = Column(Boolean, nullable=False)
    km21 = Column(Boolean, nullable=False)
    km24 = Column(Boolean, nullable=False)
    km25 = Column(Boolean, nullable=False)
    km27 = Column(Boolean, nullable=False)
    km30 = Column(Boolean, nullable=False)
    km33 = Column(Boolean, nullable=False)
    km35 = Column(Boolean, nullable=False)
    km36 = Column(Boolean, nullable=False)
    km40 = Column(Boolean, nullable=False)
    km150 = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    formulaTaller = Column(Integer, nullable=False)
    dformulataller = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    descripcion = Column(String(50), nullable=False)
    orden = Column(String(5), nullable=False)
    rupfase = Column(Integer, nullable=False)

    # Relaciones
    # rupfase_rel = relationship("Rupfase", back_populates="dformulataller_set")  # Comentado automáticamente
    # formulataller = relationship("Formulataller", back_populates="dformulataller_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Dformulataller(dformulataller={self.dformulataller})>"