# app/core/global_vars.py
"""
Módulo para manejar variables globales thread-safe
"""
import threading

# Thread-local storage para variables globales
_thread_local = threading.local()

# Funciones para pdata
def set_pdata(value):
    """Establece el valor de pdata para el thread actual"""
    _thread_local.pdata = value

def get_pdata():
    """Obtiene el valor de pdata para el thread actual"""
    return getattr(_thread_local, 'pdata', None)

# Funciones para pempresa  
def set_pempresa(value):
    """Establece el valor de pempresa para el thread actual"""
    _thread_local.pempresa = value

def get_pempresa():
    """Obtiene el valor de pempresa para el thread actual"""
    return getattr(_thread_local, 'pempresa', None)

# Funciones para pcaja
def set_pcaja(value):
    """Establece el valor de pcaja para el thread actual"""
    _thread_local.pcaja = value

def get_pcaja():
    """Obtiene el valor de pcaja para el thread actual"""
    return getattr(_thread_local, 'pcaja', None)

# Funciones para pbodega
def set_pbodega(value):
    """Establece el valor de pbodega para el thread actual"""
    _thread_local.pbodega = value

def get_pbodega():
    """Obtiene el valor de pbodega para el thread actual"""
    return getattr(_thread_local, 'pbodega', None)

# Funciones para pvendedor
def set_pvendedor(value):
    """Establece el valor de pvendedor para el thread actual"""
    _thread_local.pvendedor = value

def get_pvendedor():
    """Obtiene el valor de pvendedor para el thread actual"""
    return getattr(_thread_local, 'pvendedor', None)

# Funciones para pprodprec
def set_pprodprec(value):
    """Establece el valor de pprodprec para el thread actual"""
    _thread_local.pprodprec = value

def get_pprodprec():
    """Obtiene el valor de pprodprec para el thread actual"""
    return getattr(_thread_local, 'pprodprec', None)

# Función para limpiar todas las variables
def clear_all():
    """Limpia todas las variables globales del thread actual"""
    attrs_to_clear = ['pdata', 'pempresa', 'pcaja', 'pbodega', 'pvendedor', 'pprodprec']
    for attr in attrs_to_clear:
        if hasattr(_thread_local, attr):
            delattr(_thread_local, attr)

# Función para debug
def get_all_vars():
    """Retorna todas las variables actuales (para debug)"""
    return {
        'pdata': get_pdata(),
        'pempresa': get_pempresa(),
        'pcaja': get_pcaja(),
        'pbodega': get_pbodega(),
        'pvendedor': get_pvendedor(),
        'pprodprec': get_pprodprec()
    }