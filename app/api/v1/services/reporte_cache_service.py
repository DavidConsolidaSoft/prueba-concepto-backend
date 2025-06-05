import logging
import time
import json
import hashlib
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class ReporteCacheService:
    """
    Servicio para cachear resultados de reportes
    """
    def __init__(self):
        self.cache = {}
        self.expiration = 3600  # 1 hora por defecto

    def cache_key(self, reporte_tipo: str, params: Dict[str, Any]) -> str:
        """Genera una clave única para la caché basada en el tipo de reporte y sus parámetros"""
        params_str = json.dumps(params, sort_keys=True)
        return f"{reporte_tipo}:{hashlib.md5(params_str.encode()).hexdigest()}"

    def cache_report(self, reporte_tipo: str, params: Dict[str, Any], data: Dict[str, Any]) -> None:
        """Guarda un reporte en la caché"""
        key = self.cache_key(reporte_tipo, params)
        self.cache[key] = {
            "data": data,
            "timestamp": time.time(),
            "expires": time.time() + self.expiration
        }
        logger.info(f"Reporte {reporte_tipo} cacheado. Key: {key}")

    def get_cached_report(self, reporte_tipo: str, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Obtiene un reporte de la caché si existe y no ha expirado"""
        key = self.cache_key(reporte_tipo, params)
        cached = self.cache.get(key)
        
        if not cached:
            return None
            
        if cached["expires"] < time.time():
            del self.cache[key]
            return None
            
        logger.info(f"Reporte {reporte_tipo} recuperado de caché. Key: {key}")
        return cached["data"]

    def invalidate_cache(self, reporte_tipo: Optional[str] = None) -> int:
        """Invalida la caché para un tipo específico de reporte o para todos"""
        count = 0
        keys_to_delete = []
        
        for key in self.cache:
            if reporte_tipo is None or key.startswith(f"{reporte_tipo}:"):
                keys_to_delete.append(key)
                count += 1
                
        for key in keys_to_delete:
            del self.cache[key]
            
        logger.info(f"Caché invalidada. {count} elementos eliminados.")
        return count

    def purge_expired_cache(self) -> int:
        """Elimina entradas de caché expiradas"""
        now = time.time()
        count = 0
        keys_to_delete = []
        
        for key, value in self.cache.items():
            if value["expires"] < now:
                keys_to_delete.append(key)
                count += 1
                
        for key in keys_to_delete:
            del self.cache[key]
            
        logger.info(f"Caché expirada purgada. {count} elementos eliminados.")
        return count

    def get_cache_stats(self) -> Dict[str, Any]:
        """Obtiene estadísticas sobre la caché"""
        now = time.time()
        total = len(self.cache)
        expired = 0
        
        for value in self.cache.values():
            if value["expires"] < now:
                expired += 1
                
        return {
            "total": total,
            "active": total - expired,
            "expired": expired
        }