# Generado automáticamente
# Tabla: dbo.tablacomisiones
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Tablacomisiones(Base):
    __tablename__ = "tablacomisiones"
    __table_args__ = {"schema": "dbo"}

    tipovendedor = Column(Integer, nullable=False)
    condpago = Column(Integer, nullable=False)
    porcentaje = Column(Numeric(18, 6), nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    tablacomisiones = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tablacomisiones(tablacomisiones={self.tablacomisiones})>"