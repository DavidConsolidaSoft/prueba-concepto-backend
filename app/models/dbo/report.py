# Generado automáticamente
# Tabla: dbo.report
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Report(Base):
    __tablename__ = "report"
    __table_args__ = {"schema": "dbo"}

    nReport = Column(String(50), nullable=False)
    Activo = Column(Boolean, nullable=False)
    Report = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    sucursal = Column(Integer, nullable=False)
    manual = Column(Boolean, nullable=False)
    nprinter = Column(String(60))

    def __repr__(self):
        return "<Report(Report={self.Report})>"