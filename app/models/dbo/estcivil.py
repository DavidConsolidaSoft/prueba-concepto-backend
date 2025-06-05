# Generado automáticamente
# Tabla: dbo.estcivil
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Estcivil(Base):
    __tablename__ = "estcivil"
    __table_args__ = {"schema": "dbo"}

    nestcivil = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    estcivil = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    simbolo = Column(String(1), nullable=False)

    def __repr__(self):
        return "<Estcivil(estcivil={self.estcivil})>"