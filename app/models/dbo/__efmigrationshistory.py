# Generado automáticamente
# Tabla: dbo.__EFMigrationsHistory
# Fecha: 2025-05-13 16:44:58

from ..base import Base
from sqlalchemy import Column, String


class Efmigrationshistory(Base):
    __tablename__ = "__EFMigrationsHistory"
    __table_args__ = {"schema": "dbo"}

    MigrationId = Column(String(150), primary_key=True, nullable=False)
    ProductVersion = Column(String(32), nullable=False)

    def __repr__(self):
        return "<Efmigrationshistory(MigrationId={self.MigrationId})>"