# Generado automáticamente
# Tabla: dbo.infobanco
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Infobanco(Base):
    __tablename__ = "infobanco"
    __table_args__ = {"schema": "dbo"}

    infobanco = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    contenido = Column(String(140), nullable=False)
    vendedor = Column(Integer, nullable=False)
    codbarra = Column(String(82), nullable=False)
    fecha = Column(DateTime, nullable=False)
    monto = Column(Numeric(18, 2), nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Infobanco(infobanco={self.infobanco})>"