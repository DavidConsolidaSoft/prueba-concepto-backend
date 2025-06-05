# Generado automáticamente
# Tabla: dbo.compras
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Compras(Base):
    __tablename__ = "compras"
    __table_args__ = {"schema": "dbo"}

    periodoiva = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    nocheque = Column(String(25))
    numedocu = Column(String(45))
    proveedor = Column(Integer, nullable=False)
    moneda = Column(Integer, nullable=False)
    tasacambio = Column(Numeric(16, 6), nullable=False)
    tasacambioseg = Column(Numeric(16, 6), nullable=False)
    tasacambiotres = Column(Numeric(16, 6), nullable=False)
    excluido = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    importacion = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    retencion = Column(Numeric(16, 6), nullable=False)
    compras = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    otro = Column(Numeric(16, 6), nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    nProveedor = Column(String(70))
    nocuenta = Column(String(25), nullable=False)
    REGISTRO = Column(String(15), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    cotrans = Column(Numeric(18, 6), nullable=False)
    tipobodega = Column(Integer, nullable=False)
    percepcion = Column(Numeric(18, 6), nullable=False)
    partida = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    PAGOS = Column(Integer, nullable=False)
    idretencion = Column(Integer, nullable=False)
    importado = Column(Boolean, nullable=False)
    cuenta = Column(Integer)
    tipomov = Column(Integer)
    cuenta1 = Column(Integer)
    CESC = Column(Numeric(9, 2), nullable=False)
    serie = Column(String(15))
    pais = Column(Integer)
    servicio = Column(Integer, nullable=False)
    tipo = Column(Integer, nullable=False)
    clasificacion = Column(Integer, nullable=False)
    sector = Column(Integer, nullable=False)
    costo = Column(Integer, nullable=False)

    # Relaciones
    # periodoiva_rel = relationship("Periodoiva", back_populates="compras_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Compras(compras={self.compras})>"