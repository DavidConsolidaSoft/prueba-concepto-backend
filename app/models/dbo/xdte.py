# Generado automáticamente
# Tabla: dbo.xdte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer, SmallInteger
from sqlalchemy import Column, String


class Xdte(Base):
    __tablename__ = "xdte"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    dte = Column(SmallInteger, nullable=False)
    ncatalogo = Column(String(50), nullable=False)
    catalogo = Column(String(50), nullable=False)
    scatalogo = Column(String(50), nullable=False)
    descripcion = Column(String(200), nullable=False)

    def __repr__(self):
        return "<Xdte(dte={self.dte})>"