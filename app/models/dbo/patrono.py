# Generado automáticamente
# Tabla: dbo.patrono
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Patrono(Base):
    __tablename__ = "patrono"
    __table_args__ = {"schema": "dbo"}

    npatrono = Column(String(50), nullable=False)
    numpatro = Column(String(50))
    nacional = Column(Integer)
    direccion = Column(String(50))
    telefon1 = Column(String(15))
    telefon2 = Column(String(15))
    nomtraba = Column(String(50))
    nit = Column(String(50))
    numiva = Column(String(50))
    giro = Column(Integer)
    dirtraba = Column(String(50))
    municip = Column(Integer)
    depto = Column(Integer)
    pais = Column(Integer)
    teltrab1 = Column(Numeric(8, 0))
    teltrab2 = Column(Numeric(8, 0))
    fax = Column(String(25))
    tipo = Column(String(50))
    activo = Column(Boolean, nullable=False)
    patrono = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)

    def __repr__(self):
        return "<Patrono(patrono={self.patrono})>"