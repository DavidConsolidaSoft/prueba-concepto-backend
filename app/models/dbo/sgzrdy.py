# Generado automáticamente
# Tabla: dbo.sgzrdy
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Sgzrdy(Base):
    __tablename__ = "sgzrdy"
    __table_args__ = {"schema": "dbo"}

    archivo = Column(String(35))
    hoy = Column(DateTime)
    caccesos = Column(Integer)
    equipo = Column(String(25))
    fecha = Column(DateTime)
    idTabla = Column(Integer)
    didTabla = Column(Integer)
    tabla = Column(String(15))
    nivel = Column(Integer)
    voriginal = Column(Numeric(18, 6))
    vNuevo = Column(Numeric(18, 6))
    usuario = Column(Integer)
    Notas = Column(String(350))
    dNotas = Column(String(100))
    tpermiso = Column(Boolean)
    Empresa = Column(Integer)
    porcentaje = Column(Numeric(18, 6))
    suporcent = Column(Numeric(18, 6))
    sgzrdy = Column(Integer,primary_key=True, nullable=False, autoincrement=True)

    def __repr__(self):
        return "<Sgzrdy(archivo={self.archivo})>"