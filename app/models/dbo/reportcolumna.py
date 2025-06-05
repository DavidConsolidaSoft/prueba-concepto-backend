# Generado automáticamente
# Tabla: dbo.reportcolumna
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer, Numeric
from sqlalchemy import Column, String


class Reportcolumna(Base):
    __tablename__ = "reportcolumna"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    columna1 = Column(String(100))
    columna2 = Column(String(30))
    columna3 = Column(Numeric(18, 6))
    columna4 = Column(Numeric(18, 6))
    columna5 = Column(Numeric(18, 6))
    columna6 = Column(Numeric(18, 6))
    columna7 = Column(Numeric(18, 6))
    columna8 = Column(Numeric(18, 6))
    columna9 = Column(Numeric(18, 6))
    columna10 = Column(Numeric(18, 6))
    columna11 = Column(Numeric(18, 6))
    columna12 = Column(Numeric(18, 6))
    columna13 = Column(Numeric(18, 6))
    columna14 = Column(Numeric(18, 6))
    columna15 = Column(Numeric(18, 6))
    columna16 = Column(Numeric(18, 6))
    columna17 = Column(Numeric(18, 6))
    columna18 = Column(Numeric(18, 6))
    columna19 = Column(Numeric(18, 6))
    columna20 = Column(Numeric(18, 6))
    columna21 = Column(Numeric(18, 6))
    columna22 = Column(Numeric(18, 6))
    columna23 = Column(Numeric(18, 6))
    columna24 = Column(Numeric(18, 6))
    columna25 = Column(Numeric(18, 6))
    columna26 = Column(Numeric(18, 6))
    columna27 = Column(Numeric(18, 6))
    columna28 = Column(Numeric(18, 6))
    columna29 = Column(Numeric(18, 6))
    columna30 = Column(Numeric(18, 6))
    columna31 = Column(String(25))

    def __repr__(self):
        return "<Reportcolumna(columna1={self.columna1})>"