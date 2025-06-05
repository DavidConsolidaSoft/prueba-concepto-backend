# Generado automáticamente
# Tabla: dbo.lecturabanco
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Lecturabanco(Base):
    __tablename__ = "lecturabanco"
    __table_args__ = {"schema": "dbo"}

    datobanco = Column(String(140))
    Lectura = Column(String(84))
    FechaBanco = Column(DateTime)
    fechaLectura = Column(DateTime)
    MontoBanco = Column(Numeric(18, 6))
    MontoLectura = Column(Numeric(18, 6))
    Diferencia = Column(Numeric(19, 6))
    carnet = Column(String(25))
    factura = Column(Integer)
    impresa = Column(Boolean)
    pagos = Column(Integer)
    lecturabanco = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Lecturabanco(lecturabanco={self.lecturabanco})>"