# Generado automáticamente
# Tabla: dbo.controlcorrel
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Controlcorrel(Base):
    __tablename__ = "controlcorrel"
    __table_args__ = {"schema": "dbo"}

    correl = Column(Integer, nullable=False)
    qmin = Column(Integer, nullable=False)
    qmax = Column(Integer, nullable=False)
    ingreso = Column(Boolean, nullable=False)
    salida = Column(Boolean, nullable=False)
    notacredito = Column(Boolean, nullable=False)
    notadebito = Column(Boolean, nullable=False)
    pagos = Column(Boolean, nullable=False)
    docunico = Column(Boolean, nullable=False)
    nconcepto = Column(String(25), nullable=False)
    controlcorrel = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    horatiempo = Column(DateTime)
    empresa = Column(Integer)
    usuario = Column(Integer)
    activo = Column(Boolean)
    ventas = Column(Boolean, nullable=False)
    warningcorrel = Column(Integer, nullable=False)
    fwarning = Column(DateTime)
    produccion = Column(Boolean, nullable=False)
    empaque = Column(Boolean, nullable=False)
    Taller = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Controlcorrel(controlcorrel={self.controlcorrel})>"