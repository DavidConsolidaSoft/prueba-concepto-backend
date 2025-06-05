# Generado automáticamente
# Tabla: dbo.RupStandar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Rupstandar(Base):
    __tablename__ = "RupStandar"
    __table_args__ = {"schema": "dbo"}

    nRupStandar = Column(String(10))
    HorasStandar = Column(Numeric(9, 2), nullable=False)
    Activo = Column(Boolean, nullable=False)
    RupStandar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Rupstandar(RupStandar={self.RupStandar})>"