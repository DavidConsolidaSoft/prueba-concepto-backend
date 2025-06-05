# Generado automáticamente
# Tabla: dbo.reportHeader
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Integer, String


class Reportheader(Base):
    __tablename__ = "reportHeader"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    header1 = Column(String(100))
    header2 = Column(String(30))
    header3 = Column(String(30))
    header4 = Column(String(30))
    header5 = Column(String(30))
    header6 = Column(String(30))
    header7 = Column(String(30))
    header8 = Column(String(30))
    header9 = Column(String(30))
    header10 = Column(String(30))
    header11 = Column(String(30))
    header12 = Column(String(30))
    header13 = Column(String(30))
    header14 = Column(String(30))
    header15 = Column(String(30))
    header16 = Column(String(30))
    header17 = Column(String(30))
    header18 = Column(String(30))
    header19 = Column(String(30))
    header20 = Column(String(30))
    header21 = Column(String(30))
    header22 = Column(String(30))
    header23 = Column(String(30))
    header24 = Column(String(30))
    header25 = Column(String(30))
    header26 = Column(String(30))
    header27 = Column(String(30))
    header28 = Column(String(30))
    header29 = Column(String(30))
    header30 = Column(String(30))
    header31 = Column(String(25))

    def __repr__(self):
        return "<Reportheader(header1={self.header1})>"