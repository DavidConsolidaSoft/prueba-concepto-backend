# Generado automáticamente
# Tabla: dbo.mform983
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Numeric
from sqlalchemy import Column, String


class Mform983(Base):
    __tablename__ = "mform983"
    __table_args__ = {"schema": "dbo"}

    descripcion = Column(String(50))
    UnidadMedida = Column(String(25))
    TotalUnidades = Column(Numeric(18, 2))
    CostoNeto = Column(Numeric(18, 6))
    CostoTotal = Column(Numeric(18, 6))
    CategoriaBien = Column(String(2),primary_key=True)
    ReferenciaLibros = Column(String(2))
    anio = Column(String(4))

    def __repr__(self):
        return "<Mform983(descripcion={self.descripcion})>"