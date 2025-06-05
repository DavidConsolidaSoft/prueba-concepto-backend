import asyncio
import os
import json
import logging
import threading
import time
import concurrent.futures
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData, inspect, text, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.api.v1.routers.ai.redis_service import RedisService
from functools import partial

_cached_models = {}
_cached_models_lock = threading.Lock()

logger = logging.getLogger(__name__)

# Base global automap para SQLAlchemy
Base = automap_base()

# Diccionario global para almacenar modelos reflejados
models = {}

def reflect_and_cache_schema() -> dict:
    """
    Refleja el esquema de la base de datos y lo almacena en Redis si es necesario.
    
    Returns:
        Diccionario con los modelos de SQLAlchemy reflejados
    """
    try:
        # Declarar models como global al principio de la función
        global models
        
        # Inicializar servicio Redis
        redis = RedisService()
        
        # Verificar explícitamente si el esquema existe en Redis
        db_models_ready = redis.redis_client.get("db_models_ready")
        schema_version = redis.redis_client.get("schema_version")
        
        logger.info(f"Verificando esquema en Redis - db_models_ready: {db_models_ready}, schema_version: {schema_version}")
        
        # Si existe schema_version pero db_models_ready es None, configurarlo
        if schema_version and not db_models_ready:
            logger.info("Encontrada versión de esquema pero db_models_ready es None. Configurando valor...")
            redis.redis_client.set("db_models_ready", "1")
            db_models_ready = "1"
        
        # Intentar cargar desde Redis si existe alguna información de esquema
        if db_models_ready or schema_version:
            logger.info("Información de esquema detectada en Redis. Intentando cargarlo...")
            try:
                # Establecer un timeout para la carga desde caché
                import threading
                import time
                
                def load_with_timeout():
                    global models
                    nonlocal cached_models
                    cached_models = load_cached_schema(redis)
                
                cached_models = {}
                thread = threading.Thread(target=load_with_timeout)
                thread.daemon = True
                thread.start()
                
                # Esperar hasta 5 segundos
                thread.join(5.0)
                
                if thread.is_alive():
                    logger.warning("Timeout al cargar esquema desde Redis. Procediendo con reflexión completa.")
                    return {}  # Forzar reflexión completa
                
                if cached_models and len(cached_models) > 0:
                    logger.info(f"Esquema cargado exitosamente desde Redis con {len(cached_models)} modelos")
                    # Asegurarse de que db_models_ready se mantiene
                    redis.redis_client.set("db_models_ready", "1")
                    return cached_models
                else:
                    logger.warning("Esquema encontrado en Redis pero no se pudieron cargar modelos")
            except Exception as cache_error:
                logger.warning(f"Error al cargar esquema desde Redis: {str(cache_error)}")
                logger.warning("Procediendo con reflexión completa")
            
        # Si llegamos aquí, necesitamos realizar una reflexión completa
        logger.info("Reflejando nuevo esquema de la base de datos...")
        
        # Crear conexión a la base de datos
        engine = create_engine(settings.DATABASE_URI)
        
        # Intentar reflexión completa
        try:
            metadata = MetaData()
            metadata.reflect(bind=engine, schema='dbo')
            
            # Crear y preparar Base para autoapear modelos
            global Base
            Base = automap_base()
            Base.prepare(autoload_with=engine, schema='dbo')
            
            # Obtener modelos reflejados
            models.clear()
            
            # Contar modelos para diagnóstico
            model_count = 0
            
            for cls in Base.classes:
                # Obtener nombre original
                original_name = cls.__name__
                model_count += 1
                
                # Almacenar con múltiples formas para flexibilidad
                models[original_name] = cls           # Nombre original (RupComponente)
                models[original_name.lower()] = cls   # Nombre en minúsculas (rupcomponente)
                
                # También almacenar con prefijo de esquema
                models[f"dbo.{original_name}"] = cls
                models[f"dbo.{original_name.lower()}"] = cls
                
                # IMPORTANTE: Registra los nombres disponibles para depuración
                logger.debug(f"Modelo cargado: {original_name} (también disponible como {original_name.lower()})")
            
            logger.info(f"Reflexión completada. {model_count} modelos de clase generados, {len(models)} entradas en el diccionario models.")
            
        except Exception as reflect_error:
            logger.error(f"Error durante la reflexión automática: {str(reflect_error)}")
            logger.info("Intentando crear modelos manualmente...")
            
            # Crear modelos básicos manualmente
            try:
                # Extraer lista de tablas directamente
                with engine.connect() as conn:
                    result = conn.execute(text("""
                        SELECT name FROM sys.tables WHERE is_ms_shipped = 0
                    """))
                    table_names = [row[0] for row in result]
                
                # Crear modelos básicos
                models.clear()
                
                for table_name in table_names:
                    try:
                        model_class = type(table_name.capitalize(), (object,), {
                            '__tablename__': table_name
                        })
                        models[table_name] = model_class
                        models[table_name.lower()] = model_class
                        models[f"dbo.{table_name}"] = model_class
                        models[f"dbo.{table_name.lower()}"] = model_class
                    except Exception as model_error:
                        logger.warning(f"Error creando modelo para '{table_name}': {str(model_error)}")
                
                logger.info(f"Creados {len(models)} modelos básicos manualmente.")
                
                # Crear metadata para almacenar en Redis
                metadata = MetaData()
                
            except Exception as manual_error:
                logger.error(f"Error creando modelos manualmente: {str(manual_error)}")
                metadata = MetaData()  # Metadata vacía para continuar
        
        # Obtener versión actual del esquema
        current_version = get_schema_version(engine)
        
        # Guardar en Redis (en segundo plano)
        asyncio.create_task(process_and_cache_schema(metadata, current_version, redis))
        
        # Indicar que los modelos están disponibles
        redis.redis_client.set("db_models_ready", "1")
        
        logger.info(f"Esquema reflejado con éxito. {len(models)} modelos disponibles.")
        
        # Verificación adicional - comprobar si caja está entre los modelos
        if 'caja' in models:
            logger.info("Modelo 'caja' encontrado correctamente.")
        else:
            logger.warning("Modelo 'caja' NO encontrado. Verificando alternativas.")
            
            # Buscar variaciones del nombre
            caja_variations = ['Caja', 'CAJA', 'dbo.caja', 'dbo.Caja']
            found = False
            for variant in caja_variations:
                if variant in models:
                    logger.info(f"Modelo 'caja' encontrado como '{variant}'")
                    # Añadir explícitamente como 'caja'
                    models['caja'] = models[variant]
                    found = True
                    break
            
            # Si aún no se encuentra, crear manualmente un modelo básico
            if not found:
                logger.warning("Creando modelo 'caja' manualmente como último recurso")
                try:
                    models['caja'] = type('Caja', (object,), {'__tablename__': 'caja'})
                    logger.info("Modelo 'caja' creado manualmente")
                except Exception as e:
                    logger.error(f"Error al crear modelo 'caja' manualmente: {str(e)}")
        
        return models
        
    except Exception as e:
        logger.error(f"Error crítico al reflejar esquema: {str(e)}")
        # Intentar crear modelos manualmente desde Redis como último recurso
        try:
            redis = RedisService()
            create_models_from_redis(redis)
            return models
        except Exception as manual_e:
            logger.error(f"También falló la creación manual: {str(manual_e)}")
            return {}
                                  
def create_model_from_redis(redis, engine, table_name):
    """
    Crea un modelo manualmente a partir de los metadatos en Redis.
    """
    try:
        # Obtener metadatos de la tabla desde Redis
        table_key = f"schema:table:{table_name}"
        table_data_json = redis.redis_client.get(table_key)
        
        if not table_data_json:
            logger.error(f"No se encontraron metadatos para la tabla '{table_name}' en Redis")
            return False
            
        # Asegurarse de decodificar solo si es un objeto bytes
        if isinstance(table_data_json, bytes):
            table_data_json = table_data_json.decode('utf-8')
            
        table_data = json.loads(table_data_json)
        
        # Crear tabla manualmente
        metadata = MetaData()
        
        # Definir columnas
        columns = []
        for col_data in table_data.get('columnas', []):
            # Determinar tipo de columna básico
            col_type = col_data.get('type', 'VARCHAR(100)')
            col_name = col_data.get('name', '')
            
            if not col_name:
                continue
                
            # Crear columna
            if 'INTEGER' in col_type:
                columns.append(Column(col_name, Integer, primary_key=col_data.get('is_key', False)))
            elif 'VARCHAR' in col_type:
                size = 100
                if '(' in col_type and ')' in col_type:
                    try:
                        size = int(col_type.split('(')[1].split(')')[0])
                    except:
                        pass
                columns.append(Column(col_name, String(size), primary_key=col_data.get('is_key', False)))
            elif 'DATETIME' in col_type:
                columns.append(Column(col_name, DateTime, primary_key=col_data.get('is_key', False)))
            elif 'BIT' in col_type:
                columns.append(Column(col_name, Boolean, primary_key=col_data.get('is_key', False)))
            else:
                # Tipo genérico para otros casos
                columns.append(Column(col_name, String(100), primary_key=col_data.get('is_key', False)))
        
        # Crear tabla
        if columns:
            tabla = Table(table_name, metadata, *columns)
            
            # Crear clase para el modelo
            class_dict = {
                '__tablename__': table_name,
                '__table__': tabla
            }
            
            # Crear clase dinámicamente
            ModelClass = type(table_name.capitalize(), (object,), class_dict)
            
            # Añadir a modelos
            global models
            models[table_name] = ModelClass
            models[table_name.capitalize()] = ModelClass
            models[f"dbo.{table_name}"] = ModelClass
            
            logger.info(f"Modelo '{table_name}' creado manualmente con éxito.")
            return True
        else:
            logger.error(f"No se pudieron crear columnas para la tabla '{table_name}'")
            return False
            
    except Exception as e:
        logger.error(f"Error al crear modelo manual: {str(e)}")
        return False

def create_models_from_redis(redis: RedisService):
    """
    Crea modelos para todas las tablas en Redis.
    """
    try:
        # Obtener todas las claves de tabla
        all_table_keys = redis.redis_client.keys("schema:table:*")
        
        if not all_table_keys:
            logger.error("No se encontraron tablas en Redis")
            return False
            
        logger.info(f"Encontradas {len(all_table_keys)} tablas en Redis")
        
        # Paralelización con ThreadPoolExecutor
        import concurrent.futures
        from functools import partial
        
        # Función parcial con parámetros fijos
        create_model_partial = partial(create_model_from_redis_parallel, redis)
        
        # Número de workers - ajustar según el entorno
        max_workers = min(16, len(all_table_keys))
        
        # Crear cada modelo en paralelo
        success_count = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Extraer nombres de tabla de las claves
            table_names = []
            for table_key in all_table_keys:
                # Asegurarse de decodificar solo si es un objeto bytes
                if isinstance(table_key, bytes):
                    table_name = table_key.decode('utf-8').split("schema:table:")[1]
                else:
                    table_name = table_key.split("schema:table:")[1]
                table_names.append(table_name)
            
            # Procesar en lotes para no sobrecargar la conexión a Redis
            batch_size = 50
            for i in range(0, len(table_names), batch_size):
                batch = table_names[i:i+batch_size]
                logger.info(f"Procesando lote de {len(batch)} modelos ({i+1}-{i+len(batch)} de {len(table_names)})")
                
                # Ejecutar en paralelo
                results = list(executor.map(create_model_partial, batch))
                
                # Contar éxitos
                success_count += sum(1 for r in results if r)
                
                # Pequeña pausa entre lotes para no sobrecargar
                if i + batch_size < len(table_names):
                    time.sleep(0.1)
                
        logger.info(f"Creados {success_count} modelos en paralelo desde Redis")
        return success_count > 0
            
    except Exception as e:
        logger.error(f"Error al crear modelos desde Redis: {str(e)}")
        return False

def create_model_from_redis_parallel(redis, table_name):
    """Versión para ejecución paralela de create_model_from_redis"""
    try:
        # Obtener metadatos de la tabla desde Redis
        table_key = f"schema:table:{table_name}"
        table_data_json = redis.redis_client.get(table_key)
        
        if not table_data_json:
            return False
            
        # Asegurarse de decodificar solo si es un objeto bytes
        if isinstance(table_data_json, bytes):
            table_data_json = table_data_json.decode('utf-8')
            
        table_data = json.loads(table_data_json)
        
        # Crear clase para el modelo
        class_dict = {
            '__tablename__': table_name
        }
        
        # Crear clase dinámicamente
        ModelClass = type(table_name.capitalize(), (object,), class_dict)
        
        # Añadir a modelos (con thread lock para evitar race conditions)
        global models
        with _cached_models_lock:  # Asumiendo que ya definimos este lock
            models[table_name] = ModelClass
            models[table_name.capitalize()] = ModelClass
            models[f"dbo.{table_name}"] = ModelClass
            models[table_name.lower()] = ModelClass
            
            # También guardar en caché global
            _cached_models[table_name] = ModelClass
            _cached_models[table_name.capitalize()] = ModelClass
            _cached_models[f"dbo.{table_name}"] = ModelClass
            _cached_models[table_name.lower()] = ModelClass
        
        return True
    except Exception as e:
        logger.error(f"Error al crear modelo '{table_name}' en paralelo: {str(e)}")
        return False
def load_cached_schema(redis: RedisService) -> dict:
    """
    Carga el esquema desde Redis.
    
    Args:
        redis: Instancia del servicio Redis
        
    Returns:
        Diccionario con los modelos cacheados
    """
    try:
        # Verificar si hay información de esquema disponible
        ready_flag = redis.redis_client.get("db_models_ready")
        schema_version = redis.redis_client.get("schema_version")
        
        logger.info(f"Intentando cargar esquema de Redis - ready_flag: {ready_flag}, schema_version: {schema_version}")
        
        # Decodificar si es necesario
        if isinstance(ready_flag, bytes):
            ready_flag = ready_flag.decode('utf-8')
        
        if isinstance(schema_version, bytes):
            schema_version = schema_version.decode('utf-8')
            
        # Si el schema_version existe pero ready_flag no, configurarlo
        if schema_version and not ready_flag:
            logger.info("Encontrada versión de esquema pero ready_flag ausente. Estableciendo db_models_ready...")
            redis.redis_client.set("db_models_ready", "1")
            ready_flag = "1"
            
        # Si aún no hay indicación clara de disponibilidad, forzar reflexión
        if not ready_flag and not schema_version:
            logger.warning("No hay suficiente información en Redis para cargar el esquema")
            return {}
        
        # Obtener lista de tablas en el esquema
        schema_data = redis.redis_client.get("db_schema_metadata")
        
        if not schema_data:
            logger.warning("db_schema_metadata no encontrado en Redis")
            
            # Intentar obtener metadatos alternativos
            alt_schema_data = redis.redis_client.get("db_schema")
            if alt_schema_data:
                logger.info("Se encontró 'db_schema' como alternativa")
                schema_data = alt_schema_data
            else:
                # Intentar buscar información en otras claves relacionadas con el esquema
                all_tables = redis.redis_client.smembers("schema:all_tables")
                
                if all_tables:
                    logger.info(f"Encontradas {len(all_tables)} tablas en 'schema:all_tables' aunque 'db_schema_metadata' no existe")
                    # Forzar regeneración parcial del esquema si hay tablas
                    return create_models_from_table_list(redis, all_tables)
                else:
                    logger.warning("No se encontraron metadatos del esquema en Redis")
                    return {}
            
        # Asegurarse de decodificar solo si es un objeto bytes
        if isinstance(schema_data, bytes):
            schema_data = schema_data.decode('utf-8')
        
        logger.info("Metadatos del esquema encontrados, procediendo a cargar...")
        
        try:
            # Cargar metadatos del esquema
            schema_metadata = json.loads(schema_data)
            logger.info(f"Metadatos JSON cargados correctamente. Tablas: {len(schema_metadata.get('tables', {}))}")
        except json.JSONDecodeError as e:
            logger.error(f"Error decodificando JSON del esquema: {str(e)}")
            return {}
        
        # Crear motor de base de datos para asegurar que Base está configurado
        engine = create_engine(settings.DATABASE_URI)
        logger.info("Motor de base de datos creado")
        
        try:
            # Reflejar solo la estructura básica para SQLAlchemy
            metadata = MetaData()
            metadata.reflect(bind=engine, schema='dbo')
            logger.info("Metadata reflejado correctamente")
            
            # Preparar Base con el metadata
            global Base
            Base.prepare(metadata=metadata)
            logger.info("Base preparada correctamente")
        except Exception as e:
            logger.error(f"Error en reflexión básica: {str(e)}")
            logger.info("Intentando continuar con reflexión mínima...")
            
        # Obtener modelos reflejados
        global models
        models.clear()
        
        # Contar modelos para diagnóstico
        model_count = 0
        
        try:
            for cls in Base.classes:
                # Obtener nombre original
                original_name = cls.__name__
                model_count += 1
                
                # Almacenar con múltiples formas para flexibilidad
                models[original_name] = cls           # Nombre original (RupComponente)
                models[original_name.lower()] = cls   # Nombre en minúsculas (rupcomponente)
                
                # También almacenar con prefijo de esquema
                models[f"dbo.{original_name}"] = cls
                models[f"dbo.{original_name.lower()}"] = cls
                
                # IMPORTANTE: Registra los nombres disponibles para depuración
                logger.debug(f"Modelo cargado desde caché: {original_name}")
            
            logger.info(f"Carga desde caché completada. {model_count} modelos de clase, {len(models)} entradas en diccionario.")
        except Exception as e:
            logger.error(f"Error cargando clases de Base: {str(e)}")
            # Intentar crear modelos simples a partir del esquema
            logger.info("Intentando crear modelos simples a partir del esquema")
            
            try:
                # Usar metadata del esquema para crear modelos básicos
                for table_name in schema_metadata.get('tables', {}).keys():
                    models[table_name] = type(table_name.capitalize(), (object,), {'__tablename__': table_name})
                    models[table_name.lower()] = models[table_name]
                    models[f"dbo.{table_name}"] = models[table_name]
                    models[f"dbo.{table_name.lower()}"] = models[table_name]
                    model_count += 1
                
                logger.info(f"Creados {model_count} modelos simples a partir del esquema")
            except Exception as e2:
                logger.error(f"Error creando modelos simples: {str(e2)}")
                
        # Verificar si caja está entre los modelos
        if 'caja' in models:
            logger.info("Modelo 'caja' encontrado correctamente en caché.")
        else:
            logger.warning("Modelo 'caja' NO encontrado en caché. Verificando alternativas.")
            # Buscar variaciones del nombre
            caja_variations = ['Caja', 'CAJA', 'dbo.caja', 'dbo.Caja']
            found = False
            for variant in caja_variations:
                if variant in models:
                    logger.info(f"Modelo 'caja' encontrado como '{variant}'")
                    # Añadir explícitamente como 'caja'
                    models['caja'] = models[variant]
                    found = True
                    break
            
            # Si aún no se encuentra, crear manualmente si los metadatos existen en Redis
            if not found:
                logger.warning("Intentando cargar modelo 'caja' desde metadatos en Redis")
                try:
                    caja_created = create_model_from_redis(redis, engine, 'caja')
                    if caja_created:
                        logger.info("Modelo 'caja' creado manualmente desde Redis")
                    else:
                        logger.warning("No se pudo crear modelo 'caja' desde Redis")
                        # Crear un modelo caja básico como último recurso
                        models['caja'] = type('Caja', (object,), {'__tablename__': 'caja'})
                        logger.info("Modelo 'caja' creado manualmente como último recurso")
                except Exception as e:
                    logger.error(f"Error creando modelo 'caja': {str(e)}")
                    # Crear un modelo caja básico como último recurso
                    models['caja'] = type('Caja', (object,), {'__tablename__': 'caja'})
                    logger.info("Modelo 'caja' creado manualmente como último recurso")
            
        logger.info(f"Esquema cargado desde caché. {len(models)} modelos disponibles.")
        return models
        
    except Exception as e:
        logger.error(f"Error cargando esquema desde caché: {str(e)}")
        # Intentar crear modelos manualmente desde Redis
        try:
            create_models_from_redis(redis)
            return models
        except Exception as manual_e:
            logger.error(f"También falló la creación manual: {str(manual_e)}")
            return {}
        
def create_models_from_table_list(redis: RedisService, table_names: list) -> dict:
    """
    Crea modelos simples a partir de una lista de nombres de tablas.
    
    Args:
        redis: Instancia del servicio Redis
        table_names: Lista de nombres de tablas
        
    Returns:
        Diccionario con los modelos creados
    """
    try:
        global models
        models.clear()
        
        # Decodificar nombres de tablas si es necesario
        decoded_names = []
        for name in table_names:
            if isinstance(name, bytes):
                decoded_names.append(name.decode('utf-8'))
            else:
                decoded_names.append(name)
        
        logger.info(f"Creando modelos para {len(decoded_names)} tablas")
        
        # Crear modelos básicos para cada tabla
        for table_name in decoded_names:
            try:
                model_class = type(table_name.capitalize(), (object,), {
                    '__tablename__': table_name
                })
                models[table_name] = model_class
                models[table_name.lower()] = model_class
                models[f"dbo.{table_name}"] = model_class
                models[f"dbo.{table_name.lower()}"] = model_class
            except Exception as e:
                logger.warning(f"Error creando modelo para '{table_name}': {str(e)}")
        
        # Asegurarse de que 'caja' está presente
        if 'caja' not in models and decoded_names:
            # Buscar alguna tabla que contenga "caja"
            caja_tables = [t for t in decoded_names if "caja" in t.lower()]
            if caja_tables:
                # Usar la primera tabla con "caja" en el nombre
                models['caja'] = models[caja_tables[0]]
                logger.info(f"Modelo 'caja' asociado a {caja_tables[0]}")
            else:
                # Crear un modelo caja básico
                models['caja'] = type('Caja', (object,), {'__tablename__': 'caja'})
                logger.info("Modelo 'caja' creado manualmente como reserva")
        
        logger.info(f"Creados {len(models)} modelos a partir de lista de tablas")
        return models
    except Exception as e:
        logger.error(f"Error creando modelos desde lista: {str(e)}")
        return {}
           
def get_schema_version(engine) -> str:
    """
    Obtiene una versión simplificada del esquema que sea más estable.
    """
    try:
        with engine.connect() as conn:
            # 1. Obtener conteo de tablas
            result = conn.execute(text("""
                SELECT COUNT(*) as table_count
                FROM sys.tables 
                WHERE is_ms_shipped = 0
            """))
            table_count = result.scalar()
            
            # 2. Obtener el máximo object_id como indicador general de cambios en el esquema
            result = conn.execute(text("""
                SELECT MAX(object_id) as max_id
                FROM sys.tables
                WHERE is_ms_shipped = 0
            """))
            max_id = result.scalar()
            
            # Generar versión simplificada
            version = f"{table_count}_{max_id}"
            logger.info(f"Versión de esquema generada: {version}")
            return version
            
    except Exception as e:
        logger.error(f"Error obteniendo versión del esquema: {str(e)}")
        import time
        return f"error_{int(time.time())}"
      
async def process_and_cache_schema(metadata: MetaData, version: str, redis: RedisService):
    """
    Procesa y almacena el esquema en Redis en segundo plano.
    
    Args:
        metadata: Objeto MetaData de SQLAlchemy
        version: Versión del esquema
        redis: Servicio Redis
    """
    try:
        # Preparar metadatos
        schema_metadata = {
            "tables": {},
            "version": version,
            "timestamp": int(asyncio.get_event_loop().time())
        }
        
        # Procesar tablas
        for table_name, table in metadata.tables.items():
            # Eliminar prefijos de esquema si existen
            clean_name = table_name.split(".")[-1].lower() # Convertir a minúsculas
            
            # Guardar metadatos básicos de la tabla
            schema_metadata["tables"][clean_name] = {
                "name": clean_name,
                "columns": [
                    {"name": c.name, "type": str(c.type)} 
                    for c in table.columns
                ]
            }
        
        # Guardar en Redis
        redis.redis_client.set("db_schema_metadata", json.dumps(schema_metadata))
        redis.redis_client.set("schema_version", version)
        
        # Asegurarse de que db_models_ready esté configurado
        redis.redis_client.set("db_models_ready", "1")
        
        logger.info(f"Esquema procesado y almacenado en Redis: {len(schema_metadata['tables'])} tablas")
        
    except Exception as e:
        logger.error(f"Error al procesar y almacenar esquema: {str(e)}")
    """
    Procesa y almacena el esquema en Redis (versión síncrona)
    """
    try:
        schema_metadata = {
            "tables": {},
            "version": version,
            "timestamp": time.time()
        }
        
        for table_name, table in metadata.tables.items():
            clean_name = table_name.split(".")[-1].lower()
            schema_metadata["tables"][clean_name] = {
                "name": clean_name,
                "columns": [
                    {"name": c.name, "type": str(c.type)} 
                    for c in table.columns
                ]
            }
        
        # Guardar en Redis
        redis.redis_client.set("db_schema_metadata", json.dumps(schema_metadata))
        redis.redis_client.set("schema_version", version)
        redis.redis_client.set("db_models_ready", "1")  # Mover aquí
        
        logger.info(f"Esquema almacenado en Redis: {len(schema_metadata['tables'])} tablas")
        
    except Exception as e:
        logger.error(f"Error al procesar esquema: {str(e)}")
        raise