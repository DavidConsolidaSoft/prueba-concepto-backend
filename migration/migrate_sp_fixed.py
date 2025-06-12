#!/usr/bin/env python3
"""
MIGRADOR DE STORED PROCEDURES - VERSIÓN CORREGIDA
Soluciona el problema de parsing de parámetros en Windows
"""

import re
import logging
import psycopg2
import pyodbc
from datetime import datetime

# Configurar logging sin emojis para Windows
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'sp_migration_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FixedStoredProcedureMigrator:
    """Migrador corregido para Windows"""
    
    def __init__(self, environment: str = "demo"):
        self.environment = environment
        self.migration_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.configs = self._get_environment_configs()
        
        # Mapeo de tipos mejorado
        self.type_mapping = {
            'INT': 'INTEGER',
            'BIGINT': 'BIGINT',
            'SMALLINT': 'SMALLINT',
            'TINYINT': 'SMALLINT',
            'BIT': 'BOOLEAN',
            'DECIMAL': 'DECIMAL',
            'NUMERIC': 'DECIMAL',
            'MONEY': 'DECIMAL(19,4)',
            'FLOAT': 'DOUBLE PRECISION',
            'REAL': 'REAL',
            'DATETIME': 'TIMESTAMP WITH TIME ZONE',
            'DATETIME2': 'TIMESTAMP WITH TIME ZONE',
            'DATE': 'DATE',
            'TIME': 'TIME',
            'VARCHAR': 'VARCHAR',
            'NVARCHAR': 'VARCHAR',
            'CHAR': 'CHAR',
            'TEXT': 'TEXT',
            'NTEXT': 'TEXT',
            'UNIQUEIDENTIFIER': 'UUID',
            'VARBINARY': 'BYTEA'
        }
    
    def _get_environment_configs(self):
        return {
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
            }
        }[self.environment]
    
    def get_sql_connection(self):
        config = self.configs['sql_server']
        conn_str = (
            f"DRIVER={config['driver']};"
            f"SERVER={config['server']},{config['port']};"
            f"DATABASE={config['database']};"
            f"UID={config['username']};"
            f"PWD={config['password']};"
            f"TrustServerCertificate=yes;"
        )
        return pyodbc.connect(conn_str)
    
    def get_pg_connection(self):
        config = self.configs['postgres']
        return psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['username'],
            password=config['password']
        )
    
    def extract_stored_procedures(self):
        """Extraer SPs con mejor parsing"""
        conn = self.get_sql_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT 
            p.name AS procedure_name,
            m.definition AS procedure_definition
        FROM sys.procedures p
        INNER JOIN sys.sql_modules m ON p.object_id = m.object_id
        WHERE p.is_ms_shipped = 0
        ORDER BY p.name
        """
        
        cursor.execute(query)
        procedures = cursor.fetchall()
        
        sp_list = []
        for proc in procedures:
            sp_info = {
                'name': proc[0],
                'definition': proc[1] or ""
            }
            sp_list.append(sp_info)
        
        conn.close()
        print(f"Extraidos {len(sp_list)} stored procedures")
        return sp_list
    
    def extract_parameters_fixed(self, tsql_code: str) -> list:
        """Extracción mejorada de parámetros"""
        
        # Limpiar el código primero
        clean_code = tsql_code.replace('\r\n', '\n').replace('\r', '\n')
        
        # Buscar la sección de parámetros después de CREATE PROCEDURE
        proc_pattern = r'CREATE\s+(?:PROCEDURE|PROC)\s+(?:\[?dbo\]?\.\[?)?(\w+)\]?(.+?)(?=AS\s|BEGIN\s|\$\$|$)'
        proc_match = re.search(proc_pattern, clean_code, re.IGNORECASE | re.DOTALL)
        
        if not proc_match:
            return []
        
        param_section = proc_match.group(2).strip()
        
        # Pattern mejorado para parámetros
        params = []
        param_lines = param_section.split('\n')
        
        for line in param_lines:
            line = line.strip()
            if line and line.startswith('@'):
                # Pattern simple: @nombre tipo
                parts = line.replace(',', '').split()
                if len(parts) >= 2:
                    param_name = parts[0]
                    param_type = parts[1]
                    
                    # Limpiar tipo
                    param_type = re.sub(r'[,\s]*$', '', param_type)
                    
                    params.append({
                        'name': param_name,
                        'type': param_type,
                        'direction': 'OUTPUT' if 'OUTPUT' in line.upper() or 'OUT' in line.upper() else 'INPUT'
                    })
        
        return params
    
    def convert_type_fixed(self, sql_type: str) -> str:
        """Conversión mejorada de tipos"""
        sql_type = sql_type.upper().strip()
        
        # Casos especiales
        if 'VARCHAR(MAX)' in sql_type or 'NVARCHAR(MAX)' in sql_type:
            return 'TEXT'
        
        # Extraer tipo base
        base_type = sql_type.split('(')[0] if '(' in sql_type else sql_type
        
        # Mapear tipo
        pg_type = self.type_mapping.get(base_type, 'TEXT')
        
        # Mantener parámetros para ciertos tipos
        if '(' in sql_type and pg_type in ['VARCHAR', 'CHAR', 'DECIMAL']:
            params = sql_type.split('(')[1].split(')')[0]
            return f"{pg_type}({params})"
        
        return pg_type
    
    def convert_tsql_to_plpgsql_fixed(self, tsql_code: str, proc_name: str) -> str:
        """Conversión corregida de T-SQL a PL/pgSQL"""
        
        # Extraer parámetros ANTES de limpiar el código
        params = self.extract_parameters_fixed(tsql_code)
        
        # Limpiar código
        clean_code = tsql_code
        
        # Remover CREATE PROCEDURE
        clean_code = re.sub(r'CREATE\s+(?:PROCEDURE|PROC)\s+(?:\[?dbo\]?\.\[?)?(\w+)\]?.*?AS\s*', '', clean_code, flags=re.IGNORECASE | re.DOTALL)
        
        # Conversiones básicas
        conversions = [
            (r'DECLARE\s+(@\w+)\s+(\w+(?:\([^)]+\))?)', r'DECLARE \1 \2;'),
            (r'SET\s+(@\w+)\s*=\s*(.+)', r'\1 := \2;'),
            (r'@(\w+)', r'\1'),  # Remover @ de variables
            (r'GETDATE\s*\(\s*\)', 'NOW()'),
            (r'ISNULL\s*\(\s*(.+?),\s*(.+?)\s*\)', r'COALESCE(\1, \2)'),
            (r'LEN\s*\(\s*(.+?)\s*\)', r'LENGTH(\1)'),
            (r'PRINT\s+(.+)', r'RAISE NOTICE \'%\', \1;'),
        ]
        
        for pattern, replacement in conversions:
            clean_code = re.sub(pattern, replacement, clean_code, flags=re.IGNORECASE)
        
        # Generar declaraciones de parámetros
        param_declarations = []
        for param in params:
            param_name = param['name'].replace('@', '')
            param_type = self.convert_type_fixed(param['type'])
            
            if param['direction'] == 'OUTPUT':
                param_declarations.append(f"    {param_name} OUT {param_type}")
            else:
                param_declarations.append(f"    {param_name} IN {param_type}")
        
        # Plantilla corregida
        function_template = f"""-- Migrated SP: {proc_name}
CREATE OR REPLACE FUNCTION legacy_procedures.{proc_name.lower()}(
{chr(10).join(param_declarations) if param_declarations else ''}
) RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    -- Original procedure logic converted
{self.indent_code(clean_code)}
    
    RETURN;
EXCEPTION
    WHEN OTHERS THEN
        RAISE LOG 'Error in %: %', '{proc_name}', SQLERRM;
        RAISE;
END;
$$;
"""
        
        return function_template
    
    def indent_code(self, code: str, spaces: int = 4) -> str:
        """Indentación simple"""
        lines = code.split('\n')
        indented = []
        
        for line in lines:
            if line.strip():
                indented.append(' ' * spaces + line.strip())
            else:
                indented.append('')
        
        return '\n'.join(indented)
    
    def migrate_procedures(self):
        """Migrar todos los procedimientos"""
        
        print("Iniciando migracion de stored procedures...")
        print("=" * 50)
        
        # Validar conexiones
        try:
            sql_conn = self.get_sql_connection()
            print("SQL Server conectado")
            sql_conn.close()
            
            pg_conn = self.get_pg_connection()
            print("PostgreSQL conectado")
            
            # Crear schema
            cur = pg_conn.cursor()
            cur.execute("CREATE SCHEMA IF NOT EXISTS legacy_procedures")
            cur.execute("CREATE SCHEMA IF NOT EXISTS erp_control")
            pg_conn.commit()
            pg_conn.close()
            
        except Exception as e:
            print(f"Error de conexion: {e}")
            return
        
        # Extraer procedimientos
        procedures = self.extract_stored_procedures()
        if not procedures:
            print("No se encontraron stored procedures")
            return
        
        # Conectar a PostgreSQL para migración
        pg_conn = self.get_pg_connection()
        pg_conn.autocommit = False
        cur = pg_conn.cursor()
        
        # Crear tabla de log
        try:
            cur.execute("""
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
        except:
            pass
        
        success_count = 0
        failed_count = 0
        
        # Migrar cada procedimiento
        for i, proc in enumerate(procedures, 1):
            proc_name = proc['name']
            print(f"[{i}/{len(procedures)}] Migrando: {proc_name}")
            
            try:
                cur.execute("SAVEPOINT sp_migration")
                
                # Convertir
                plpgsql_code = self.convert_tsql_to_plpgsql_fixed(proc['definition'], proc_name)
                
                # Ejecutar
                cur.execute(plpgsql_code)
                
                # Log success
                cur.execute("""
                    INSERT INTO erp_control.sp_migration_log 
                    (migration_id, procedure_name, status) 
                    VALUES (%s, %s, 'SUCCESS')
                """, (self.migration_id, proc_name))
                
                cur.execute("RELEASE SAVEPOINT sp_migration")
                
                print(f"✓ {proc_name} - OK")
                success_count += 1
                
            except Exception as e:
                cur.execute("ROLLBACK TO SAVEPOINT sp_migration")
                
                error_msg = str(e)
                print(f"✗ {proc_name} - FAILED: {error_msg}")
                
                # Guardar SP fallido
                failed_file = f"failed_sp_{proc_name}_{self.migration_id}.sql"
                with open(failed_file, 'w', encoding='utf-8') as f:
                    f.write(f"-- FAILED: {proc_name}\n")
                    f.write(f"-- Error: {error_msg}\n\n")
                    f.write("-- Original T-SQL:\n")
                    f.write(proc['definition'])
                    f.write(f"\n\n-- Attempted PL/pgSQL:\n")
                    f.write(plpgsql_code)
                
                # Log error
                try:
                    cur.execute("""
                        INSERT INTO erp_control.sp_migration_log 
                        (migration_id, procedure_name, status, error_message) 
                        VALUES (%s, %s, 'FAILED', %s)
                    """, (self.migration_id, proc_name, error_msg))
                except:
                    pass
                
                failed_count += 1
        
        # Commit final
        try:
            pg_conn.commit()
        except Exception as e:
            pg_conn.rollback()
            print(f"Error en commit: {e}")
        
        pg_conn.close()
        
        # Resumen
        print("\n" + "=" * 50)
        print("MIGRACION COMPLETADA")
        print(f"Total: {len(procedures)} procedimientos")
        print(f"Exitosos: {success_count}")
        print(f"Fallidos: {failed_count}")
        
        if failed_count > 0:
            print(f"\nArchivos generados para revision:")
            for proc in procedures:
                if any(proc['name'] in str(e) for e in []):  # Logic for failed ones
                    print(f"  - failed_sp_{proc['name']}_{self.migration_id}.sql")
        
        return success_count > 0

def main():
    print("MIGRADOR DE STORED PROCEDURES - VERSION CORREGIDA")
    print("=" * 55)
    
    migrator = FixedStoredProcedureMigrator('demo')
    result = migrator.migrate_procedures()
    
    if result:
        print("\n¡Migracion exitosa!")
        print("Algunas funciones pueden requerir ajustes manuales menores.")
    else:
        print("\nRevisar archivos failed_sp_*.sql para ajustes manuales.")

if __name__ == "__main__":
    main()
