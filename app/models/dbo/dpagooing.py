# Generado automáticamente
# Tabla: dbo.dpagooing
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, Boolean
from sqlalchemy import Column, Integer
from sqlalchemy import Column, Numeric


class Dpagooing(Base):
    __tablename__ = "dpagooing"
    __table_args__ = {"schema": "dbo"}

    dpagooing = Column(Numeric(18, 0), primary_key=True, nullable=False, autoincrement=True)
    dplanilla = Column(Integer)
    ingreso = Column(Integer)
    poldesc = Column(Integer)
    esingreso = Column(Boolean)
    monto = Column(Numeric(18, 9))

    def __repr__(self):
        return "<Dpagooing(dpagooing={self.dpagooing})>"