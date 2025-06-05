# Generado automáticamente
# Tabla: dbo.idcaller
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Idcaller(Base):
    __tablename__ = "idcaller"
    __table_args__ = {"schema": "dbo"}

    idCaller = Column(Integer,primary_key=True, nullable=False, autoincrement=True)
    fecha = Column(DateTime)
    uFechaAcceso = Column(DateTime)
    Iprouter = Column(String(200))
    IpLocal = Column(String(100))
    IpRemota = Column(String(100))
    LocalHostName = Column(String(100))
    remoteHostName = Column(String(100))
    equipo = Column(String(60))
    registro = Column(String(200))
    valor = Column(String(200))
    activo = Column(Boolean)
    usuario = Column(Integer)
    empresa = Column(Integer)
    horatiempo = Column(DateTime)

    def __repr__(self):
        return "<Idcaller(idCaller={self.idCaller})>"