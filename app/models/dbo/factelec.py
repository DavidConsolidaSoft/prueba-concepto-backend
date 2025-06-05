# Generado automáticamente
# Tabla: dbo.factElec
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class FactElec(Base):
    __tablename__ = "factElec"
    __table_args__ = {"schema": "dbo"}

    factura = Column(Integer, nullable=False)
    uuid = Column(String(45), nullable=False)
    serie = Column(String(15), nullable=False)
    numero = Column(String(40))
    factelec = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pagos = Column(Integer, nullable=False)
    lafecha = Column(DateTime)
    compra = Column(Integer)
    remision = Column(Integer)
    retencion = Column(Integer)
    conting = Column(Integer)
    invalida = Column(Integer)
    fhProcesamiento = Column(DateTime)
    sellorecibido = Column(String(100))
    eljson = Column(String)
    factnew = Column(Integer)
    contingencia = Column(Integer)
    contingenvio = Column(Integer)
    anulacion = Column(Integer)
    anulada = Column(Integer)
    _correo = Column(String(35))
    _clave = Column(String(35))
    donacion = Column(Boolean, nullable=False)
    almacen = Column(Integer)
    exclunula = Column(Integer)
    donanula = Column(Integer)
    retennula = Column(Integer)
    exponula = Column(Integer)
    reminula = Column(Integer)
    ppagos = Column(Integer)
    ncreten_nula = Column(Integer)

    def __repr__(self):
        return "<Factelec(factelec={self.factelec})>"