# Generado automáticamente
# Tabla: dbo.autorizar
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, BigInteger
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Autorizar(Base):
    __tablename__ = "autorizar"
    __table_args__ = {"schema": "dbo"}

    autorizar = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    autorizo = Column(Integer, nullable=False)
    proceso = Column(Integer, nullable=False)
    fechasolicitud = Column(DateTime, nullable=False)
    fecharevision = Column(DateTime)
    autorizado = Column(Boolean, nullable=False)
    negado = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Autorizar(autorizar={self.autorizar})>"