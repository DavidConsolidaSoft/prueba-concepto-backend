# Generado automáticamente
# Tabla: dbo.docompra
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Docompra(Base):
    __tablename__ = "docompra"
    __table_args__ = {"schema": "dbo"}

    activo = Column(Boolean, nullable=False)
    cantidad = Column(Numeric(16, 6), nullable=False)
    reservado = Column(Numeric(16, 6), nullable=False)
    bonificado = Column(Numeric(16, 6), nullable=False)
    precio = Column(Numeric(16, 6), nullable=False)
    preciolist = Column(Numeric(16, 6), nullable=False)
    montfact = Column(Numeric(16, 6), nullable=False)
    afecta = Column(Numeric(16, 6), nullable=False)
    exenta = Column(Numeric(16, 6), nullable=False)
    viva = Column(Numeric(16, 6), nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    tax = Column(Numeric(16, 6), nullable=False)
    cprecio = Column(Numeric(16, 6), nullable=False)
    vtax = Column(Numeric(16, 6), nullable=False)
    gasto = Column(Numeric(16, 6), nullable=False)
    producto = Column(Integer, nullable=False)
    lote = Column(Integer, nullable=False)
    bodega = Column(Integer, nullable=False)
    ocompra = Column(Integer, nullable=False)
    compra = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    pdesc = Column(Numeric(16, 6), nullable=False)
    vdesc = Column(Numeric(16, 6), nullable=False)
    vgdesc = Column(Numeric(16, 6), nullable=False)
    fovial = Column(Numeric(16, 6), nullable=False)
    rcantidad = Column(Numeric(16, 6), nullable=False)
    rreservado = Column(Numeric(16, 6), nullable=False)
    rbonificado = Column(Numeric(16, 6), nullable=False)
    rprecio = Column(Numeric(16, 6), nullable=False)
    rmontfact = Column(Numeric(16, 6), nullable=False)
    rpdesc = Column(Numeric(16, 6), nullable=False)
    rvdesc = Column(Numeric(16, 6), nullable=False)
    ccantidad = Column(Numeric(16, 6), nullable=False)
    presenta = Column(Integer, nullable=False)
    docompra = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    unidades = Column(Numeric(16, 6), nullable=False)
    cbonificado = Column(Numeric(18, 6), nullable=False)
    linea = Column(Integer)
    fechaDespacho = Column(DateTime)
    fechaRecepcion = Column(DateTime)
    umedida = Column(Integer, nullable=False)
    ocantidad = Column(Numeric(18, 6), nullable=False)
    cusuario = Column(Integer, nullable=False)
    cenvio = Column(String(15), nullable=False)
    kardex = Column(Integer, nullable=False)
    original = Column(Numeric(18, 6), nullable=False)
    devolucion1 = Column(Numeric(18, 6), nullable=False)
    devolucion2 = Column(Numeric(18, 6), nullable=False)
    devolucion3 = Column(Numeric(18, 6), nullable=False)
    devolucion4 = Column(Numeric(18, 6), nullable=False)
    devolucion5 = Column(Numeric(18, 6), nullable=False)
    entrega1 = Column(Numeric(18, 6), nullable=False)
    entrega2 = Column(Numeric(18, 6), nullable=False)
    entrega3 = Column(Numeric(18, 6), nullable=False)
    entrega4 = Column(Numeric(18, 6), nullable=False)
    entrega5 = Column(Numeric(18, 6), nullable=False)
    nproducto = Column(String(100), nullable=False)
    peso = Column(Numeric(18, 6), nullable=False)
    minimo = Column(Numeric(18, 6), nullable=False)
    maximo = Column(Numeric(18, 6), nullable=False)
    miimagen = Column(String(250), nullable=False)
    tipoprod = Column(Integer, nullable=False)
    tipoescala = Column(Integer, nullable=False)
    micolor = Column(Integer, nullable=False)
    sexo = Column(Integer, nullable=False)
    clase = Column(Integer, nullable=False)
    temporada = Column(Integer, nullable=False)
    fabricacion = Column(Integer, nullable=False)
    casaprod = Column(Integer, nullable=False)
    categori = Column(Integer, nullable=False)
    envio = Column(Integer, nullable=False)
    icdbarra1 = Column(String(25), nullable=False)
    icdbarra2 = Column(String(25), nullable=False)
    icdbarra3 = Column(String(25), nullable=False)
    icdbarra4 = Column(String(25), nullable=False)
    icdbarra5 = Column(String(25), nullable=False)
    icdbarra6 = Column(String(25), nullable=False)
    icdbarra7 = Column(String(25), nullable=False)
    icdbarra8 = Column(String(25), nullable=False)
    tipoescala_cm3 = Column(Numeric(18, 6), nullable=False)
    recibido = Column(Boolean, nullable=False)
    vcantidad = Column(Numeric(18, 6), nullable=False)
    impuesto = Column(Numeric(18, 6), nullable=False)
    parancel = Column(Numeric(18, 6), nullable=False)
    arancel = Column(Numeric(18, 6), nullable=False)
    varancel = Column(Numeric(18, 6), nullable=False)
    crecinto = Column(Numeric(18, 6), nullable=False)
    m3 = Column(Numeric(18, 6), nullable=False)
    vcip = Column(Numeric(18, 6), nullable=False)

    def __repr__(self):
        return "<Docompra(docompra={self.docompra})>"