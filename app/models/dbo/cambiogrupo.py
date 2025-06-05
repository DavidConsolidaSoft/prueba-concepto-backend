# Generado automáticamente
# Tabla: dbo.cambiogrupo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cambiogrupo(Base):
    __tablename__ = "cambiogrupo"
    __table_args__ = {"schema": "dbo"}

    grupo = Column(Integer, nullable=False)
    descripcion = Column(String(100), nullable=False)
    empleado = Column(Integer, nullable=False)
    cambiogrupo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    fechacambio = Column(DateTime, nullable=False)
    grupo2 = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Cambiogrupo(cambiogrupo={self.cambiogrupo})>"