# Generado automáticamente
# Tabla: dbo.lecturabomba
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Lecturabomba(Base):
    __tablename__ = "lecturabomba"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(DateTime, nullable=False)
    bomba = Column(Integer, nullable=False)
    Producto = Column(Integer, nullable=False)
    valor = Column(Numeric(18, 6), nullable=False)
    galones = Column(Numeric(18, 6), nullable=False)
    lecturaBomba = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)

    def __repr__(self):
        return "<Lecturabomba(lecturaBomba={self.lecturaBomba})>"