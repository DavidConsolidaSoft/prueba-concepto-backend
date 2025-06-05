# Generado automáticamente
# Tabla: dbo.dalmacennc
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dalmacennc(Base):
    __tablename__ = "dalmacennc"
    __table_args__ = {"schema": "dbo"}

    dalmacen = Column(Integer)
    descuento = Column(Numeric(9, 2))
    fecha = Column(DateTime)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    dalmacennc = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Dalmacennc(dalmacennc={self.dalmacennc})>"