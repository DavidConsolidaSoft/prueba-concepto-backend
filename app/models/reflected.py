# app/models/reflected.py
"""
Modelos reflejados automáticamente desde la base de datos
"""
from app.db.database_reflection import get_automap_base, get_model, initialize_common_models

# Obtener la base automap
Base = get_automap_base()

# Inicializar modelos comunes
common_models = initialize_common_models()

# Exportar modelos comunes
Factura = common_models.get('Factura')
DFactura = common_models.get('Dfactura')
Clientes = common_models.get('Clientes')
Vendedor = common_models.get('Vendedor')
Producto = common_models.get('Producto')
Kardex = common_models.get('Kardex')
Bodega = common_models.get('Bodega')
TipoMov = common_models.get('Tipomov')
CondPago = common_models.get('Condpago')
Caja = common_models.get('Caja')
Empresa = common_models.get('Empresa')

# Función para obtener cualquier modelo por nombre
def get_reflected_model(name: str):
    """Obtiene un modelo reflejado por nombre"""
    return get_model(name)

# Lista todos los modelos disponibles
def list_available_models():
    """Lista todos los modelos disponibles en la base de datos"""
    if Base and hasattr(Base, 'classes'):
        return list(Base.classes.keys())
    return []

__all__ = [
    'Base',
    'Factura', 'DFactura', 'Clientes', 'Vendedor', 'Producto',
    'Kardex', 'Bodega', 'TipoMov', 'CondPago', 'Caja', 'Empresa',
    'get_reflected_model', 'list_available_models'
]