# Generado automáticamente
# Tabla: dbo.tipoVehiculo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Tipovehiculo(Base):
    __tablename__ = "tipoVehiculo"
    __table_args__ = {"schema": "dbo"}

    nTipoVehiculo = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    TipoVehiculo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Tipovehiculo(TipoVehiculo={self.TipoVehiculo})>"