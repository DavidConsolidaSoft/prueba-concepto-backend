# auto_generate_models_advanced.py
"""
Script avanzado para generar modelos SQLAlchemy automáticamente
Maneja esquemas complejos con 600+ tablas incluyendo relaciones
"""
import os
import sys
from urllib.parse import quote_plus
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from datetime import datetime
import json
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_DRIVER = os.getenv('DB_DRIVER', 'ODBC Driver 18 for SQL Server')

# URL encode la contraseña para manejar caracteres especiales
password_encoded = quote_plus(DB_PASSWORD)

# Construir la cadena de conexión con TrustServerCertificate para Azure SQL
connection_string = (
    f"mssql+pyodbc://{DB_USER}:{password_encoded}@{DB_SERVER}/{DB_NAME}"
    f"?driver={DB_DRIVER}&TrustServerCertificate=yes&Encrypt=yes&timeout=60"
)

class ModelGenerator:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None
        self.metadata = MetaData()
        self.inspector = None
        self.schema_info = {}
        
    def connect(self):
        """Establece conexión con la base de datos"""
        try:
            self.engine = create_engine(
                self.connection_string,
                pool_pre_ping=True,
                pool_recycle=3600,
                echo=False,
                pool_size=20,
                max_overflow=40
            )
            self.inspector = inspect(self.engine)
            logger.info("✅ Conexión exitosa a la base de datos")
            return True
        except Exception as e:
            logger.error(f"❌ Error al conectar: {str(e)}")
            return False
    
    def get_schema_info(self):
        """Obtiene información completa del esquema"""
        logger.info("Analizando esquema de la base de datos...")
        
        # Obtener todos los esquemas
        schemas = self.inspector.get_schema_names()
        
        # Filtrar esquemas del sistema
        system_schemas = [
            'information_schema', 'sys', 'guest', 'db_accessadmin', 
            'db_backupoperator', 'db_datareader', 'db_datawriter', 
            'db_ddladmin', 'db_denydatareader', 'db_denydatawriter', 
            'db_owner', 'db_securityadmin'
        ]
        
        for schema in schemas:
            if schema not in system_schemas:
                logger.info(f"Procesando esquema: {schema}")
                self.schema_info[schema] = {
                    'tables': {},
                    'views': []
                }
                
                # Obtener tablas
                tables = self.inspector.get_table_names(schema=schema)
                logger.info(f"  Encontradas {len(tables)} tablas en esquema {schema}")
                
                # Procesar tablas en lotes para mejorar rendimiento
                batch_size = 50
                for i in range(0, len(tables), batch_size):
                    batch = tables[i:i + batch_size]
                    logger.info(f"    Procesando lote {i//batch_size + 1} de {len(tables)//batch_size + 1}")
                    
                    for table in batch:
                        try:
                            table_info = {
                                'columns': self.inspector.get_columns(table, schema=schema),
                                'primary_keys': self.inspector.get_pk_constraint(table, schema=schema),
                                'foreign_keys': self.inspector.get_foreign_keys(table, schema=schema),
                                'indexes': self.inspector.get_indexes(table, schema=schema)
                            }
                            
                            # Las siguientes operaciones pueden no estar soportadas
                            try:
                                table_info['unique_constraints'] = self.inspector.get_unique_constraints(table, schema=schema)
                            except NotImplementedError:
                                table_info['unique_constraints'] = []
                                
                            try:
                                table_info['check_constraints'] = self.inspector.get_check_constraints(table, schema=schema)
                            except NotImplementedError:
                                table_info['check_constraints'] = []
                            
                            self.schema_info[schema]['tables'][table] = table_info
                            
                        except Exception as e:
                            logger.warning(f"Error procesando tabla {schema}.{table}: {str(e)}")
                            continue
        
        return self.schema_info
    
    def generate_sqlalchemy_models(self, output_dir='app/models'):
        """Genera archivos de modelos SQLAlchemy"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Generar archivo __init__.py
        with open(os.path.join(output_dir, '__init__.py'), 'w') as f:
            f.write("# Modelos generados automáticamente\n")
            f.write("from .base import Base\n")
        
        # Generar archivo base.py
        with open(os.path.join(output_dir, 'base.py'), 'w') as f:
            f.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
            f.write("Base = declarative_base()\n")
        
        total_tables = 0
        
        # Generar modelos por esquema
        for schema, schema_data in self.schema_info.items():
            if schema_data['tables']:
                schema_dir = os.path.join(output_dir, schema.lower())
                os.makedirs(schema_dir, exist_ok=True)
                
                # __init__.py del esquema
                with open(os.path.join(schema_dir, '__init__.py'), 'w') as f:
                    f.write(f"# Modelos del esquema {schema}\n")
                
                # Generar modelos para cada tabla
                for table_name, table_data in schema_data['tables'].items():
                    model_code = self._generate_model_code(schema, table_name, table_data)
                    
                    # Guardar en archivo individual
                    filename = f"{table_name.lower()}.py"
                    with open(os.path.join(schema_dir, filename), 'w', encoding='utf-8') as f:
                        f.write(model_code)
                    
                    total_tables += 1
                    
                    # Actualizar __init__.py del esquema
                    with open(os.path.join(schema_dir, '__init__.py'), 'a') as f:
                        class_name = self._to_class_name(table_name)
                        f.write(f"from .{table_name.lower()} import {class_name}\n")
                
                # Actualizar __init__.py principal
                with open(os.path.join(output_dir, '__init__.py'), 'a') as f:
                    f.write(f"from . import {schema.lower()}\n")
        
        logger.info(f"✅ Se generaron modelos para {total_tables} tablas")
        
        # Generar archivo de documentación
        self._generate_documentation(output_dir)
        
        return total_tables
    
    def _generate_model_code(self, schema, table_name, table_data):
        """Genera el código del modelo para una tabla"""
        class_name = self._to_class_name(table_name)
        
        code = []
        code.append("# Generado automáticamente")
        code.append(f"# Tabla: {schema}.{table_name}")
        code.append(f"# Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        code.append("")
        
        # Imports
        imports = set()
        imports.add("from sqlalchemy import Column, ForeignKey")
        imports.add("from ..base import Base")
        
        # Determinar tipos necesarios
        type_imports = set()
        for column in table_data['columns']:
            sql_type = self._get_sqlalchemy_type(column['type'])
            if sql_type:
                # Extraer tipo base
                type_name = sql_type.split('(')[0]
                if type_name not in ['Column', 'ForeignKey']:
                    type_imports.add(type_name)
        
        # Agregar tipos a imports
        if type_imports:
            imports.add(f"from sqlalchemy import {', '.join(sorted(type_imports))}")
        
        # Verificar si hay relaciones
        if table_data['foreign_keys']:
            imports.add("from sqlalchemy.orm import relationship")
        
        # Añadir imports
        for imp in sorted(imports):
            code.append(imp)
        
        code.append("")
        code.append("")
        
        # Definición de la clase
        code.append(f"class {class_name}(Base):")
        code.append(f'    __tablename__ = "{table_name}"')
        code.append(f'    __table_args__ = {{"schema": "{schema}"}}')
        code.append("")
        
        # Columnas
        for column in table_data['columns']:
            col_code = self._generate_column_code(column, table_data['primary_keys'])
            code.append(f"    {col_code}")
        
        code.append("")
        
        # Relaciones
        relationships = self._generate_relationships(table_name, table_data['foreign_keys'])
        if relationships:
            code.append("    # Relaciones")
            for rel in relationships:
                code.append(f"    {rel}")
            code.append("")
        
        # Método __repr__
        primary_keys = table_data['primary_keys'].get('constrained_columns', [])
        
        if primary_keys:
            repr_attrs = primary_keys[:3]  # Máximo 3 atributos
        else:
            # Si no hay primary key, usar la primera columna
            repr_attrs = [table_data['columns'][0]['name']] if table_data['columns'] else []
        
        if repr_attrs:
            code.append("    def __repr__(self):")
            repr_parts = [f"{attr}={{self.{attr}}}" for attr in repr_attrs]
            code.append(f'        return "<{class_name}({", ".join(repr_parts)})>"')
        
        return '\n'.join(code)
    
    def _generate_column_code(self, column, primary_keys):
        """Genera el código para una columna"""
        col_name = column['name']
        col_type = self._get_sqlalchemy_type(column['type'])
        
        parts = [f"{col_name} = Column({col_type}"]
        
        # Primary key
        if col_name in primary_keys['constrained_columns']:
            parts.append("primary_key=True")
        
        # Nullable
        if not column['nullable']:
            parts.append("nullable=False")
        
        # Default
        if column.get('default'):
            default_value = self._format_default(column['default'])
            if default_value:
                parts.append(f"server_default={default_value}")
        
        # Autoincrement
        if column.get('autoincrement'):
            parts.append("autoincrement=True")
        
        return ', '.join(parts) + ')'
    
    def _generate_relationships(self, table_name, foreign_keys):
        """Genera código para las relaciones"""
        relationships = []
        
        for fk in foreign_keys:
            # Nombre de la relación
            referred_table = fk['referred_table']
            rel_name = self._to_variable_name(referred_table)
            
            # Evitar conflictos de nombres
            if rel_name == table_name:
                rel_name = f"{rel_name}_ref"
            
            # Construir relación
            rel_code = f'{rel_name} = relationship("{self._to_class_name(referred_table)}"'
            rel_code += f', back_populates="{self._to_variable_name(table_name)}_set")'
            
            relationships.append(rel_code)
        
        return relationships
    
    def _get_sqlalchemy_type(self, sql_type):
        """Mapea tipos SQL Server a SQLAlchemy"""
        sql_type_upper = str(sql_type).upper()
        
        # Extraer tipo base sin parámetros
        base_type = sql_type_upper.split('(')[0]
        
        type_mapping = {
            'INT': 'Integer',
            'INTEGER': 'Integer',
            'BIGINT': 'BigInteger',
            'SMALLINT': 'SmallInteger',
            'TINYINT': 'SmallInteger',
            'BIT': 'Boolean',
            'DECIMAL': 'Numeric',
            'NUMERIC': 'Numeric',
            'MONEY': 'Numeric(19, 4)',
            'SMALLMONEY': 'Numeric(10, 4)',
            'FLOAT': 'Float',
            'REAL': 'Float',
            'VARCHAR': 'String',
            'CHAR': 'String',
            'NVARCHAR': 'String',
            'NCHAR': 'String',
            'TEXT': 'Text',
            'NTEXT': 'Text',
            'DATETIME': 'DateTime',
            'DATETIME2': 'DateTime',
            'SMALLDATETIME': 'DateTime',
            'DATE': 'Date',
            'TIME': 'Time',
            'BINARY': 'LargeBinary',
            'VARBINARY': 'LargeBinary',
            'IMAGE': 'LargeBinary',
            'UNIQUEIDENTIFIER': 'String(36)',
            'XML': 'Text',
            'JSON': 'JSON'
        }
        
        # Obtener tipo base
        sqlalchemy_type = type_mapping.get(base_type, 'String')
        
        # Manejar tipos con parámetros
        if base_type in ['VARCHAR', 'NVARCHAR', 'CHAR', 'NCHAR'] and '(' in str(sql_type):
            try:
                # Extraer longitud
                length = str(sql_type).split('(')[1].split(')')[0]
                if length.upper() == 'MAX':
                    return 'Text'
                else:
                    return f'String({length})'
            except:
                pass
        
        elif base_type in ['DECIMAL', 'NUMERIC'] and '(' in str(sql_type):
            try:
                # Extraer precisión y escala
                params = str(sql_type).split('(')[1].split(')')[0]
                return f'Numeric({params})'
            except:
                pass
        
        return sqlalchemy_type
    
    def _to_class_name(self, table_name):
        """Convierte nombre de tabla a nombre de clase"""
        # Remover prefijos comunes
        prefixes = ['tbl_', 'tb_', 't_']
        clean_name = table_name.lower()
        for prefix in prefixes:
            if clean_name.startswith(prefix):
                clean_name = clean_name[len(prefix):]
                break
        
        # Convertir a CamelCase
        parts = clean_name.split('_')
        return ''.join(word.capitalize() for word in parts)
    
    def _to_variable_name(self, table_name):
        """Convierte nombre de tabla a nombre de variable"""
        class_name = self._to_class_name(table_name)
        return class_name[0].lower() + class_name[1:]
    
    def _format_default(self, default):
        """Formatea valores por defecto"""
        if default is None:
            return None
        
        default_str = str(default).strip()
        
        # Quitar paréntesis externos
        if default_str.startswith('(') and default_str.endswith(')'):
            default_str = default_str[1:-1]
        
        # Valores especiales
        if default_str.upper() in ['GETDATE()', 'CURRENT_TIMESTAMP']:
            return 'text("GETDATE()")'
        elif default_str.upper() == 'NEWID()':
            return 'text("NEWID()")'
        elif default_str.startswith("'") and default_str.endswith("'"):
            return f'"{default_str[1:-1]}"'
        
        return f'text("{default_str}")'
    
    def _generate_documentation(self, output_dir):
        """Genera documentación del esquema"""
        doc_path = os.path.join(output_dir, 'schema_documentation.md')
        
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write("# Documentación del Esquema de Base de Datos\n\n")
            f.write(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Resumen
            total_tables = sum(len(s['tables']) for s in self.schema_info.values())
            f.write(f"## Resumen\n")
            f.write(f"- Total de esquemas: {len(self.schema_info)}\n")
            f.write(f"- Total de tablas: {total_tables}\n\n")
            
            # Detalles por esquema
            for schema, schema_data in self.schema_info.items():
                f.write(f"## Esquema: {schema}\n")
                f.write(f"- Tablas: {len(schema_data['tables'])}\n\n")
                
                for table_name, table_data in sorted(schema_data['tables'].items()):
                    f.write(f"### Tabla: {table_name}\n")
                    
                    # Columnas
                    f.write("#### Columnas\n")
                    f.write("| Nombre | Tipo | Nullable | Primary Key |\n")
                    f.write("|--------|------|----------|-------------|\n")
                    
                    pk_columns = table_data['primary_keys']['constrained_columns']
                    
                    for col in table_data['columns']:
                        is_pk = '✓' if col['name'] in pk_columns else ''
                        nullable = '✓' if col['nullable'] else ''
                        f.write(f"| {col['name']} | {col['type']} | {nullable} | {is_pk} |\n")
                    
                    # Foreign Keys
                    if table_data['foreign_keys']:
                        f.write("\n#### Foreign Keys\n")
                        for fk in table_data['foreign_keys']:
                            f.write(f"- {fk['constrained_columns']} → {fk['referred_table']}.{fk['referred_columns']}\n")
                    
                    # Índices
                    if table_data['indexes']:
                        f.write("\n#### Índices\n")
                        for idx in table_data['indexes']:
                            unique = '(UNIQUE)' if idx.get('unique') else ''
                            f.write(f"- {idx['name']}: {idx['column_names']} {unique}\n")
                    
                    f.write("\n")
        
        logger.info(f"📄 Documentación guardada en: {doc_path}")

def main():
    """Función principal"""
    print("=== Generador Avanzado de Modelos SQLAlchemy ===")
    print(f"Base de datos: {DB_SERVER}/{DB_NAME}")
    print(f"Usuario: {DB_USER}")
    print("")
    
    generator = ModelGenerator(connection_string)
    
    # Conectar
    if not generator.connect():
        print("No se pudo conectar a la base de datos")
        return
    
    try:
        # Mostrar esquemas disponibles
        schemas = generator.inspector.get_schema_names()
        user_schemas = [s for s in schemas if s not in [
            'information_schema', 'sys', 'guest', 'db_accessadmin',
            'db_backupoperator', 'db_datareader', 'db_datawriter',
            'db_ddladmin', 'db_denydatareader', 'db_denydatawriter',
            'db_owner', 'db_securityadmin'
        ]]
        
        print(f"Esquemas de usuario disponibles: {', '.join(user_schemas)}")
        
        # Opción para seleccionar esquemas específicos
        print("\nOpciones:")
        print("1. Procesar todos los esquemas de usuario")
        print("2. Procesar solo el esquema 'dbo'")
        print("3. Seleccionar esquemas específicos")
        
        choice = input("\nSelecciona una opción (1-3) [default: 2]: ").strip() or "2"
        
        # Analizar esquemas seleccionados
        print("\n🔍 Analizando esquema de la base de datos...")
        
        if choice == "1":
            schema_info = generator.get_schema_info()
        elif choice == "2":
            # Solo procesar dbo
            generator.schema_info['dbo'] = {
                'tables': {},
                'views': []
            }
            
            tables = generator.inspector.get_table_names(schema='dbo')
            print(f"Encontradas {len(tables)} tablas en esquema dbo")
            
            # Procesar en lotes
            batch_size = 50
            for i in range(0, len(tables), batch_size):
                batch = tables[i:i + batch_size]
                print(f"Procesando lote {i//batch_size + 1} de {len(tables)//batch_size + 1}")
                
                for table in batch:
                    try:
                        table_info = {
                            'columns': generator.inspector.get_columns(table, schema='dbo'),
                            'primary_keys': generator.inspector.get_pk_constraint(table, schema='dbo'),
                            'foreign_keys': generator.inspector.get_foreign_keys(table, schema='dbo'),
                            'indexes': generator.inspector.get_indexes(table, schema='dbo'),
                            'unique_constraints': [],
                            'check_constraints': []
                        }
                        generator.schema_info['dbo']['tables'][table] = table_info
                    except Exception as e:
                        logger.warning(f"Error procesando tabla dbo.{table}: {str(e)}")
                        continue
        else:
            # Esquemas específicos
            selected = input("Ingresa los esquemas separados por comas: ").strip()
            for schema in selected.split(','):
                schema = schema.strip()
                if schema in user_schemas:
                    # Similar al proceso anterior pero para esquemas específicos
                    pass
        
        # Preguntar por límite de tablas para prueba
        limit_tables = input("\n¿Limitar el número de tablas para prueba? (ej: 10, o Enter para todas): ").strip()
        
        if limit_tables:
            try:
                limit = int(limit_tables)
                for schema in generator.schema_info:
                    tables = list(generator.schema_info[schema]['tables'].keys())[:limit]
                    generator.schema_info[schema]['tables'] = {
                        t: generator.schema_info[schema]['tables'][t] 
                        for t in tables
                    }
                print(f"\nLimitado a {limit} tablas por esquema")
            except ValueError:
                pass
        
        # Guardar información del esquema
        with open('schema_info.json', 'w', encoding='utf-8') as f:
            json.dump(generator.schema_info, f, indent=2, default=str)
        print("📄 Información del esquema guardada en schema_info.json")
        
        # Generar modelos
        print("\n🛠️ Generando modelos SQLAlchemy...")
        total_tables = generator.generate_sqlalchemy_models()
        
        print(f"\n✅ Proceso completado exitosamente")
        print(f"📊 Se generaron modelos para {total_tables} tablas")
        print("📁 Los modelos se guardaron en app/models/")
        
        # Ofrecer generar también con sqlacodegen
        if input("\n¿Generar también con sqlacodegen para comparación? (s/n): ").lower() == 's':
            os.system("python sqlacodegen_generator.py")
        
    except Exception as e:
        print(f"\n❌ Error durante la generación: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        if generator.engine:
            generator.engine.dispose()
            print("\n🔌 Conexión cerrada")

if __name__ == "__main__":
    main()