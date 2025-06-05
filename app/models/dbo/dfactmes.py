# Generado automáticamente
# Tabla: dbo.dfactmes
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Dfactmes(Base):
    __tablename__ = "dfactmes"
    __table_args__ = {"schema": "dbo"}

    dfactura = Column(Integer, nullable=False)
    dregciclo = Column(Integer, nullable=False)
    mes = Column(DateTime)
    activo = Column(Boolean)
    dfactmes = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Dfactmes(dfactmes={self.dfactmes})>"