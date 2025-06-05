# Generado automáticamente
# Tabla: dbo.razoncuenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer


class Razoncuenta(Base):
    __tablename__ = "razoncuenta"
    __table_args__ = {"schema": "dbo"}

    activocirculante = Column(Boolean, nullable=False)
    pasivocirculante = Column(Boolean, nullable=False)
    inventario = Column(Boolean, nullable=False)
    costoventa = Column(Boolean, nullable=False)
    cuentasxcobrar = Column(Boolean, nullable=False)
    cuentasxpagar = Column(Boolean, nullable=False)
    ventas = Column(Boolean, nullable=False)
    devventas = Column(Boolean, nullable=False)
    activostotales = Column(Boolean, nullable=False)
    pasivostotales = Column(Boolean, nullable=False)
    pasivolargoplazo = Column(Boolean, nullable=False)
    capitalsocial = Column(Boolean, nullable=False)
    ingresofinanciero = Column(Boolean, nullable=False)
    oingresosnograv = Column(Boolean, nullable=False)
    ogastosnodeduc = Column(Boolean, nullable=False)
    gastosoperacion = Column(Boolean, nullable=False)
    gastosventa = Column(Boolean, nullable=False)
    gastosadmon = Column(Boolean, nullable=False)
    gastosfinan = Column(Boolean, nullable=False)
    otrosingresos = Column(Boolean, nullable=False)
    otrosgastos = Column(Boolean, nullable=False)
    utilidad = Column(Boolean, nullable=False)
    reservacapital = Column(Boolean, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    razoncuenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    cuenta = Column(Integer, nullable=False)
    interes = Column(Boolean, nullable=False)
    efectivo = Column(Boolean)

    def __repr__(self):
        return "<Razoncuenta(razoncuenta={self.razoncuenta})>"