# Generado automáticamente
# Tabla: dbo.order
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Integer
from sqlalchemy import Column, String


class Order(Base):
    __tablename__ = "order"
    __table_args__ = {"schema": "dbo"}

    order_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer)
    order_date = Column(DateTime)
    ready_date = Column(DateTime)
    status = Column(String(50))
    empresa = Column(Integer, nullable=False)
    rusuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<Order(order_id={self.order_id})>"