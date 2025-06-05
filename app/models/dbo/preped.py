# Generado automáticamente
# Tabla: dbo.prePed
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Preped(Base):
    __tablename__ = "prePed"
    __table_args__ = {"schema": "dbo"}

    numedocu = Column(String(9))
    fecha = Column(DateTime)
    Notas = Column(String(125))
    au1 = Column(Integer)
    au2 = Column(Integer)
    au3 = Column(Integer)
    au4 = Column(Integer)
    b1 = Column(Integer)
    b2 = Column(Integer)
    caja1 = Column(Integer)
    caja2 = Column(Integer)
    impresa = Column(Boolean, nullable=False)
    nula = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    prePed = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Preped(prePed={self.prePed})>"