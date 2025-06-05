# Generado automáticamente
# Tabla: dbo.facturasexpress
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Facturasexpress(Base):
    __tablename__ = "facturasexpress"
    __table_args__ = {"schema": "dbo"}

    facturasexpress = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    factura = Column(Integer, nullable=False)
    proveedor = Column(String(200), nullable=False)
    bl = Column(String(50), nullable=False)
    descripgods = Column(String(200), nullable=False)
    piezas = Column(String(15), nullable=False)
    volumen = Column(String(15), nullable=False)
    contenedor = Column(String(20), nullable=False)
    direccion = Column(String(200), nullable=False)
    exportcarrier = Column(String(200), nullable=False)
    foreingport = Column(String(200), nullable=False)
    marksnum1 = Column(String(15), nullable=False)
    marksnum2 = Column(String(15), nullable=False)
    marksnum3 = Column(String(15), nullable=False)
    marksnum4 = Column(String(15), nullable=False)
    marksnum5 = Column(String(15), nullable=False)
    numbers1 = Column(Numeric(18, 6), nullable=False)
    numbers2 = Column(Numeric(18, 6), nullable=False)
    numbers3 = Column(Numeric(18, 6), nullable=False)
    numbers4 = Column(Numeric(18, 6), nullable=False)
    numbers5 = Column(Numeric(18, 6), nullable=False)
    descripcomm1 = Column(String(200), nullable=False)
    descripcomm2 = Column(String(200), nullable=False)
    descripcomm3 = Column(String(200), nullable=False)
    descripcomm4 = Column(String(200), nullable=False)
    descripcomm5 = Column(String(200), nullable=False)
    gross1 = Column(Numeric(18, 6), nullable=False)
    gross2 = Column(Numeric(18, 6), nullable=False)
    gross3 = Column(Numeric(18, 6), nullable=False)
    gross4 = Column(Numeric(18, 6), nullable=False)
    gross5 = Column(Numeric(18, 6), nullable=False)
    measureme1 = Column(Numeric(18, 6), nullable=False)
    measureme2 = Column(Numeric(18, 6), nullable=False)
    measureme3 = Column(Numeric(18, 6), nullable=False)
    measureme4 = Column(Numeric(18, 6), nullable=False)
    measureme5 = Column(Numeric(18, 6), nullable=False)
    empresa = Column(Integer, nullable=False)
    usuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)
    peso1 = Column(String(15), nullable=False)
    peso2 = Column(String(15), nullable=False)
    peso3 = Column(String(15), nullable=False)
    peso4 = Column(String(15), nullable=False)
    peso5 = Column(String(15), nullable=False)
    peso6 = Column(String(15), nullable=False)
    peso7 = Column(String(15), nullable=False)
    peso8 = Column(String(15), nullable=False)
    peso9 = Column(String(15), nullable=False)
    peso10 = Column(String(15), nullable=False)
    carriageby = Column(String(50), nullable=False)
    placeofrecipient = Column(String(50), nullable=False)
    portofloadingexport = Column(String(50), nullable=False)
    fortrans = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Facturasexpress(facturasexpress={self.facturasexpress})>"