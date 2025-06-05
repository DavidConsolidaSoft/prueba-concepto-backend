# Diseño Schema Multitenant Moderno
## Reemplazo Completo del Legacy de 559 Tablas

### Análisis del Problema Legacy

**Schema Legacy Identificado:**
- 559 tablas mal diseñadas
- Sin multitenant (100+ bases de datos separadas)
- Nomenclatura inconsistente (AddingsClientes, acomision, caccesos)
- Redundancia masiva (campo `empresa` en cada tabla)
- Tipos de datos inconsistentes
- Foreign keys mal definidas

### Diseño Nuevo: PostgreSQL Multitenant

## SCHEMA CORE - MULTITENANT

### 1. Tenant Management
```sql
-- Tabla principal de tenants (reemplaza 100+ bases de datos)
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(50) UNIQUE NOT NULL, -- empresa1, empresa2, etc
    company_name VARCHAR(255) NOT NULL,
    nit VARCHAR(20),
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    country_code VARCHAR(3) DEFAULT 'SLV',
    timezone VARCHAR(50) DEFAULT 'America/El_Salvador',
    
    -- Configuración SaaS
    plan_type VARCHAR(20) DEFAULT 'basic', -- basic, premium, enterprise
    max_users INTEGER DEFAULT 10,
    max_products INTEGER DEFAULT 1000,
    max_storage_mb INTEGER DEFAULT 1024,
    
    -- Features habilitadas
    features JSONB DEFAULT '{}', -- {"inventory": true, "billing": true, "hr": false}
    
    -- Metadatos
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true,
    
    -- Legacy mapping (para migración)
    legacy_empresa_id INTEGER, -- mapeo con el campo "empresa" legacy
    
    CONSTRAINT valid_slug CHECK (slug ~ '^[a-z0-9_-]+$'),
    CONSTRAINT valid_plan CHECK (plan_type IN ('basic', 'premium', 'enterprise'))
);

-- Índices optimizados
CREATE INDEX idx_tenants_slug ON tenants(slug) WHERE is_active = true;
CREATE INDEX idx_tenants_legacy_id ON tenants(legacy_empresa_id) WHERE legacy_empresa_id IS NOT NULL;
```

### 2. Users & Authentication (Reemplaza multiple tablas de usuarios)
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    -- Credenciales
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    username VARCHAR(50),
    
    -- Información personal
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    avatar_url VARCHAR(500),
    
    -- Configuración
    language VARCHAR(5) DEFAULT 'es',
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    last_login TIMESTAMP,
    
    -- Metadatos
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_usuario_id INTEGER,
    
    CONSTRAINT unique_email_per_tenant UNIQUE(tenant_id, email),
    CONSTRAINT unique_username_per_tenant UNIQUE(tenant_id, username)
);

-- RLS (Row Level Security) automático
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY users_tenant_isolation ON users 
    FOR ALL TO authenticated 
    USING (tenant_id = current_setting('app.current_tenant')::UUID);
```

### 3. Roles & Permissions (Moderno vs legacy confuso)
```sql
CREATE TABLE roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    permissions JSONB DEFAULT '{}', -- {"can_create_invoice": true, "can_view_reports": false}
    is_system_role BOOLEAN DEFAULT false, -- admin, employee, viewer
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE user_roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    assigned_at TIMESTAMP DEFAULT NOW(),
    assigned_by UUID REFERENCES users(id),
    
    CONSTRAINT unique_user_role UNIQUE(user_id, role_id)
);
```

## SCHEMA BUSINESS - CORE ERP

### 4. Customers (Reemplaza clientes + agrupaclientes + múltiples tablas)
```sql
CREATE TABLE customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    -- Identificación
    customer_code VARCHAR(25), -- código interno
    tax_id VARCHAR(20), -- NIT/RUC
    legal_name VARCHAR(255) NOT NULL,
    commercial_name VARCHAR(255),
    
    -- Contacto
    email VARCHAR(255),
    phone VARCHAR(20),
    mobile VARCHAR(20),
    website VARCHAR(255),
    
    -- Dirección
    address_line1 TEXT,
    address_line2 TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country_code VARCHAR(3) DEFAULT 'SLV',
    
    -- Configuración comercial
    customer_type VARCHAR(20) DEFAULT 'regular', -- regular, vip, wholesale
    payment_terms INTEGER DEFAULT 30, -- días
    credit_limit DECIMAL(15,2) DEFAULT 0,
    discount_percentage DECIMAL(5,2) DEFAULT 0,
    
    -- Estado
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_cliente_id VARCHAR(25),
    
    CONSTRAINT unique_customer_code UNIQUE(tenant_id, customer_code),
    CONSTRAINT unique_tax_id UNIQUE(tenant_id, tax_id),
    CONSTRAINT valid_customer_type CHECK (customer_type IN ('regular', 'vip', 'wholesale', 'government')),
    CONSTRAINT valid_status CHECK (status IN ('active', 'inactive', 'blocked'))
);

-- RLS automático
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
CREATE POLICY customers_tenant_isolation ON customers 
    FOR ALL TO authenticated 
    USING (tenant_id = current_setting('app.current_tenant')::UUID);
```

### 5. Products & Inventory (Reemplaza producto + categoria + bodega + múltiples)
```sql
CREATE TABLE product_categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_id UUID REFERENCES product_categories(id),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_categoria_id INTEGER
);

CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    category_id UUID REFERENCES product_categories(id),
    
    -- Identificación
    sku VARCHAR(50) NOT NULL,
    barcode VARCHAR(50),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    
    -- Precios
    cost_price DECIMAL(15,4) DEFAULT 0,
    selling_price DECIMAL(15,4) DEFAULT 0,
    min_selling_price DECIMAL(15,4) DEFAULT 0,
    
    -- Inventario
    track_inventory BOOLEAN DEFAULT true,
    current_stock DECIMAL(10,3) DEFAULT 0,
    min_stock DECIMAL(10,3) DEFAULT 0,
    max_stock DECIMAL(10,3) DEFAULT 0,
    
    -- Configuración
    is_active BOOLEAN DEFAULT true,
    is_service BOOLEAN DEFAULT false,
    
    -- Metadatos
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_producto_id INTEGER,
    
    CONSTRAINT unique_sku UNIQUE(tenant_id, sku),
    CONSTRAINT unique_barcode UNIQUE(tenant_id, barcode)
);

CREATE TABLE warehouses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) NOT NULL,
    address TEXT,
    is_main BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_bodega_id INTEGER,
    
    CONSTRAINT unique_warehouse_code UNIQUE(tenant_id, code)
);

CREATE TABLE inventory_movements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES products(id),
    warehouse_id UUID NOT NULL REFERENCES warehouses(id),
    
    -- Movimiento
    movement_type VARCHAR(20) NOT NULL, -- in, out, adjustment, transfer
    quantity DECIMAL(10,3) NOT NULL,
    unit_cost DECIMAL(15,4),
    reference_type VARCHAR(20), -- invoice, purchase, adjustment, transfer
    reference_id UUID,
    
    -- Metadatos
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    created_by UUID REFERENCES users(id),
    
    CONSTRAINT valid_movement_type CHECK (movement_type IN ('in', 'out', 'adjustment', 'transfer'))
);
```

### 6. Invoicing & Billing (Reemplaza factura + dfactura + pagos + múltiples)
```sql
CREATE TABLE invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    customer_id UUID NOT NULL REFERENCES customers(id),
    
    -- Identificación
    invoice_number VARCHAR(50) NOT NULL,
    invoice_series VARCHAR(10),
    
    -- Fechas
    issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE,
    
    -- Montos
    subtotal DECIMAL(15,2) DEFAULT 0,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    discount_amount DECIMAL(15,2) DEFAULT 0,
    total_amount DECIMAL(15,2) DEFAULT 0,
    
    -- Estado
    status VARCHAR(20) DEFAULT 'draft', -- draft, sent, paid, overdue, cancelled
    payment_status VARCHAR(20) DEFAULT 'pending', -- pending, partial, paid, overdue
    
    -- Configuración
    currency_code VARCHAR(3) DEFAULT 'USD',
    exchange_rate DECIMAL(10,4) DEFAULT 1.0000,
    
    -- Notas
    notes TEXT,
    terms_and_conditions TEXT,
    
    -- Metadatos
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    created_by UUID REFERENCES users(id),
    
    -- Legacy mapping
    legacy_factura_id INTEGER,
    
    CONSTRAINT unique_invoice_number UNIQUE(tenant_id, invoice_number, invoice_series),
    CONSTRAINT valid_status CHECK (status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')),
    CONSTRAINT valid_payment_status CHECK (payment_status IN ('pending', 'partial', 'paid', 'overdue'))
);

CREATE TABLE invoice_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    invoice_id UUID NOT NULL REFERENCES invoices(id) ON DELETE CASCADE,
    product_id UUID REFERENCES products(id),
    
    -- Producto
    description VARCHAR(255) NOT NULL,
    quantity DECIMAL(10,3) NOT NULL,
    unit_price DECIMAL(15,4) NOT NULL,
    discount_percentage DECIMAL(5,2) DEFAULT 0,
    tax_percentage DECIMAL(5,2) DEFAULT 0,
    
    -- Cálculos
    line_total DECIMAL(15,2) NOT NULL,
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 7. Purchases (Reemplaza compra + dcompra + proveedor + múltiples)
```sql
CREATE TABLE suppliers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    -- Similar structure to customers but for suppliers
    supplier_code VARCHAR(25),
    tax_id VARCHAR(20),
    legal_name VARCHAR(255) NOT NULL,
    commercial_name VARCHAR(255),
    
    -- Contact info
    email VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    
    -- Commercial config
    payment_terms INTEGER DEFAULT 30,
    
    -- Status
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Legacy mapping
    legacy_proveedor_id VARCHAR(25)
);

CREATE TABLE purchase_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    supplier_id UUID NOT NULL REFERENCES suppliers(id),
    
    -- Identification
    po_number VARCHAR(50) NOT NULL,
    
    -- Dates
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expected_delivery_date DATE,
    
    -- Amounts
    subtotal DECIMAL(15,2) DEFAULT 0,
    tax_amount DECIMAL(15,2) DEFAULT 0,
    total_amount DECIMAL(15,2) DEFAULT 0,
    
    -- Status
    status VARCHAR(20) DEFAULT 'draft',
    
    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    created_by UUID REFERENCES users(id),
    
    -- Legacy mapping
    legacy_compra_id INTEGER
);
```

## SCHEMA ANALYTICS - IA & REPORTING

### 8. AI Conversations (Nueva funcionalidad)
```sql
CREATE TABLE ai_conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id),
    
    -- Contexto
    context_module VARCHAR(50), -- 'customers', 'inventory', 'invoicing'
    context_entity_id UUID, -- ID del cliente/producto/factura en contexto
    
    -- Conversación
    title VARCHAR(255),
    is_active BOOLEAN DEFAULT true,
    
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ai_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL REFERENCES ai_conversations(id) ON DELETE CASCADE,
    
    -- Mensaje
    role VARCHAR(20) NOT NULL, -- 'user', 'assistant', 'system'
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}', -- contexto adicional, acciones sugeridas
    
    created_at TIMESTAMP DEFAULT NOW(),
    
    CONSTRAINT valid_role CHECK (role IN ('user', 'assistant', 'system'))
);

CREATE TABLE ai_automations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    
    -- Trigger
    trigger_module VARCHAR(50) NOT NULL,
    trigger_condition JSONB NOT NULL,
    
    -- Action
    ai_prompt TEXT NOT NULL,
    action_type VARCHAR(50) NOT NULL,
    action_config JSONB DEFAULT '{}',
    
    -- Status
    is_active BOOLEAN DEFAULT true,
    execution_count INTEGER DEFAULT 0,
    last_executed TIMESTAMP,
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

## MIGRACIÓN STRATEGY

### 9. Migration Mapping (Para migración automática)
```sql
CREATE TABLE migration_mappings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    
    -- Legacy info
    legacy_table VARCHAR(100) NOT NULL,
    legacy_id VARCHAR(50) NOT NULL,
    
    -- New info
    new_table VARCHAR(100) NOT NULL,
    new_id UUID NOT NULL,
    
    -- Status
    migrated_at TIMESTAMP DEFAULT NOW(),
    migration_notes TEXT,
    
    CONSTRAINT unique_legacy_mapping UNIQUE(tenant_id, legacy_table, legacy_id)
);
```

## BENEFICIOS DEL NUEVO DISEÑO

### Performance
- ✅ RLS automático (Row Level Security)
- ✅ Índices optimizados por tenant
- ✅ Particionado por tenant (opcional)
- ✅ Un solo cluster PostgreSQL vs 100+ bases SQL Server

### Escalabilidad
- ✅ Un tenant nuevo = insertar 1 fila vs crear 559 tablas
- ✅ Backup unificado
- ✅ Monitoreo centralizado
- ✅ Updates de schema centralizados

### Mantenibilidad
- ✅ Schema consistente y normalizado
- ✅ Nombres claros en inglés
- ✅ Tipos de datos consistentes
- ✅ Foreign keys bien definidas

### SaaS Ready
- ✅ Multitenant nativo
- ✅ Feature flags por tenant
- ✅ Billing por tenant
- ✅ Analytics por tenant

### IA Ready
- ✅ Contexto conversacional
- ✅ Automatizaciones inteligentes
- ✅ Análisis cross-tenant (agregado)
- ✅ Embeddings y semantic search

## NEXT STEPS

1. **Validar diseño** con business logic actual
2. **Crear migration scripts** automáticos 
3. **Implementar en Postgres** con RLS
4. **Migrar tenant por tenant** de forma gradual
5. **Integrar IA** desde día 1