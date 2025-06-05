# Generado automáticamente
# Tabla: dbo.impvineta
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Impvineta(Base):
    __tablename__ = "impvineta"
    __table_args__ = {"schema": "dbo"}

    rollonum = Column(Integer, nullable=False)
    factura = Column(Integer, nullable=False)
    dfactura = Column(Integer, nullable=False)
    codigo = Column(String(25), nullable=False)
    icdbarra = Column(String(25), nullable=False)
    nproducto = Column(String(100), nullable=False)
    nolote = Column(String(20), nullable=False)
    fecvence = Column(DateTime)
    fechaliquida = Column(DateTime)
    pagada = Column(Boolean, nullable=False)
    reimpresa = Column(Boolean, nullable=False)
    vinetanum = Column(Integer, nullable=False)
    vvineta = Column(Numeric(18, 6), nullable=False)
    precioa = Column(Numeric(18, 6), nullable=False)
    preciob = Column(Numeric(18, 6), nullable=False)
    dfactura1 = Column(Integer, nullable=False)
    codigo1 = Column(String(25), nullable=False)
    icdbarra1 = Column(String(25), nullable=False)
    nproducto1 = Column(String(100), nullable=False)
    nolote1 = Column(String(20), nullable=False)
    fecvence1 = Column(DateTime)
    fechaliquida1 = Column(DateTime)
    pagada1 = Column(Boolean, nullable=False)
    reimpresa1 = Column(Boolean, nullable=False)
    vinetanum1 = Column(Integer, nullable=False)
    vvineta1 = Column(Numeric(18, 6), nullable=False)
    precioa1 = Column(Numeric(18, 6), nullable=False)
    preciob1 = Column(Numeric(18, 6), nullable=False)
    dfactura2 = Column(Integer, nullable=False)
    codigo2 = Column(String(25), nullable=False)
    icdbarra2 = Column(String(25), nullable=False)
    nproducto2 = Column(String(100), nullable=False)
    nolote2 = Column(String(20), nullable=False)
    fecvence2 = Column(DateTime)
    fechaliquida2 = Column(DateTime)
    pagada2 = Column(Boolean, nullable=False)
    reimpresa2 = Column(Boolean, nullable=False)
    vinetanum2 = Column(Integer, nullable=False)
    vvineta2 = Column(Numeric(18, 6), nullable=False)
    precioa2 = Column(Numeric(18, 6), nullable=False)
    preciob2 = Column(Numeric(18, 6), nullable=False)
    dfactura3 = Column(Integer, nullable=False)
    codigo3 = Column(String(25), nullable=False)
    icdbarra3 = Column(String(25), nullable=False)
    nproducto3 = Column(String(100), nullable=False)
    nolote3 = Column(String(20), nullable=False)
    fecvence3 = Column(DateTime)
    fechaliquida3 = Column(DateTime)
    pagada3 = Column(Boolean, nullable=False)
    reimpresa3 = Column(Boolean, nullable=False)
    vinetanum3 = Column(Integer, nullable=False)
    vvineta3 = Column(Numeric(18, 6), nullable=False)
    precioa3 = Column(Numeric(18, 6), nullable=False)
    preciob3 = Column(Numeric(18, 6), nullable=False)
    impvineta = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    activo = Column(Boolean, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    empresa = Column(Integer, nullable=False)
    precioc = Column(Numeric(18, 6), nullable=False)
    preciod = Column(Numeric(18, 6), nullable=False)
    precioc1 = Column(Numeric(18, 6), nullable=False)
    precioc2 = Column(Numeric(18, 6), nullable=False)
    precioc3 = Column(Numeric(18, 6), nullable=False)
    preciod1 = Column(Numeric(18, 6), nullable=False)
    preciod2 = Column(Numeric(18, 6), nullable=False)
    preciod3 = Column(Numeric(18, 6), nullable=False)
    dispensador = Column(Boolean, nullable=False)
    recvineta = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Impvineta(impvineta={self.impvineta})>"