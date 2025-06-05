# Generado automáticamente
# Tabla: dbo.cuentaclave
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Cuentaclave(Base):
    __tablename__ = "cuentaclave"
    __table_args__ = {"schema": "dbo"}

    cuentaclave = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ncuentaclave = Column(String(35), nullable=False)
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
    RubroIntereses = Column(Boolean, nullable=False)
    caja = Column(Boolean, nullable=False)
    costoVariable = Column(Boolean, nullable=False)
    costoFijo = Column(Boolean, nullable=False)
    resultados = Column(Boolean, nullable=False)
    nonegociable = Column(Boolean, nullable=False)
    activo = Column(Integer, nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    CuentaXPagar = Column(Boolean, nullable=False)
    Anticipo = Column(Boolean, nullable=False)

    def __repr__(self):
        return "<Cuentaclave(cuentaclave={self.cuentaclave})>"