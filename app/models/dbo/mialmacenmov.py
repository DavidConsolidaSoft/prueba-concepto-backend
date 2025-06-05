# Generado automáticamente
# Tabla: dbo.miAlmacenmov
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Mialmacenmov(Base):
    __tablename__ = "miAlmacenmov"
    __table_args__ = {"schema": "dbo"}

    idkardex = Column(Integer,primary_key=True)
    dia = Column(DateTime)
    TipoMovimiento = Column(String(90))
    Signo = Column(String(1))
    Documento = Column(String(15))
    Codigo = Column(String(25))
    Producto = Column(String(160))
    Bodega = Column(String(100))
    Lote = Column(String(30))
    cantidad = Column(Numeric(18, 6))
    reservado = Column(Numeric(18, 6))
    Revision = Column(Numeric(18, 6))
    CostoPromedio = Column(Numeric(18, 6))
    Fabricante = Column(String(70))
    Categoria = Column(String(70))
    presentacion = Column(String(70))
    nTipoProd = Column(String(40))
    factor = Column(Numeric(18, 6))
    propio = Column(String(6))
    fecvence = Column(DateTime)
    empresa = Column(String(55))
    fechadesde = Column(DateTime)
    fechaHasta = Column(DateTime)

    def __repr__(self):
        return "<Mialmacenmov(idkardex={self.idkardex})>"