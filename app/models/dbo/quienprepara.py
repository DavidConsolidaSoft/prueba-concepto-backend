# Generado automáticamente
# Tabla: dbo.quienprepara
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Quienprepara(Base):
    __tablename__ = "quienprepara"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer)
    cambodega = Column(Integer)
    fecha1 = Column(DateTime)
    fecha2 = Column(DateTime)
    fecha3 = Column(DateTime)
    bodeguero1 = Column(Integer)
    bodeguero2 = Column(Integer)
    quienprepara = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    bultos = Column(Integer)

    def __repr__(self):
        return "<Quienprepara(quienprepara={self.quienprepara})>"