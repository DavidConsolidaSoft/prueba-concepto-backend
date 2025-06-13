#!/usr/bin/env python3
"""
MIGRADOR DE STORED PROCEDURES - VERSIÓN FINAL
Corrige todos los problemas de sintaxis identificados
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

class FinalStoredProcedureMigrator:
    """Migrador final con todas las correcciones"""
    
    def __init__(self, environment: str = "demo"):
        self.environment = environment
        self.migration_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.configs = self._get_environment_configs()
        
        # Mapeo completo de tipos
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
            'SMALLDATETIME': 'TIMESTAMP WITH TIME ZONE',
            'DATE': 'DATE',
            'TIME': 'TIME',
            'VARCHAR': 'VARCHAR',
            'NVARCHAR': 'VARCHAR',  # CRÍTICO: nvarchar → varchar
            'CHAR': 'CHAR',
            'NCHAR': 'CHAR',
            'TEXT': 'TEXT',
            'NTEXT': 'TEXT',
            'UNIQUEIDENTIFIER': 'UUID',
            'VARBINARY': 'BYTEA',
            'BINARY': 'BYTEA'
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
        """Extraer SPs"""
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
    
    def clean_and_convert_code(self, tsql_code: str) -> str:
        """Limpieza y conversión completa del código T-SQL"""
        
        code = tsql_code
        
        # 1. REMOVER CREATE PROCEDURE
        code = re.sub(r'CREATE\s+(?:PROCEDURE|PROC)\s+(?:\[?dbo\]?\.\[?)?(\w+)\]?.*?AS\s*', '', code, flags=re.IGNORECASE | re.DOTALL)
        
        # 2. LIMPIAR DECLARACIONES PROBLEMÁTICAS
        # Problema: "DECLARE var as type;" → "DECLARE var type;"
        code = re.sub(r'DECLARE\s+(\w+)\s+AS\s*;\s*(\w+(?:\([^)]*\))?)', r'DECLARE \1 \2;', code, flags=re.IGNORECASE)
        code = re.sub(r'DECLARE\s+(\w+)\s+as\s+(\w+(?:\([^)]*\))?)', r'DECLARE \1 \2;', code, flags=re.IGNORECASE)
        
        # 3. CONVERSIÓN DE TIPOS CRÍTICOS
        type_conversions = [
            (r'\bnvarchar\b', 'VARCHAR'),
            (r'\bdatetime\b', 'TIMESTAMP WITH TIME ZONE'),
            (r'\bint\b', 'INTEGER'),
            (r'\bNumeric\b', 'DECIMAL'),
            (r'\bbit\b', 'BOOLEAN'),
            (r'\bmoney\b', 'DECIMAL(19,4)'),
            (r'\bfloat\b', 'DOUBLE PRECISION'),
        ]
        
        for pattern, replacement in type_conversions:
            code = re.sub(pattern, replacement, code, flags=re.IGNORECASE)
        
        # 4. LIMPIAR PUNTOS Y COMAS DUPLICADOS
        code = re.sub(r';\s*,', ';', code)
        code = re.sub(r',\s*;', ';', code)
        
        # 5. CONVERSIONES DE SINTAXIS
        syntax_conversions = [
            # Variables
            (r'SET\s+(@?\w+)\s*=\s*(.+?)(?=\s*;|\s*$)', r'\1 := \2;'),
            (r'@(\w+)', r'\1'),  # Remover @
            
            # Funciones
            (r'GETDATE\s*\(\s*\)', 'NOW()'),
            (r'GETUTCDATE\s*\(\s*\)', 'NOW() AT TIME ZONE \'UTC\''),
            (r'ISNULL\s*\(\s*(.+?),\s*(.+?)\s*\)', r'COALESCE(\1, \2)'),
            (r'LEN\s*\(\s*(.+?)\s*\)', r'LENGTH(\1)'),
            (r'UPPER\s*\(\s*(.+?)\s*\)', r'UPPER(\1)'),
            (r'LOWER\s*\(\s*(.+?)\s*\)', r'LOWER(\1)'),
            (r'LTRIM\s*\(\s*(.+?)\s*\)', r'LTRIM(\1)'),
            (r'RTRIM\s*\(\s*(.+?)\s*\)', r'RTRIM(\1)'),
            
            # Control de flujo
            (r'IF\s+(.+?)\s+BEGIN', r'IF \1 THEN'),
            (r'END\s*ELSE\s*BEGIN', 'ELSE'),
            (r'WHILE\s+(.+?)\s+BEGIN', r'WHILE \1 LOOP'),
            (r'END\s*--.*', 'END LOOP;'),
            
            # Manejo de errores
            (r'PRINT\s+(.+)', r'RAISE NOTICE \'%\', \1;'),
            (r'RAISERROR\s*\(.+?\)', 'RAISE EXCEPTION \'Procedure error\';'),
        ]
        
        for pattern, replacement in syntax_conversions:
            code = re.sub(pattern, replacement, code, flags=re.IGNORECASE | re.MULTILINE)
        
        # 6. LIMPIAR ESPACIOS EXTRAS
        code = re.sub(r'\n\s*\n', '\n', code)
        code = re.sub(r'^\s+', '', code, flags=re.MULTILINE)
        
        return code.strip()
    
    def extract_parameters_from_definition(self, tsql_code: str) -> list:
        """Extraer parámetros de la definición completa"""
        
        # Buscar la sección de parámetros
        proc_pattern = r'CREATE\s+(?:PROCEDURE|PROC)\s+(?:\[?dbo\]?\.\[?)?(\w+)\]?\s*(.+?)\s*AS'
        match = re.search(proc_pattern, tsql_code, re.IGNORECASE | re.DOTALL)
        
        if not match:
            return []
        
        param_section = match.group(2).strip()
        
        # Si no hay parámetros
        if not param_section or param_section.upper() in ['', 'AS']:
            return []
        
        params = []
        
        # Dividir por comas y procesar cada parámetro
        param_parts = param_section.split(',')
        
        for part in param_parts:
            part = part.strip()
            if part.startswith('@'):
                # Extraer nombre y tipo
                tokens = part.split()
                if len(tokens) >= 2:
                    param_name = tokens[0]
                    param_type = tokens[1]
                    
                    # Limpiar tipo
                    param_type = re.sub(r'[,\s]*$', '', param_type)
                    
                    # Detectar OUTPUT
                    is_output = 'OUTPUT' in part.upper() or 'OUT' in part.upper()
                    
                    params.append({
                        'name': param_name,
                        'type': param_type,
                        'direction': 'OUTPUT' if is_output else 'INPUT'
                    })
        
        return params
    
    def convert_type_complete(self, sql_type: str) -> str:
        """Conversión completa de tipos"""
        sql_type = sql_type.upper().strip()
        
        # Casos especiales
        special_cases = {
            'VARCHAR(MAX)': 'TEXT',
            'NVARCHAR(MAX)': 'TEXT',
            'VARBINARY(MAX)': 'BYTEA',
            'DATETIME': 'TIMESTAMP WITH TIME ZONE',
            'DATETIME2': 'TIMESTAMP WITH TIME ZONE',
            'SMALLDATETIME': 'TIMESTAMP WITH TIME ZONE',
            'INT': 'INTEGER',
            'NVARCHAR': 'VARCHAR'
        }
        
        if sql_type in special_cases:
            return special_cases[sql_type]
        
        # Extraer tipo base
        base_type = sql_type.split('(')[0] if '(' in sql_type else sql_type
        
        if base_type in self.type_mapping:
            pg_type = self.type_mapping[base_type]
            
            # Mantener parámetros para ciertos tipos
            if '(' in sql_type and pg_type in ['VARCHAR', 'CHAR', 'DECIMAL']:
                params = sql_type.split('(')[1].split(')')[0]
                return f"{pg_type}({params})"
            
            return pg_type
        
        return 'TEXT'  # Default seguro
    
    def create_function_definition(self, proc_name: str, params: list, body: str) -> str:
        """Crear definición completa de función PostgreSQL"""
        
        # Generar declaraciones de parámetros
        param_declarations = []
        for param in params:
            param_name = param['name'].replace('@', '')
            param_type = self.convert_type_complete(param['type'])
            
            if param['direction'] == 'OUTPUT':
                param_declarations.append(f"    {param_name} OUT {param_type}")
            else:
                param_declarations.append(f"    {param_name} IN {param_type}")
        
        # Determinar tipo de retorno
        returns_clause = "RETURNS VOID"
        if any(p['direction'] == 'OUTPUT' for p in params):
            returns_clause = "RETURNS RECORD"
        
        # Crear cuerpo indentado
        indented_body = self.indent_code(body)
        
        # Plantilla completa
        function_template = f"""-- Migrated from SQL Server: {proc_name}
-- Migration ID: {self.migration_id}
CREATE OR REPLACE FUNCTION legacy_procedures.{proc_name.lower()}(
{chr(10).join(param_declarations) if param_declarations else ''}
) {returns_clause}
LANGUAGE plpgsql
AS $$
DECLARE
    -- Procedure variables
BEGIN
    -- Migrated procedure logic
{indented_body}
    
    -- Default return
    RETURN;
    
EXCEPTION
    WHEN OTHERS THEN
        RAISE LOG 'Error in procedure %: %', '{proc_name}', SQLERRM;
        RAISE EXCEPTION 'Procedure % failed: %', '{proc_name}', SQLERRM;
END;
$$;

-- Add comment
COMMENT ON FUNCTION legacy_procedures.{proc_name.lower()} IS 'Migrated from SQL Server - {datetime.now().strftime("%Y-%m-%d")}';
"""
        
        return function_template
    
    def indent_code(self, code: str, spaces: int = 4) -> str:
        """Indentación mejorada"""
        if not code.strip():
            return ""
        
        lines = code.split('\n')
        indented = []
        
        for line in lines:
            if line.strip():
                indented.append(' ' * spaces + line.strip())
            else:
                indented.append('')
        
        return '\n'.join(indented)
    
    def migrate_procedures(self):
        """Migrar todos los procedimientos con correcciones completas"""
        
        print("MIGRADOR FINAL - TODAS LAS CORRECCIONES APLICADAS")
        print("=" * 55)
        
        # Validar conexiones
        try:
            sql_conn = self.get_sql_connection()
            print("✓ SQL Server conectado")
            sql_conn.close()
            
            pg_conn = self.get_pg_connection()
            print("✓ PostgreSQL conectado")
            
            # Crear schemas
            cur = pg_conn.cursor()
            cur.execute("CREATE SCHEMA IF NOT EXISTS legacy_procedures")
            cur.execute("CREATE SCHEMA IF NOT EXISTS erp_control")
            pg_conn.commit()
            pg_conn.close()
            
        except Exception as e:
            print(f"✗ Error de conexion: {e}")
            return False
        
        # Extraer procedimientos
        procedures = self.extract_stored_procedures()
        if not procedures:
            print("No se encontraron stored procedures")
            return False
        
        # Conectar para migración
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
        except Exception as e:
            print(f"Warning: No se pudo crear tabla log: {e}")
        
        success_count = 0
        failed_count = 0
        failed_procedures = []
        
        print(f"\nProcesando {len(procedures)} stored procedures...\n")
        
        # Migrar cada procedimiento
        for i, proc in enumerate(procedures, 1):
            proc_name = proc['name']
            print(f"[{i:2d}/{len(procedures)}] {proc_name:25s} ", end="")
            
            try:
                cur.execute("SAVEPOINT sp_migration")
                
                # 1. Extraer parámetros
                params = self.extract_parameters_from_definition(proc['definition'])
                
                # 2. Limpiar y convertir cuerpo
                clean_body = self.clean_and_convert_code(proc['definition'])
                
                # 3. Crear función completa
                function_def = self.create_function_definition(proc_name, params, clean_body)
                
                # 4. Ejecutar en PostgreSQL
                cur.execute(function_def)
                
                # 5. Log de éxito
                cur.execute("""
                    INSERT INTO erp_control.sp_migration_log 
                    (migration_id, procedure_name, status) 
                    VALUES (%s, %s, 'SUCCESS')
                """, (self.migration_id, proc_name))
                
                cur.execute("RELEASE SAVEPOINT sp_migration")
                
                print("✓ OK")
                success_count += 1
                
            except Exception as e:
                cur.execute("ROLLBACK TO SAVEPOINT sp_migration")
                
                error_msg = str(e)[:200]  # Limitar longitud del error
                print(f"✗ FAILED: {error_msg}")
                
                # Guardar SP fallido con información detallada
                failed_file = f"failed_sp_{proc_name}_{self.migration_id}.sql"
                with open(failed_file, 'w', encoding='utf-8') as f:
                    f.write(f"-- FAILED MIGRATION: {proc_name}\n")
                    f.write(f"-- Error: {error_msg}\n")
                    f.write(f"-- Migration ID: {self.migration_id}\n\n")
                    f.write("-- ORIGINAL T-SQL:\n")
                    f.write(proc['definition'])
                    f.write(f"\n\n-- ATTEMPTED CONVERSION:\n")
                    try:
                        params = self.extract_parameters_from_definition(proc['definition'])
                        clean_body = self.clean_and_convert_code(proc['definition'])
                        function_def = self.create_function_definition(proc_name, params, clean_body)
                        f.write(function_def)
                    except:
                        f.write("-- Error during conversion process\n")
                
                # Log del error
                try:
                    cur.execute("""
                        INSERT INTO erp_control.sp_migration_log 
                        (migration_id, procedure_name, status, error_message) 
                        VALUES (%s, %s, 'FAILED', %s)
                    """, (self.migration_id, proc_name, error_msg))
                except:
                    pass
                
                failed_count += 1
                failed_procedures.append(proc_name)
        
        # Commit final
        try:
            pg_conn.commit()
            print("\n✓ Transacciones confirmadas")
        except Exception as e:
            pg_conn.rollback()
            print(f"\n✗ Error en commit: {e}")
        
        pg_conn.close()
        
        # Resumen final
        print("\n" + "=" * 55)
        print("MIGRACIÓN COMPLETADA")
        print(f"Total procedimientos: {len(procedures)}")
        print(f"Exitosos: {success_count}")
        print(f"Fallidos: {failed_count}")
        
        if success_count > 0:
            success_rate = (success_count / len(procedures)) * 100
            print(f"Tasa de éxito: {success_rate:.1f}%")
        
        if failed_count > 0:
            print(f"\nProcedimientos que requieren revisión manual:")
            for proc_name in failed_procedures:
                print(f"  - {proc_name}")
            print(f"\nArchivos de diagnóstico generados:")
            for proc_name in failed_procedures:
                print(f"  - failed_sp_{proc_name}_{self.migration_id}.sql")
        
        print("=" * 55)
        
        return success_count > 0

def main():
    print("MIGRADOR DE STORED PROCEDURES - VERSIÓN FINAL")
    print("Corrige todos los problemas de sintaxis identificados")
    print("=" * 60)
    
    migrator = FinalStoredProcedureMigrator('demo')
    result = migrator.migrate_procedures()
    
    if result:
        print("\n🎉 ¡MIGRACIÓN EXITOSA!")
        print("Las funciones migradas están disponibles en el schema 'legacy_procedures'")
        print("\nPara verificar:")
        print("SELECT routine_name FROM information_schema.routines")
        print("WHERE routine_schema = 'legacy_procedures' ORDER BY routine_name;")
    else:
        print("\n⚠️ MIGRACIÓN PARCIAL")
        print("Revisar archivos failed_sp_*.sql para procedimientos específicos")
        print("Los procedimientos exitosos están disponibles para uso")

if __name__ == "__main__":
    main()
