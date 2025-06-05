# Generado automáticamente
# Tabla: dbo.office
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Office(Base):
    __tablename__ = "office"
    __table_args__ = {"schema": "dbo"}

    licencias = Column(Integer)
    noffice = Column(String(50))
    horatiempo = Column(DateTime, nullable=False)
    office = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    email = Column(String(40))
    col1 = Column(String(35))
    Col2 = Column(String(35))

    def __repr__(self):
        return "<Office(office={self.office})>"