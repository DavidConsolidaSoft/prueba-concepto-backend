## Contenido

- [Introducción](#introducción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Arquitectura y Patrones](#arquitectura-y-patrones)
- [Flujo de Solicitudes](#flujo-de-solicitudes)
- [Componentes Principales](#componentes-principales)
  - [Archivo Principal (main.py)](#archivo-principal-mainpy)
  - [Configuración (app/core/config.py)](#configuración-appcoreconfigpy)
  - [Base de Datos (app/db/database.py)](#base-de-datos-appdbdatabasepy)
  - [Autenticación (app/api/v1/routers/auth)](#autenticación-appapiv1routersauth)
  - [Modelos y Schemas](#modelos-y-schemas)
- [Características Técnicas Avanzadas](#características-técnicas-avanzadas)
  - [Asíncronia para SQL Server](#emulación-asíncrona-para-sql-server)
  - [Generación Automática de Modelos](#generación-automática-de-modelos)
  - [Comentado de Relaciones](#comentado-de-relaciones)
  - [Autenticación con Azure AD](#autenticación-con-azure-ad)
  - [Multi-tenant y Conexiones Dinámicas](#multi-tenant-y-conexiones-dinámicas)
- [Dominios Funcionales](#dominios-funcionales)
  - [Facturación](#facturación)
  - [Clientes](#clientes)
  - [Productos](#productos)
  - [Formas de Pago](#formas-de-pago)
  - [Tipos de Documento](#tipos-de-documento)
- [Guía de Desarrollo](#guía-de-desarrollo)
  - [Configuración del Entorno](#configuración-del-entorno)
  - [Estructura de Nuevos Endpoints](#estructura-de-nuevos-endpoints)
  - [Trabajando con los Modelos](#trabajando-con-los-modelos)
  - [Debugging](#debugging)
- [Prácticas Recomendadas](#prácticas-recomendadas)
  - [Estructura y Organización](#estructura-y-organización)
  - [Manejo de Errores](#manejo-de-errores)
  - [Optimización de Rendimiento](#optimización-de-rendimiento)
  - [Seguridad](#seguridad)

## Introducción

Este documento sirve como guía para incorporarse al desarrollo del backend de ConsolidaERP, una API desarrollada con FastAPI. La aplicación está diseñada como un servidor API RESTful que permite a los clientes (web, móvil y sistemas ERP) conectarse y realizar operaciones CRUD sobre los datos de la empresa. 

El backend está construido con FastAPI y SQLAlchemy, con soporte para múltiples sistemas de base de datos, aunque está optimizado para SQL Server. La arquitectura está diseñada para ser modular, escalable y fácil de mantener, siguiendo las mejores prácticas de desarrollo de APIs modernas.

## Estructura del Proyecto

```
consolidaerp-api/
├── _pycache_
├── .github
├── app/
│   ├── _pycache_
│   ├── api/
│   │   ├── _pycache_
│   │   ├── v1/
│   │   │   ├── _pycache_
│   │   │   ├── routers/      # Endpoints de la API organizados por dominio
│   │   │   │   ├── ai/       # Funcionalidades de inteligencia artificial
│   │   │   │   ├── auth/     # Autenticación con Azure AD
│   │   │   │   ├── clientes/ # Gestión de clientes
│   │   │   │   ├── facturacion/ # Sistema de facturación
│   │   │   │   ├── formaPago/ # Métodos de pago
│   │   │   │   ├── productos/ # Gestión de productos
│   │   │   │   ├── tipoDocumento/ # Tipos de documentos
│   │   │   │   ├── vendedores/ # Gestión de vendedores
│   │   │   │   └── ...
│   │   │   ├── services/     # Servicios de lógica de negocio
│   │   │   └── ...
│   ├── auth/                 # Sistema central de autenticación
│   ├── core/                 # Configuración central
│   │   ├── config.py         # Configuración central (Pydantic)
│   │   ├── global_vars.py    # Variables globales
│   ├── db/                   # Configuración de base de datos
│   │   ├── base.py           # Configuración de conexión
│   │   ├── database.py       # Gestión de sesiones y async
│   ├── models/               # Modelos SQLAlchemy (ORM)
│   │   ├── dbo/              # Modelos autogenerados para el esquema dbo
│   │   ├── facturacion/      # Modelos específicos para facturación
│   │   ├── base.py           # Clase base para todos los modelos
│   ├── schemas/              # Schemas Pydantic para validación
│   ├── services/             # Servicios comunes para toda la aplicación
│   ├── tests/                # Pruebas automatizadas
│   ├── utils/                # Utilidades y helpers
│   │   ├── comment_all_relationships.py  # Herramienta para modelos
├── env/                      # Entorno virtual (no incluido en git)
├── _init_.py                 # Define el proyecto como paquete Python
├── .env                      # Variables de entorno (no incluido en git)
├── .gitignore                # Archivos ignorados por git
├── auto_generate_models.py   # Script para generar modelos desde BD
├── fix_column_imports.py     # Script para arreglar importaciones
├── generate_models.py        # Script adicional para generación
├── main.py                   # Punto de entrada de la aplicación
├── README.md                 # Documentación básica
├── requirements.txt          # Dependencias del proyecto
└── schema_info.json          # Información de esquema de BD
```

## Arquitectura y Patrones

El proyecto sigue una arquitectura de capas clara:

### 1. Routers (Controladores)

Los routers definen los endpoints HTTP y manejan las solicitudes entrantes:

- Ubicados en `app/api/v1/routers/`
- Organizados por dominio de negocio (clientes, facturación, etc.)
- Se encargan de la validación inicial de datos usando Pydantic
- Convierten las solicitudes HTTP en llamadas a servicios

Ejemplo de router:
```python
@router.get("/clientes/{cliente_id}", response_model=ClienteResponse)
async def get_cliente(
    cliente_id: str,
    empresa_id: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db)
):
    """Obtiene un cliente específico por su ID dentro de una empresa."""
    service = ClientesServiceORM(db)
    cliente_dict = service.get_cliente_by_id(cliente_id, empresa_id)
    
    if not cliente_dict:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return ClienteDetalle.model_validate(cliente_dict)
```

### 2. Services (Servicios)

Los servicios contienen toda la lógica de negocio:

- Ubicados en `app/api/v1/services/` y `app/services/`
- Implementan operaciones de negocio específicas
- Abstraen la interacción con los modelos y la base de datos
- Manejan transacciones y validaciones complejas

Ejemplo de servicio:
```python
def get_cliente_by_id(self, cliente_id: str, empresa_id: int) -> Optional[Dict]:
    """Obtiene un cliente específico por su ID, dentro de una empresa específica."""
    try:
        # Importar modelos relacionados
        from app.models.dbo.tipcli import TipCli
        from app.models.dbo.municip import Municip
        from app.models.dbo.depto import Depto
        
        # Consulta con joins a tablas relacionadas
        query = self.db.query(
            Clientes,
            TipCli.ntipcli,
            Municip.nmunicip,
            Depto.ndepto
        ).outerjoin(
            TipCli, Clientes.tipcli == TipCli.tipcli
        ).outerjoin(
            Municip, Clientes.municip == Municip.municip
        ).outerjoin(
            Depto, Municip.depto == Depto.depto
        ).filter(
            Clientes.clientes == cliente_id,
            Clientes.empresa == empresa_id
        )
        
        result = query.first()
        # ... procesamiento adicional...
        return cliente_dict
    except Exception as e:
        print(f"Error al obtener cliente: {str(e)}")
        return None
```

### 3. Models (Modelos)

Los modelos representan las entidades de la base de datos:

- Ubicados en `app/models/`
- Implementados usando SQLAlchemy ORM
- La mayoría son generados automáticamente con `auto_generate_models.py`
- Representan directamente tablas de la base de datos

Ejemplo de modelo:
```python
class Cliente(Base):
    __tablename__ = "Clientes"
    __table_args__ = {"schema": "dbo"}
    
    clientes = Column(String(20), primary_key=True)
    empresa = Column(Integer, primary_key=True)
    nclientes = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    direccion = Column(String(250))
    telefono1 = Column(String(15))
    # ... más campos ...
```

### 4. Schemas (Esquemas)

Los esquemas definen la estructura de las solicitudes y respuestas:

- Implementados usando Pydantic
- Proporcionan validación automática de datos
- Definen la estructura de las respuestas API
- Permiten conversión entre objetos SQLAlchemy y JSON

Ejemplo de esquema:
```python
class ClienteBase(BaseModel):
    nclientes: Optional[str] = None
    propietario: Optional[str] = ""
    activo: Optional[bool] = True
    direccion: Optional[str] = ""
    telefono1: Optional[str] = ""
    email: Optional[str] = None
    # ... más campos ...
    
    class Config:
        from_attributes = True

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    clientes: str
    empresa: int
    # ... campos adicionales ...
```

### Patrones Adicionales

El proyecto también implementa:

- **Dependency Injection**: A través del sistema de dependencias de FastAPI
- **Repository Pattern**: Abstracción del acceso a datos en los servicios
- **Middleware**: Para CORS, manejo de excepciones y autenticación
- **Async/Await**: Operaciones asíncronas nativas para SQL Server

## Flujo de Solicitudes

Este diagrama ilustra el flujo típico de una solicitud a través del sistema:

1. **Recepción**: Una solicitud HTTP llega a un endpoint definido en un router.
2. **Validación**: FastAPI valida los parámetros y el cuerpo de la solicitud usando Pydantic.
3. **Autenticación**: El middleware JWT verifica el token de acceso (en rutas protegidas).
4. **Servicio**: El router llama a un servicio para procesar la lógica de negocio.
5. **Base de Datos**: El servicio interactúa con los modelos SQLAlchemy y la base de datos.
6. **Respuesta**: Los datos resultantes se convierten a JSON y se devuelven al cliente.

Ejemplo de flujo completo:

```python
# 1. Endpoint en el router
@router.get("/facturas/{factura_id}", response_model=FacturaDetalle)
async def get_factura_detalle(
    factura_id: int,
    empresa: int = Query(..., description="ID de la empresa"),
    db: Session = Depends(get_db)
):
    try:
        # 2. Llamada al servicio
        service = FacturaServiceSimpleORM(db)
        factura_detalle = service.get_factura_detalle(
            factura_id=factura_id,
            empresa=empresa
        )
        
        # 3. Manejo de errores
        if not factura_detalle:
            raise HTTPException(
                status_code=404,
                detail=f"Factura {factura_id} no encontrada"
            )
        
        # 4. Retorno de la respuesta
        return factura_detalle
        
    except HTTPException:
        raise
    except Exception as e:
        # 5. Manejo de excepciones inesperadas
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener el detalle de la factura: {str(e)}"
        )
```

## Componentes Principales

### Archivo Principal (main.py)

El archivo `main.py` es el punto de entrada de la aplicación. Sus responsabilidades clave incluyen:

1. **Inicialización de la aplicación FastAPI**:
   ```python
   app = FastAPI(
       debug=True,
       title=API_TITLE,
       description=API_DESCRIPTION,
       version=API_VERSION,
       lifespan=lifespan
   )
   ```

2. **Manejo del ciclo de vida de la aplicación**:
   ```python
   @asynccontextmanager
   async def lifespan(app: FastAPI):
       # Código que se ejecuta al inicio
       logger.info("Ejecutando código de inicio del ciclo de vida...")
       
       # Inicializar servicios opcionales
       if USE_REDIS_SERVICES:
           await initialize_services()
       
       # Almacenar procesador en app.state
       if enhanced_processor:
           app.state.enhanced_processor = enhanced_processor
       
       yield
       
       # Código que se ejecuta al cierre
       logger.info("Ejecutando código de cierre del ciclo de vida...")
   ```

3. **Carga condicional de servicios**:
   ```python
   # Flag para servicios opcionales
   USE_REDIS_SERVICES = os.getenv("USE_REDIS_SERVICES", "False").lower() == "true"
   USE_AI_SERVICES = os.getenv("USE_AI_SERVICES", "False").lower() == "true"
   
   # Cargar servicios condicionalmente
   if USE_AI_SERVICES:
       try:
           from app.api.v1.routers.ai.query_processor import QueryProcessor
           # ...
       except Exception as e:
           logger.error(f"Error al inicializar procesador de consultas: {str(e)}")
   ```

4. **Registro de rutas (routers)**:
   ```python
   # Incluir routers
   if api_router:
       app.include_router(api_router, prefix="/api/v1")
   ```

5. **Configuración de middleware**:
   ```python
   # Configurar CORS
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5000", "https://siscal-agent-ai.siscal.one"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

6. **Manejo global de excepciones**:
   ```python
   @app.exception_handler(Exception)
   async def global_exception_handler(request, exc):
       logger.error(f"Error no controlado: {str(exc)}", exc_info=True)
       return HTTPException(
           status_code=500,
           detail="Error interno del servidor"
       )
   ```

### Configuración (app/core/config.py)

El archivo `config.py` utiliza Pydantic para la validación y gestión de configuración:

```python
class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Azure Consolida ERP"
   
    # Database
    DB_DRIVER: str = "ODBC Driver 18 for SQL Server"
    DB_SERVER: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
   
    # Azure AD
    AZURE_CLIENT_ID: str
    AZURE_CLIENT_SECRET: str
    AZURE_TENANT_ID: str
    AZURE_REDIRECT_URI: str = "https://siscal-agent-ai.siscal.one/api/v1/auth/callback"
    
    # ... más configuraciones ...

    @property
    def DATABASE_URI(self):
        from urllib.parse import quote_plus
        password_encoded = quote_plus(self.DB_PASSWORD)
        return (
            f"mssql+pyodbc://{self.DB_USER}:{password_encoded}"
            f"@{self.DB_SERVER}:1433/{self.DB_NAME}?"
            f"driver={self.DB_DRIVER}&Encrypt=yes&TrustServerCertificate=no"
        )
```

Ventajas de usar Pydantic para la configuración:
- Validación automática de tipos
- Valores por defecto
- Carga desde variables de entorno
- Propiedad calculada para la cadena de conexión

### Base de Datos (app/db/database.py)

Este componente maneja la conexión a la base de datos y proporciona sesiones:

1. **Detección automática del tipo de base de datos**:
   ```python
   def get_async_db_uri(uri: str) -> str:
       """Convierte una URI de base de datos en su equivalente para controladores asíncronos"""
       # Convertir PostgreSQL a asyncpg
       if uri.startswith("postgresql://"):
           return uri.replace("postgresql://", "postgresql+asyncpg://")
       # Para MySQL
       elif uri.startswith("mysql://"):
           return uri.replace("mysql://", "mysql+aiomysql://")
       # ...
   ```

2. **asíncrona para SQL Server**:
   ```python
   # Solo para SQL Server
   if is_mssql:
       async def get_db() -> AsyncGenerator[object, None]:
           db = SyncSessionLocal()
           try:
               # Creamos un objeto proxy que emula las operaciones asíncronas
               class AsyncSessionEmulator:
                   # ... implementación de la emulación ...
               
               emulator = AsyncSessionEmulator(db)
               yield emulator
               await run_sync(db.commit)
           except Exception as e:
               await run_sync(db.rollback)
               # ... manejo de errores ...
   ```

3. **Dependencia para inyectar sesiones de base de datos**:
   ```python
   # Para bases de datos con soporte asíncrono nativo
   async def get_db() -> AsyncGenerator[AsyncSession, None]:
       async with AsyncSessionLocal() as session:
           try:
               yield session
               await session.commit()
           except Exception as e:
               await session.rollback()
               logger.error(f"Error en la sesión de base de datos: {str(e)}")
               raise HTTPException(status_code=500, detail="Error interno de la base de datos")
   ```

4. **Conexiones dinámicas para multi-tenant**:
   ```python
   async def uget_db(origin: str = None) -> AsyncGenerator[object, None]:
       # Obtener parámetros de conexión para esta solicitud
       ma = global_vars.get_pdata()
       
       # Descifrar cadena de conexión
       encrypt_data = ma.encode()
       cData = cipher_suite.decrypt(encrypt_data).decode()
       cString = f"{cData}"
       
       # Crear engine y sesión según el tipo de base de datos
       # ...
   ```

### Autenticación (app/api/v1/routers/auth)

El sistema de autenticación implementa integración con Microsoft Entra ID (Azure AD):

1. **azure_auth.py**: 
   - Implementa la integración con Azure AD
   - Maneja el flujo OAuth 2.0
   - Verifica tokens de ID

   ```python
   def get_auth_url():
       """Genera la URL para iniciar el flujo de autenticación con Azure AD"""
       params = {
           "client_id": settings.AZURE_CLIENT_ID,
           "response_type": "code",
           "redirect_uri": settings.AZURE_REDIRECT_URI,
           "response_mode": "query",
           "scope": "openid profile email offline_access User.Read",
           "state": "12345"  # En producción, debería ser un valor aleatorio
       }
       return f"{AUTH_ENDPOINT}?{urlencode(params)}"
   ```

2. **jwt_handler.py**: 
   - Crea y verifica tokens JWT para uso interno
   - Maneja caducidad y renovación de tokens

   ```python
   def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
       """Crea un token JWT con los datos proporcionados"""
       to_encode = data.copy()
       if expires_delta:
           expire = datetime.now(timezone.utc) + expires_delta
       else:
           expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
      
       to_encode.update({"exp": expire})
       encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
       return encoded_jwt
   ```

3. **router.py**: 
   - Define endpoints de autenticación
   - Maneja callbacks de Azure AD
   - Gestiona sesiones de usuario

   ```python
   @router.get("/callback")
   async def callback(
       request: Request, 
       code: str = None, 
       error: str = None,
       db: Session = Depends(get_db)
   ):
       """Maneja la respuesta de Azure AD después del inicio de sesión."""
       if error:
           logger.error(f"Error en autenticación: {error}")
           return {"error": error}
       
       # Obtener tokens de Azure AD
       tokens = await get_token(code)
       
       # Validar token ID y obtener claims
       claims = validate_token(tokens["id_token"])
       
       # Obtener información adicional del usuario
       user_info = await get_user_info(tokens["access_token"])
       
       # Crear o actualizar usuario en la base de datos
       db_user = await usuario_service.get_or_create_user(...)
       
       # Crear token JWT propio
       jwt_token = create_access_token(...)
       
       # ...
   ```

### Modelos y Schemas

1. **SQLAlchemy Models** (app/models/):
   - Representan tablas de la base de datos
   - La mayoría generados automáticamente
   - Ejemplo:
   ```python
   class Factura(Base):
       __tablename__ = "Factura"
       __table_args__ = {"schema": "dbo"}
       
       factura = Column(Integer, primary_key=True)
       empresa = Column(Integer, primary_key=True)
       numedocu = Column(String(15), nullable=False)
       fecha = Column(DateTime, nullable=False)
       # ... más columnas ...
   ```

2. **Pydantic Schemas** (app/schemas/ y app/models/facturacion/):
   - Definen la estructura de entrada/salida de API
   - Proporcionan validación automática
   - Ejemplo:
   ```python
   class FacturaListItem(BaseModel):
       """Modelo simplificado para la lista de facturas"""
       empresa: int
       factura: int
       numedocu: str
       fecha: datetime
       nombre_cliente: str
       nombre_vendedor: str
       monto_total: float
       estado: str  # "Abierta", "Cerrada", "Nula"
       impresa: bool
       nula: bool
       # ... más campos ...
       
       class Config:
           from_attributes = True
   ```

## Características Técnicas Avanzadas

### Asíncronia para SQL Server

La aplicación implementa un sistema de asincronia que ejecuta operaciones en hilos separados pero mantiene una interfaz asíncrona consistente:

```python
# Solo para SQL Server
async def get_db() -> AsyncGenerator[object, None]:
    db = SyncSessionLocal()
    try:
        class AsyncSessionEmulator:
            def __init__(self, sync_session):
                self.sync_session = sync_session
                self._results = {}
                self._result_counter = 0
            
            # Método query para compatibilidad con código antiguo
            def query(self, *entities, **kwargs):
                return self.sync_session.query(*entities, **kwargs)
            
            # Método asíncrono para ejecutar consultas modernas
            async def execute(self, stmt):
                # Ejecutar en un thread separado
                result = await run_sync(self.sync_session.execute, stmt)
                # ... resto del código ...
                
        emulator = AsyncSessionEmulator(db)
        yield emulator
        await run_sync(db.commit)
    except Exception as e:
        await run_sync(db.rollback)
        # ... manejo de errores ...
```

Este enfoque permite:
- Usar una API asíncrona consistente en toda la aplicación
- Aprovechar async/await en FastAPI
- Mantener compatibilidad con SQL Server

### Generación Automática de Modelos

El script `auto_generate_models.py` automatiza la creación de modelos SQLAlchemy a partir del esquema de la base de datos:

1. **Inspección del esquema**:
   ```python
   def get_schema_info(self):
       """Obtiene información completa del esquema"""
       schemas = self.inspector.get_schema_names()
       
       # Filtrar esquemas del sistema
       system_schemas = [
           'information_schema', 'sys', 'guest', 'db_accessadmin', 
           # ...
       ]
       
       for schema in schemas:
           if schema not in system_schemas:
               # Procesar tablas del esquema
               # ...
   ```

2. **Generación de código Python**:
   ```python
   def _generate_model_code(self, schema, table_name, table_data):
       """Genera el código del modelo para una tabla"""
       class_name = self._to_class_name(table_name)
       
       code = []
       code.append("# Generado automáticamente")
       code.append(f"# Tabla: {schema}.{table_name}")
       
       # Imports
       # Columnas
       # Relaciones
       # ...
       
       return '\n'.join(code)
   ```

3. **Organización por esquemas**:
   ```python
   def generate_sqlalchemy_models(self, output_dir='app/models'):
       """Genera archivos de modelos SQLAlchemy"""
       os.makedirs(output_dir, exist_ok=True)
       
       # Generar archivo base.py
       # ...
       
       # Generar modelos por esquema
       for schema, schema_data in self.schema_info.items():
           schema_dir = os.path.join(output_dir, schema.lower())
           os.makedirs(schema_dir, exist_ok=True)
           
           # Generar modelos para cada tabla
           # ...
   ```

4. **Documentación automática**:
   ```python
   def _generate_documentation(self, output_dir):
       """Genera documentación del esquema"""
       doc_path = os.path.join(output_dir, 'schema_documentation.md')
       
       with open(doc_path, 'w', encoding='utf-8') as f:
           f.write("# Documentación del Esquema de Base de Datos\n\n")
           # ... detalles por esquema y tabla ...
   ```

### Comentado de Relaciones

Para evitar problemas de referencias circulares en los modelos generados automáticamente, se incluye un script `comment_all_relationships.py` que comenta todas las relaciones:

```python
def comment_all_relationships(models_dir='app/models/dbo'):
    """Comenta todas las relaciones en todos los archivos de modelos"""
    fixed_count = 0
   
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(models_dir, filename)
            modified = False
           
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
               
                # Comentar import de relationship
                if 'from sqlalchemy.orm import relationship' in content:
                    content = re.sub(
                        r'from sqlalchemy\.orm import relationship',
                        '# from sqlalchemy.orm import relationship  # Comentado temporalmente',
                        content
                    )
                    modified = True
               
                # Encontrar y comentar todas las relaciones
                relationship_pattern = r'(\s*)(\w+)\s*=\s*relationship\([^)]+\)'
                # ...
```

### Autenticación con Azure AD

La implementación de autenticación con Microsoft Entra ID (Azure AD) sigue el flujo OAuth 2.0:

1. **Inicio de sesión**:
   ```python
   @router.get("/login")
   async def login():
       """Inicia el flujo de autenticación con Azure AD."""
       auth_url = get_auth_url()
       return RedirectResponse(url=auth_url)
   ```

2. **Manejo de callback**:
   ```python
   @router.get("/callback")
   async def callback(
       request: Request, 
       code: str = None, 
       error: str = None,
       db: Session = Depends(get_db)
   ):
       # Obtener tokens de Azure AD
       result = await azure_auth.authenticate_azure_user(code, db, redirect_uri)
       
       # ... procesar resultado y crear token JWT ...
       
       # Devolver respuesta adecuada según el tipo de cliente (web o móvil)
       return azure_auth.create_response_html("success", success_response, redirect_uri)
   ```

3. **Verificación de token**:
   ```python
   def verify_token(token: str)

3. **Verificación de token**:
   ```python
   def verify_token(token: str) -> dict:
       """Verifica un token JWT y retorna los datos decodificados"""
       try:
           payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
           return payload
       except JWTError:
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Could not validate credentials",
               headers={"WWW-Authenticate": "Bearer"},
           )
   ```

4. **Información del usuario autenticado**:
   ```python
   @router.get("/me", response_model=None)
   async def get_current_user_info(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
       """Devuelve la información completa del usuario autenticado"""
       try:
           # Verificamos el token JWT y obtenemos los datos
           payload = jwt_handler.verify_token(token)
           email = payload.get("sub")
           user_id = payload.get("user_id")
           empresa_id = payload.get("empresa_id")
           
           # ... obtener información detallada del usuario y la empresa ...
           
           return {
               "user": { ... },
               "empresa_actual": empresa,
               "empresas_disponibles": empresas_disponibles,
               "token_data": { ... }
           }
       except Exception as e:
           # ... manejo de errores ...
   ```

### Multi-tenant y Conexiones Dinámicas

La aplicación implementa un sistema multi-tenant que permite conexiones a diferentes bases de datos según el contexto:

1. **Conexiones dinámicas** para diferentes empresas/usuarios:
   ```python
   async def uget_db(origin: str = None) -> AsyncGenerator[object, None]:
       """Dependencia para obtener una sesión asíncrona de base de datos de usuario."""
       # Obtener parámetros de conexión específicos para esta solicitud
       ma = global_vars.get_pdata()
       
       if not cipher_suite:
           raise ValueError("No se ha configurado FERNET_KEY para descifrar conexiones")

       # Descifrar la cadena de conexión
       encrypt_data = ma.encode()
       cData = cipher_suite.decrypt(encrypt_data).decode()
       cString = f"{cData}"
       
       # Determinar el tipo de base de datos y crear la conexión adecuada
       # ...
   ```

2. **Cifrado de credenciales** de conexión:
   ```python
   # Configurar Fernet para descifrado
   if os.getenv("FERNET_KEY"):
       encryption_key = os.getenv("FERNET_KEY").encode("utf-8")
       cipher_suite = Fernet(encryption_key)
   else:
       logger.warning("FERNET_KEY no está definido. No se podrá descifrar información.")
       cipher_suite = None
   ```

3. **Cambio de empresa** para el usuario:
   ```python
   @router.post("/switch-company")
   async def switch_company(data: dict, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
       """Permite al usuario cambiar entre empresas a las que tiene acceso"""
       try:
           empresa_id = data.get("empresa_id")
           # ... verificar acceso y obtener datos de la empresa ...
           
           # Crear un nuevo token con la información actualizada
           jwt_token = jwt_handler.create_access_token(data=jwt_data)
           
           return {
               "access_token": jwt_token,
               "token_type": "bearer",
               "user_info": { ... },
               "empresa_info": empresa_info
           }
       except Exception as e:
           # ... manejo de errores ...
   ```

## Dominios Funcionales

### Facturación

El módulo de facturación (`app/api/v1/routers/facturacion/`) gestiona todo lo relacionado con facturas:

1. **Listado de Facturas**:
   ```python
   @router.get("/lista", response_model=List[FacturaListItem])
   async def get_facturas(
       fecha_inicio: Optional[date] = Query(None),
       fecha_fin: Optional[date] = Query(None),
       cliente: Optional[str] = Query(None),
       pedido: Optional[str] = Query(None),
       # ... más parámetros de filtro ...
       db: Session = Depends(get_db)
   ):
       """Obtiene la lista de facturas filtradas por los parámetros especificados."""
       try:
           # ... código para obtener facturas ...
           
           service = FacturaServiceSimpleORM(db)
           facturas = service.get_facturas_list(
               empresa=empresa,
               fecha_inicio=fecha_inicio_dt,
               fecha_fin=fecha_fin_dt,
               # ... más parámetros ...
           )
           
           # ... filtrado adicional ...
           
           return facturas
       except Exception as e:
           # ... manejo de errores ...
   ```

2. **Detalle de Factura**:
   ```python
   @router.get("/detalle/{factura_id}", response_model=FacturaDetalle)
   async def get_factura_detalle(
       factura_id: int,
       empresa: int = Query(..., description="ID de la empresa"),
       db: Session = Depends(get_db)
   ):
       """Obtiene el detalle completo de una factura específica."""
       try:
           service = FacturaServiceSimpleORM(db)
           factura_detalle = service.get_factura_detalle(
               factura_id=factura_id,
               empresa=empresa
           )
           
           if not factura_detalle:
               raise HTTPException(
                   status_code=404,
                   detail=f"Factura {factura_id} no encontrada"
               )
           
           return factura_detalle
       except Exception as e:
           # ... manejo de errores ...
   ```

3. **Servicio de Facturación** (`factura_service_simple_orm.py`):
   ```python
   def get_factura_detalle(self, factura_id: int, empresa: int) -> Optional[FacturaDetalle]:
       """Obtiene el detalle completo de una factura específica"""
       # Importar modelos necesarios
       from app.models.dbo.factura import Factura
       from app.models.dbo.tipomov import TipoMov
       # ... más importaciones ...
       
       # Query para obtener datos de la factura  
       factura_query = self.db.query(
           Factura,
           TipoMov.ntipomov,
           Clientes.nclientes,
           # ... más campos ...
       ).join(
           TipoMov, Factura.tipomov == TipoMov.tipomov
       ).outerjoin(
           Clientes, and_(
               Factura.clientes == Clientes.clientes,
               Clientes.empresa == empresa
           )
       )
       # ... más joins y filtros ...
       
       # Crear objeto FacturaDetalle con la información
       # ...
       
       return factura_detalle
   ```

### Clientes

El módulo de clientes (`app/api/v1/routers/clientes/`) gestiona la información de clientes:

1. **Listado de Clientes**:
   ```python
   @router.get("/", response_model=ClientesPaginados)
   def get_clientes_por_empresa(
       empresa_id: int,
       activo: Optional[bool] = Query(None),
       tipcli: Optional[int] = Query(None),
       search: Optional[str] = Query(None),
       page: int = Query(1, ge=1),
       size: int = Query(50, ge=1, le=100),
       db: Session = Depends(get_db)
   ):
       """Obtiene la lista paginada de clientes por empresa."""
       service = ClientesServiceORM(db)
       skip = (page - 1) * size
       clientes, total = service.get_clientes_by_empresa(
           empresa_id=empresa_id, 
           activo=activo, 
           tipcli=tipcli, 
           search=search, 
           skip=skip, 
           limit=size
       )
       
       # ... procesamiento y conversión de resultados ...
       
       return ClientesPaginados(
           items=clientes_response,
           total=total,
           page=page,
           size=size,
           pages=pages
       )
   ```

2. **Detalle de Cliente**:
   ```python
   @router.get("/{cliente_id}", response_model=ClienteDetalle)
   def get_cliente(
       cliente_id: str = Path(..., description="Código del cliente"),
       empresa_id: int = Query(..., description="ID de la empresa"),
       db: Session = Depends(get_db)
   ):
       """Obtiene un cliente específico por su ID dentro de una empresa."""
       service = ClientesServiceORM(db)
       cliente_dict = service.get_cliente_by_id(cliente_id, empresa_id)
       
       if not cliente_dict:
           raise HTTPException(status_code=404, detail="Cliente no encontrado")
       
       return ClienteDetalle.model_validate(cliente_dict)
   ```

3. **Servicio de Clientes** (`clientes_service.py`):
   ```python
   def get_cliente_by_id(self, cliente_id: str, empresa_id: int) -> Optional[Dict]:
       """Obtiene un cliente específico por su ID, dentro de una empresa específica."""
       try:
           # Importar modelos relacionados
           from app.models.dbo.tipcli import TipCli
           # ... más importaciones ...
           
           # Consulta con joins a tablas relacionadas
           query = self.db.query(
               Clientes,
               TipCli.ntipcli,
               Municip.nmunicip,
               # ... más campos ...
           ).outerjoin(
               TipCli, Clientes.tipcli == TipCli.tipcli
           )
           # ... más joins y filtros ...
           
           result = query.first()
           
           if not result:
               return None
           
           # Convertir a diccionario y agregar campos extra
           cliente_dict = {c.name: getattr(cliente, c.name) for c in cliente.__table__.columns}
           # ... procesar y devolver resultado ...
           
           return cliente_dict
       except Exception as e:
           # ... manejo de errores ...
           return None
   ```

### Productos

El módulo de productos (`app/api/v1/routers/productos/`) gestiona el catálogo de productos:

1. **Consulta de Productos en Kardex**:
   ```python
   @router.get("/kardex", response_model=ProductosResponse)
   def get_productos_kardex(
       empresa_id: int,
       caja_id: int,
       prodprec_id: int,
       busqueda: Optional[str] = Query("%"),
       bodega: Optional[str] = Query("%"),
       solo_existencias: Optional[bool] = Query(True),
       # ... más parámetros ...
       db: Session = Depends(get_db)
   ):
       """Obtiene productos del kardex para mostrar en la factura con paginación"""
       service = ProductosServiceORM(db)
      
       try:
           resultado = service.get_productos_kardex(
               empresa_id=empresa_id,
               caja_id=caja_id,
               prodprec_id=prodprec_id,
               # ... más parámetros ...
           )
          
           return resultado
       except Exception as e:
           raise HTTPException(status_code=500, detail=f"Error al obtener productos: {str(e)}")
   ```

2. **Servicio de Productos** (`productos_service.py`):
   ```python
   def get_productos_kardex(
       self,
       empresa_id: int,
       caja_id: int,
       prodprec_id: int,
       # ... más parámetros ...
   ) -> Dict[str, Any]:
       """Obtiene productos del kardex para mostrar en la factura con paginación"""
       # Obtener fecha del periodo
       fecha_periodo = self.get_fecha_periodo(empresa_id, caja_id)
       # ... más código y consultas complejas ...
       
       # Construcción de subconsultas
       rcant_subquery = (
           self.db.query(
               func.sum(DCamboBodega.cantidad).label("rcantidad"),
               Kardex.kardex.label("kardex_id")
           )
           # ... joins y filtros ...
           .subquery()
       )
       
       # Consulta principal
       query = self.db.query(
           # ... múltiples columnas y expresiones ...
       )
       
       # ... múltiples joins y filtros ...
       
       # Aplicar paginación y ordenamiento
       # ... ejecutar consulta y procesamiento ...
       
       return {
           "productos": productos,
           "total": total_count,
           "pagina": pagina,
           "total_paginas": total_paginas,
           "items_por_pagina": items_por_pagina,
           "tiene_promociones": tiene_promociones
       }
   ```

### Formas de Pago

El módulo de formas de pago (`app/api/v1/routers/formaPago/`) gestiona los métodos de pago:

```python
@router.get("/", response_model=List[FormaPagoBase])
def get_formas_pago_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None),
    frecuente: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene la lista de formas de pago por empresa."""
    service = FormaPagoServiceORM(db)
    formas_pago = service.get_formas_pago_by_empresa(empresa_id, activo, frecuente)
    if not formas_pago:
        return []
    return formas_pago

@router.get("/condiciones/", response_model=List[CondPagoBase])
def get_condiciones_pago(
    empresa_id: int,
    tipo: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene las condiciones de pago según el tipo especificado"""
    service = FormaPagoServiceORM(db)
    
    if tipo == "contado":
        condiciones = service.get_condiciones_pago(empresa_id, solo_contado=True)
    elif tipo == "credito":
        condiciones = service.get_condiciones_pago(empresa_id, solo_credito=True)
    else:  # tipo == "todos" o None
        condiciones = service.get_condiciones_pago(empresa_id)
    
    return condiciones
```

### Tipos de Documento

El módulo de tipos de documento (`app/api/v1/routers/tipoDocumento/`) gestiona los tipos de documentos:

```python
@router.get("/", response_model=List[TipoDocumentoBase])
def get_documentos_por_empresa(
    empresa_id: int,
    activo: Optional[bool] = Query(None),
    tipo: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene la lista de tipos de documento por empresa."""
    service = TipoDocumentoServiceORM(db)
    documentos = service.get_documentos_by_empresa(empresa_id, activo, tipo)
    if not documentos:
        return []
    return documentos

@router.get("/facturas/pais", response_model=List[TipoDocumentoFacturaPais])
def get_facturas_por_empresa_pais(
    empresa_id: int,
    caja_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Obtiene la lista de tipos de documento de factura según la lógica específica por país"""
    service = TipoDocumentoServiceORM(db)
    documentos = service.get_facturas_by_empresa_pais(empresa_id, caja_id)
    
    if not documentos:
        return []
    
    return documentos
```

## Guía de Desarrollo

### Configuración del Entorno

1. **Clonar el repositorio**:
   ```bash
   git clone <repo-url> consolidaerp-api
   cd consolidaerp-api
   ```

2. **Crear y activar entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**:
   - Crea un archivo `.env` en la raíz del proyecto
   - Configura las variables necesarias:
     ```
     # Base de datos
     DB_SERVER=server_name
     DB_NAME=database_name
     DB_USER=user
     DB_PASSWORD=password
     
     # Azure AD
     AZURE_CLIENT_ID=your_client_id
     AZURE_CLIENT_SECRET=your_client_secret
     AZURE_TENANT_ID=your_tenant_id
     AZURE_REDIRECT_URI=your_redirect_uri
     
     # Seguridad
     SECRET_KEY=your_secret_key
     FERNET_KEY=your_fernet_key
     
     # Servicios opcionales
     USE_REDIS_SERVICES=False
     USE_AI_SERVICES=False
     ```

5. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```
   
   O con uvicorn directamente:
   ```bash
   uvicorn main:app --reload
   ```

6. **Verificar la instalación**:
   - Accede a la documentación interactiva: http://localhost:8000/docs
   - Prueba el endpoint de estado: http://localhost:8000/app/status

### Estructura de Nuevos Endpoints

Para crear nuevos endpoints, sigue esta estructura:

1. **Crear un esquema Pydantic** para validación de datos:
   ```python
   # app/schemas/nuevo_schema.py
   from pydantic import BaseModel, Field
   from typing import Optional
   
   class ItemBase(BaseModel):
       nombre: str = Field(..., max_length=100)
       descripcion: Optional[str] = None
       
   class ItemCreate(ItemBase):
       pass
       
   class ItemResponse(ItemBase):
       id: int
       
       class Config:
           from_attributes = True
   ```

2. **Crear un servicio** para la lógica de negocio:
   ```python
   # app/api/v1/services/item_service.py
   from sqlalchemy.ext.asyncio import AsyncSession
   from sqlalchemy import select, insert
   from app.models.dbo.item import Item
   
   async def get_items(db: AsyncSession, empresa_id: int):
       query = select(Item).filter(Item.empresa == empresa_id)
       result = await db.execute(query)
       return result.scalars().all()
       
   async def create_item(db: AsyncSession, empresa_id: int, data: dict):
       item = Item(empresa=empresa_id, **data)
       db.add(item)
       await db.commit()
       await db.refresh(item)
       return item
   ```

3. **Crear un router** para los endpoints:
   ```python
   # app/api/v1/routers/items/router.py
   from fastapi import APIRouter, Depends, HTTPException, Query
   from sqlalchemy.ext.asyncio import AsyncSession
   from app.db.database import get_db
   from app.api.v1.services import item_service
   from app.schemas.nuevo_schema import ItemCreate, ItemResponse
   
   router = APIRouter()
   
   @router.get("/", response_model=List[ItemResponse])
   async def get_items(
       empresa_id: int = Query(..., description="ID de la empresa"),
       db: AsyncSession = Depends(get_db)
   ):
       items = await item_service.get_items(db, empresa_id)
       return items
       
   @router.post("/", response_model=ItemResponse, status_code=201)
   async def create_item(
       item: ItemCreate,
       empresa_id: int = Query(..., description="ID de la empresa"),
       db: AsyncSession = Depends(get_db)
   ):
       new_item = await item_service.create_item(db, empresa_id, item.dict())
       return new_item
   ```

4. **Registrar el router** en el router principal:
   ```python
   # app/api/v1/routers/routers.py
   from fastapi import APIRouter
   from .items.router import router as items_router
   # ... otros imports ...
   
   api_router = APIRouter()
   api_router.include_router(items_router, prefix="/items", tags=["Items"])
   # ... otros routers ...
   ```

### Trabajando con los Modelos

La mayoría de los modelos son generados automáticamente. Para trabajar con ellos:

1. **Importar modelos**:
   ```python
   from app.models.dbo.cliente import Cliente
   from app.models.dbo.factura import Factura
   # ... otros modelos ...
   ```

2. **Consultas básicas con SQLAlchemy**:
   ```python
   # Consulta simple
   query = select(Cliente).filter(Cliente.empresa == empresa_id)
   
   # Consulta con JOIN
   query = (
       select(Factura, Cliente)
       .join(Cliente, Cliente.clientes == Factura.clientes)
       .filter(Factura.empresa == empresa_id)
   )
   
   # Consultas paginadas
   query = (
       select(Cliente)
       .filter(Cliente.empresa == empresa_id)
       .order_by(Cliente.nclientes)
       .offset(skip)
       .limit(limit)
   )
   ```

3. **Ejecutar consultas de forma asíncrona**:
   ```python
   # Para un solo resultado
   result = await db.execute(query)
   item = result.scalar_one_or_none()
   
   # Para múltiples resultados
   result = await db.execute(query)
   items = result.scalars().all()
   
   # Para joins con múltiples modelos
   result = await db.execute(query)
   rows = result.all()
   for factura, cliente in rows:
       # Procesar factura y cliente
   ```

4. **Insertar y actualizar datos**:
   ```python
   # Insertar
   new_item = Item(**data)
   db.add(new_item)
   await db.commit()
   await db.refresh(new_item)
   
   # Actualizar
   item = await get_item_by_id(db, item_id)
   for key, value in data.items():
       setattr(item, key, value)
   await db.commit()
   await db.refresh(item)
   ```

### Debugging

1. **Logs**:
   La aplicación utiliza el módulo `logging` para registrar información:
   ```python
   import logging
   logger = logging.getLogger(__name__)
   
   try:
       # Código que podría fallar
   except Exception as e:
       logger.error(f"Error: {str(e)}", exc_info=True)
   ```

2. **Documentación interactiva de FastAPI**:
   - Accede a `http://localhost:8000/docs` para probar endpoints
   - Prueba los endpoints con diferentes parámetros
   - Verifica los esquemas de solicitud/respuesta

3. **Debugging con print**:
   - Usa `print()` para depuración rápida
   - Imprime variables JSON con formato:
   ```python
   import json
   print(json.dumps(data, indent=2))
   ```

4. **Debugging con debugger**:
   - Configura puntos de interrupción en VS Code
   - Usa `breakpoint()` en Python 3.7+ para entrar en modo depuración

## Prácticas Recomendadas

### Estructura y Organización

1. **Sigue la separación de responsabilidades**:
   - **Routers**: Solo lógica HTTP y validación
   - **Services**: Toda la lógica de negocio
   - **Models**: Representación de datos
   - **Schemas**: Validación de entrada/salida

2. **Usa nombres claros y descriptivos**:
   - Para funciones: `get_cliente_by_id()`, `create_factura()`
   - Para variables: `cliente_id`, `facturas_pendientes`
   - Para clases: `ClienteCreate`, `FacturaDetalle`

3. **Escribe docstrings** para funciones y clases:
   ```python
   def get_facturas_list(self, empresa: int, fecha_inicio: datetime, fecha_fin: datetime, ...):
       """
       Obtiene la lista de facturas usando ORM sin relaciones automáticas
       
       Args:
           empresa: ID de la empresa
           fecha_inicio: Fecha inicial para filtrar
           fecha_fin: Fecha final para filtrar
           
       Returns:
           List[FacturaListItem]: Lista de facturas
       """
       # ... implementación ...
   ```

4. **Organiza importaciones** en grupos lógicos:
   ```python
   # Importaciones estándar
   import os
   import json
   from datetime import datetime
   
   # Importaciones de terceros
   from fastapi import APIRouter, Depends, HTTPException
   from sqlalchemy import select, and_, or_
   
   # Importaciones del proyecto
   from app.db.database import get_db
   from app.models.dbo.cliente import Cliente
   ```

### Manejo de Errores

1. **Usa HTTPException para errores HTTP**:
   ```python
   from fastapi import HTTPException
   
   if not cliente:
       raise HTTPException(status_code=404, detail="Cliente no encontrado")
   ```

2. **Implementa bloques try-except**:
   ```python
   try:
       # Operaciones de base de datos o lógica de negocio
       result = await service.process_data(data)
       return result
   except ValueError as e:
       # Error de validación o negocio
       raise HTTPException(status_code=400, detail=str(e))
   except Exception as e:
       # Error inesperado
       logger.error(f"Error: {str(e)}", exc_info=True)
       raise HTTPException(status_code=500, detail="Error interno del servidor")
   ```

3. **Maneja transacciones correctamente**:
   ```python
   try:
       # Operaciones de base de datos
       db.add(item)
       await db.commit()
       await db.refresh(item)
       return item
   except Exception as e:
       await db.rollback()
       logger.error(f"Error de base de datos: {str(e)}")
       raise HTTPException(status_code=500, detail="Error de base de datos")
   ```

4. **Implementa validación con Pydantic**:
   ```python
   from pydantic import BaseModel, Field, validator
   
   class UserCreate(BaseModel):
       username: str = Field(..., min_length=3, max_length=50)
       email: EmailStr
       password: str = Field(..., min_length=8)
       
       @validator('password')
       def password_strength(cls, v):
           # Validación personalizada
           if not any(c.isdigit() for c in v):
               raise ValueError('La contraseña debe contener al menos un número')
           return v
   ```

### Optimización de Rendimiento

1. **Usa consultas específicas** en lugar de cargar objetos completos:
   ```python
   # En lugar de:
   query = select(Cliente)
   
   # Usa:
   query = select(Cliente.id, Cliente.nombre, Cliente.email)
   ```

2. **Implementa paginación** para colecciones grandes:
   ```python
   @router.get("/", response_model=List[ItemResponse])
   async def get_items(
       skip: int = Query(0, ge=0),
       limit: int = Query(100, ge=1, le=1000),
       db: AsyncSession = Depends(get_db)
   ):
       query = select(Item).offset(skip).limit(limit)
       # ...
   ```

3. **Usa índices adecuados** en la base de datos:
   - Asegúrate de que las columnas de filtro y ordenamiento tengan índices
   - Analiza las consultas lentas con herramientas de base de datos

4. **Considera implementar caché** para datos que cambian poco:
   ```python
   @router.get("/estadisticas")
   async def get_estadisticas(db: AsyncSession = Depends(get_db)):
       # Verificar caché
       cached = await redis.get("estadisticas")
       if cached:
           return json.loads(cached)
       
       # Si no está en caché, calcular
       stats = await calcular_estadisticas(db)
       
       # Guardar en caché por 1 hora
       await redis.set("estadisticas", json.dumps(stats), ex=3600)
       
       return stats
   ```

### Seguridad

1. **Protege endpoints sensibles** con autenticación:
   ```python
   from app.auth.jwt_bearer import JWTBearer
   
   @router.post("/", dependencies=[Depends(JWTBearer())])
   async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
       # ...
   ```

2. **Valida y sanitiza todas las entradas**:
   - Usa Pydantic para validación
   - Define claramente los tipos y restricciones
   - Implementa validadores personalizados

3. **No exponer información sensible**:
   - No devuelvas contraseñas o tokens de seguridad
   - Limita información en respuestas de error
   - Usa HTTPS en producción

4. **Implementa límites de tasa (rate limiting)** para prevenir abusos:
   ```python
   from fastapi import Depends, HTTPException
   from fastapi.security import APIKeyHeader
   
   # Implementación simplificada
   class RateLimiter:
       def __init__(self):
           self.requests = {}
       
       async def __call__(self, api_key: str = Depends(APIKeyHeader(name="X-API-Key"))):
           # Verificar límites
           # ...
   
   rate_limiter = RateLimiter()
   
   @router.get("/", dependencies=[Depends(rate_limiter)])
   async def get_items():
       # ...
   ```

---

Esta guía es un documento vivo que se actualizará conforme el proyecto evolucione. Para cualquier duda o sugerencia, contacta al equipo de desarrollo.# Guía de Desarrollo: Backend FastAPI ConsolidaERP