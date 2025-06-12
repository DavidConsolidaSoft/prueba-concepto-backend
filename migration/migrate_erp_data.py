#!/usr/bin/env python3
"""
MIGRADOR DE DATOS ERP: SQL Server → PostgreSQL
Proceso automatizado para migración de datos del piloto (5 tablas)
Basado en schema ya creado en PostgreSQL
"""

import psycopg2
import pyodbc
import logging
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any
import sys
import os

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'migration_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class ERPMigrator:
    """Migrador principal para ERP SQL Server → PostgreSQL"""
    
    def __init__(self):
        # Configuración de conexiones
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
        
        # Orden de migración (respetando dependencias FK)
        self.migration_order = [
            'agrupaclientes',  # Sin dependencias - PRIMERO
            'clientes',        # Depende de agrupaclientes
            'clientedatos',    # Depende de clientes
            'saldocliente',    # Depende de clientes
            'RangoCliente'     # Depende de clientes (nombre exacto de SQL Server)
        ]
        
        # Mapeo de nombres de tabla SQL Server → PostgreSQL
        self.table_mapping = {
            'agrupaclientes': 'agrupaclientes',
            'clientes': 'clientes', 
            'clientedatos': 'clientedatos',
            'saldocliente': 'saldocliente',
            'RangoCliente': 'rangocliente'  # Normalizar nombre
        }
        
        # Conexiones
        self.sql_conn = None
        self.pg_conn = None
        
    def connect_databases(self) -> bool:
        """Establecer conexiones a ambas bases de datos"""
        try:
            # Conexión SQL Server
            sql_conn_str = (
                f"DRIVER={self.sql_server_config['driver']};"
                f"SERVER={self.sql_server_config['server']},{self.sql_server_config['port']};"
                f"DATABASE={self.sql_server_config['database']};"
                f"UID={self.sql_server_config['username']};"
                f"PWD={self.sql_server_config['password']};"
                f"TrustServerCertificate=yes;"
            )
            
            self.sql_conn = pyodbc.connect(sql_conn_str)
            logger.info("✅ Conexión SQL Server establecida")
            
            # Conexión PostgreSQL
            self.pg_conn = psycopg2.connect(
                host=self.postgres_config['host'],
                port=self.postgres_config['port'],
                database=self.postgres_config['database'],
                user=self.postgres_config['username'],
                password=self.postgres_config['password']
            )
            logger.info("✅ Conexión PostgreSQL establecida")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error conectando bases de datos: {e}")
            return False
    
    def get_table_structure(self, table_name: str) -> Dict[str, Any]:
        """Obtener estructura de tabla desde SQL Server"""
        try:
            cursor = self.sql_conn.cursor()
            
            # Query para obtener estructura completa
            structure_query = """
            SELECT 
                COLUMN_NAME,
                DATA_TYPE,
                CHARACTER_MAXIMUM_LENGTH,
                NUMERIC_PRECISION,
                NUMERIC_SCALE,
                IS_NULLABLE,
                COLUMN_DEFAULT,
                COLUMNPROPERTY(OBJECT_ID(TABLE_SCHEMA+'.'+TABLE_NAME), COLUMN_NAME, 'IsIdentity') as IS_IDENTITY
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = ?
            ORDER BY ORDINAL_POSITION
            """
            
            cursor.execute(structure_query, table_name)
            columns = cursor.fetchall()
            
            # Query para obtener conteo de registros
            count_query = f"SELECT COUNT(*) FROM {table_name}"
            cursor.execute(count_query)
            record_count = cursor.fetchone()[0]
            
            structure = {
                'table_name': table_name,
                'record_count': record_count,
                'columns': []
            }
            
            for col in columns:
                column_info = {
                    'name': col[0],
                    'data_type': col[1],
                    'max_length': col[2],
                    'precision': col[3],
                    'scale': col[4],
                    'nullable': col[5] == 'YES',
                    'default': col[6],
                    'is_identity': bool(col[7])
                }
                structure['columns'].append(column_info)
            
            logger.info(f"📊 Tabla {table_name}: {record_count} registros, {len(columns)} columnas")
            return structure
            
        except Exception as e:
            logger.error(f"❌ Error obteniendo estructura de {table_name}: {e}")
            raise
    
    def register_migration_start(self, table_name: str, record_count: int) -> int:
        """Registrar inicio de migración en tabla de control"""
        try:
            cursor = self.pg_conn.cursor()
            
            insert_query = """
            INSERT INTO erp_control.migration_status 
            (table_name, migration_phase, records_migrated, status)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """
            
            cursor.execute(insert_query, (table_name, 'DATA_MIGRATION', 0, 'RUNNING'))
            migration_id = cursor.fetchone()[0]
            self.pg_conn.commit()
            
            logger.info(f"🚀 Migración iniciada para {table_name} (ID: {migration_id})")
            return migration_id
            
        except Exception as e:
            logger.error(f"❌ Error registrando inicio de migración: {e}")
            raise
    
    def migrate_table_data(self, source_table: str) -> bool:
        """Migrar datos de una tabla específica"""
        target_table = self.table_mapping[source_table]
        
        try:
            # Obtener estructura
            structure = self.get_table_structure(source_table)
            record_count = structure['record_count']
            
            if record_count == 0:
                logger.info(f"⚠️  Tabla {source_table} está vacía, saltando...")
                return True
            
            # Registrar inicio
            migration_id = self.register_migration_start(target_table, record_count)
            
            # Preparar query de extracción
            column_names = [col['name'] for col in structure['columns']]
            select_query = f"SELECT {', '.join(column_names)} FROM {source_table}"
            
            # Preparar query de inserción PostgreSQL
            pg_columns = []
            placeholders = []
            
            for col in structure['columns']:
                col_name = col['name']
                
                # Mapear nombres de columnas si es necesario
                if source_table == 'RangoCliente' and col_name == 'RangoCliente':
                    pg_columns.append('rangocliente')  # PK normalizada
                else:
                    pg_columns.append(col_name.lower())  # PostgreSQL lowercase
                
                placeholders.append('%s')
            
            insert_query = f"""
                INSERT INTO erp_main.{target_table} ({', '.join(pg_columns)})
                VALUES ({', '.join(placeholders)})
            """
            
            # Ejecutar migración en lotes
            batch_size = 1000
            total_migrated = 0
            
            sql_cursor = self.sql_conn.cursor()
            sql_cursor.execute(select_query)
            
            pg_cursor = self.pg_conn.cursor()
            
            while True:
                rows = sql_cursor.fetchmany(batch_size)
                if not rows:
                    break
                
                # Procesar lote
                processed_rows = []
                for row in rows:
                    # Convertir tipos de datos problemáticos
                    processed_row = []
                    for i, (value, col_info) in enumerate(zip(row, structure['columns'])):
                        
                        # Manejar valores NULL
                        if value is None:
                            processed_row.append(None)
                            continue
                        
                        # Conversiones específicas por tipo
                        data_type = col_info['data_type'].lower()
                        
                        if data_type == 'bit':
                            processed_row.append(bool(value))
                        elif data_type in ['datetime', 'datetime2', 'smalldatetime']:
                            processed_row.append(value)  # psycopg2 maneja automáticamente
                        elif data_type in ['decimal', 'numeric', 'money']:
                            processed_row.append(float(value) if value else 0)
                        else:
                            processed_row.append(value)
                    
                    processed_rows.append(tuple(processed_row))
                
                # Insertar lote en PostgreSQL
                pg_cursor.executemany(insert_query, processed_rows)
                total_migrated += len(processed_rows)
                
                # Actualizar progreso
                update_query = """
                UPDATE erp_control.migration_status 
                SET records_migrated = %s 
                WHERE id = %s
                """
                pg_cursor.execute(update_query, (total_migrated, migration_id))
                self.pg_conn.commit()
                
                logger.info(f"📈 {target_table}: {total_migrated}/{record_count} registros migrados")
            
            # Marcar como completado
            complete_query = """
            UPDATE erp_control.migration_status 
            SET status = %s, end_time = NOW()
            WHERE id = %s
            """
            pg_cursor.execute(complete_query, ('COMPLETED', migration_id))
            self.pg_conn.commit()
            
            logger.info(f"✅ Tabla {target_table} migrada exitosamente: {total_migrated} registros")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error migrando {source_table}: {e}")
            
            # Marcar como fallido
            try:
                cursor = self.pg_conn.cursor()
                fail_query = """
                UPDATE erp_control.migration_status 
                SET status = %s, error_message = %s, end_time = NOW()
                WHERE id = %s
                """
                cursor.execute(fail_query, ('FAILED', str(e), migration_id))
                self.pg_conn.commit()
            except:
                pass
            
            return False
    
    def validate_migration(self) -> bool:
        """Validar que la migración sea exitosa"""
        logger.info("🔍 Iniciando validación de migración...")
        
        validation_results = {}
        all_valid = True
        
        try:
            for source_table in self.migration_order:
                target_table = self.table_mapping[source_table]
                
                # Conteo en SQL Server
                sql_cursor = self.sql_conn.cursor()
                sql_cursor.execute(f"SELECT COUNT(*) FROM {source_table}")
                source_count = sql_cursor.fetchone()[0]
                
                # Conteo en PostgreSQL
                pg_cursor = self.pg_conn.cursor()
                pg_cursor.execute(f"SELECT COUNT(*) FROM erp_main.{target_table}")
                target_count = pg_cursor.fetchone()[0]
                
                # Validar integridad
                is_valid = source_count == target_count
                validation_results[source_table] = {
                    'source_count': source_count,
                    'target_count': target_count,
                    'valid': is_valid
                }
                
                if is_valid:
                    logger.info(f"✅ {source_table}: {source_count} = {target_count} registros")
                else:
                    logger.error(f"❌ {source_table}: {source_count} ≠ {target_count} registros")
                    all_valid = False
            
            # Guardar resultados de validación
            pg_cursor = self.pg_conn.cursor()
            validation_query = """
            UPDATE erp_control.session_continuity 
            SET validation_results = %s
            WHERE migration_phase = 'SCHEMA_CREATION'
            ORDER BY created_at DESC
            LIMIT 1
            """
            pg_cursor.execute(validation_query, (json.dumps(validation_results),))
            self.pg_conn.commit()
            
            if all_valid:
                logger.info("🎉 ¡MIGRACIÓN VALIDADA EXITOSAMENTE!")
            else:
                logger.error("💥 MIGRACIÓN TIENE ERRORES DE INTEGRIDAD")
            
            return all_valid
            
        except Exception as e:
            logger.error(f"❌ Error en validación: {e}")
            return False
    
    def run_complete_migration(self) -> bool:
        """Ejecutar migración completa del piloto"""
        logger.info("🚀 INICIANDO MIGRACIÓN COMPLETA ERP PILOTO")
        logger.info(f"📋 Tablas a migrar: {', '.join(self.migration_order)}")
        
        try:
            # Conectar bases de datos
            if not self.connect_databases():
                return False
            
            # Migrar cada tabla en orden
            for table_name in self.migration_order:
                logger.info(f"📤 Migrando tabla: {table_name}")
                
                if not self.migrate_table_data(table_name):
                    logger.error(f"💥 Migración falló en tabla: {table_name}")
                    return False
            
            # Validar migración completa
            if not self.validate_migration():
                logger.error("💥 Validación de migración falló")
                return False
            
            logger.info("🎉 ¡MIGRACIÓN PILOTO COMPLETADA EXITOSAMENTE!")
            return True
            
        except Exception as e:
            logger.error(f"💥 Error fatal en migración: {e}")
            return False
        
        finally:
            # Cerrar conexiones
            if self.sql_conn:
                self.sql_conn.close()
            if self.pg_conn:
                self.pg_conn.close()
            logger.info("🔌 Conexiones cerradas")

def main():
    """Función principal"""
    print("=" * 60)
    print("🔄 MIGRADOR ERP: SQL Server → PostgreSQL")
    print("📊 Módulo Piloto: 5 tablas maestras")
    print("=" * 60)
    
    migrator = ERPMigrator()
    success = migrator.run_complete_migration()
    
    if success:
        print("\n🎉 MIGRACIÓN COMPLETADA EXITOSAMENTE")
        print("✅ Todos los datos han sido migrados y validados")
        print("🔍 Revisar logs para detalles completos")
        sys.exit(0)
    else:
        print("\n💥 MIGRACIÓN FALLÓ")
        print("❌ Revisar logs para diagnosticar errores")
        sys.exit(1)

if __name__ == "__main__":
    main()
