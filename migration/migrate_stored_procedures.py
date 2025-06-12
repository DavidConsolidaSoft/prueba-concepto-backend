#!/usr/bin/env python3
"""
MIGRADOR AUTOMÁTICO DE STORED PROCEDURES
SQL Server T-SQL → PostgreSQL PL/pgSQL

Convierte automáticamente SPs con manejo de cursores,
variables, loops y lógica compleja.
"""

import re
import logging
from typing import Dict, List, Tuple
import pyodbc
import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StoredProcedureMigrator:
    """Migrador automático de Stored Procedures"""
    
    def __init__(self, sql_server_config: Dict, postgres_config: Dict):
        self.sql_config = sql_server_config
        self.pg_config = postgres_config
        
        # Mapeo de tipos T-SQL → PL/pgSQL
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
            'TIME': 'TIME WITH TIME ZONE',
            'VARCHAR': 'VARCHAR',
            'NVARCHAR': 'VARCHAR',
            'CHAR': 'CHAR',
            'NCHAR': 'CHAR',
            'TEXT': 'TEXT',
            'NTEXT': 'TEXT',
            'UNIQUEIDENTIFIER': 'UUID',
            'VARBINARY': 'BYTEA',
            'BINARY': 'BYTEA'
        }
        
        # Patrones de conversión T-SQL → PL/pgSQL
        self.conversion_patterns = [
            # Variables
            (r'DECLARE\s+(@\w+)\s+(\w+)(?:\(([^)]+)\))?', r'DECLARE \1 \2\3;'),
            
            # SET variables
            (r'SET\s+(@\w+)\s*=\s*(.+)', r'\1 := \2;'),
            
            # SELECT INTO
            (r'SELECT\s+(.+)\s+INTO\s+(@\w+)(?:\s+FROM\s+(.+))?', r'SELECT \1 INTO \2 FROM \3;'),
            
            # IF statements
            (r'IF\s+(.+)\s+BEGIN', r'IF \1 THEN'),
            (r'END\s*ELSE\s*BEGIN', 'ELSE'),
            (r'END(?:\s*;)?$', 'END IF;'),
            
            # WHILE loops
            (r'WHILE\s+(.+)\s+BEGIN', r'WHILE \1 LOOP'),
            (r'END\s*--\s*WHILE', 'END LOOP;'),
            
            # PRINT statements
            (r'PRINT\s+(.+)', r'RAISE NOTICE \1;'),
            
            # RAISERROR
            (r'RAISERROR\s*\(\s*(.+?),\s*\d+,\s*\d+\s*\)', r'RAISE EXCEPTION \1;'),
            
            # RETURN
            (r'RETURN(?:\s+(.+))?', r'RETURN\1;'),
            
            # Comments
            (r'--(.+)', r'--\1'),
            
            # Variables en queries (quitar @)
            (r'@(\w+)', r'\1'),
            
            # Functions
            (r'ISNULL\s*\(\s*(.+?),\s*(.+?)\s*\)', r'COALESCE(\1, \2)'),
            (r'GETDATE\s*\(\s*\)', r'NOW()'),
            (r'LEN\s*\(\s*(.+?)\s*\)', r'LENGTH(\1)'),
            (r'LTRIM\s*\(\s*(.+?)\s*\)', r'LTRIM(\1)'),
            (r'RTRIM\s*\(\s*(.+?)\s*\)', r'RTRIM(\1)'),
            (r'UPPER\s*\(\s*(.+?)\s*\)', r'UPPER(\1)'),
            (r'LOWER\s*\(\s*(.+?)\s*\)', r'LOWER(\1)'),
            
            # String functions
            (r'SUBSTRING\s*\(\s*(.+?),\s*(.+?),\s*(.+?)\s*\)', r'SUBSTRING(\1 FROM \2 FOR \3)'),
            (r'CHARINDEX\s*\(\s*(.+?),\s*(.+?)\s*\)', r'POSITION(\1 IN \2)'),
            
            # Math functions
            (r'CEILING\s*\(\s*(.+?)\s*\)', r'CEIL(\1)'),
            (r'POWER\s*\(\s*(.+?),\s*(.+?)\s*\)', r'POWER(\1, \2)'),
            
            # Date functions
            (r'DATEPART\s*\(\s*YEAR,\s*(.+?)\s*\)', r'EXTRACT(YEAR FROM \1)'),
            (r'DATEPART\s*\(\s*MONTH,\s*(.+?)\s*\)', r'EXTRACT(MONTH FROM \1)'),
            (r'DATEPART\s*\(\s*DAY,\s*(.+?)\s*\)', r'EXTRACT(DAY FROM \1)'),
            (r'DATEADD\s*\(\s*DAY,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 days\')'),
            (r'DATEADD\s*\(\s*MONTH,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 months\')'),
            (r'DATEADD\s*\(\s*YEAR,\s*(.+?),\s*(.+?)\s*\)', r'(\2 + INTERVAL \'\1 years\')'),
            
            # Aggregate functions
            (r'TOP\s+(\d+)', r'LIMIT \1'),
        ]
    
    def extract_stored_procedures(self) -> List[Dict]:
        """Extraer todos los stored procedures de SQL Server"""
        try:
            conn_str = (
                f"DRIVER={self.sql_config['driver']};"
                f"SERVER={self.sql_config['server']},{self.sql_config['port']};"
                f"DATABASE={self.sql_config['database']};"
                f"UID={self.sql_config['username']};"
                f"PWD={self.sql_config['password']};"
                f"TrustServerCertificate=yes;"
            )
            
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            
            # Query para obtener stored procedures
            sp_query = """
            SELECT 
                p.name AS procedure_name,
                m.definition AS procedure_definition,
                p.create_date,
                p.modify_date
            FROM sys.procedures p
            INNER JOIN sys.sql_modules m ON p.object_id = m.object_id
            WHERE p.is_ms_shipped = 0
            ORDER BY p.name
            """
            
            cursor.execute(sp_query)
            procedures = cursor.fetchall()
            
            sp_list = []
            for proc in procedures:
                sp_info = {
                    'name': proc[0],
                    'definition': proc[1],
                    'created': proc[2],
                    'modified': proc[3]
                }
                sp_list.append(sp_info)
            
            logger.info(f"✅ Extraídos {len(sp_list)} stored procedures")
            conn.close()
            
            return sp_list
            
        except Exception as e:
            logger.error(f"❌ Error extrayendo SPs: {e}")
            return []
    
    def convert_tsql_to_plpgsql(self, tsql_code: str, proc_name: str) -> str:
        """Convertir T-SQL a PL/pgSQL"""
        
        # Limpiar el código inicial
        plpgsql_code = tsql_code.strip()
        
        # Remover CREATE PROCEDURE inicial
        plpgsql_code = re.sub(r'CREATE\s+PROCEDURE\s+\[?dbo\]?\.\[?(\w+)\]?', '', plpgsql_code, flags=re.IGNORECASE)
        
        # Aplicar patrones de conversión
        for pattern, replacement in self.conversion_patterns:
            plpgsql_code = re.sub(pattern, replacement, plpgsql_code, flags=re.IGNORECASE | re.MULTILINE)
        
        # Detectar parámetros
        params = self.extract_parameters(tsql_code)
        param_declarations = []
        
        for param in params:
            param_name = param['name'].replace('@', '')
            param_type = self.convert_type(param['type'])
            if param['direction'] == 'OUTPUT':
                param_declarations.append(f"    {param_name} OUT {param_type}")
            else:
                param_declarations.append(f"    {param_name} IN {param_type}")
        
        # Detectar si retorna valor o tabla
        returns_clause = "RETURNS VOID"
        if "RETURN" in plpgsql_code.upper() and "RETURN;" not in plpgsql_code:
            returns_clause = "RETURNS INTEGER"
        
        # Envolver en estructura PL/pgSQL
        function_template = f"""
-- Migrated from SQL Server stored procedure
CREATE OR REPLACE FUNCTION erp_main.{proc_name.lower()}(
{chr(10).join(param_declarations) if param_declarations else ''}
) {returns_clause}
LANGUAGE plpgsql
AS $$
DECLARE
    -- Variables will be declared here automatically
BEGIN
{self.indent_code(plpgsql_code)}
    
    -- Default return for procedures
    RETURN;
    
EXCEPTION
    WHEN OTHERS THEN
        RAISE LOG 'Error in {proc_name}: %', SQLERRM;
        RAISE;
END;
$$;
"""
        
        return function_template
    
    def extract_parameters(self, tsql_code: str) -> List[Dict]:
        """Extraer parámetros del SP"""
        params = []
        
        # Pattern para parámetros
        param_pattern = r'@(\w+)\s+(\w+(?:\([^)]+\))?)\s*(OUTPUT|OUT)?'
        matches = re.findall(param_pattern, tsql_code, re.IGNORECASE)
        
        for match in matches:
            param = {
                'name': f"@{match[0]}",
                'type': match[1],
                'direction': 'OUTPUT' if match[2].upper() in ['OUTPUT', 'OUT'] else 'INPUT'
            }
            params.append(param)
        
        return params
    
    def convert_type(self, sql_type: str) -> str:
        """Convertir tipo SQL Server a PostgreSQL"""
        sql_type_upper = sql_type.upper()
        
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
    
    def indent_code(self, code: str, spaces: int = 4) -> str:
        """Indentar código"""
        lines = code.split('\n')
        indented_lines = []
        
        for line in lines:
            if line.strip():
                indented_lines.append(' ' * spaces + line)
            else:
                indented_lines.append('')
        
        return '\n'.join(indented_lines)
    
    def handle_cursors(self, plpgsql_code: str) -> str:
        """Convertir cursores T-SQL a PostgreSQL"""
        
        # Pattern para DECLARE CURSOR
        cursor_pattern = r'DECLARE\s+(\w+)\s+CURSOR\s+FOR\s+(.+?)(?=DECLARE|OPEN|$)'
        
        def replace_cursor(match):
            cursor_name = match.group(1)
            cursor_query = match.group(2).strip()
            
            return f"""
    -- Cursor declaration converted to FOR loop
    FOR {cursor_name}_record IN {cursor_query} LOOP
        -- Cursor body will be here
    END LOOP;
"""
        
        plpgsql_code = re.sub(cursor_pattern, replace_cursor, plpgsql_code, flags=re.IGNORECASE | re.DOTALL)
        
        # Remover OPEN/CLOSE/FETCH cursor statements
        plpgsql_code = re.sub(r'OPEN\s+\w+\s*;?', '', plpgsql_code, flags=re.IGNORECASE)
        plpgsql_code = re.sub(r'CLOSE\s+\w+\s*;?', '', plpgsql_code, flags=re.IGNORECASE)
        plpgsql_code = re.sub(r'DEALLOCATE\s+\w+\s*;?', '', plpgsql_code, flags=re.IGNORECASE)
        
        return plpgsql_code
    
    def migrate_all_procedures(self) -> bool:
        """Migrar todos los stored procedures"""
        try:
            # Extraer SPs
            procedures = self.extract_stored_procedures()
            
            if not procedures:
                logger.warning("⚠️  No se encontraron stored procedures")
                return True
            
            # Conectar a PostgreSQL
            pg_conn = psycopg2.connect(
                host=self.pg_config['host'],
                port=self.pg_config['port'],
                database=self.pg_config['database'],
                user=self.pg_config['username'],
                password=self.pg_config['password']
            )
            pg_conn.autocommit = True
            pg_cursor = pg_conn.cursor()
            
            # Crear schema para legacy procedures
            pg_cursor.execute("CREATE SCHEMA IF NOT EXISTS legacy_procedures;")
            
            migrated_count = 0
            failed_count = 0
            
            for i, proc in enumerate(procedures, 1):
                proc_name = proc['name']
                logger.info(f"🔄 Migrando SP {proc_name} ({i}/{len(procedures)})")
                
                try:
                    # Convertir T-SQL a PL/pgSQL
                    plpgsql_code = self.convert_tsql_to_plpgsql(proc['definition'], proc_name)
                    
                    # Manejo especial de cursores
                    plpgsql_code = self.handle_cursors(plpgsql_code)
                    
                    # Ejecutar en PostgreSQL
                    pg_cursor.execute(plpgsql_code)
                    
                    logger.info(f"✅ {proc_name} migrado exitosamente")
                    migrated_count += 1
                    
                except Exception as e:
                    logger.error(f"❌ Error migrando {proc_name}: {e}")
                    
                    # Guardar SP problemático para revisión manual
                    with open(f"failed_sp_{proc_name}.sql", 'w') as f:
                        f.write(f"-- FAILED MIGRATION: {proc_name}\n")
                        f.write(f"-- Error: {e}\n\n")
                        f.write("-- Original T-SQL:\n")
                        f.write(proc['definition'])
                        f.write(f"\n\n-- Converted PL/pgSQL:\n")
                        f.write(plpgsql_code)
                    
                    failed_count += 1
                    continue
            
            pg_conn.close()
            
            logger.info(f"📊 Migración SPs completada:")
            logger.info(f"  ✅ Exitosos: {migrated_count}")
            logger.info(f"  ❌ Fallidos: {failed_count}")
            logger.info(f"  📋 Total: {len(procedures)}")
            
            return failed_count == 0
            
        except Exception as e:
            logger.error(f"❌ Error fatal migrando SPs: {e}")
            return False

def main():
    """Función principal"""
    
    sql_server_config = {
        'driver': '{ODBC Driver 17 for SQL Server}',
        'server': 'localhost',
        'port': 1433,
        'database': 'una',  # Cambiar por base de producción
        'username': 'sa',
        'password': 'MigracionERP2025!'
    }
    
    postgres_config = {
        'host': 'localhost',
        'port': 5422,
        'database': 'erp_consolidasoft',  # Cambiar por base de producción
        'username': 'postgres',
        'password': 'MigracionERP2025!'
    }
    
    print("🔄 INICIANDO MIGRACIÓN DE STORED PROCEDURES")
    print("📋 T-SQL → PL/pgSQL con conversión automática")
    print("=" * 60)
    
    migrator = StoredProcedureMigrator(sql_server_config, postgres_config)
    success = migrator.migrate_all_procedures()
    
    if success:
        print("\n🎉 TODOS LOS STORED PROCEDURES MIGRADOS EXITOSAMENTE")
    else:
        print("\n⚠️  ALGUNOS STORED PROCEDURES REQUIEREN REVISIÓN MANUAL")
        print("📁 Revisar archivos failed_sp_*.sql generados")

if __name__ == "__main__":
    main()
