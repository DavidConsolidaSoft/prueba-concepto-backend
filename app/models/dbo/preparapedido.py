# Generado automáticamente
# Tabla: dbo.PreparaPedido
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Preparapedido(Base):
    __tablename__ = "PreparaPedido"
    __table_args__ = {"schema": "dbo"}

    PreparaPedido = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    Prioridad = Column(Integer)
    fecha = Column(DateTime)
    factura = Column(Integer)
    bodeguero = Column(Integer)
    rupStatus = Column(Integer)
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)
    notas = Column(String(250))
    cambodega = Column(Integer, nullable=False)
    preparar = Column(Boolean, nullable=False)
    Preparado = Column(Boolean, nullable=False)
    bultos = Column(Integer, nullable=False)
    terminarpedido = Column(DateTime)
    prepararpedido = Column(DateTime)

    def __repr__(self):
        return "<Preparapedido(PreparaPedido={self.PreparaPedido})>"