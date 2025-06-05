# Generado automáticamente
# Tabla: dbo.Todos
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, DateTime
from sqlalchemy import Column, SmallInteger
from sqlalchemy import Column, String


class Todos(Base):
    __tablename__ = "Todos"
    __table_args__ = {"schema": "dbo"}

    TodoID = Column(String(36), primary_key=True, nullable=False)
    Author = Column(String(150), nullable=False)
    TodoDate = Column(DateTime, nullable=False)
    TodoDescription = Column(String(4000), nullable=False)
    TodoState = Column(SmallInteger, nullable=False)

    def __repr__(self):
        return "<Todos(TodoID={self.TodoID})>"