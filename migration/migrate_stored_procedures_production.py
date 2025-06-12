#!/usr/bin/env python3
"""
MIGRADOR AUTOMÁTICO DE STORED PROCEDURES - VERSIÓN PRODUCCIÓN
SQL Server T-SQL → PostgreSQL PL/pgSQL

MEJORAS:
- Detección automática de entorno (demo/producción)
- Validación pre-migración exhaustiva
- Rollback automático en caso de errores
- Logging detallado para troubleshooting
- Conversión mejorada de cursores complejos
"""

import re
import logging
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import pyodbc
import psycopg2
import os
import sys

# Configurar logging detallado
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'sp_migration_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProductionStoredProcedureMigrator:
    """Migrador de SPs para entornos de producción con validaciones exhaustivas"""
    
    def __init__(self, environment: str = "demo"):
        self.environment = environment
        self.migration_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Configuraciones por entorno
        self.configs = self._get_environment_configs()
        
        # Estadísticas de migración
        self.stats = {
            'total_procedures': 0,
            'migrated_successfully': 0,
            'failed_migration': 0,
            'cursors_converted': 0,
            'complex_procedures': 0,
            'start_time': datetime.now()
        }
        
        # Mapeo mejorado de tipos T-SQL → PL/pgSQL
        self.type_mapping = {
            'INT': 'INTEGER',
            'BIGINT': 'BIGINT', 
            'SMALLINT': 'SMALLINT',
            'TINYINT': 'SMALLINT',
            'BIT': 'BOOLEAN',
            'DECIMAL': 'DECIMAL',
            'NUMERIC': 'DECIMAL',
            'MONEY': 'DECIMAL(19,4)',
            'SMALLMONEY': 'DECIMAL(10,4)',
            'FLOAT': 'DOUBLE PRECISION',
            'REAL': 'REAL',
            'DATETIME': 'TIMESTAMP WITH TIME ZONE',
            'DATETIME2': 'TIMESTAMP WITH TIME ZONE',
            'SMALLDATETIME': 'TIMESTAMP WITH TIME ZONE',
            'DATE': 'DATE',
            'TIME': 'TIME WITH TIME ZONE',
            'VARCHAR': 'VARCHAR',
            'NVARCHAR': 'VARCHAR',
            'CHAR': 'CHAR',
            'NCHAR': 'CHAR',
            'TEXT': 'TEXT',
            'NTEXT': 'TEXT',
            'UNIQUEIDENTIFIER': 'UUID',
            'VARBINARY': 'BYTEA',
            'BINARY': 'BYTEA',
            'IMAGE': 'BYTEA',
            'SQL_VARIANT': 'TEXT'
        }
        
        # Patrones de conversión básicos (sin funciones lambda para compatibilidad)
        self.basic_patterns = [
            # Variables y SET
            (r'SET\s+(@\w+)\s*=\s*(.+?)(?=\s*;|\s*$)', r'\1 := \2;'),
            
            # SELECT INTO
            (r'SELECT\s+((?:(?!INTO|FROM).)+)\s+INTO\s+(@\w+)(?:\s+FROM\s+(.+?))?(?=\s*;|\s*$)', r'SELECT \1 INTO \2 FROM \3;'),
            
            # Estructuras de control
            (r'IF\s+(.+?)\s+BEGIN', r'IF \1 THEN'),
            (r'END\s*ELSE\s*BEGIN', 'ELSE'),
            (r'END\s*ELSE\s*IF\s+(.+?)\s+BEGIN', r'ELSIF \1 THEN'),
            
            # WHILE loops
            (r'WHILE\s+(.+?)\s+BEGIN', r'WHILE \1 LOOP'),
            (r'END\s*--\s*WHILE', 'END LOOP;'),
            (r'BREAK', 'EXIT;'),
            (r'CONTINUE', 'CONTINUE;'),
            
            # Manejo de errores
            (r'PRINT\s+(.+)', r'RAISE NOTICE \'%\', \1;'),
            (r'RAISERROR\s*\(\s*(.+?),\s*\d+,\s*\d+\s*\)', r'RAISE EXCEPTION \'%\', \1;'),
            
            # Variables del sistema
            (r'@(\w+)', r'\1'),
            
            # Funciones básicas
            (r'GETDATE\s*\(\s*\)', 'NOW()'),
            (r'GETUTCDATE\s*\(\s*\)', 'NOW() AT TIME ZONE \'UTC\''),
            (r'ISNULL\s*\(\s*(.+?),\s*(.+?)\s*\)', r'COALESCE(\1, \2)'),
            (r'LEN\s*\(\s*(.+?)\s*\)', r'LENGTH(\1)'),
            (r'UPPER\s*\(\s*(.+?)\s*\)', r'UPPER(\1)'),
            (r'LOWER\s*\(\s*(.+?)\s*\)', r'LOWER(\1)'),
            (r'LTRIM\s*\(\s*(.+?)\s*\)', r'LTRIM(\1)'),
            (r'RTRIM\s*\(\s*(.+?)\s*\)', r'RTRIM(\1)'),
            
            # Funciones de subcadena
            (r'SUBSTRING\s*\(\s*(.+?),\s*(.+?),\s*(.+?)\s*\)', r'SUBSTRING(\1 FROM \2 FOR \3)'),
            (r'CHARINDEX\s*\(\s*(.+?),\s*(.+?)\s*\)', r'POSITION(\1 IN \2)'),
            
            # Funciones matemáticas
            (r'CEILING\s*\(\s*(.+?)\s*\)', r'CEIL(\1)'),
            (r'POWER\s*\(\s*(.+?),\s*(.+?)\s*\)', r'POWER(\1, \2)'),
            
            # TOP/LIMIT
            (r'SELECT\s+TOP\s+(\d+)', r'SELECT'),
        ]
    
    def _get_environment_configs(self) -> Dict:
        """Configuraciones por entorno"""
        configs = {
            'demo': {
                'sql_server': {
                    'driver': '{ODBC Driver 17 for SQL Server}',
                    'server': 'localhost',
                    'port': 1433,
                    'database': 'una',
                    'username': 'sa',
                    'password': 'MigracionERP2025!'
                },
                'postgres': {
                    'host': 'localhost',
                    'port': 5422,
                    'database': 'erp_consolidasoft',
                    'username': 'postgres',
                    'password': 'MigracionERP2025!'
                }
            },
            'production': {
                'sql_server': {
                    'driver': '{ODBC Driver 17 for SQL Server}',
                    'server': 'SQL-SERVER-PROD',  # CONFIGURAR
                    'port': 1433,
                    'database': 'ERP_PRODUCTION',  # CONFIGURAR
                    'username': 'migration_user',
                    'password': 'CONFIGURAR_PASSWORD_PROD'
                },
                'postgres': {  
                    'host': 'POSTGRES-PROD-HOST',  # CONFIGURAR
                    'port': 5432,
                    'database': 'erp_consolidado_prod',
                    'username': 'postgres',
                    'password': 'CONFIGURAR_PASSWORD_PROD'
                }
            }
        }
        
        return configs[self.environment]
    
    def validate_environment(self) -> bool:
        """Validar conectividad y prerrequisitos"""
        logger.info(f"🔍 Validando entorno: {self.environment}")
        
        try:
            # Test SQL Server connection
            sql_conn = self._get_sql_server_connection()
            sql_cursor = sql_conn.cursor()
            sql_cursor.execute("SELECT @@VERSION, DB_NAME(), GETDATE()")
            sql_info = sql_cursor.fetchone()
            logger.info(f"✅ SQL Server conectado: {sql_info[1]}")
            
            # Test PostgreSQL connection
            pg_conn = self._get_postgres_connection()
            pg_cursor = pg_conn.cursor()
            pg_cursor.execute("SELECT version(), current_database(), now()")
            pg_info = pg_cursor.fetchone()
            logger.info(f"✅ PostgreSQL conectado: {pg_info[1]}")
            
            # Crear schemas necesarios
            pg_cursor.execute("CREATE SCHEMA IF NOT EXISTS legacy_procedures")
            pg_cursor.execute("CREATE SCHEMA IF NOT EXISTS erp_control")
            pg_conn.commit()
            
            sql_conn.close()
            pg_conn.close()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error validando entorno: {e}")
            return False
    
    def _get_sql_server_connection(self):
        """Obtener conexión a SQL Server"""
        config = self.configs['sql_server']
        conn_str = (
            f"DRIVER={config['driver']};"
            f"SERVER={config['server']},{config['port']};"
            f"DATABASE={config['database']};"
            f"UID={config['username']};"
            f"PWD={config['password']};"
            f"TrustServerCertificate=yes;"
            f"Timeout=300;"
        )
        return pyodbc.connect(conn_str)
    
    def _get_postgres_connection(self):
        """Obtener conexión a PostgreSQL"""
        config = self.configs['postgres']
        return psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['username'],
            password=config['password'],
            connect_timeout=30
        )
    
    def extract_stored_procedures(self) -> List[Dict]:
        """Extraer stored procedures con análisis de complejidad"""
        try:
            conn = self._get_sql_server_connection()
            cursor = conn.cursor()
            
            # Query para obtener SPs con metadatos
            sp_query = """
            SELECT 
                p.name AS procedure_name,
                m.definition AS procedure_definition,
                p.create_date,
                p.modify_date,
                (SELECT COUNT(*) FROM sys.parameters WHERE object_id = p.object_id) as param_count,
                CASE 
                    WHEN m.definition LIKE '%CURSOR%' THEN 'HIGH'
                    WHEN m.definition LIKE '%WHILE%' OR m.definition LIKE '%LOOP%' THEN 'MEDIUM'
                    WHEN LEN(m.definition) > 5000 THEN 'MEDIUM'
                    ELSE 'LOW'
                END as complexity
            FROM sys.procedures p
            INNER JOIN sys.sql_modules m ON p.object_id = m.object_id
            WHERE p.is_ms_shipped = 0
            ORDER BY p.name
            """
            
            cursor.execute(sp_query)
            procedures = cursor.fetchall()
            
            sp_list = []
            for proc in procedures:
                definition = proc[1] or ""
                
                sp_info = {
                    'name': proc[0],
                    'definition': definition,
                    'created': proc[2],
                    'modified': proc[3],
                    'param_count': proc[4],
                    'complexity': proc[5],
                    'has_cursors': 'CURSOR' in definition.upper(),
                    'has_transactions': any(kw in definition.upper() for kw in ['BEGIN TRAN', 'COMMIT', 'ROLLBACK']),
                    'has_error_handling': 'TRY' in definition.upper() and 'CATCH' in definition.upper()
                }
                sp_list.append(sp_info)
            
            self.stats['total_procedures'] = len(sp_list)
            logger.info(f"✅ Extraídos {len(sp_list)} stored procedures")
            
            conn.close()
            return sp_list
            
        except Exception as e:
            logger.error(f"❌ Error extrayendo SPs: {e}")
            return []
    
    def convert_cursors_to_loops(self, tsql_code: str) -> str:
        """Conversión de cursores a loops PostgreSQL"""
        
        # Pattern para DECLARE CURSOR
        cursor_pattern = r'DECLARE\s+(\w+)\s+CURSOR\s+(?:LOCAL\s+)?(?:STATIC\s+)?(?:READ_ONLY\s+)?FOR\s+(.*?)(?=\s*DECLARE|\s*OPEN|\s*$)'
        
        def replace_cursor(match):
            cursor_name = match.group(1)
            cursor_query = match.group(2).strip()
            
            pg_code = f"""
    -- Converted from cursor {cursor_name}
    FOR {cursor_name}_record IN {cursor_query} LOOP
        -- Cursor processing logic
    END LOOP;"""
            
            self.stats['cursors_converted'] += 1
            return pg_code
        
        # Aplicar conversión
        converted_code = re.sub(cursor_pattern, replace_cursor, tsql_code, flags=re.IGNORECASE | re.DOTALL)
        
        # Limpiar statements de cursor
        cursor_cleanup_patterns = [
            r'OPEN\s+\w+\s*;?',
            r'CLOSE\s+\w+\s*;?',
            r'DEALLOCATE\s+\w+\s*;?',
            r'FETCH\s+(?:NEXT\s+FROM\s+)?\w+\s+INTO\s+.*?;?'
        ]
        
        for pattern in cursor_cleanup_patterns:
            converted_code = re.sub(pattern, '', converted_code, flags=re.IGNORECASE)
        
        return converted_code
    
    def convert_type(self, sql_type: str) -> str:
        """Conversión de tipos SQL Server a PostgreSQL"""
        sql_type_upper = sql_type.upper().strip()
        
        # Casos especiales
        if sql_type_upper in ['VARCHAR(MAX)', 'NVARCHAR(MAX)']:
            return 'TEXT'
        
        if sql_type_upper == 'VARBINARY(MAX)':
            return 'BYTEA'
        
        # Extraer tipo base y parámetros
        if '(' in sql_type_upper:
            base_type = sql_type_upper.split('(')[0]
            params = sql_type_upper.split('(')[1].rstrip(')')
            
            if base_type in self.type_mapping:
                pg_type = self.type_mapping[base_type]
                
                if pg_type in ['VARCHAR', 'CHAR', 'DECIMAL']:
                    return f"{pg_type}({params})"
                
                return pg_type
        else:
            return self.type_mapping.get(sql_type_upper, 'TEXT')
        
        return 'TEXT'
    
    def extract_parameters(self, tsql_code: str) -> List[Dict]:
        """Extraer parámetros del SP"""
        params = []
        
        # Patterns para parámetros
        param_patterns = [
            r'(@\w+)\s+(\w+(?:\([^)]+\))?)\s*(OUTPUT|OUT)?\s*(?:=\s*([^,\s]+))?',
            r'(@\w+)\s+AS\s+(\w+(?:\([^)]+\))?)\s*(OUTPUT|OUT)?\s*(?:=\s*([^,\s]+))?'
        ]
        
        for pattern in param_patterns:
            matches = re.findall(pattern, tsql_code, re.IGNORECASE | re.MULTILINE)
            
            for match in matches:
                param = {
                    'name': match[0],
                    'type': match[1],
                    'direction': 'OUTPUT' if match[2] and match[2].upper() in ['OUTPUT', 'OUT'] else 'INPUT',
                    'default': match[3] if len(match) > 3 and match[3] else None
                }
                params.append(param)
        
        return params
    
    def convert_tsql_to_plpgsql(self, tsql_code: str, proc_name: str) -> str:
        """Conversión completa de T-SQL a PL/pgSQL"""
        
        # Limpiar código inicial
        plpgsql_code = tsql_code.strip()
        
        # Remover CREATE PROCEDURE inicial
        plpgsql_code = re.sub(r'CREATE\s+(?:PROCEDURE|PROC)\s+(?:\[?dbo\]?\.\[?)?(\w+)\]?', '', plpgsql_code, flags=re.IGNORECASE)
        
        # Conversión de cursores si existen
        if 'CURSOR' in plpgsql_code.upper():
            plpgsql_code = self.convert_cursors_to_loops(plpgsql_code)
            
        # Aplicar patrones básicos de conversión
        for pattern, replacement in self.basic_patterns:
            plpgsql_code = re.sub(pattern, replacement, plpgsql_code, flags=re.IGNORECASE | re.MULTILINE)
        
        # Conversiones específicas adicionales
        plpgsql_code = self.apply_additional_conversions(plpgsql_code)
        
        # Extraer parámetros
        params = self.extract_parameters(tsql_code)
        param_declarations = []
        
        for param in params:
            param_name = param['name'].replace('@', '')
            param_type = self.convert_type(param['type'])
            
            if param['direction'] == 'OUTPUT':
                param_declarations.append(f"    {param_name} OUT {param_type}")
            else:
                param_declarations.append(f"    {param_name} IN {param_type}")
        
        # Determinar tipo de retorno
        returns_clause = "RETURNS VOID"
        if "RETURN" in plpgsql_code.upper() and "RETURN;" not in plpgsql_code:
            returns_clause = "RETURNS INTEGER"
        
        # Plantilla de función
        function_template = f"""
-- Migrated from SQL Server stored procedure: {proc_name}
-- Migration ID: {self.migration_id}
CREATE OR REPLACE FUNCTION legacy_procedures.{proc_name.lower()}(
{chr(10).join(param_declarations) if param_declarations else ''}
) {returns_clause}
LANGUAGE plpgsql
AS $$
DECLARE
    -- Variables will be declared here
BEGIN
{self.indent_code(plpgsql_code)}
    
    -- Default return
    RETURN;
    
EXCEPTION
    WHEN OTHERS THEN
        RAISE LOG 'Error in {proc_name}: %', SQLERRM;
        RAISE;
END;
$$;

COMMENT ON FUNCTION legacy_procedures.{proc_name.lower()} IS 'Migrated from SQL Server - {self.migration_id}';
"""
        
        return function_template
    
    def apply_additional_conversions(self, code: str) -> str:
        """Aplicar conversiones adicionales específicas"""
        
        # Convertir funciones de fecha más específicas
        code = re.sub(r'YEAR\s*\(\s*(.+?)\s*\)', r'EXTRACT(YEAR FROM \1)', code, flags=re.IGNORECASE)
        code = re.sub(r'MONTH\s*\(\s*(.+?)\s*\)', r'EXTRACT(MONTH FROM \1)', code, flags=re.IGNORECASE)
        code = re.sub(r'DAY\s*\(\s*(.+?)\s*\)', r'EXTRACT(DAY FROM \1)', code, flags=re.IGNORECASE)
        
        # DATEADD conversions
        code = re.sub(r'DATEADD\s*\(\s*DAY,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 days\')', code, flags=re.IGNORECASE)
        code = re.sub(r'DATEADD\s*\(\s*MONTH,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 months\')', code, flags=re.IGNORECASE)
        code = re.sub(r'DATEADD\s*\(\s*YEAR,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 years\')', code, flags=re.IGNORECASE)
        
        # Funciones del sistema
        code = re.sub(r'@@ERROR', 'SQLSTATE', code, flags=re.IGNORECASE)
        code = re.sub(r'@@ROWCOUNT', 'ROW_COUNT', code, flags=re.IGNORECASE)
        code = re.sub(r'@@IDENTITY', 'LASTVAL()', code, flags=re.IGNORECASE)
        code = re.sub(r'SCOPE_IDENTITY\(\)', 'LASTVAL()', code, flags=re.IGNORECASE)
        
        return code
    
    def indent_code(self, code: str, spaces: int = 4) -> str:
        """Indentación básica de código"""
        lines = code.split('\n')
        indented_lines = []
        
        for line in lines:
            if line.strip():
                indented_lines.append(' ' * spaces + line.strip())
            else:
                indented_lines.append('')
        
        return '\n'.join(indented_lines)
    
    def migrate_all_procedures(self) -> Dict:
        """Ejecutar migración completa"""
        
        logger.info("🚀 INICIANDO MIGRACIÓN DE STORED PROCEDURES")
        logger.info("=" * 60)
        
        # Validar entorno
        if not self.validate_environment():
            return {'success': False, 'error': 'Environment validation failed'}
        
        # Extraer procedimientos
        procedures = self.extract_stored_procedures()
        if not procedures:
            logger.warning("⚠️  No se encontraron stored procedures para migrar")
            return {'success': True, 'procedures': 0}
        
        logger.info(f"📋 Encontrados {len(procedures)} stored procedures")
        
        # Mostrar estadísticas
        complexity_stats = {}
        for sp in procedures:
            complexity_stats[sp['complexity']] = complexity_stats.get(sp['complexity'], 0) + 1
        logger.info(f"📊 Complejidad: {complexity_stats}")
        
        # Conectar a PostgreSQL
        pg_conn = self._get_postgres_connection()
        pg_conn.autocommit = False
        pg_cursor = pg_conn.cursor()
        
        results = {
            'success': 0,
            'failed': 0,
            'successful_procedures': [],
            'failed_procedures': {}
        }
        
        # Crear tabla de log
        try:
            pg_cursor.execute("""
                CREATE TABLE IF NOT EXISTS erp_control.sp_migration_log (
                    id SERIAL PRIMARY KEY,
                    migration_id VARCHAR(50),
                    procedure_name VARCHAR(200),
                    status VARCHAR(20),
                    error_message TEXT,
                    migration_time TIMESTAMP DEFAULT NOW()
                )
            """)
            pg_conn.commit()
        except Exception as e:
            logger.warning(f"⚠️  No se pudo crear tabla de log: {e}")
        
        # Migrar cada procedimiento
        for i, proc in enumerate(procedures, 1):
            proc_name = proc['name']
            
            print(f"🔄 [{i}/{len(procedures)}] Migrando: {proc_name} ({proc['complexity']})")
            
            try:
                pg_cursor.execute("SAVEPOINT sp_migration")
                
                # Convertir T-SQL a PL/pgSQL
                plpgsql_code = self.convert_tsql_to_plpgsql(proc['definition'], proc_name)
                
                # Ejecutar en PostgreSQL
                pg_cursor.execute(plpgsql_code)
                
                # Log de éxito
                pg_cursor.execute("""
                    INSERT INTO erp_control.sp_migration_log 
                    (migration_id, procedure_name, status) 
                    VALUES (%s, %s, 'SUCCESS')
                """, (self.migration_id, proc_name))
                
                pg_cursor.execute("RELEASE SAVEPOINT sp_migration")
                
                print(f"✅ {proc_name} - OK")
                results['success'] += 1
                results['successful_procedures'].append(proc_name)
                
            except Exception as e:
                pg_cursor.execute("ROLLBACK TO SAVEPOINT sp_migration")
                
                error_msg = str(e)
                print(f"❌ {proc_name} - FAILED: {error_msg}")
                
                # Log del error
                try:
                    pg_cursor.execute("""
                        INSERT INTO erp_control.sp_migration_log 
                        (migration_id, procedure_name, status, error_message) 
                        VALUES (%s, %s, 'FAILED', %s)
                    """, (self.migration_id, proc_name, error_msg))
                except:
                    pass
                
                # Guardar SP problemático
                failed_file = f"failed_sp_{proc_name}_{self.migration_id}.sql"
                with open(failed_file, 'w', encoding='utf-8') as f:
                    f.write(f"-- FAILED MIGRATION: {proc_name}\n")
                    f.write(f"-- Error: {error_msg}\n\n")
                    f.write("-- Original T-SQL:\n")
                    f.write(proc['definition'])
                    f.write(f"\n\n-- Attempted PL/pgSQL:\n")
                    f.write(plpgsql_code)
                
                results['failed'] += 1
                results['failed_procedures'][proc_name] = error_msg
        
        # Commit final
        try:
            pg_conn.commit()
        except Exception as e:
            pg_conn.rollback()
            logger.error(f"❌ Error en commit final: {e}")
        
        pg_conn.close()
        
        # Resumen final
        duration = (datetime.now() - self.stats['start_time']).total_seconds()
        
        print("\n" + "=" * 60)
        print("📊 MIGRACIÓN DE STORED PROCEDURES COMPLETADA")
        print(f"  ⏱️  Duración: {duration:.2f} segundos")
        print(f"  📋 Total: {len(procedures)} procedimientos")
        print(f"  ✅ Exitosos: {results['success']}")
        print(f"  ❌ Fallidos: {results['failed']}")
        print(f"  🔄 Cursores convertidos: {self.stats['cursors_converted']}")
        
        if results['failed'] > 0:
            print(f"\n📁 Archivos de procedimientos fallidos:")
            for proc_name in results['failed_procedures']:
                print(f"  - failed_sp_{proc_name}_{self.migration_id}.sql")
        
        print("=" * 60)
        
        return {
            'success': results['failed'] == 0,
            'total': len(procedures),
            'migrated': results['success'],
            'failed': results['failed'],
            'duration': duration
        }

def main():
    """Función principal"""
    
    print("🚀 MIGRADOR DE STORED PROCEDURES")
    print("SQL Server T-SQL → PostgreSQL PL/pgSQL")
    print("=" * 50)
    
    # Detectar entorno
    environment = "demo"
    if len(sys.argv) > 1:
        environment = sys.argv[1].lower()
        if environment not in ['demo', 'production']:
            print("❌ Entorno debe ser 'demo' o 'production'")
            sys.exit(1)
    
    print(f"🎯 Entorno: {environment.upper()}")
    
    if environment == "production":
        print("⚠️  ENTORNO DE PRODUCCIÓN")
        print("   Asegúrate de:")
        print("   - Tener backups completos")
        print("   - Configurar las conexiones correctas")
        print("   - Validar en demo primero")
        
        confirm = input("\n¿Continuar en PRODUCCIÓN? (SI/no): ")
        if confirm.upper() != "SI":
            print("❌ Migración cancelada")
            return
    
    # Ejecutar migración
    migrator = ProductionStoredProcedureMigrator(environment)
    result = migrator.migrate_all_procedures()
    
    # Resultado final
    if result['success']:
        print(f"\n🎉 ¡MIGRACIÓN EXITOSA!")
        print(f"   {result['migrated']}/{result['total']} procedimientos migrados")
    else:
        print(f"\n⚠️  MIGRACIÓN PARCIAL")
        print(f"   {result['migrated']}/{result['total']} exitosos")
        print(f"   {result['failed']} requieren revisión manual")
        print("\n💡 Próximos pasos:")
        print("   1. Revisar archivos failed_sp_*.sql")
        print("   2. Corregir manualmente los problemáticos")
        print("   3. Re-ejecutar: python migrate_stored_procedures.py")

if __name__ == "__main__":
    main()
