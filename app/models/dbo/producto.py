# Generado automáticamente
# Tabla: dbo.producto
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Producto(Base):
    __tablename__ = "producto"
    __table_args__ = {"schema": "dbo"}

    nproducto = Column(String(100), nullable=False)
    otroname = Column(String(1000))
    activo = Column(Boolean, nullable=False)
    controla = Column(Boolean, nullable=False)
    bonificado = Column(Boolean, nullable=False)
    vineta = Column(Boolean, nullable=False)
    enventa = Column(Boolean, nullable=False)
    incluir = Column(Boolean, nullable=False)
    fabricar = Column(Boolean, nullable=False)
    exento = Column(Boolean, nullable=False)
    desccontado = Column(Boolean, nullable=False)
    parte = Column(Boolean, nullable=False)
    servicios = Column(Boolean, nullable=False)
    tipoprod = Column(Integer, nullable=False)
    categori = Column(Integer, nullable=False)
    umedida = Column(Integer, nullable=False)
    presenta = Column(Integer, nullable=False)
    casaprod = Column(Integer, nullable=False)
    costo = Column(Numeric(16, 6), nullable=False)
    cantidadreor = Column(Numeric(16, 6), nullable=False)
    minimo = Column(Numeric(16, 6), nullable=False)
    cantidadcompra = Column(Numeric(16, 6), nullable=False)
    compraminima = Column(Numeric(16, 6), nullable=False)
    compramaxima = Column(Numeric(16, 6), nullable=False)
    promedio = Column(Numeric(16, 6), nullable=False)
    promlicitacionexport = Column(Numeric(16, 6), nullable=False)
    promedioexportacion = Column(Numeric(16, 6), nullable=False)
    promlicitacion = Column(Numeric(16, 6), nullable=False)
    codbarra = Column(String(25), nullable=False)
    icdbarra = Column(String(25), nullable=False)
    producto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    peso = Column(Numeric(16, 6), nullable=False)
    condicion1 = Column(Boolean, nullable=False)
    recargo = Column(Boolean, nullable=False)
    cicloanterior = Column(Boolean, nullable=False)
    vvineta = Column(Numeric(16, 6), nullable=False)
    mformula = Column(Integer, nullable=False)
    sretencion = Column(Boolean)
    condicion2 = Column(Boolean, nullable=False)
    indicador = Column(Integer, nullable=False)
    estatus = Column(Integer, nullable=False)
    dispensador = Column(Boolean, nullable=False)
    codblister = Column(String(25), nullable=False)
    noblister = Column(Integer, nullable=False)
    nosujeto = Column(Boolean, nullable=False)
    cuenta = Column(Integer, nullable=False)
    BODEGA = Column(Integer, nullable=False)
    PRODPREC = Column(Integer, nullable=False)
    TPRECIO = Column(Numeric(18, 6), nullable=False)
    FPRECIO = Column(Numeric(18, 6), nullable=False)
    Cargofull = Column(Boolean, nullable=False)
    marchamo = Column(Boolean, nullable=False)
    viajecompleto = Column(Boolean, nullable=False)
    combustible = Column(Boolean, nullable=False)
    repuesto = Column(Boolean, nullable=False)
    produccion = Column(Boolean, nullable=False)
    ActivoFijo = Column(Boolean, nullable=False)
    CostoTipo = Column(Integer, nullable=False)
    CategoriaBien = Column(Integer, nullable=False)
    batch = Column(Numeric(18, 6), nullable=False)
    factor1 = Column(Numeric(18, 6), nullable=False)
    umedida1 = Column(Integer, nullable=False)
    taller = Column(Boolean, nullable=False)
    miImagen = Column(String(250), nullable=False)
    volumen = Column(Numeric(18, 6), nullable=False)
    TipoEscala = Column(Integer, nullable=False)
    miColor = Column(Integer, nullable=False)
    controlado = Column(Boolean, nullable=False)
    sexo = Column(Integer, nullable=False)
    estilo = Column(Integer, nullable=False)
    maximo = Column(Numeric(18, 6), nullable=False)
    clase = Column(Integer, nullable=False)
    temporada = Column(Integer, nullable=False)
    fabricacion = Column(Integer, nullable=False)
    envio = Column(Integer, nullable=False)
    deTemporada = Column(Boolean, nullable=False)
    feature01 = Column(String(25), nullable=False)
    feature02 = Column(String(25), nullable=False)
    feature03 = Column(String(25), nullable=False)
    orden = Column(String(3))
    pingreso = Column(Boolean, nullable=False)
    fila = Column(Integer, nullable=False)
    columna = Column(Integer, nullable=False)
    hproduccion = Column(Numeric(18, 6), nullable=False)
    diasvence = Column(Integer, nullable=False)
    showroom = Column(Boolean, nullable=False)
    talla = Column(Numeric(5, 2), nullable=False)
    tallau = Column(Numeric(5, 2), nullable=False)
    tallak = Column(Numeric(5, 2), nullable=False)
    parte1 = Column(Boolean, nullable=False)
    cocina = Column(Boolean, nullable=False)
    mibar = Column(Boolean, nullable=False)
    apdesc = Column(Boolean, nullable=False)

    # Relaciones
    # casaprod_rel = relationship("Casaprod", back_populates="producto_set")  # Comentado automáticamente
    # categori_rel = relationship("Categori", back_populates="producto_set")  # Comentado automáticamente
    # presenta_rel = relationship("Presenta", back_populates="producto_set")  # Comentado automáticamente
    # tipoprod_rel = relationship("Tipoprod", back_populates="producto_set")  # Comentado automáticamente
    # umedida_rel = relationship("Umedida", back_populates="producto_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Producto(producto={self.producto})>"