# Generado automáticamente
# Tabla: dbo.MiFlujoProy
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Miflujoproy(Base):
    __tablename__ = "MiFlujoProy"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    MiFlujoProy = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Anio = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    descripcion = Column(String(150), nullable=False)
    Enero = Column(Numeric(18, 6), nullable=False)
    Febrero = Column(Numeric(18, 6), nullable=False)
    Marzo = Column(Numeric(18, 6), nullable=False)
    Abril = Column(Numeric(18, 6), nullable=False)
    Mayo = Column(Numeric(18, 6), nullable=False)
    Junio = Column(Numeric(18, 6), nullable=False)
    Julio = Column(Numeric(18, 6), nullable=False)
    Agosto = Column(Numeric(18, 6), nullable=False)
    Septiembre = Column(Numeric(18, 6), nullable=False)
    Octubre = Column(Numeric(18, 6), nullable=False)
    Noviembre = Column(Numeric(18, 6), nullable=False)
    Diciembre = Column(Numeric(18, 6), nullable=False)
    TipoFlujo = Column(Integer, nullable=False)
    nocuenta = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Miflujoproy(MiFlujoProy={self.MiFlujoProy})>"