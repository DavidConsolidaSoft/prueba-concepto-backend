# app/db/database_reflection.py
"""
Sistema para usar reflexión de base de datos y automap en tiempo real
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
from app.core.config import settings

# Base global para automap
AutoBase = None
_engine = None
_SessionLocal = None

def get_automap_base():
    """
    Obtiene la base automap, cargándola una sola vez
    """
    global AutoBase, _engine, _SessionLocal
    
    if AutoBase is None:
        try:
            # Crear el engine
            _engine = create_engine(settings.DATABASE_URI)
            
            # Crear la base automap
            AutoBase = automap_base()
            
            # Reflejar todas las tablas
            AutoBase.prepare(_engine, reflect=True)
            
            # Crear SessionLocal
            _SessionLocal = sessionmaker(bind=_engine, expire_on_commit=False)
            
            print(f"Base de datos reflejada. Tablas disponibles: {list(AutoBase.classes.keys())}")
            
        except Exception as e:
            print(f"Error al reflejar la base de datos: {str(e)}")
            raise
    
    return AutoBase

def get_reflected_db():
    """
    Generador de sesiones usando la base reflejada
    """
    if _SessionLocal is None:
        get_automap_base()
    
    db = _SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

# Funciones de utilidad para obtener modelos específicos
def get_model(model_name: str):
    """
    Obtiene un modelo específico por nombre
    """
    base = get_automap_base()
    
    # Intentar obtener el modelo con el nombre exacto
    if hasattr(base.classes, model_name):
        return getattr(base.classes, model_name)
    
    # Intentar con el nombre en minúsculas
    if hasattr(base.classes, model_name.lower()):
        return getattr(base.classes, model_name.lower())
    
    # Intentar con primera letra mayúscula
    if hasattr(base.classes, model_name.capitalize()):
        return getattr(base.classes, model_name.capitalize())
    
    raise AttributeError(f"No se encontró el modelo '{model_name}'")

# Diccionario para cachear modelos
_models_cache = {}

def get_models():
    """
    Obtiene todos los modelos disponibles
    """
    base = get_automap_base()
    
    if not _models_cache:
        for name in base.classes.keys():
            _models_cache[name] = getattr(base.classes, name)
    
    return _models_cache

# Exportar modelos comunes para facilitar su uso
def initialize_common_models():
    """
    Inicializa y exporta modelos comunes
    """
    models = {}
    common_models = [
        'factura', 'dfactura', 'clientes', 'vendedor', 'producto',
        'kardex', 'bodega', 'tipomov', 'condpago', 'caja', 'empresa'
    ]
    
    base = get_automap_base()
    
    for model_name in common_models:
        try:
            if hasattr(base.classes, model_name):
                models[model_name.title()] = getattr(base.classes, model_name)
        except Exception as e:
            print(f"No se pudo cargar el modelo {model_name}: {str(e)}")
    
    return models