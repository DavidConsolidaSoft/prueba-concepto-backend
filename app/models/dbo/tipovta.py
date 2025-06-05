# Generado automáticamente
# Tabla: dbo.tipovta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class TipoVta(Base):
    __tablename__ = "tipovta"
    __table_args__ = {"schema": "dbo"}

    ntipovta = Column(String(40), nullable=False)
    activo = Column(Boolean, nullable=False)
    otra = Column(Boolean, nullable=False)
    normal = Column(Boolean, nullable=False)
    exportacion = Column(Boolean, nullable=False)
    licitacion = Column(Boolean, nullable=False)
    informe = Column(String(25), nullable=False)
    tipovta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    hora1 = Column(String(8), nullable=False)
    hora2 = Column(String(8), nullable=False)

    def __repr__(self):
        return "<Tipovta(tipovta={self.tipovta})>"