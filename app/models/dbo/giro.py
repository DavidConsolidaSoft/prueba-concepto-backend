# Generado automáticamente
# Tabla: dbo.giro
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Giro(Base):
    __tablename__ = "giro"
    __table_args__ = {"schema": "dbo"}

    ngiro = Column(String(80), nullable=False)
    activo = Column(Boolean, nullable=False)
    giro = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Giro(ngiro={self.ngiro})>"