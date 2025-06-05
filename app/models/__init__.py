# app/models/__init__.py
"""
Modelos de la aplicación
"""
from .base import Base

# Importar modelos del esquema dbo
try:
    from . import dbo
except ImportError as e:
    print(f"Advertencia al importar dbo: {e}")

# Mantener compatibilidad con código existente
__all__ = ['Base']