# Generado automáticamente
# Tabla: dbo.dtranspte
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Dtranspte(Base):
    __tablename__ = "dtranspte"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    fecha = Column(DateTime, nullable=False)
    numedocu = Column(String(10))
    transpte = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    impresa = Column(Boolean, nullable=False)
    tdespacho = Column(Integer, nullable=False)
    dtranspte = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    entregada = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    bultos = Column(Integer, nullable=False)
    imprimir = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Dtranspte(dtranspte={self.dtranspte})>"