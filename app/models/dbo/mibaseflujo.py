# Generado automáticamente
# Tabla: dbo.mibaseflujo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Mibaseflujo(Base):
    __tablename__ = "mibaseflujo"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    anio = Column(Integer, nullable=False)
    mes = Column(Integer, nullable=False)
    Mayorno = Column(String(25), nullable=False)
    MayorNombre = Column(String(70), nullable=False)
    concepto = Column(String(70))
    monto = Column(Numeric(18, 6))
    grupo = Column(String(25), nullable=False)
    gruponombre = Column(String(70), nullable=False)
    empresa_ = Column(String(70))
    horatiempo = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    ejecutado = Column(Numeric(18, 6), nullable=False)
    proyectado = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Mibaseflujo(anio={self.anio})>"