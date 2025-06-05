# Generado automáticamente
# Tabla: dbo.HistoricoNomina
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Historiconomina(Base):
    __tablename__ = "HistoricoNomina"
    __table_args__ = {"schema": "dbo"}

    HistoricoNomina = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    categoriaNomina = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    empleado = Column(Integer, nullable=False)
    fHistoricoNomina = Column(String(250), nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Historiconomina(HistoricoNomina={self.HistoricoNomina})>"