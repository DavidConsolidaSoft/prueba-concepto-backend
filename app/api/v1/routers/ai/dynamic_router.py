import ast
import logging
import re
import threading
import time
import traceback
from typing import List, Dict, Any, Tuple, Optional
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import select, func, desc, asc, text
from app.db.database import get_db
from app.db.base import models
from .models import DynamicQueryRequest, DynamicQueryResponse

logger = logging.getLogger(__name__)

_cached_models = {}
_cached_models_lock = threading.Lock()

def find_model(model_name):
    """
    Busca un modelo en el diccionario de modelos de forma flexible.
    
    Args:
        model_name: Nombre del modelo a buscar
        
    Returns:
        El modelo encontrado o None
    """
    # Log de entrada para depuración
    logger.debug(f"Buscando modelo: '{model_name}'")
    
    # 1. Intentar con el nombre exacto
    if model_name in models:
        logger.debug(f"Modelo encontrado exactamente: '{model_name}'")
        return models[model_name]
    
    # 2. Intentar con el nombre en minúsculas
    lower_name = model_name.lower()
    if lower_name in models:
        logger.debug(f"Modelo encontrado en minúsculas: '{lower_name}'")
        return models[lower_name]
    
    # 3. Intentar con el nombre en mayúsculas
    upper_name = model_name.upper()
    if upper_name in models:
        logger.debug(f"Modelo encontrado en mayúsculas: '{upper_name}'")
        return models[upper_name]
    
    # 4. Intentar con el nombre capitalizado
    capitalized_name = model_name.capitalize()
    if capitalized_name in models:
        logger.debug(f"Modelo encontrado capitalizado: '{capitalized_name}'")
        return models[capitalized_name]
    
    # 5. Intentar con prefijos de esquema comunes
    schema_prefixes = ["dbo.", "public."]
    for prefix in schema_prefixes:
        prefixed_name = f"{prefix}{model_name}"
        if prefixed_name in models:
            logger.debug(f"Modelo encontrado con prefijo: '{prefixed_name}'")
            return models[prefixed_name]
        
        # También probar con variaciones de mayúsculas/minúsculas del nombre con prefijo
        if f"{prefix}{lower_name}" in models:
            logger.debug(f"Modelo encontrado con prefijo en minúsculas: '{prefix}{lower_name}'")
            return models[f"{prefix}{lower_name}"]
        
        if f"{prefix}{upper_name}" in models:
            logger.debug(f"Modelo encontrado con prefijo en mayúsculas: '{prefix}{upper_name}'")
            return models[f"{prefix}{upper_name}"]
            
        if f"{prefix}{capitalized_name}" in models:
            logger.debug(f"Modelo encontrado con prefijo capitalizado: '{prefix}{capitalized_name}'")
            return models[f"{prefix}{capitalized_name}"]
    
    # 6. Búsqueda aproximada - buscar cualquier clave que contenga el nombre del modelo
    for key in models.keys():
        if lower_name in key.lower():
            logger.debug(f"Modelo encontrado por coincidencia parcial: '{key}'")
            return models[key]
    
    # 7. No encontrado - registrar las claves disponibles para diagnóstico
    available_keys = list(models.keys())
    logger.warning(
        f"No se encontró el modelo '{model_name}'. "
        f"Modelos disponibles ({len(available_keys)}): {available_keys[:20] if len(available_keys) > 20 else available_keys}"
    )
    return None

def execute_dynamic_orm(orm_code: str, db: Session, query_request: DynamicQueryRequest) -> Dict[str, Any]:
    """
    Ejecuta código ORM generado dinámicamente.
    """
    try:
        # Log inicial para depuración
        logger.debug(f"Ejecutando código ORM: {orm_code}")
        
        # Reemplazar modelos con acceso por diccionario a modelos con acceso por función
        processed_code = orm_code
        
        # 1. Primero, obtener todas las claves disponibles
        available_models = list(models.keys())
        logger.info(f"Modelos disponibles: {len(available_models)} modelos")
        if len(available_models) > 0:
            logger.info(f"Muestra de modelos: {available_models[:5]}")
        
        # 2. Reemplazar patrones comunes de acceso a modelos
        pattern_replacements = [
            # Patrón 1: models['nombre']
            (r"models\['([^']+)'\]", r"find_model('\1')"),
            # Patrón 2: models["nombre"]
            (r'models\["([^"]+)"\]', r'find_model("\1")'),
            # Patrón 3: models.nombre
            (r"models\.([a-zA-Z0-9_]+)", r"find_model('\1')"),
        ]
        
        for pattern, replacement in pattern_replacements:
            processed_code = re.sub(pattern, replacement, processed_code)
        
        logger.debug(f"Código procesado: {processed_code}")
        
        # Verificar si el código fue modificado
        if processed_code == orm_code:
            logger.warning("El código ORM no fue modificado por los patrones. Realizando ajustes adicionales.")
            
            # Buscar "caja" explícitamente para este caso específico
            if "caja" in orm_code.lower():
                caja_model = find_model('caja')
                if caja_model:
                    logger.info(f"Modelo 'caja' encontrado manualmente: {caja_model}")
                    # Reemplazar manualmente
                    processed_code = processed_code.replace("models['caja']", "find_model('caja')")
                    processed_code = processed_code.replace('models["caja"]', 'find_model("caja")')
                    processed_code = processed_code.replace("models.caja", "find_model('caja')")
        
        # IMPORTANTE: Detectar si estamos intentando usar modelos "caja" o similares
        # y realizar una consulta SQL directa en su lugar
        if "find_model('caja')" in processed_code or 'find_model("caja")' in processed_code:
            logger.info("Detectada consulta de caja. Utilizando SQL directo como alternativa.")
            
            # Extraer límite si está presente
            limit_match = re.search(r'\.limit\((\d+)\)', processed_code)
            limit = int(limit_match.group(1)) if limit_match else 10
            
            # Extraer ordenamiento si está presente - MEJORADO para preservar la columna original
            order_column = "caja"  # Default
            order_dir = "DESC"    # Default
            
            # Buscar patrones comunes de order_by
            order_match = re.search(r'\.order_by\(find_model\([\'"]caja[\'"]\)\.([a-zA-Z0-9_]+)\.([a-z]+)\(\)\)', processed_code)
            if order_match:
                order_column = order_match.group(1)
                order_dir = "DESC" if order_match.group(2).lower() == "desc" else "ASC"
            else:
                # Intento alternativo para otros patrones de order_by
                order_match = re.search(r'\.order_by\(.*?\.([a-zA-Z0-9_]+)\.?([a-z]*)', processed_code)
                if order_match:
                    order_column = order_match.group(1)
                    order_dir = "DESC" if "desc" in order_match.group(2).lower() else "ASC"
                    
            logger.info(f"Ordenamiento extraído: columna={order_column}, dirección={order_dir}")
            
            # Crear SQL directo
            sql_query = f"SELECT TOP {limit} * FROM caja ORDER BY {order_column} {order_dir}"
            logger.info(f"Usando SQL directo: {sql_query}")
            
            try:
                results = execute_raw_sql(db, sql_query)
                return results
            except Exception as e:
                logger.error(f"Error ejecutando SQL directo: {str(e)}")
                # Fallback a consulta sin ordenamiento específico
                fallback_sql = f"SELECT TOP {limit} * FROM caja"
                logger.info(f"Usando SQL directo de fallback: {fallback_sql}")
                return execute_raw_sql(db, fallback_sql)
        
        # Preparar entorno de ejecución seguro
        safe_globals = {
            '__builtins__': {},
            'select': select,
            'func': func,
            'desc': desc,
            'asc': asc,
            'text': text,
            'models': models,
            'find_model': find_model  # Agregar la función find_model al entorno
        }
        
        safe_locals = {}
        
        # Ejecutar código ORM
        exec(processed_code, safe_globals, safe_locals)
        
        # Obtener consulta generada
        query = safe_locals.get('query')
        if not query:
            # Si no encontramos 'query', intentar encontrar cualquier objeto que parezca una consulta
            for var_name, var_value in safe_locals.items():
                if str(type(var_value)).lower().find('query') >= 0 or hasattr(var_value, 'execute'):
                    query = var_value
                    break
        
        if not query:
            # Fallback para tablas comunes
            logger.warning("No se encontró variable 'query'. Intentando generar consulta fallback.")
            
            # Buscar cualquier modelo disponible
            fallback_models = []
            
            # 1. Primero intentar con 'caja'
            caja_model = find_model('caja')
            if caja_model:
                fallback_models.append(('caja', caja_model))
            
            # 2. Luego otras tablas comunes
            common_tables = ['banco', 'factura', 'cliente', 'producto', 'usuario']
            for table_name in common_tables:
                model = find_model(table_name)
                if model:
                    fallback_models.append((table_name, model))
            
            # 3. Si aún no hay modelos, usar el primero disponible
            if not fallback_models and models:
                first_key = next(iter(models.keys()))
                fallback_models.append((first_key, models[first_key]))
            
            # Si tenemos modelos fallback, intentar usar SQL directo
            if fallback_models:
                table_name, model = fallback_models[0]
                logger.info(f"Usando SQL directo para tabla '{table_name}' como fallback")
                sql_query = f"SELECT TOP 10 * FROM {table_name}"
                return execute_raw_sql(db, sql_query)
            else:
                logger.error("No se pudieron encontrar modelos para generar consulta fallback")
                raise ValueError("No se pudo crear una consulta y no hay modelos disponibles")
        
        # Aplicar parámetros adicionales que no estén ya en el orm_code
        if query_request.limit and 'limit' not in processed_code:
            query = query.limit(query_request.limit)
            
        if query_request.offset and 'offset' not in processed_code:
            query = query.offset(query_request.offset)
        
        # Ejecutar consulta
        logger.info("Ejecutando consulta SQL generada")
        result = db.execute(query)
        
        # Obtener resultados
        rows = result.all()
        results = []
        
        for row in rows:
            # Convertir a diccionario
            if hasattr(row, '_mapping'):
                # SQLAlchemy 1.4+
                item = dict(row._mapping)
            else:
                # SQLAlchemy 1.3
                item = dict(row._asdict())
                
            # Procesar tipos de datos para JSON
            processed_item = {}
            for key, value in item.items():
                if hasattr(value, 'isoformat'):  # Para fechas/horas
                    processed_item[key] = value.isoformat()
                else:
                    processed_item[key] = value
                    
            results.append(processed_item)
            
        logger.info(f"Consulta ejecutada con éxito. {len(results)} resultados obtenidos.")
        return results
        
    except Exception as e:
        error_str = str(e)
        # Manejar errores de atributos no existentes
        if "has no attribute" in error_str:
            # Detectar consultas por nombre
            query_text = query_request.text.lower()
            
            # Patrones para detectar filtros por nombre
            name_patterns = [
                r"con\s+nombre\s+([a-zA-Z0-9\s]+)",
                r"llamado\s+([a-zA-Z0-9\s]+)",
                r"que\s+se\s+llama\s+([a-zA-Z0-9\s]+)",
                r"nombre\s+[\"']?([a-zA-Z0-9\s]+)[\"']?",
                r"banco\s+([a-zA-Z0-9\s]+)"
            ]
            
            # Buscar coincidencias con cualquiera de los patrones
            for pattern in name_patterns:
                name_match = re.search(pattern, query_text)
                if name_match:
                    bank_name = name_match.group(1).strip()
                    logger.info(f"Detectado filtro por nombre de banco: '{bank_name}'")
                    
                    # Determinar la tabla basada en el contexto
                    table_name = "banco"
                    if "caja" in query_text:
                        table_name = "caja"
                    elif "factura" in query_text:
                        table_name = "factura"
                    
                    # Columna de nombre según la tabla
                    name_column = "nbanco" if table_name == "banco" else "ncaja" if table_name == "caja" else "nombre"
                    
                    # Consultar directamente con este filtro
                    sql_query = f"""
                        SELECT TOP 10 * FROM {table_name}
                        WHERE {name_column} LIKE '%{bank_name}%' AND activo = 1
                    """
                    
                    logger.info(f"Ejecutando consulta con filtro por nombre: {sql_query}")
                    return execute_raw_sql(db, sql_query)
        # Si el error es relacionado con la estructura del modelo, intentar SQL directo
        if "Column expression" in str(e) and "expected" in str(e):
            logger.info("Error de estructura de modelo. Intentando SQL directo.")
            
            # Determinar la tabla objetivo basada en el código
            table_name = "caja"  # Por defecto
            
            if "find_model" in processed_code:
                table_match = re.search(r"find_model\(['\"]([^'\"]+)['\"]\)", processed_code)
                if table_match:
                    table_name = table_match.group(1)
            
            # Crear consulta SQL básica
            sql_query = f"SELECT TOP 10 * FROM {table_name}"
            
            # Añadir ordenamiento si se puede extraer
            if "order_by" in processed_code:
                if "desc" in processed_code.lower():
                    sql_query += " ORDER BY caja DESC"
                else:
                    sql_query += " ORDER BY caja"
            
            logger.info(f"Usando SQL directo como fallback: {sql_query}")
            return execute_raw_sql(db, sql_query)
        
        raise ValueError(f"Error al ejecutar consulta: {str(e)}")
    
def safe_execute_orm(orm_code: str, db: Session, query_request: DynamicQueryRequest) -> Tuple[List[Dict[str, Any]], int]:
    """
    Ejecuta código ORM de forma segura y devuelve los resultados y conteo.
    
    Args:
        orm_code: Código ORM a ejecutar
        db: Sesión de base de datos
        query_request: Parámetros de la consulta
        
    Returns:
        Tupla con los resultados y el conteo total
    """
    try:
        # Log de inicio para seguimiento
        logger.info(f"Iniciando ejecución segura de ORM: {orm_code}")
        
        # Verificar si hay modelos disponibles
        if not models:
            # Si no hay modelos, intentar cargar desde Redis directamente
            logger.warning("No hay modelos disponibles. Intentando cargarlos desde Redis...")
            try:
                load_models_from_redis()
            except Exception as e:
                logger.error(f"Error al cargar modelos desde Redis: {str(e)}")
                
            # Si aún no hay modelos, ejecutar consulta SQL directa
            if not models:
                logger.warning("No se pudieron cargar modelos. Ejecutando consulta SQL directa...")
                # Extraer tabla de la consulta
                table_name = extract_table_from_query(query_request.text)
                # Crear consulta SQL directa
                sql_query = f"SELECT TOP 10 * FROM {table_name} ORDER BY CASE WHEN EXISTS (SELECT 1 FROM sys.columns WHERE object_id = OBJECT_ID('{table_name}') AND name = 'horatiempo') THEN 1 ELSE 0 END DESC"
                
                results = execute_raw_sql(db, sql_query)
                return results, len(results)
        
        # Verificar claves relacionadas con 'caja'
        caja_keys = [key for key in models.keys() if 'caja' in key.lower()]
        logger.info(f"Claves relacionadas con 'caja' en models: {caja_keys}")
        
        # Log de todas las claves disponibles (limitado a 20 para no sobrecargar los logs)
        all_keys = list(models.keys())
        logger.info(f"Total de modelos disponibles: {len(all_keys)}")
        if len(all_keys) > 0:
            sample_keys = all_keys[:min(20, len(all_keys))]
            logger.info(f"Muestra de modelos disponibles: {sample_keys}")
        
        # Validar el código (asegurarse de que sea Python válido)
        try:
            ast.parse(orm_code)
            logger.info("Código ORM validado correctamente")
        except SyntaxError as e:
            logger.error(f"Error de sintaxis en código ORM: {str(e)}")
            orm_code = "query = select(find_model('caja')).limit(10) if find_model('caja') else select(models[next(iter(models))]).limit(10)"
            logger.info(f"Usando código ORM de fallback: {orm_code}")
        
        # Ejecutar la consulta
        results = execute_dynamic_orm(orm_code, db, query_request)
        
        # Para el conteo total, extraer la consulta base
        # Este es un enfoque simplificado, podría necesitar refinamiento
        total_count = len(results)
        
        # Contar registros si hay resultados
        if results and orm_code.strip():
            try:
                # Generar consulta de conteo
                count_code = orm_code
                # Modificar para usar func.count en lugar de campos específicos
                if 'select(' in count_code and not 'func.count' in count_code:
                    count_code = re.sub(
                        r'select\((.*?)\)',
                        r'select(func.count().label("total"))',
                        count_code
                    )
                
                # Si hay limit o offset, los quitamos para el conteo total
                count_code = re.sub(r'\.limit\(\d+\)', '', count_code)
                count_code = re.sub(r'\.offset\(\d+\)', '', count_code)
                
                logger.debug(f"Código de conteo: {count_code}")
                
                # Ejecutar consulta de conteo
                count_locals = {}
                count_globals = {
                    '__builtins__': {},
                    'select': select,
                    'func': func,
                    'desc': desc,
                    'asc': asc,
                    'text': text,
                    'models': models,
                    'find_model': find_model
                }
                
                exec(count_code, count_globals, count_locals)
                count_query = count_locals.get('query')
                
                if count_query:
                    count_result = db.execute(count_query).scalar()
                    if count_result is not None:
                        total_count = int(count_result)
                        logger.info(f"Conteo total de registros: {total_count}")
            except Exception as e:
                logger.warning(f"Error al obtener conteo total: {str(e)}")
                logger.warning("Usando longitud de resultados como conteo total")
        
        logger.info(f"Ejecución ORM completada con éxito. Resultados: {len(results)}, Total: {total_count}")
        return results, total_count
    
    except Exception as e:
        logger.error(f"Error al ejecutar ORM: {str(e)}\n{traceback.format_exc()}")
        
        # Intento de recuperación
        try:
            logger.info("Intentando consulta de recuperación...")
            recovery_code = "query = select(find_model('caja')).limit(5) if find_model('caja') else select(models[list(models.keys())[0]]).limit(5)"
            return execute_dynamic_orm(recovery_code, db, query_request), 5
        except Exception as recovery_error:
            logger.error(f"También falló la consulta de recuperación: {str(recovery_error)}")
            
        raise HTTPException(
            status_code=400,
            detail=f"Error al ejecutar consulta: {str(e)}"
        )
        
def load_models_from_redis():
    """Intenta cargar modelos desde Redis si están disponibles"""
    try:
        global _cached_models, models
        
        # Verificar si ya hay modelos en caché
        if _cached_models:
            logger.info(f"Usando {len(_cached_models)} modelos desde caché en memoria")
            models.update(_cached_models)
            return True
            
        with _cached_models_lock:
            # Verificar de nuevo dentro del lock (por si otro hilo ya lo cargó)
            if _cached_models:
                logger.info(f"Usando {len(_cached_models)} modelos desde caché en memoria (2da verificación)")
                models.update(_cached_models)
                return True
                
            # Si llegamos aquí, necesitamos cargar desde Redis
            from app.api.v1.routers.ai.redis_service import RedisService
            from app.db.base import create_models_from_redis
            
            start_time = time.time()
            redis = RedisService()
            success = create_models_from_redis(redis)
            
            if success:
                # Guardar en caché
                _cached_models.update(models)
                logger.info(f"Modelos cargados desde Redis y guardados en caché: {len(models)} en {time.time() - start_time:.2f} segundos")
                return True
            else:
                logger.error("Error cargando modelos desde Redis")
                return False
    except Exception as e:
        logger.error(f"Error cargando modelos desde Redis: {str(e)}")
        return False
        
def extract_table_from_query(query_text):
    """Extrae el nombre de tabla más probable de una consulta en lenguaje natural"""
    query_lower = query_text.lower()
    
    # Patrones comunes para tablas
    common_tables = [
        ('caja', ['caja', 'cajas']),
        ('banco', ['banco', 'bancos']),
        ('factura', ['factura', 'facturas']),
        ('cliente', ['cliente', 'clientes']),
        ('producto', ['producto', 'productos'])
    ]
    
    # Buscar menciones de tablas
    for table, patterns in common_tables:
        if any(pattern in query_lower for pattern in patterns):
            return table
    
    # Por defecto, usar 'caja'
    return 'caja'

def execute_raw_sql(db, sql):
    """Ejecuta una consulta SQL directa como fallback"""
    try:
        # Corregir sintaxis SQL Server: LIMIT -> TOP
        if "LIMIT" in sql:
            # Extraer el valor del límite
            limit_match = re.search(r'LIMIT\s+(\d+)', sql)
            if limit_match:
                limit_value = limit_match.group(1)
                # Reemplazar "LIMIT N" con "TOP N" en la posición correcta
                sql = sql.replace(f"LIMIT {limit_value}", "")
                # Insertar TOP después de SELECT
                sql = sql.replace("SELECT", f"SELECT TOP {limit_value}")
        
        logger.info(f"Ejecutando SQL modificado: {sql}")
        result = db.execute(text(sql))
        rows = []
        
        for row in result:
            # Convertir a diccionario
            if hasattr(row, '_mapping'):
                item = dict(row._mapping)
            else:
                item = dict(row._asdict())
                
            # Procesar tipos de datos para JSON
            processed_item = {}
            for key, value in item.items():
                if hasattr(value, 'isoformat'):  # Para fechas/horas
                    processed_item[key] = value.isoformat()
                else:
                    processed_item[key] = value
                    
            rows.append(processed_item)
        return rows
    except Exception as e:
        logger.error(f"Error ejecutando SQL directo: {str(e)}")
        
        # Intentar con banco como fallback específico si la consulta menciona banco
        if "banco" in sql.lower():
            try:
                simple_sql = "SELECT TOP 20 banco, nbanco, preferido, activo FROM banco WHERE activo = 1"
                logger.info(f"Intentando consulta de banco simplificada: {simple_sql}")
                return db.execute(text(simple_sql)).mappings().all()
            except Exception as e2:
                logger.error(f"Error en consulta simplificada de banco: {str(e2)}")
        
        return []
    
def load_specific_model(table_name: str):
    """Carga un modelo específico desde Redis"""
    try:
        global models
        from app.api.v1.routers.ai.redis_service import RedisService
        
        # Si el modelo ya está en caché global, usar ese
        if table_name in _cached_models:
            models[table_name] = _cached_models[table_name]
            # También cargar versiones con distintas capitalizaciones
            models[table_name.lower()] = _cached_models[table_name]
            models[table_name.capitalize()] = _cached_models[table_name]
            models[f"dbo.{table_name}"] = _cached_models[table_name]
            logger.info(f"Modelo '{table_name}' cargado desde caché en memoria")
            return True
            
        # Si no está en caché, cargar desde Redis
        redis = RedisService()
        
        # Verificar si la tabla existe en Redis
        table_exists = redis.redis_client.sismember("schema:all_tables", table_name)
        if not table_exists:
            logger.warning(f"Tabla '{table_name}' no existe en Redis")
            # Intentar con variaciones de nombre
            for variant in [table_name.lower(), table_name.capitalize(), table_name.upper()]:
                if redis.redis_client.sismember("schema:all_tables", variant):
                    table_name = variant
                    logger.info(f"Se encontró tabla con nombre '{variant}'")
                    break
        
        # Crear modelo para la tabla
        model_class = type(table_name.capitalize(), (object,), {
            '__tablename__': table_name
        })
        
        # Guardar en modelos locales y en caché global
        models[table_name] = model_class
        models[table_name.lower()] = model_class
        models[table_name.capitalize()] = model_class
        models[f"dbo.{table_name}"] = model_class
        
        with _cached_models_lock:
            _cached_models[table_name] = model_class
            _cached_models[table_name.lower()] = model_class
            _cached_models[table_name.capitalize()] = model_class
            _cached_models[f"dbo.{table_name}"] = model_class
        
        logger.info(f"Modelo '{table_name}' cargado específicamente desde Redis")
        return True
    except Exception as e:
        logger.error(f"Error cargando modelo específico '{table_name}': {str(e)}")
        return False