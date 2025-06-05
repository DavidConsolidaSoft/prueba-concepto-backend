# Generado automáticamente
# Tabla: dbo.TipoEscala
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Tipoescala(Base):
    __tablename__ = "TipoEscala"
    __table_args__ = {"schema": "dbo"}

    TipoEscala = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nTipoEscala = Column(String(15), nullable=False)
    corridaz1 = Column(Numeric(4, 1), nullable=False)
    corridaz2 = Column(Numeric(4, 1), nullable=False)
    corridaz3 = Column(Numeric(4, 1), nullable=False)
    corridaz4 = Column(Numeric(4, 1), nullable=False)
    corridaz5 = Column(Numeric(4, 1), nullable=False)
    corridaz6 = Column(Numeric(4, 1), nullable=False)
    corridaz7 = Column(Numeric(4, 1), nullable=False)
    corridaz8 = Column(Numeric(4, 1), nullable=False)
    corridaA1 = Column(Integer, nullable=False)
    corridaA2 = Column(Integer, nullable=False)
    corridaA3 = Column(Integer, nullable=False)
    corridaA4 = Column(Integer, nullable=False)
    corridaA5 = Column(Integer, nullable=False)
    corridaA6 = Column(Integer, nullable=False)
    corridaA7 = Column(Integer, nullable=False)
    corridaA8 = Column(Integer, nullable=False)
    TotalEscala = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    subescala = Column(Boolean, nullable=False)
    tiposubescala = Column(Integer, nullable=False)
    tipo_uer = Column(Boolean, nullable=False)
    tipo_us = Column(Boolean, nullable=False)
    tipo_uk = Column(Boolean, nullable=False)
    sexo = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Tipoescala(TipoEscala={self.TipoEscala})>"