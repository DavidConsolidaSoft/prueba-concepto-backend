# Generado automáticamente
# Tabla: dbo.PerfilUsuario
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Perfilusuario(Base):
    __tablename__ = "PerfilUsuario"
    __table_args__ = {"schema": "dbo"}

    PerfilUsuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nPerfilUsuario = Column(String(35), nullable=False)
    supervisor = Column(Boolean, nullable=False)
    notas = Column(String(250), nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    nivel = Column(Integer, nullable=False)
    uno = Column(Boolean, nullable=False)
    dos = Column(Boolean, nullable=False)
    tres = Column(Boolean, nullable=False)
    cuatro = Column(Boolean, nullable=False)
    cinco = Column(Boolean, nullable=False)
    seis = Column(Boolean, nullable=False)
    siete = Column(Boolean, nullable=False)
    ocho = Column(Boolean, nullable=False)
    nueve = Column(Boolean, nullable=False)
    diez = Column(Boolean, nullable=False)
    veCostos = Column(Boolean, nullable=False)
    puedeBackup = Column(Boolean, nullable=False)
    PuedePrecio = Column(Boolean, nullable=False)
    puedepermiso = Column(Boolean, nullable=False)
    conta1 = Column(Boolean, nullable=False)
    conta2 = Column(Boolean, nullable=False)
    conta3 = Column(Boolean, nullable=False)
    conta4 = Column(Boolean, nullable=False)
    conta5 = Column(Boolean, nullable=False)
    conta6 = Column(Boolean, nullable=False)
    vecxc = Column(Boolean, nullable=False)
    puedecantidad = Column(Boolean, nullable=False)
    saltaPrecio = Column(Boolean, nullable=False)
    superventas = Column(Boolean, nullable=False)
    precio1 = Column(Boolean, nullable=False)
    precio2 = Column(Boolean, nullable=False)
    precio3 = Column(Boolean, nullable=False)
    precio4 = Column(Boolean, nullable=False)
    precio5 = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Perfilusuario(PerfilUsuario={self.PerfilUsuario})>"