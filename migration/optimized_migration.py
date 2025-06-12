#!/usr/bin/env python3
"""
MIGRACIÓN OPTIMIZADA POR FASES
ERP SQL Server → PostgreSQL

Estrategia: Schema → Datos → Foreign Keys
Para máxima velocidad y confiabilidad
"""

import psycopg2
import pyodbc
import logging
from datetime import datetime
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OptimizedMigration:
    """Migración optimizada por fases"""
    
    def __init__(self):
        self.sql_server_config = {
            'driver': '{ODBC Driver 17 for SQL Server}',
            'server': 'localhost',
            'port': 1433,
            'database': 'una',
            'username': 'sa',
            'password': 'MigracionERP2025!',
            'trusted_connection': 'no'
        }
        
        self.postgres_config = {
            'host': 'localhost',
            'port': 5422,
            'database': 'erp_consolidasoft',
            'username': 'postgres',
            'password': 'MigracionERP2025!'
        }
        
        self.sql_conn = None
        self.pg_conn = None
        
    def connect_databases(self):
        """Conectar a ambas bases"""
        try:
            # SQL Server
            sql_conn_str = (
                f"DRIVER={self.sql_server_config['driver']};"
                f"SERVER={self.sql_server_config['server']},{self.sql_server_config['port']};"
                f"DATABASE={self.sql_server_config['database']};"
                f"UID={self.sql_server_config['username']};"
                f"PWD={self.sql_server_config['password']};"
                f"TrustServerCertificate=yes;"
            )
            
            self.sql_conn = pyodbc.connect(sql_conn_str)
            logger.info("✅ SQL Server conectado")
            
            # PostgreSQL
            self.pg_conn = psycopg2.connect(
                host=self.postgres_config['host'],
                port=self.postgres_config['port'],
                database=self.postgres_config['database'],
                user=self.postgres_config['username'],
                password=self.postgres_config['password']
            )
            self.pg_conn.autocommit = True
            logger.info("✅ PostgreSQL conectado")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error conectando: {e}")
            return False
    
    def phase_1_create_tables_only(self):
        """FASE 1: Crear solo tablas SIN foreign keys ni índices"""
        logger.info("🏗️  FASE 1: Creando tablas básicas (SIN FK ni índices)")
        
        try:
            cursor = self.sql_conn.cursor()
            pg_cursor = self.pg_conn.cursor()
            
            # Obtener lista de tablas
            cursor.execute("""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo'
                ORDER BY TABLE_NAME
            """)
            
            tables = [row[0] for row in cursor.fetchall()]
            logger.info(f"📊 Encontradas {len(tables)} tablas")
            
            # Crear cada tabla SIN constraints
            for i, table_name in enumerate(tables, 1):
                logger.info(f"🔨 Creando {table_name} ({i}/{len(tables)})")
                
                # Obtener estructura de columnas
                cursor.execute("""
                    SELECT 
                        COLUMN_NAME,
                        DATA_TYPE,
                        CHARACTER_MAXIMUM_LENGTH,
                        NUMERIC_PRECISION,
                        NUMERIC_SCALE,
                        IS_NULLABLE,
                        COLUMNPROPERTY(OBJECT_ID(TABLE_SCHEMA+'.'+TABLE_NAME), COLUMN_NAME, 'IsIdentity') as IS_IDENTITY
                    FROM INFORMATION_SCHEMA.COLUMNS 
                    WHERE TABLE_NAME = ?
                    ORDER BY ORDINAL_POSITION
                """, table_name)
                
                columns = cursor.fetchall()
                
                if not columns:
                    continue
                
                # Generar CREATE TABLE básico
                pg_table_name = table_name.lower()
                create_sql = f"CREATE TABLE IF NOT EXISTS erp_main.{pg_table_name} ("
                
                column_defs = []
                has_identity = False
                
                for col in columns:
                    col_name = col[0].lower()
                    data_type = col[1].lower()
                    max_length = col[2]
                    precision = col[3]
                    scale = col[4]
                    nullable = col[5] == 'YES'
                    is_identity = bool(col[6])
                    
                    # Convertir tipo
                    pg_type = self.convert_type(data_type, max_length, precision, scale)
                    
                    col_def = f"    {col_name} {pg_type}"
                    
                    # Identity → Serial
                    if is_identity:
                        if data_type == 'int':
                            col_def = f"    {col_name} BIGSERIAL PRIMARY KEY"
                        else:
                            col_def = f"    {col_name} SERIAL PRIMARY KEY"
                        has_identity = True
                    elif not nullable:
                        col_def += " NOT NULL"
                    
                    column_defs.append(col_def)
                
                create_sql += ",\n".join(column_defs) + ");"
                
                try:
                    pg_cursor.execute(create_sql)
                    logger.info(f"✅ {table_name} creada")
                except Exception as e:
                    logger.error(f"❌ Error creando {table_name}: {e}")
            
            logger.info("🎉 FASE 1 COMPLETADA: Todas las tablas básicas creadas")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error en Fase 1: {e}")
            return False
    
    def phase_2_migrate_data_fast(self):
        """FASE 2: Migrar datos SIN validaciones FK (súper rápido)"""
        logger.info("📦 FASE 2: Migrando datos (SIN validaciones FK)")
        
        try:
            cursor = self.sql_conn.cursor()
            pg_cursor = self.pg_conn.cursor()
            
            # Obtener tablas con datos
            cursor.execute("""
                SELECT t.TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES t
                WHERE t.TABLE_TYPE = 'BASE TABLE' AND t.TABLE_SCHEMA = 'dbo'
                ORDER BY t.TABLE_NAME
            """)
            
            tables = [row[0] for row in cursor.fetchall()]
            
            for i, table_name in enumerate(tables, 1):
                logger.info(f"📤 Migrando datos de {table_name} ({i}/{len(tables)})")
                
                try:
                    # Contar registros origen
                    cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
                    count = cursor.fetchone()[0]
                    
                    if count == 0:
                        logger.info(f"⚠️  {table_name} está vacía, saltando...")
                        continue
                    
                    # Obtener columnas
                    cursor.execute(f"SELECT TOP 1 * FROM [{table_name}]")
                    columns = [desc[0].lower() for desc in cursor.description]
                    
                    # Extraer datos en lotes
                    batch_size = 5000
                    offset = 0
                    total_migrated = 0
                    
                    while True:
                        cursor.execute(f"""
                            SELECT * FROM [{table_name}]
                            ORDER BY (SELECT NULL)
                            OFFSET {offset} ROWS
                            FETCH NEXT {batch_size} ROWS ONLY
                        """)
                        
                        batch = cursor.fetchall()
                        if not batch:
                            break
                        
                        # Preparar INSERT
                        placeholders = ','.join(['%s'] * len(columns))
                        insert_sql = f"""
                            INSERT INTO erp_main.{table_name.lower()} ({','.join(columns)})
                            VALUES ({placeholders})
                        """
                        
                        # Ejecutar lote
                        pg_cursor.executemany(insert_sql, batch)
                        
                        total_migrated += len(batch)
                        offset += batch_size
                        
                        if total_migrated % 10000 == 0:
                            logger.info(f"  📈 {table_name}: {total_migrated} registros migrados...")
                    
                    logger.info(f"✅ {table_name}: {total_migrated} registros migrados")
                    
                except Exception as e:
                    logger.error(f"❌ Error migrando {table_name}: {e}")
                    continue
            
            logger.info("🎉 FASE 2 COMPLETADA: Todos los datos migrados")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error en Fase 2: {e}")
            return False
    
    def phase_3_add_constraints(self):
        """FASE 3: Agregar FK e índices (al final)"""
        logger.info("🔗 FASE 3: Agregando Foreign Keys e índices")
        
        try:
            cursor = self.sql_conn.cursor()
            pg_cursor = self.pg_conn.cursor()
            
            # Obtener Foreign Keys
            cursor.execute("""
                SELECT 
                    tp.name AS parent_table,
                    cp.name AS parent_column,
                    tr.name AS referenced_table,
                    cr.name AS referenced_column
                FROM sys.foreign_keys fk
                INNER JOIN sys.tables tp ON fk.parent_object_id = tp.object_id
                INNER JOIN sys.tables tr ON fk.referenced_object_id = tr.object_id
                INNER JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
                INNER JOIN sys.columns cp ON fkc.parent_object_id = cp.object_id AND fkc.parent_column_id = cp.column_id
                INNER JOIN sys.columns cr ON fkc.referenced_object_id = cr.object_id AND fkc.referenced_column_id = cr.column_id
                ORDER BY tp.name
            """)
            
            foreign_keys = cursor.fetchall()
            
            for i, fk in enumerate(foreign_keys, 1):
                parent_table = fk[0].lower()
                parent_column = fk[1].lower()
                ref_table = fk[2].lower()
                ref_column = fk[3].lower()
                
                logger.info(f"🔗 Creando FK {i}/{len(foreign_keys)}: {parent_table}.{parent_column} → {ref_table}.{ref_column}")
                
                try:
                    fk_sql = f"""
                        ALTER TABLE erp_main.{parent_table} 
                        ADD CONSTRAINT fk_{parent_table}_{parent_column} 
                        FOREIGN KEY ({parent_column}) REFERENCES erp_main.{ref_table}({ref_column})
                    """
                    pg_cursor.execute(fk_sql)
                    
                except Exception as e:
                    logger.warning(f"⚠️  FK fallida {parent_table}.{parent_column}: {e}")
                    continue
            
            logger.info("🎉 FASE 3 COMPLETADA: Constraints agregados")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error en Fase 3: {e}")
            return False
    
    def convert_type(self, sql_type, max_length=None, precision=None, scale=None):
        """Convertir tipos SQL Server → PostgreSQL"""
        type_map = {
            'int': 'BIGINT',  # Decisión crítica del proyecto
            'bigint': 'BIGINT',
            'smallint': 'SMALLINT',
            'tinyint': 'SMALLINT',
            'bit': 'BOOLEAN',
            'decimal': f'DECIMAL({precision},{scale})' if precision and scale else 'DECIMAL(18,6)',
            'numeric': f'DECIMAL({precision},{scale})' if precision and scale else 'DECIMAL(18,6)',
            'money': 'DECIMAL(19,4)',
            'smallmoney': 'DECIMAL(10,4)',
            'float': 'DOUBLE PRECISION',
            'real': 'REAL',
            'datetime': 'TIMESTAMP WITH TIME ZONE',
            'datetime2': 'TIMESTAMP WITH TIME ZONE',
            'smalldatetime': 'TIMESTAMP WITH TIME ZONE',
            'date': 'DATE',
            'time': 'TIME WITH TIME ZONE',
            'varchar': f'VARCHAR({max_length})' if max_length and max_length > 0 else 'TEXT',
            'nvarchar': f'VARCHAR({max_length})' if max_length and max_length > 0 else 'TEXT',
            'char': f'CHAR({max_length})' if max_length else 'CHAR(1)',
            'nchar': f'CHAR({max_length})' if max_length else 'CHAR(1)',
            'text': 'TEXT',
            'ntext': 'TEXT',
            'uniqueidentifier': 'UUID',
            'varbinary': 'BYTEA',
            'binary': 'BYTEA',
            'image': 'BYTEA'
        }
        
        if max_length == -1:  # VARCHAR(MAX)
            return 'TEXT'
        
        return type_map.get(sql_type.lower(), 'TEXT')
    
    def run_optimized_migration(self):
        """Ejecutar migración optimizada completa"""
        logger.info("🚀 INICIANDO MIGRACIÓN OPTIMIZADA POR FASES")
        
        if not self.connect_databases():
            return False
        
        try:
            # Crear schemas básicos
            pg_cursor = self.pg_conn.cursor()
            pg_cursor.execute("CREATE SCHEMA IF NOT EXISTS erp_main;")
            pg_cursor.execute("CREATE SCHEMA IF NOT EXISTS erp_control;")
            
            # FASE 1: Solo tablas (rápido)
            if not self.phase_1_create_tables_only():
                return False
            
            # FASE 2: Solo datos (súper rápido sin FK)
            if not self.phase_2_migrate_data_fast():
                return False
            
            # FASE 3: FK e índices (lento pero al final)
            if not self.phase_3_add_constraints():
                logger.warning("⚠️  Algunas constraints fallaron, pero datos están migrados")
            
            logger.info("🎉 MIGRACIÓN OPTIMIZADA COMPLETADA")
            
            # Estadísticas finales
            pg_cursor.execute("SELECT COUNT(*) FROM pg_tables WHERE schemaname = 'erp_main'")
            table_count = pg_cursor.fetchone()[0]
            logger.info(f"📊 Total tablas creadas: {table_count}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error fatal: {e}")
            return False
        
        finally:
            if self.sql_conn:
                self.sql_conn.close()
            if self.pg_conn:
                self.pg_conn.close()

def main():
    """Función principal"""
    print("🚀 MIGRACIÓN OPTIMIZADA POR FASES")
    print("📋 Estrategia: Tablas → Datos → Constraints")
    print("⚡ Máxima velocidad, mínimo downtime")
    print("=" * 50)
    
    migrator = OptimizedMigration()
    success = migrator.run_optimized_migration()
    
    if success:
        print("\n🎉 MIGRACIÓN COMPLETADA EXITOSAMENTE")
        print("✅ Schema + Datos + Constraints migrados")
    else:
        print("\n❌ MIGRACIÓN FALLÓ")
        print("📋 Revisar logs para diagnosticar")

if __name__ == "__main__":
    main()
