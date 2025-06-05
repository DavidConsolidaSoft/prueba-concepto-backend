# Generado automáticamente
# Tabla: dbo.anivel
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Anivel(Base):
    __tablename__ = "anivel"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    nanivel = Column(String(35), nullable=False)
    nomiembros = Column(Integer, nullable=False)
    orden = Column(String(1), nullable=False)
    porctje = Column(Numeric(4, 2), nullable=False)
    compramin = Column(Numeric(15, 6), nullable=False)
    acompramin = Column(Numeric(15, 6), nullable=False)
    montobono = Column(Numeric(15, 6), nullable=False)
    nivel1 = Column(Boolean, nullable=False)
    nivel2 = Column(Boolean, nullable=False)
    topacio = Column(Boolean, nullable=False)
    zafiro = Column(Boolean, nullable=False)
    esmeralda = Column(Boolean, nullable=False)
    anivel = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    membresia = Column(Boolean, nullable=False)
    bono = Column(Boolean)

    def __repr__(self):
        return "<Anivel(anivel={self.anivel})>"