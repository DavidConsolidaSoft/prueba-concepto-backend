# Generado automáticamente
# Tabla: dbo.ccosto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Date
from sqlalchemy import Column, String


class Ccosto(Base):
    __tablename__ = "ccosto"
    __table_args__ = {"schema": "dbo"}

    nopartida = Column(String(25),primary_key=True)
    fecha = Column(Date)
    noctrocosto = Column(String(25))
    nocuenta = Column(String(25))

    def __repr__(self):
        return "<Ccosto(nopartida={self.nopartida})>"