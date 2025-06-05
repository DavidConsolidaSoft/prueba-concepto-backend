# Generado automáticamente
# Tabla: dbo.controlvineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Controlvineta(Base):
    __tablename__ = "controlvineta"
    __table_args__ = {"schema": "dbo"}

    dfactura = Column(Integer, nullable=False)
    vvineta = Column(Numeric(18, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    danoimpresa = Column(Boolean, nullable=False)
    danopegado = Column(Boolean, nullable=False)
    contador = Column(Integer, nullable=False)
    bobina = Column(Integer, nullable=False)
    impresa = Column(Boolean, nullable=False)
    facturanula = Column(Boolean, nullable=False)
    controlvineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Controlvineta(controlvineta={self.controlvineta})>"