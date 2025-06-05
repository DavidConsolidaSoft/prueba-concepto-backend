# Generado automáticamente
# Tabla: dbo.modulo
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Modulo(Base):
    __tablename__ = "modulo"
    __table_args__ = {"schema": "dbo"}

    nmodulo = Column(String(30), nullable=False)
    activo = Column(Boolean, nullable=False)
    contabilidad = Column(Boolean, nullable=False)
    integracion = Column(Boolean, nullable=False)
    ventas = Column(Boolean, nullable=False)
    facturacion = Column(Boolean, nullable=False)
    planilla = Column(Boolean, nullable=False)
    produccion = Column(Boolean, nullable=False)
    ctascobrar = Column(Boolean, nullable=False)
    ctaspagar = Column(Boolean, nullable=False)
    compras = Column(Boolean, nullable=False)
    bancos = Column(Boolean, nullable=False)
    almacen = Column(Boolean, nullable=False)
    gerencia = Column(Boolean, nullable=False)
    manttogral = Column(Boolean, nullable=False)
    iva = Column(Boolean, nullable=False)
    enlace = Column(Boolean, nullable=False)
    controlproy = Column(Boolean, nullable=False)
    recons = Column(Boolean, nullable=False)
    cotiza = Column(Boolean, nullable=False)
    modulo = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    formulacion = Column(Boolean, nullable=False)
    mismanttos = Column(Boolean, nullable=False)
    controlCarga = Column(Boolean, nullable=False)
    manttosadmin = Column(Boolean, nullable=False)
    controlvence = Column(Boolean, nullable=False)
    controlhacienda = Column(Boolean, nullable=False)
    CONTROLMEDIOS = Column(Boolean, nullable=False)
    gestiontaller = Column(Integer, nullable=False)
    cocinabar = Column(Boolean, nullable=False)
    activofijo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Modulo(modulo={self.modulo})>"