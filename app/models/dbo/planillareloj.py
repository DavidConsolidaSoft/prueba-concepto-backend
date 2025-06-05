# Generado automáticamente
# Tabla: dbo.planillareloj
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Planillareloj(Base):
    __tablename__ = "planillareloj"
    __table_args__ = {"schema": "dbo"}

    empleado = Column(Integer, nullable=False)
    codreloj = Column(String(25), nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipodia = Column(String(50), nullable=False)
    horario = Column(Integer, nullable=False)
    horaentrada = Column(String(25))
    horasalida = Column(String(25))
    horasnormal = Column(Numeric(18, 6))
    horasxtras = Column(Numeric(18, 6))
    montohnormal = Column(Numeric(18, 6))
    montohxtras = Column(Numeric(18, 6))
    denegado = Column(Boolean, nullable=False)
    enfirme = Column(Boolean, nullable=False)
    planillareloj = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    usuarioautoriza = Column(Integer)
    fechaautoriza = Column(DateTime)
    heantesentrada = Column(Numeric(18, 6), nullable=False)
    hedespuessalida = Column(Numeric(18, 6), nullable=False)
    cambienhn = Column(Boolean, nullable=False)
    cambienhe = Column(Boolean, nullable=False)
    jornada = Column(Integer, nullable=False)
    reloj = Column(Integer)

    def __repr__(self):
        return "<Planillareloj(planillareloj={self.planillareloj})>"