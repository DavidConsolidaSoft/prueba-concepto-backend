# Generado automáticamente
# Tabla: dbo.miempleado
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Miempleado(Base):
    __tablename__ = "miempleado"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    codigo = Column(Integer)
    Nombres = Column(String(255))
    Apellidos = Column(String(255))
    NombresegunISSS = Column(String(255))
    Dirección = Column(String(255))
    Telcasamovil = Column(Numeric(18, 0))
    TelMovil = Column(Numeric(18, 0))
    TipoSangre = Column(String(255))
    Sexo = Column(String(255))
    Nacionalidad = Column(String(255))
    Profesión = Column(String(255))
    LugarNac = Column(String(255))
    Email = Column(String(255))
    FechaIngreso = Column(DateTime)
    FechaVcto = Column(String(255))
    Departamento = Column(String(255))
    Cargo = Column(String(255))
    Jornada = Column(String(255))
    Plaza = Column(String(255))
    SalarioMes = Column(Numeric(19, 4))
    FmaPago = Column(String(255))
    NoISSS = Column(String(255))
    AFP = Column(String(255))
    NoAFP = Column(Numeric(18, 0))
    DUI = Column(String(255))
    NIT = Column(String(255))
    PASAPORTE = Column(String(255))

    def __repr__(self):
        return "<Miempleado(codigo={self.codigo})>"