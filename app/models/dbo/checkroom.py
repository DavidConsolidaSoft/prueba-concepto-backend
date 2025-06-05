# Generado automáticamente
# Tabla: dbo.checkroom
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Checkroom(Base):
    __tablename__ = "checkroom"
    __table_args__ = {"schema": "dbo"}

    checkroom = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    room = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    activo = Column(Boolean, nullable=False)
    horain = Column(String(5), nullable=False)
    horaout = Column(String(5), nullable=False)
    valor = Column(Numeric(16, 6), nullable=False)
    categori = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    vendedor1 = Column(Integer, nullable=False)
    rato = Column(Boolean, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Checkroom(checkroom={self.checkroom})>"