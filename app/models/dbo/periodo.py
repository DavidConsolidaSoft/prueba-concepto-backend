# Generado automáticamente
# Tabla: dbo.periodo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Periodo(Base):
    __tablename__ = "periodo"
    __table_args__ = {"schema": "dbo"}

    fechaini = Column(DateTime)
    fechafin = Column(DateTime)
    mesesmas = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    liqgtoing = Column(Boolean, nullable=False)
    periodo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Periodo(periodo={self.periodo})>"