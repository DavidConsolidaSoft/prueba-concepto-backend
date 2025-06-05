# Generado automáticamente
# Tabla: dbo.cuenta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship  # Comentado temporalmente


class Cuenta(Base):
    __tablename__ = "cuenta"
    __table_args__ = {"schema": "dbo"}

    nocuenta = Column(String(25), nullable=False)
    ncuenta = Column(String(70), nullable=False)
    nocheque = Column(String(10), nullable=False)
    miformato = Column(String(20), nullable=False)
    ctalong = Column(Integer, nullable=False)
    rubro = Column(Integer, nullable=False)
    banco = Column(Boolean, nullable=False)
    activo = Column(Boolean, nullable=False)
    cuenta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    proveedor = Column(Boolean, nullable=False)
    provbol = Column(Boolean, nullable=False)
    Iva = Column(Boolean, nullable=False)
    Ret = Column(Boolean, nullable=False)
    Excl = Column(Boolean, nullable=False)
    Fovial = Column(Boolean, nullable=False)
    Renta = Column(Boolean, nullable=False)
    factor = Column(Numeric(18, 6), nullable=False)
    debe = Column(Boolean, nullable=False)
    micheque = Column(String(15))
    AplicaRete = Column(Boolean, nullable=False)
    REGISTRO = Column(String(15), nullable=False)
    IMPORTACION = Column(Boolean, nullable=False)
    misformato = Column(String(20), nullable=False)
    cotrans = Column(Boolean)
    lineascheque = Column(Integer, nullable=False)
    nit = Column(String(17))
    giro = Column(String(50), nullable=False)
    razonsoc = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    sitioweb = Column(String(50), nullable=False)
    notas = Column(String(50), nullable=False)
    direccion = Column(String(200), nullable=False)
    PERCEPCION = Column(Boolean, nullable=False)
    CxCProveedor = Column(Boolean, nullable=False)
    cuentaCxC = Column(Integer, nullable=False)
    nivelGasto = Column(Boolean, nullable=False)
    telefono = Column(String(15), nullable=False)
    deduccion1 = Column(Boolean, nullable=False)
    deduccion2 = Column(Boolean, nullable=False)
    AplicaPercepcion = Column(Boolean, nullable=False)
    ActivoCirculante = Column(Boolean, nullable=False)
    ActivoFijo = Column(Boolean, nullable=False)
    PasivoCirculante = Column(Boolean, nullable=False)
    PasivoLargoPlazo = Column(Boolean, nullable=False)
    RubroProveedores = Column(Boolean, nullable=False)
    ObligacionesBancarias = Column(Boolean, nullable=False)
    ImpuestosxPagar = Column(Boolean, nullable=False)
    RubroBancos = Column(Boolean, nullable=False)
    CuentasxCobrar = Column(Boolean, nullable=False)
    Inventarios = Column(Boolean, nullable=False)
    Compras = Column(Boolean, nullable=False)
    RebajasyDevoluciones = Column(Boolean, nullable=False)
    GastosAdom = Column(Boolean, nullable=False)
    GastosVentas = Column(Boolean, nullable=False)
    GastosFinancieros = Column(Boolean, nullable=False)
    GastosOtros = Column(Boolean, nullable=False)
    GastosOperacion = Column(Boolean, nullable=False)
    RubroActivo = Column(Boolean, nullable=False)
    RubroPasivo = Column(Boolean, nullable=False)
    RubroCapital = Column(Boolean, nullable=False)
    RubroIngresos = Column(Boolean, nullable=False)
    RubroGastos = Column(Boolean, nullable=False)
    CostoVentas = Column(Boolean, nullable=False)
    ProductosFinancieros = Column(Boolean, nullable=False)
    Intereses = Column(Boolean, nullable=False)
    ReservaLegal = Column(Boolean, nullable=False)
    OtrosProdFinancieros = Column(Boolean, nullable=False)
    GastosNoDeducc = Column(Boolean, nullable=False)
    caja = Column(Boolean, nullable=False)
    costoVariable = Column(Boolean, nullable=False)
    costoFijo = Column(Boolean, nullable=False)
    resultados = Column(Boolean, nullable=False)
    nonegociable = Column(Boolean, nullable=False)
    cuentaclave = Column(Integer, nullable=False)
    saldobanco = Column(Numeric(18, 6), nullable=False)
    ingreso = Column(Integer)
    nosujeto = Column(Integer)
    isr10 = Column(Integer)
    tarjeta = Column(Integer)
    debitofiscal = Column(Integer)
    creditofiscal = Column(Integer)
    automatica = Column(Boolean, nullable=False)
    cesc = Column(Boolean, nullable=False)
    entransito = Column(Boolean, nullable=False)
    tipo = Column(Integer, nullable=False)
    clasificacion = Column(Integer, nullable=False)
    sector = Column(Integer, nullable=False)
    costo = Column(Integer, nullable=False)

    # Relaciones
    # ctalong_rel = relationship("Ctalong", back_populates="cuenta_set")  # Comentado automáticamente
    # rubro_rel = relationship("Rubro", back_populates="cuenta_set")  # Comentado automáticamente

    def __repr__(self):
        return "<Cuenta(cuenta={self.cuenta})>"