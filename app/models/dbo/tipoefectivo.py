# Generado automáticamente
# Tabla: dbo.TipoEfectivo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Tipoefectivo(Base):
    __tablename__ = "TipoEfectivo"
    __table_args__ = {"schema": "dbo"}

    valor = Column(Numeric(18, 6), nullable=False)
    TipoEfectivo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    pais = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipoefectivo(TipoEfectivo={self.TipoEfectivo})>"