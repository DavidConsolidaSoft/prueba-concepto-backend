# Generado automáticamente
# Tabla: dbo.repo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Repo(Base):
    __tablename__ = "repo"
    __table_args__ = {"schema": "dbo"}

    nrepo = Column(String(25))
    nprinter = Column(String(150))
    fuente = Column(String(35))
    cabeza = Column(Boolean)
    pie = Column(Boolean)
    alto = Column(Boolean)
    campo = Column(String(150))
    vpos = Column(Numeric(9, 5))
    hpos = Column(Numeric(9, 5))
    ancho = Column(Numeric(9, 5))
    mascara = Column(String(9))
    repoid = Column(String(35))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    repo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    otipo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Repo(repo={self.repo})>"