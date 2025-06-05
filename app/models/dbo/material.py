# Generado automáticamente
# Tabla: dbo.material
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Material(Base):
    __tablename__ = "material"
    __table_args__ = {"schema": "dbo"}

    nmaterial = Column(String(30))
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    material = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    producto = Column(Integer)
    cantidad = Column(Numeric(16, 6))
    rupot = Column(Integer)
    precio1 = Column(Numeric(18, 6))
    precio2 = Column(Numeric(18, 6))
    precio3 = Column(Numeric(18, 6))
    aprobado = Column(Integer)
    ocompra = Column(Integer)
    proveedor = Column(Integer)

    def __repr__(self):
        return "<Material(material={self.material})>"