# Generado automáticamente
# Tabla: dbo.CategoriaNomina
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Categorianomina(Base):
    __tablename__ = "CategoriaNomina"
    __table_args__ = {"schema": "dbo"}

    CategoriaNomina = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    nCategoriaNomina = Column(String(150), nullable=False)
    Sancion = Column(Boolean, nullable=False)
    Reconocimiento = Column(Boolean, nullable=False)
    capacitacion = Column(Boolean, nullable=False)
    Titulos = Column(Boolean, nullable=False)
    asensos = Column(Boolean, nullable=False)
    permisos = Column(Boolean, nullable=False)
    inacistencias = Column(Boolean, nullable=False)
    accidentes = Column(Boolean, nullable=False)
    solicitudEmpleo = Column(Boolean, nullable=False)
    despido = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Categorianomina(CategoriaNomina={self.CategoriaNomina})>"