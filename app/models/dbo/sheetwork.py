# Generado automáticamente
# Tabla: dbo.sheetwork
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Sheetwork(Base):
    __tablename__ = "sheetwork"
    __table_args__ = {"schema": "dbo"}

    dia = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    empleado = Column(Integer, nullable=False)
    ingesp = Column(Integer, nullable=False)
    hingesp = Column(Integer, nullable=False)
    hnormal = Column(Numeric(18, 6), nullable=False)
    hextra = Column(Numeric(18, 6), nullable=False)
    presentada = Column(Boolean, nullable=False)
    liquidada = Column(Boolean, nullable=False)
    sheetwork = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    camion = Column(Integer, nullable=False)
    rutacamion = Column(Integer, nullable=False)
    jornada = Column(Integer, nullable=False)
    HED = Column(Integer, nullable=False)
    HEN = Column(Integer, nullable=False)
    estaller = Column(Boolean, nullable=False)

    # Relaciones
    # ingesp_rel = relationship("Ingesp", back_populates="sheetwork_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Sheetwork(sheetwork={self.sheetwork})>"