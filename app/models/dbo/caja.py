# Generado automáticamente
# Tabla: dbo.caja
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Caja(Base):
    __tablename__ = "caja"
    __table_args__ = {"schema": "dbo"}

    caja = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ncaja = Column(String(35), nullable=False)
    EQUIPO = Column(String(50), nullable=False)
    Corrf = Column(Integer, nullable=False)
    MaximoF = Column(Integer, nullable=False)
    CorrC = Column(Integer, nullable=False)
    MaximoC = Column(Integer, nullable=False)
    CorrP = Column(Integer, nullable=False)
    MaximoP = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    CorrT = Column(Integer, nullable=False)
    MaximoT = Column(Integer, nullable=False)
    controlcorrel = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    controlbodega = Column(Boolean, nullable=False)
    controlcorrelnc = Column(Integer, nullable=False)
    sucursal = Column(Integer, nullable=False)
    vendedor = Column(Integer, nullable=False)
    corrnc = Column(Integer, nullable=False)
    controlsucursal = Column(Boolean, nullable=False)
    puntoventa = Column(Boolean, nullable=False)
    prodprec = Column(Integer, nullable=False)
    micaja = Column(Integer, nullable=False)
    puedeImprimir = Column(Boolean, nullable=False)
    MUESTRAEXIST = Column(Boolean, nullable=False)
    clientes = Column(String(25), nullable=False)
    ingreso = Column(Integer, nullable=False)
    salida = Column(Integer, nullable=False)
    cambodega = Column(Integer, nullable=False)
    ctrocosto = Column(Integer, nullable=False)
    prodprec2 = Column(Integer, nullable=False)
    notaremision = Column(Integer, nullable=False)
    supervisor = Column(Boolean, nullable=False)
    serialprinter = Column(String(25), nullable=False)
    puerto = Column(String(5), nullable=False)
    cashdrawer = Column(Boolean, nullable=False)
    soloImprime = Column(Boolean, nullable=False)
    REGMOSTRADOS = Column(Integer, nullable=False)
    notacredito = Column(Integer, nullable=False)
    notadebito = Column(Integer, nullable=False)
    impf = Column(String(100), nullable=False)
    impc = Column(String(100), nullable=False)
    impt = Column(String(100), nullable=False)
    bodegaConsigna = Column(Integer, nullable=False)
    cocina = Column(Boolean, nullable=False)
    mibar = Column(Boolean, nullable=False)
    abono = Column(Integer, nullable=False)
    pedido = Column(Integer, nullable=False)
    lotengo = Column(Boolean, nullable=False)
    corrno = Column(Integer, nullable=False)
    calculosiniva = Column(Boolean, nullable=False)
    ventadiferida = Column(Boolean, nullable=False)
    correxp = Column(Integer, nullable=False)
    corrotro = Column(Integer, nullable=False)
    ocompra = Column(Integer)
    esmostrador = Column(Boolean, nullable=False)
    variaspc = Column(Boolean, nullable=False)
    compra = Column(Integer, nullable=False)
    micorr = Column(Integer, nullable=False)
    devnc = Column(Integer, nullable=False)
    offline = Column(Boolean)
    precioconIva = Column(Boolean)

    def __repr__(self):
        return "<Caja(caja={self.caja})>"