# Generado automáticamente
# Tabla: dbo.anticipofactura
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Anticipofactura(Base):
    __tablename__ = "anticipofactura"
    __table_args__ = {"schema": "dbo"}

    anticipofactura = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    anticipos = Column(Integer, nullable=False)
    pagos = Column(Integer, nullable=False)
    monto = Column(Numeric(18, 6), nullable=False)
    fecha = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    usuario = Column(Integer, nullable=False)
    liquidada = Column(Boolean)

    def __repr__(self):
        return "<Anticipofactura(anticipofactura={self.anticipofactura})>"