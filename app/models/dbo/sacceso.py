# Generado automáticamente
# Tabla: dbo.sacceso
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Sacceso(Base):
    __tablename__ = "sacceso"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    voriginal = Column(Numeric(18, 6), nullable=False)
    vnuevo = Column(Numeric(18, 6), nullable=False)
    idtabla = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    caccesos = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    encargado = Column(Integer, nullable=False)
    tabla = Column(String(12), nullable=False)
    notas = Column(String(300))
    sacceso = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    numedocu = Column(String(15), nullable=False)
    archivo = Column(String(35), nullable=False)
    documento = Column(String(15), nullable=False)
    hoy = Column(DateTime, nullable=False)
    equipo = Column(String(25), nullable=False)
    nivel = Column(Integer, nullable=False)
    tpermiso = Column(Boolean, nullable=False)
    porcentaje = Column(Numeric(18, 6), nullable=False)
    suPorcent = Column(Numeric(18, 6), nullable=False)
    dNotas = Column(String(100), nullable=False)
    didTabla = Column(Integer, nullable=False)
    ausuario = Column(Integer, nullable=False)
    ahora = Column(DateTime)
    anulada = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Sacceso(activo={self.activo})>"