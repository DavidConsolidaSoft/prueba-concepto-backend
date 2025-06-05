# Generado automáticamente
# Tabla: dbo.cintaAuditoria
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cintaauditoria(Base):
    __tablename__ = "cintaAuditoria"
    __table_args__ = {"schema": "dbo"}

    qfecha2 = Column(DateTime)
    pmicaja = Column(Integer)
    valor = Column(Integer)
    reporte = Column(Integer)
    horaImpresion = Column(DateTime)
    qusuario = Column(Integer)
    cintaAuditoria = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    CORREL = Column(String(12), nullable=False)

    def __repr__(self):
        return "<Cintaauditoria(qfecha2={self.qfecha2})>"