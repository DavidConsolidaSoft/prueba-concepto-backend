# Generado automáticamente
# Tabla: dbo.order_detail
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, Float
from sqlalchemy import Column, Integer


class OrderDetail(Base):
    __tablename__ = "order_detail"
    __table_args__ = {"schema": "dbo"}

    order_detial_id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Float)
    unit_price = Column(Float)
    empresa = Column(Integer, nullable=False)
    rusuario = Column(Integer, nullable=False)
    horatiempo = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<OrderDetail(order_detial_id={self.order_detial_id})>"