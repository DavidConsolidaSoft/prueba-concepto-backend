# Generado automáticamente
# Tabla: dbo.cxp
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Date
from sqlalchemy import Column, Float
from sqlalchemy import Column, String


class Cxp(Base):
    __tablename__ = "cxp"
    __table_args__ = {"schema": "dbo"}

    fecha = Column(Date)
    debe = Column(Float,primary_key=True)
    haber = Column(Float)
    cdebe = Column(Float)
    cmonto = Column(Float)
    chaber = Column(Float)
    nopartida = Column(String(15))
    noquedan = Column(String(15))
    nocheque = Column(String(15))
    fecha2 = Column(Date)
    debe2 = Column(Float)
    haber2 = Column(Float)
    cdebe2 = Column(Float)
    cmonto2 = Column(Float)
    chaber2 = Column(Float)
    nopartida2 = Column(String(15))
    noquedan2 = Column(String(15))
    nocheque2 = Column(String(15))
    abono = Column(Float)

    def __repr__(self):
        return "<Cxp(fecha={self.fecha})>"