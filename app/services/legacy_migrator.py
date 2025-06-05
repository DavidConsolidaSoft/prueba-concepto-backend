"""
Sistema de migración automática desde el schema legacy (559 tablas) 
al nuevo schema multitenant optimizado
"""

import logging
import asyncio
from typing import Dict, List, Optional, Any, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import text, create_engine
from datetime import datetime
import uuid
import json

from app.models.multitenant import (
    Tenant, User, Customer, Product, ProductCategory, 
    Warehouse, Invoice, InvoiceItem, Supplier, PurchaseOrder,
    MigrationMapping, Base
)
from app.core.config import settings

logger = logging.getLogger(__name__)

class LegacyMigrator:
    """
    Migrador automático desde esquema legacy a multitenant
    """
    
    def __init__(self, legacy_connection_string: str, new_connection_string: str):
        self.legacy_engine = create_engine(legacy_connection_string)
        self.new_engine = create_engine(new_connection_string)
        
        # Mapeo de tablas legacy -> nuevas
        self.table_mappings = {
            # Core business
            'clientes': 'customers',
            'producto': 'products', 
            'categori': 'product_categories',
            'bodega': 'warehouses',
            'factura': 'invoices',
            'dfactura': 'invoice_items',
            'proveedor': 'suppliers',
            'compra': 'purchase_orders',
            
            # Auth/Users (múltiples tablas legacy)
            'usuario': 'users',
            'accesos': 'user_roles',
            'caccesos': 'roles',
            
            # Inventory
            'almacen': 'inventory_movements',
            'cambodega': 'inventory_movements',
            
            # Legacy mapping
            'empresa': 'tenants'  # Cada empresa -> tenant
        }

    def create_new_schema(self):
        """Crear el nuevo schema en PostgreSQL"""
        logger.info("Creando nuevo schema multitenant...")
        
        # Crear todas las tablas
        Base.metadata.create_all(self.new_engine)
        
        # Crear Row Level Security policies
        self._setup_rls_policies()
        
        logger.info("✅ Schema multitenant creado exitosamente")

    def _setup_rls_policies(self):
        """Configurar Row Level Security automático"""
        with self.new_engine.connect() as conn:
            rls_tables = [
                'users', 'customers', 'products', 'product_categories',
                'warehouses', 'inventory_movements', 'invoices', 
                'suppliers', 'purchase_orders', 'ai_conversations'
            ]
            
            for table in rls_tables:
                try:
                    # Habilitar RLS
                    conn.execute(text(f"ALTER TABLE {table} ENABLE ROW LEVEL SECURITY"))
                    
                    # Crear policy de isolation por tenant
                    policy_sql = f"""
                    CREATE POLICY {table}_tenant_isolation ON {table}
                    FOR ALL TO authenticated 
                    USING (tenant_id = current_setting('app.current_tenant')::UUID)
                    """
                    conn.execute(text(policy_sql))
                    logger.info(f"✅ RLS configurado para {table}")
                    
                except Exception as e:
                    logger.warning(f"Error configurando RLS para {table}: {e}")
            
            conn.commit()

    async def analyze_legacy_data(self) -> Dict[str, Any]:
        """Analizar datos legacy para planificar migración"""
        logger.info("Analizando datos legacy...")
        
        analysis = {
            'empresas': [],
            'tables_summary': {},
            'data_quality_issues': [],
            'estimated_migration_time': 0
        }
        
        with self.legacy_engine.connect() as conn:
            # Encontrar todas las empresas (tenants)
            try:
                empresas_result = conn.execute(text("""
                    SELECT DISTINCT empresa, COUNT(*) as records
                    FROM clientes 
                    WHERE empresa IS NOT NULL
                    GROUP BY empresa 
                    ORDER BY empresa
                """))
                
                for row in empresas_result:
                    empresa_id = row[0]
                    client_count = row[1]
                    
                    # Analizar datos por empresa
                    empresa_analysis = await self._analyze_empresa_data(conn, empresa_id)
                    empresa_analysis['client_count'] = client_count
                    analysis['empresas'].append(empresa_analysis)
                
            except Exception as e:
                logger.error(f"Error analizando empresas: {e}")
            
            # Resumen general por tabla
            for legacy_table, new_table in self.table_mappings.items():
                try:
                    count_result = conn.execute(text(f"SELECT COUNT(*) FROM {legacy_table}"))
                    count = count_result.scalar()
                    analysis['tables_summary'][legacy_table] = {
                        'legacy_table': legacy_table,
                        'new_table': new_table,
                        'record_count': count
                    }
                except Exception as e:
                    logger.warning(f"No se pudo analizar tabla {legacy_table}: {e}")
        
        # Calcular tiempo estimado (records / 1000 per minute)
        total_records = sum([t['record_count'] for t in analysis['tables_summary'].values()])
        analysis['estimated_migration_time'] = total_records / 1000  # minutos
        
        logger.info(f"Análisis completado: {len(analysis['empresas'])} empresas, {total_records} registros")
        return analysis

    async def _analyze_empresa_data(self, conn, empresa_id: int) -> Dict:
        """Analizar datos específicos de una empresa"""
        empresa_data = {
            'empresa_id': empresa_id,
            'tables': {},
            'data_quality_score': 100
        }
        
        # Contar registros por tabla para esta empresa
        tables_to_check = ['clientes', 'producto', 'factura', 'usuario', 'bodega']
        
        for table in tables_to_check:
            try:
                result = conn.execute(text(f"""
                    SELECT COUNT(*) FROM {table} 
                    WHERE empresa = :empresa_id
                """), {'empresa_id': empresa_id})
                
                count = result.scalar()
                empresa_data['tables'][table] = count
                
            except Exception as e:
                logger.warning(f"Error contando {table} para empresa {empresa_id}: {e}")
                empresa_data['data_quality_score'] -= 10
        
        return empresa_data

    async def migrate_all_empresas(self) -> Dict[str, Any]:
        """Migrar todas las empresas de legacy a multitenant"""
        logger.info("🚀 Iniciando migración completa...")
        
        migration_results = {
            'migrated_tenants': [],
            'failed_tenants': [],
            'total_records_migrated': 0,
            'start_time': datetime.now(),
            'errors': []
        }
        
        # Primero analizar datos
        analysis = await self.analyze_legacy_data()
        
        # Migrar empresa por empresa
        for empresa_info in analysis['empresas']:
            empresa_id = empresa_info['empresa_id']
            
            try:
                logger.info(f"Migrando empresa {empresa_id}...")
                
                # Crear tenant
                tenant = await self._create_tenant_from_empresa(empresa_id)
                
                # Migrar datos por módulos
                records_migrated = await self._migrate_empresa_data(empresa_id, tenant.id)
                
                migration_results['migrated_tenants'].append({
                    'empresa_id': empresa_id,
                    'tenant_id': str(tenant.id),
                    'tenant_slug': tenant.slug,
                    'records_migrated': records_migrated
                })
                
                migration_results['total_records_migrated'] += records_migrated
                
                logger.info(f"✅ Empresa {empresa_id} migrada exitosamente como {tenant.slug}")
                
            except Exception as e:
                logger.error(f"❌ Error migrando empresa {empresa_id}: {e}")
                migration_results['failed_tenants'].append({
                    'empresa_id': empresa_id,
                    'error': str(e)
                })
                migration_results['errors'].append(str(e))
        
        migration_results['end_time'] = datetime.now()
        migration_results['duration'] = (migration_results['end_time'] - migration_results['start_time']).total_seconds()
        
        logger.info(f"🎉 Migración completada: {len(migration_results['migrated_tenants'])} tenants migrados")
        return migration_results

    async def _create_tenant_from_empresa(self, empresa_id: int) -> Tenant:
        """Crear un tenant desde datos de empresa legacy"""
        
        with Session(self.new_engine) as session:
            # Verificar si ya existe
            existing_tenant = session.query(Tenant).filter(
                Tenant.legacy_empresa_id == empresa_id
            ).first()
            
            if existing_tenant:
                logger.info(f"Tenant para empresa {empresa_id} ya existe: {existing_tenant.slug}")
                return existing_tenant
            
            # Obtener datos de la empresa desde legacy
            empresa_data = await self._get_empresa_info(empresa_id)
            
            # Crear nuevo tenant
            tenant = Tenant(
                slug=f"empresa_{empresa_id}",
                company_name=empresa_data.get('nombre', f"Empresa {empresa_id}"),
                nit=empresa_data.get('nit'),
                email=empresa_data.get('email'),
                phone=empresa_data.get('telefono'),
                address=empresa_data.get('direccion'),
                plan_type='basic',
                features={
                    'inventory': True,
                    'billing': True,
                    'hr': True,
                    'ai_chat': True
                },
                legacy_empresa_id=empresa_id
            )
            
            session.add(tenant)
            session.commit()
            session.refresh(tenant)
            
            return tenant

    async def _get_empresa_info(self, empresa_id: int) -> Dict:
        """Obtener información de empresa desde legacy"""
        
        empresa_info = {
            'empresa_id': empresa_id,
            'nombre': f'Empresa {empresa_id}',
            'nit': None,
            'email': None,
            'telefono': None,
            'direccion': None
        }
        
        with self.legacy_engine.connect() as conn:
            try:
                # Intentar obtener datos de empresa desde clientes representativos
                result = conn.execute(text("""
                    SELECT TOP 1 
                        razonsoc as nombre,
                        nit,
                        email,
                        telefono1 as telefono,
                        direccion
                    FROM clientes 
                    WHERE empresa = :empresa_id 
                    AND razonsoc IS NOT NULL
                    ORDER BY clientes
                """), {'empresa_id': empresa_id})
                
                row = result.fetchone()
                if row:
                    empresa_info.update({
                        'nombre': row[0] or f'Empresa {empresa_id}',
                        'nit': row[1],
                        'email': row[2], 
                        'telefono': row[3],
                        'direccion': row[4]
                    })
                    
            except Exception as e:
                logger.warning(f"No se pudieron obtener datos de empresa {empresa_id}: {e}")
        
        return empresa_info

    async def _migrate_empresa_data(self, empresa_id: int, tenant_id: uuid.UUID) -> int:
        """Migrar todos los datos de una empresa específica"""
        
        total_records = 0
        
        with Session(self.new_engine) as session:
            # Set tenant context for RLS
            session.execute(text(f"SET app.current_tenant = '{tenant_id}'"))
            
            # Migrar en orden de dependencias
            total_records += await self._migrate_categories(empresa_id, tenant_id, session)
            total_records += await self._migrate_warehouses(empresa_id, tenant_id, session)
            total_records += await self._migrate_customers(empresa_id, tenant_id, session)
            total_records += await self._migrate_suppliers(empresa_id, tenant_id, session)
            total_records += await self._migrate_products(empresa_id, tenant_id, session)
            total_records += await self._migrate_users(empresa_id, tenant_id, session)
            total_records += await self._migrate_invoices(empresa_id, tenant_id, session)
            
            session.commit()
        
        return total_records

    async def _migrate_customers(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar clientes de legacy a nuevo schema"""
        
        with self.legacy_engine.connect() as conn:
            customers_query = text("""
                SELECT 
                    clientes, razonsoc, nagencia, nit, email, telefono1, telefono2,
                    direccion, tipcli, condpago, limitecredito, descuento,
                    activo, usuario, horatiempo
                FROM clientes 
                WHERE empresa = :empresa_id
                ORDER BY clientes
            """)
            
            results = conn.execute(customers_query, {'empresa_id': empresa_id})
            migrated_count = 0
            
            for row in results:
                try:
                    # Crear customer
                    customer = Customer(
                        tenant_id=tenant_id,
                        customer_code=row[0],  # clientes
                        legal_name=row[1] or f'Cliente {row[0]}',  # razonsoc
                        commercial_name=row[2],  # nagencia
                        tax_id=row[3],  # nit
                        email=row[4],  # email
                        phone=row[5],  # telefono1
                        mobile=row[6],  # telefono2
                        address_line1=row[7],  # direccion
                        customer_type='regular',
                        payment_terms=row[9] or 30,  # condpago
                        credit_limit=float(row[10] or 0),  # limitecredito
                        discount_percentage=float(row[11] or 0),  # descuento
                        status='active' if row[12] else 'inactive',  # activo
                        legacy_cliente_id=row[0]
                    )
                    
                    session.add(customer)
                    migrated_count += 1
                    
                    # Crear mapping
                    mapping = MigrationMapping(
                        tenant_id=tenant_id,
                        legacy_table='clientes',
                        legacy_id=str(row[0]),
                        new_table='customers',
                        new_id=customer.id
                    )
                    session.add(mapping)
                    
                except Exception as e:
                    logger.error(f"Error migrando cliente {row[0]}: {e}")
                    continue
            
            logger.info(f"Migrados {migrated_count} clientes para empresa {empresa_id}")
            return migrated_count

    async def _migrate_products(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar productos de legacy a nuevo schema"""
        
        with self.legacy_engine.connect() as conn:
            products_query = text("""
                SELECT 
                    producto, nproducto, categori, codigo, precio1, precio2, 
                    costo, existencia, minimo, maximo, activo, servicio
                FROM producto 
                WHERE empresa = :empresa_id
                ORDER BY producto
            """)
            
            results = conn.execute(products_query, {'empresa_id': empresa_id})
            migrated_count = 0
            
            for row in results:
                try:
                    # Buscar categoría migrada
                    category_mapping = session.query(MigrationMapping).filter(
                        MigrationMapping.tenant_id == tenant_id,
                        MigrationMapping.legacy_table == 'categori',
                        MigrationMapping.legacy_id == str(row[2])
                    ).first()
                    
                    category_id = category_mapping.new_id if category_mapping else None
                    
                    product = Product(
                        tenant_id=tenant_id,
                        category_id=category_id,
                        sku=row[3] or f'SKU-{row[0]}',  # codigo
                        name=row[1] or f'Producto {row[0]}',  # nproducto
                        selling_price=float(row[4] or 0),  # precio1
                        cost_price=float(row[6] or 0),  # costo
                        current_stock=float(row[7] or 0),  # existencia
                        min_stock=float(row[8] or 0),  # minimo
                        max_stock=float(row[9] or 0),  # maximo
                        is_active=bool(row[10]),  # activo
                        is_service=bool(row[11]),  # servicio
                        legacy_producto_id=row[0]
                    )
                    
                    session.add(product)
                    migrated_count += 1
                    
                    # Crear mapping
                    mapping = MigrationMapping(
                        tenant_id=tenant_id,
                        legacy_table='producto',
                        legacy_id=str(row[0]),
                        new_table='products',
                        new_id=product.id
                    )
                    session.add(mapping)
                    
                except Exception as e:
                    logger.error(f"Error migrando producto {row[0]}: {e}")
                    continue
            
            logger.info(f"Migrados {migrated_count} productos para empresa {empresa_id}")
            return migrated_count

    async def _migrate_categories(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar categorías de productos"""
        
        with self.legacy_engine.connect() as conn:
            categories_query = text("""
                SELECT categori, ncategori, activo
                FROM categori 
                WHERE empresa = :empresa_id
                ORDER BY categori
            """)
            
            results = conn.execute(categories_query, {'empresa_id': empresa_id})
            migrated_count = 0
            
            for row in results:
                try:
                    category = ProductCategory(
                        tenant_id=tenant_id,
                        name=row[1] or f'Categoría {row[0]}',
                        is_active=bool(row[2]),
                        legacy_categoria_id=row[0]
                    )
                    
                    session.add(category)
                    migrated_count += 1
                    
                    # Crear mapping
                    mapping = MigrationMapping(
                        tenant_id=tenant_id,
                        legacy_table='categori',
                        legacy_id=str(row[0]),
                        new_table='product_categories',
                        new_id=category.id
                    )
                    session.add(mapping)
                    
                except Exception as e:
                    logger.error(f"Error migrando categoría {row[0]}: {e}")
                    continue
            
            logger.info(f"Migradas {migrated_count} categorías para empresa {empresa_id}")
            return migrated_count

    async def _migrate_warehouses(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar bodegas"""
        
        with self.legacy_engine.connect() as conn:
            warehouses_query = text("""
                SELECT bodega, nbodega, activo, preferido
                FROM bodega 
                WHERE empresa = :empresa_id
                ORDER BY bodega
            """)
            
            results = conn.execute(warehouses_query, {'empresa_id': empresa_id})
            migrated_count = 0
            
            for row in results:
                try:
                    warehouse = Warehouse(
                        tenant_id=tenant_id,
                        name=row[1] or f'Bodega {row[0]}',
                        code=f'BOD-{row[0]}',
                        is_active=bool(row[2]),
                        is_main=bool(row[3]),
                        legacy_bodega_id=row[0]
                    )
                    
                    session.add(warehouse)
                    migrated_count += 1
                    
                    # Crear mapping
                    mapping = MigrationMapping(
                        tenant_id=tenant_id,
                        legacy_table='bodega',
                        legacy_id=str(row[0]),
                        new_table='warehouses',
                        new_id=warehouse.id
                    )
                    session.add(mapping)
                    
                except Exception as e:
                    logger.error(f"Error migrando bodega {row[0]}: {e}")
                    continue
            
            logger.info(f"Migradas {migrated_count} bodegas para empresa {empresa_id}")
            return migrated_count

    async def _migrate_suppliers(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar proveedores"""
        
        with self.legacy_engine.connect() as conn:
            suppliers_query = text("""
                SELECT proveedor, nproveedor, nit, telefono, direccion, activo
                FROM proveedor 
                WHERE empresa = :empresa_id
                ORDER BY proveedor
            """)
            
            results = conn.execute(suppliers_query, {'empresa_id': empresa_id})
            migrated_count = 0
            
            for row in results:
                try:
                    supplier = Supplier(
                        tenant_id=tenant_id,
                        supplier_code=str(row[0]),
                        legal_name=row[1] or f'Proveedor {row[0]}',
                        tax_id=row[2],
                        phone=row[3],
                        address=row[4],
                        status='active' if row[5] else 'inactive',
                        legacy_proveedor_id=str(row[0])
                    )
                    
                    session.add(supplier)
                    migrated_count += 1
                    
                    # Crear mapping
                    mapping = MigrationMapping(
                        tenant_id=tenant_id,
                        legacy_table='proveedor',
                        legacy_id=str(row[0]),
                        new_table='suppliers',
                        new_id=supplier.id
                    )
                    session.add(mapping)
                    
                except Exception as e:
                    logger.error(f"Error migrando proveedor {row[0]}: {e}")
                    continue
            
            logger.info(f"Migrados {migrated_count} proveedores para empresa {empresa_id}")
            return migrated_count

    async def _migrate_users(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar usuarios (simplificado)"""
        
        # Crear usuario admin por defecto
        admin_user = User(
            tenant_id=tenant_id,
            email=f'admin@empresa{empresa_id}.com',
            password_hash='$2b$12$placeholder_hash',  # Se debe cambiar
            username=f'admin_{empresa_id}',
            first_name='Administrador',
            last_name=f'Empresa {empresa_id}',
            is_active=True,
            email_verified=True,
            legacy_usuario_id=1
        )
        
        session.add(admin_user)
        
        logger.info(f"Creado usuario admin para empresa {empresa_id}")
        return 1

    async def _migrate_invoices(self, empresa_id: int, tenant_id: uuid.UUID, session: Session) -> int:
        """Migrar facturas (simplificado por complejidad)"""
        
        # Por ahora crear estructura básica
        # La migración completa de facturas requeriría mapear todas las relaciones
        
        logger.info(f"Migración de facturas pendiente para empresa {empresa_id}")
        return 0

    async def validate_migration(self, tenant_id: uuid.UUID) -> Dict[str, Any]:
        """Validar integridad de la migración"""
        
        validation_results = {
            'tenant_id': str(tenant_id),
            'validation_passed': True,
            'tables_validated': {},
            'errors': []
        }
        
        with Session(self.new_engine) as session:
            # Set tenant context
            session.execute(text(f"SET app.current_tenant = '{tenant_id}'"))
            
            # Validar cada tabla
            tables_to_validate = [
                (Customer, 'customers'),
                (Product, 'products'),
                (ProductCategory, 'product_categories'),
                (Warehouse, 'warehouses'),
                (Supplier, 'suppliers')
            ]
            
            for model_class, table_name in tables_to_validate:
                try:
                    count = session.query(model_class).filter(
                        model_class.tenant_id == tenant_id
                    ).count()
                    
                    validation_results['tables_validated'][table_name] = {
                        'record_count': count,
                        'status': 'OK'
                    }
                    
                except Exception as e:
                    validation_results['validation_passed'] = False
                    validation_results['errors'].append(f"Error validando {table_name}: {e}")
                    validation_results['tables_validated'][table_name] = {
                        'record_count': 0,
                        'status': 'ERROR',
                        'error': str(e)
                    }
        
        logger.info(f"Validación completada para tenant {tenant_id}: {'✅' if validation_results['validation_passed'] else '❌'}")
        return validation_results

# ===== CLI PARA MIGRACIÓN =====

async def main():
    """Script principal de migración"""
    
    # Configuración de conexiones
    legacy_conn = "mssql+pyodbc://user:pass@server/database?driver=ODBC+Driver+17+for+SQL+Server"
    new_conn = "postgresql://user:pass@localhost/new_database"
    
    migrator = LegacyMigrator(legacy_conn, new_conn)
    
    print("🔧 Creando nuevo schema...")
    migrator.create_new_schema()
    
    print("📊 Analizando datos legacy...")
    analysis = await migrator.analyze_legacy_data()
    print(f"Encontradas {len(analysis['empresas'])} empresas para migrar")
    
    print("🚀 Iniciando migración...")
    results = await migrator.migrate_all_empresas()
    
    print(f"✅ Migración completada:")
    print(f"  - Tenants migrados: {len(results['migrated_tenants'])}")
    print(f"  - Registros migrados: {results['total_records_migrated']}")
    print(f"  - Tiempo total: {results['duration']:.2f} segundos")
    
    if results['failed_tenants']:
        print(f"❌ Tenants fallidos: {len(results['failed_tenants'])}")

if __name__ == "__main__":
    asyncio.run(main())
