# Generado automáticamente
# Tabla: dbo.estado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Estado(Base):
    __tablename__ = "estado"
    __table_args__ = {"schema": "dbo"}

    estado = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nestado = Column(String(50), nullable=False)
    activo = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    preferido = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Estado(estado={self.estado})>"