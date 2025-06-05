from typing import AsyncGenerator
import asyncio
import os
import sys
import logging
import urllib.parse
import re
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from fastapi import HTTPException
from cryptography.fernet import Fernet

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.core.config import settings
from app.core import global_vars

# Configurar logger
logger = logging.getLogger(__name__)

# Configurar Fernet para descifrado
if os.getenv("FERNET_KEY"):
    encryption_key = os.getenv("FERNET_KEY").encode("utf-8")
    cipher_suite = Fernet(encryption_key)
else:
    logger.warning("FERNET_KEY no está definido. No se podrá descifrar información.")
    cipher_suite = None

# Convertir cadena de conexión a formato adecuado para async (PostgreSQL)
def get_async_db_uri(uri: str) -> str:
    """Convierte una URI de base de datos en su equivalente para controladores asíncronos"""
    # Convertir PostgreSQL a asyncpg
    if uri.startswith("postgresql://"):
        return uri.replace("postgresql://", "postgresql+asyncpg://")
    # Para MySQL
    elif uri.startswith("mysql://"):
        return uri.replace("mysql://", "mysql+aiomysql://")
    # Para SQLite
    elif uri.startswith("sqlite://"):
        return uri.replace("sqlite://", "sqlite+aiosqlite://")
    # Para SQL Server con pyodbc u otros drivers sin soporte asíncrono
    elif uri.startswith("mssql+pyodbc://") or uri.startswith("mssql://"):
        logger.warning("MSSQL con pyodbc no tiene soporte asíncrono nativo. Usando emulación.")
        return uri
    else:
        # Para otras bases de datos, intentamos determinar el dialecto
        match = re.match(r'^(\w+)(\+\w+)?://', uri)
        if match:
            dialect = match.group(1)
            logger.warning(f"Dialecto '{dialect}' sin soporte asíncrono conocido. Usando emulación.")
            return uri
        else:
            raise ValueError(f"No se pudo determinar el dialecto para: {uri}")

# Creamos un engine síncrono para los casos de drivers sin soporte asíncrono
is_mssql = settings.DATABASE_URI.startswith("mssql")
if is_mssql:
    logger.info("Configurando para SQL Server con emulación asíncrona")
    
    # Modificamos las opciones de conexión para MSSQL
    connect_args = {
        "timeout": 30,
    }
    
    # Añadir opciones para mejorar el manejo de múltiples consultas si es MSSQL con pyodbc
    if "pyodbc" in settings.DATABASE_URI:
        # Usar autocommit para cerrar resultados después de cada consulta
        connect_args["autocommit"] = True
        # Usar fast_executemany para mejorar rendimiento en operaciones de bulk
        connect_args["fast_executemany"] = True
    
    sync_engine = create_engine(
        settings.DATABASE_URI,
        echo=False,
        poolclass=NullPool,
        connect_args=connect_args
    )
    
    # Crear sesión síncrona
    SyncSessionLocal = sessionmaker(
        bind=sync_engine,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False
    )

    # Creamos un wrapper asíncrono para ejecutar código síncrono en threads
    async def run_sync(callable_obj, *args, **kwargs):
        """Ejecuta una función síncrona en un thread"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: callable_obj(*args, **kwargs))

# Para casos con drivers que soportan operaciones asíncronas
else:
    logger.info("Configurando para base de datos con soporte asíncrono nativo")
    # Convertir URI y crear engine
    async_db_uri = get_async_db_uri(settings.DATABASE_URI)
    async_engine = create_async_engine(
        async_db_uri,
        echo=False,
        poolclass=NullPool,
        connect_args={
            "timeout": 30,
        }
    )

    # Crear sesión asíncrona
    AsyncSessionLocal = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False, 
        autoflush=False
    )

# Dependencia para sesión de base de datos (versión emulada para MSSQL)
if is_mssql:
    async def get_db() -> AsyncGenerator[object, None]:
        """
        Dependencia de FastAPI que emula una sesión asíncrona para MSSQL.
        Internamente usa una sesión síncrona en threads separados.
        """
        # Creamos una conexión nueva para cada solicitud
        db = SyncSessionLocal()
        try:
            # Creamos un objeto proxy que emula las operaciones asíncronas
            class AsyncSessionEmulator:
                def __init__(self, sync_session):
                    self.sync_session = sync_session
                    self._results = {}  # Para mantener referencias a resultados abiertos
                    self._result_counter = 0
                
                # Método query para compatibilidad con código antiguo
                def query(self, *entities, **kwargs):
                    # Ejecutar la consulta en la sesión síncrona y conservar el acceso a los métodos
                    # habituales como filter(), all(), first(), etc.
                    return self.sync_session.query(*entities, **kwargs)
                
                # Método asíncrono para ejecutar consultas modernas
                async def execute(self, stmt):
                    # Ejecutar en un thread separado y devolver un resultado emulado
                    try:
                        # Usar run_sync para ejecutar en un thread
                        result = await run_sync(self.sync_session.execute, stmt)
                        
                        # Mantener referencia al resultado para evitar que se cierre prematuramente
                        self._result_counter += 1
                        result_id = self._result_counter
                        self._results[result_id] = result
                        
                        # Emular la API de resultados asíncronos
                        class ResultProxy:
                            def __init__(self, parent, result, result_id):
                                self.parent = parent
                                self.result = result
                                self.result_id = result_id
                            
                            def scalars(self):
                                return self
                            
                            def all(self):
                                try:
                                    # Capturar los resultados
                                    if hasattr(self.result, 'fetchall'):
                                        rows = self.result.fetchall()
                                    else:
                                        rows = self.result.all()
                                    
                                    # Liberar el resultado después de obtener los datos
                                    if self.result_id in self.parent._results:
                                        del self.parent._results[self.result_id]
                                    
                                    return rows
                                except Exception as e:
                                    logger.error(f"Error al obtener resultados: {e}")
                                    return []
                            
                            def first(self):
                                try:
                                    # Capturar el primer resultado
                                    if hasattr(self.result, 'fetchone'):
                                        row = self.result.fetchone()
                                    else:
                                        row = self.result.first()
                                    
                                    # Liberar el resultado después de obtener los datos
                                    if self.result_id in self.parent._results:
                                        del self.parent._results[self.result_id]
                                    
                                    return row
                                except Exception as e:
                                    logger.error(f"Error al obtener el primer resultado: {e}")
                                    return None
                        
                        return ResultProxy(self, result, result_id)
                    except Exception as e:
                        logger.error(f"Error al ejecutar consulta: {e}")
                        raise
                
                # Métodos para operaciones de transacción
                async def commit(self):
                    try:
                        await run_sync(self.sync_session.commit)
                    except Exception as e:
                        logger.error(f"Error al hacer commit: {e}")
                        raise
                
                async def rollback(self):
                    try:
                        await run_sync(self.sync_session.rollback)
                    except Exception as e:
                        logger.error(f"Error al hacer rollback: {e}")
                        raise
                
                async def close(self):
                    try:
                        # Liberar todos los resultados pendientes
                        self._results.clear()
                        await run_sync(self.sync_session.close)
                    except Exception as e:
                        logger.error(f"Error al cerrar sesión: {e}")
                        raise
                
                # Añadir soporte para operador 'with'
                async def __aenter__(self):
                    return self
                
                async def __aexit__(self, exc_type, exc_val, exc_tb):
                    await self.close()
            
            # Yield our emulated session
            emulator = AsyncSessionEmulator(db)
            yield emulator
            
            # Commit al final si no hubo excepciones
            await run_sync(db.commit)
        except Exception as e:
            await run_sync(db.rollback)
            logger.error(f"Error en la sesión de base de datos: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Error interno de la base de datos"
            )
        finally:
            # Asegurarnos de cerrar la sesión
            try:
                await run_sync(db.close)
            except Exception as e:
                logger.error(f"Error al cerrar la sesión: {str(e)}")
else:
    # Versión estándar para DBs con soporte asíncrono nativo
    async def get_db() -> AsyncGenerator[AsyncSession, None]:
        """
        Dependencia de FastAPI que proporciona una sesión asíncrona de base de datos.
        """
        async with AsyncSessionLocal() as session:
            try:
                yield session
                await session.commit()
            except Exception as e:
                await session.rollback()
                logger.error(f"Error en la sesión de base de datos: {str(e)}")
                raise HTTPException(
                    status_code=500,
                    detail="Error interno de la base de datos"
                )

# Función de utilidad para probar la conexión
async def test_connection():
    """Prueba la conexión a la base de datos"""
    try:
        if is_mssql:
            # Versión para MSSQL (usando thread)
            def test_sync_connection():
                with sync_engine.connect() as conn:
                    conn.execute("SELECT 1")
                return True
            
            success = await run_sync(test_sync_connection)
            if success:
                logger.info("Conexión a la base de datos exitosa (MSSQL)")
            return success
        else:
            # Versión estándar asíncrona
            async with async_engine.connect() as conn:
                await conn.execute("SELECT 1")
                logger.info("Conexión a la base de datos exitosa")
                return True
    except Exception as e:
        logger.error(f"Error al conectar a la base de datos: {str(e)}")
        return False

# ------------------ Base de datos de usuarios ------------------

# Función para crear un engine para una conexión específica
def create_sync_engine_for_connection(cString):
    """Crea un engine síncrono para una cadena de conexión específica"""
    connect_args = {
        "timeout": 30,
    }
    
    # Añadir opciones para mejorar el manejo de múltiples consultas si es MSSQL con pyodbc
    if cString.startswith("mssql") and "pyodbc" in cString:
        connect_args["autocommit"] = True
        connect_args["fast_executemany"] = True
    
    return create_engine(
        cString,
        echo=False,
        poolclass=NullPool,
        connect_args=connect_args
    )

# Dependencia para obtener una sesión de base de datos de usuario asíncrona
async def uget_db(origin: str = None) -> AsyncGenerator[object, None]:
    """
    Dependencia para obtener una sesión asíncrona de base de datos de usuario.
    
    Args:
        origin: Origen de la solicitud (opcional)
    
    Yields:
        AsyncSession o un emulador: Sesión SQLAlchemy asíncrona o un emulador
    """
    # Get connection parameters for this specific request
    ma = global_vars.get_pdata()
    
    if not cipher_suite:
        raise ValueError("No se ha configurado FERNET_KEY para descifrar conexiones")

    encrypt_data = ma.encode()
    cData = cipher_suite.decrypt(encrypt_data).decode()
    cString = f"{cData}"
    
    # Determinar si es MSSQL
    is_user_mssql = cString.startswith("mssql")
    
    if is_user_mssql:
        # Crear engine y sesión síncrona
        engine = create_sync_engine_for_connection(cString)
        
        SessionMaker = sessionmaker(
            bind=engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False
        )
        
        session = SessionMaker()
        
        try:
            # Para SQL Server, usamos emulación con la misma lógica que en get_db
            class AsyncSessionEmulator:
                def __init__(self, sync_session, engine):
                    self.sync_session = sync_session
                    self.engine = engine
                    self._results = {}
                    self._result_counter = 0
                
                # Soporte para la API antigua (query)
                def query(self, *entities, **kwargs):
                    return self.sync_session.query(*entities, **kwargs)
                
                # Soporte para la API moderna (execute)
                async def execute(self, stmt):
                    # Ejecutar en un thread separado
                    try:
                        result = await run_sync(self.sync_session.execute, stmt)
                        
                        # Mantener referencia al resultado para evitar que se cierre prematuramente
                        self._result_counter += 1
                        result_id = self._result_counter
                        self._results[result_id] = result
                        
                        # Emular la API de resultados asíncronos
                        class ResultProxy:
                            def __init__(self, parent, result, result_id):
                                self.parent = parent
                                self.result = result
                                self.result_id = result_id
                            
                            def scalars(self):
                                return self
                            
                            def all(self):
                                try:
                                    # Capturar los resultados
                                    if hasattr(self.result, 'fetchall'):
                                        rows = self.result.fetchall()
                                    else:
                                        rows = self.result.all()
                                    
                                    # Liberar el resultado después de obtener los datos
                                    if self.result_id in self.parent._results:
                                        del self.parent._results[self.result_id]
                                    
                                    return rows
                                except Exception as e:
                                    logger.error(f"Error al obtener resultados: {e}")
                                    return []
                            
                            def first(self):
                                try:
                                    # Capturar el primer resultado
                                    if hasattr(self.result, 'fetchone'):
                                        row = self.result.fetchone()
                                    else:
                                        row = self.result.first()
                                    
                                    # Liberar el resultado después de obtener los datos
                                    if self.result_id in self.parent._results:
                                        del self.parent._results[self.result_id]
                                    
                                    return row
                                except Exception as e:
                                    logger.error(f"Error al obtener el primer resultado: {e}")
                                    return None
                        
                        return ResultProxy(self, result, result_id)
                    except Exception as e:
                        logger.error(f"Error al ejecutar consulta: {e}")
                        raise
                
                # Métodos de transacción
                async def commit(self):
                    try:
                        await run_sync(self.sync_session.commit)
                    except Exception as e:
                        logger.error(f"Error al hacer commit: {e}")
                        raise
                
                async def rollback(self):
                    try:
                        await run_sync(self.sync_session.rollback)
                    except Exception as e:
                        logger.error(f"Error al hacer rollback: {e}")
                        raise
                
                async def close(self):
                    try:
                        # Liberar todos los resultados pendientes
                        self._results.clear()
                        await run_sync(self.sync_session.close)
                        await run_sync(self.engine.dispose)
                    except Exception as e:
                        logger.error(f"Error al cerrar sesión: {e}")
            
            # Yield nuestro emulador
            emulator = AsyncSessionEmulator(session, engine)
            yield emulator
            
            # Commit al final si no hubo excepciones
            await emulator.commit()
        except Exception as e:
            # Rollback en caso de error
            try:
                await run_sync(session.rollback)
            except:
                pass
            logger.error(f"Error en la sesión de base de datos: {str(e)}")
            raise HTTPException(
                status_code=500, 
                detail="Error interno de la base de datos"
            )
        finally:
            # Cerrar sesión y engine
            try:
                await run_sync(session.close)
                await run_sync(engine.dispose)
            except Exception as e:
                logger.error(f"Error al liberar recursos: {e}")
    else:
        # Para bases de datos con soporte asíncrono nativo
        # Convertir la cadena de conexión para drivers asíncronos
        async_cString = get_async_db_uri(cString)
        async_engine = create_async_engine(
            async_cString,
            echo=False,
            poolclass=NullPool,
            connect_args={
                "timeout": 30,
            }
        )
        
        # Crear session factory para este engine específico
        AsyncSessionL = sessionmaker(
            bind=async_engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
            class_=AsyncSession
        )
        
        # Usar el modo estándar asíncrono
        async with AsyncSessionL() as sdb:
            try:
                yield sdb
                await sdb.commit()
            except Exception as e:
                await sdb.rollback()
                logger.error(f"Error en la sesión de base de datos: {str(e)}")
                raise HTTPException(
                    status_code=500, 
                    detail="Error interno de la base de datos"
                )
            finally:
                await async_engine.dispose()