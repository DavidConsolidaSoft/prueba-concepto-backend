# Generado automáticamente
# Tabla: dbo.dpreparar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Dpreparar(Base):
    __tablename__ = "dpreparar"
    __table_args__ = {"schema": "dbo"}

    dfactura = Column(Integer)
    fecha = Column(DateTime, nullable=False)
    dpreparar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    dcambodega = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Dpreparar(dpreparar={self.dpreparar})>"