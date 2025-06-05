"""
Modelos SQLAlchemy para el nuevo schema multitenant
Reemplaza las 559 tablas legacy con un diseño moderno y optimizado
"""

from sqlalchemy import Column, String, Integer, Boolean, DateTime, Numeric, Text, JSON, ForeignKey, UniqueConstraint, CheckConstraint, Index, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class TenantMixin:
    """Mixin para isolation automático por tenant"""
    tenant_id = Column(UUID(as_uuid=True), nullable=False, index=True)

class TimestampMixin:
    """Mixin para timestamps automáticos"""
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class Tenant(Base):
    """
    Tabla principal de tenants - Reemplaza 100+ bases de datos separadas
    """
    __tablename__ = 'tenants'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = Column(String(50), unique=True, nullable=False, index=True)
    company_name = Column(String(255), nullable=False)
    nit = Column(String(20))
    email = Column(String(255))
    phone = Column(String(20))
    address = Column(Text)
    country_code = Column(String(3), default='SLV')
    timezone = Column(String(50), default='America/El_Salvador')
    
    # Configuración SaaS
    plan_type = Column(String(20), default='basic')
    max_users = Column(Integer, default=10)
    max_products = Column(Integer, default=1000)
    max_storage_mb = Column(Integer, default=1024)
    
    # Features habilitadas por tenant
    features = Column(JSON, default={})
    
    # Estado
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Legacy mapping para migración
    legacy_empresa_id = Column(Integer, index=True)
    
    # Constraints
    __table_args__ = (
        CheckConstraint("slug ~ '^[a-z0-9_-]+$'", name='valid_slug'),
        CheckConstraint("plan_type IN ('basic', 'premium', 'enterprise')", name='valid_plan'),
        Index('idx_tenants_active_slug', 'slug', postgresql_where='is_active = true'),
    )
    
    # Relationships
    users = relationship("User", back_populates="tenant", cascade="all, delete-orphan")
    customers = relationship("Customer", back_populates="tenant", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="tenant", cascade="all, delete-orphan")

class User(Base, TenantMixin, TimestampMixin):
    """
    Usuarios del sistema - Reemplaza múltiples tablas de usuarios legacy
    """
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Credenciales
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    username = Column(String(50))
    
    # Información personal
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    avatar_url = Column(String(500))
    
    # Configuración
    language = Column(String(5), default='es')
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)
    last_login = Column(DateTime)
    
    # Legacy mapping
    legacy_usuario_id = Column(Integer)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'email', name='unique_email_per_tenant'),
        UniqueConstraint('tenant_id', 'username', name='unique_username_per_tenant'),
        Index('idx_users_tenant_email', 'tenant_id', 'email'),
    )
    
    # Relationships
    tenant = relationship("Tenant", back_populates="users")
    roles = relationship("UserRole", back_populates="user", cascade="all, delete-orphan")

class Role(Base, TenantMixin, TimestampMixin):
    """
    Roles del sistema - Sistema moderno vs accesos legacy confusos
    """
    __tablename__ = 'roles'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    permissions = Column(JSON, default={})
    is_system_role = Column(Boolean, default=False)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'name', name='unique_role_per_tenant'),
    )
    
    # Relationships
    user_roles = relationship("UserRole", back_populates="role", cascade="all, delete-orphan")

class UserRole(Base):
    """
    Asignación de roles a usuarios
    """
    __tablename__ = 'user_roles'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)
    assigned_at = Column(DateTime, default=func.now())
    assigned_by = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('user_id', 'role_id', name='unique_user_role'),
    )
    
    # Relationships
    user = relationship("User", back_populates="roles", foreign_keys=[user_id])
    role = relationship("Role", back_populates="user_roles")
    assigner = relationship("User", foreign_keys=[assigned_by])

class Customer(Base, TenantMixin, TimestampMixin):
    """
    Clientes - Reemplaza clientes + agrupaclientes + múltiples tablas legacy
    """
    __tablename__ = 'customers'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Identificación
    customer_code = Column(String(25))
    tax_id = Column(String(20))
    legal_name = Column(String(255), nullable=False)
    commercial_name = Column(String(255))
    
    # Contacto
    email = Column(String(255))
    phone = Column(String(20))
    mobile = Column(String(20))
    website = Column(String(255))
    
    # Dirección
    address_line1 = Column(Text)
    address_line2 = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    postal_code = Column(String(20))
    country_code = Column(String(3), default='SLV')
    
    # Configuración comercial
    customer_type = Column(String(20), default='regular')
    payment_terms = Column(Integer, default=30)
    credit_limit = Column(Numeric(15, 2), default=0)
    discount_percentage = Column(Numeric(5, 2), default=0)
    
    # Estado
    status = Column(String(20), default='active')
    
    # Legacy mapping
    legacy_cliente_id = Column(String(25))
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'customer_code', name='unique_customer_code'),
        UniqueConstraint('tenant_id', 'tax_id', name='unique_tax_id'),
        CheckConstraint("customer_type IN ('regular', 'vip', 'wholesale', 'government')", name='valid_customer_type'),
        CheckConstraint("status IN ('active', 'inactive', 'blocked')", name='valid_status'),
        Index('idx_customers_tenant_status', 'tenant_id', 'status'),
        Index('idx_customers_tenant_code', 'tenant_id', 'customer_code'),
    )
    
    # Relationships
    tenant = relationship("Tenant", back_populates="customers")
    invoices = relationship("Invoice", back_populates="customer", cascade="all, delete-orphan")

class ProductCategory(Base, TenantMixin, TimestampMixin):
    """
    Categorías de productos - Reemplaza categoria + múltiples tablas legacy
    """
    __tablename__ = 'product_categories'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'))
    is_active = Column(Boolean, default=True)
    
    # Legacy mapping
    legacy_categoria_id = Column(Integer)
    
    # Relationships
    products = relationship("Product", back_populates="category")
    parent = relationship("ProductCategory", remote_side=[id])

class Product(Base, TenantMixin, TimestampMixin):
    """
    Productos - Reemplaza producto + múltiples tablas legacy
    """
    __tablename__ = 'products'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'))
    
    # Identificación
    sku = Column(String(50), nullable=False)
    barcode = Column(String(50))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    
    # Precios
    cost_price = Column(Numeric(15, 4), default=0)
    selling_price = Column(Numeric(15, 4), default=0)
    min_selling_price = Column(Numeric(15, 4), default=0)
    
    # Inventario
    track_inventory = Column(Boolean, default=True)
    current_stock = Column(Numeric(10, 3), default=0)
    min_stock = Column(Numeric(10, 3), default=0)
    max_stock = Column(Numeric(10, 3), default=0)
    
    # Configuración
    is_active = Column(Boolean, default=True)
    is_service = Column(Boolean, default=False)
    
    # Legacy mapping
    legacy_producto_id = Column(Integer)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'sku', name='unique_sku'),
        UniqueConstraint('tenant_id', 'barcode', name='unique_barcode'),
        Index('idx_products_tenant_sku', 'tenant_id', 'sku'),
        Index('idx_products_tenant_active', 'tenant_id', 'is_active'),
    )
    
    # Relationships
    tenant = relationship("Tenant", back_populates="products")
    category = relationship("ProductCategory", back_populates="products")
    inventory_movements = relationship("InventoryMovement", back_populates="product")

class Warehouse(Base, TenantMixin, TimestampMixin):
    """
    Bodegas - Reemplaza bodega + múltiples tablas legacy
    """
    __tablename__ = 'warehouses'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    code = Column(String(20), nullable=False)
    address = Column(Text)
    is_main = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    # Legacy mapping
    legacy_bodega_id = Column(Integer)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'code', name='unique_warehouse_code'),
        Index('idx_warehouses_tenant_active', 'tenant_id', 'is_active'),
    )
    
    # Relationships
    inventory_movements = relationship("InventoryMovement", back_populates="warehouse")

class InventoryMovement(Base, TenantMixin, TimestampMixin):
    """
    Movimientos de inventario - Reemplaza almacen + dalmacen + múltiples
    """
    __tablename__ = 'inventory_movements'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'), nullable=False)
    warehouse_id = Column(UUID(as_uuid=True), ForeignKey('warehouses.id'), nullable=False)
    
    # Movimiento
    movement_type = Column(String(20), nullable=False)
    quantity = Column(Numeric(10, 3), nullable=False)
    unit_cost = Column(Numeric(15, 4))
    reference_type = Column(String(20))
    reference_id = Column(UUID(as_uuid=True))
    
    # Metadatos
    notes = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    # Constraints
    __table_args__ = (
        CheckConstraint("movement_type IN ('in', 'out', 'adjustment', 'transfer')", name='valid_movement_type'),
        Index('idx_movements_tenant_product', 'tenant_id', 'product_id'),
        Index('idx_movements_tenant_warehouse', 'tenant_id', 'warehouse_id'),
    )
    
    # Relationships
    product = relationship("Product", back_populates="inventory_movements")
    warehouse = relationship("Warehouse", back_populates="inventory_movements")
    creator = relationship("User")

class Invoice(Base, TenantMixin, TimestampMixin):
    """
    Facturas - Reemplaza factura + dfactura + múltiples tablas legacy
    """
    __tablename__ = 'invoices'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.id'), nullable=False)
    
    # Identificación
    invoice_number = Column(String(50), nullable=False)
    invoice_series = Column(String(10))
    
    # Fechas
    issue_date = Column(Date, nullable=False, default=func.current_date())
    due_date = Column(Date)
    
    # Montos
    subtotal = Column(Numeric(15, 2), default=0)
    tax_amount = Column(Numeric(15, 2), default=0)
    discount_amount = Column(Numeric(15, 2), default=0)
    total_amount = Column(Numeric(15, 2), default=0)
    
    # Estado
    status = Column(String(20), default='draft')
    payment_status = Column(String(20), default='pending')
    
    # Configuración
    currency_code = Column(String(3), default='USD')
    exchange_rate = Column(Numeric(10, 4), default=1.0000)
    
    # Notas
    notes = Column(Text)
    terms_and_conditions = Column(Text)
    
    # Metadata
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    # Legacy mapping
    legacy_factura_id = Column(Integer)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'invoice_number', 'invoice_series', name='unique_invoice_number'),
        CheckConstraint("status IN ('draft', 'sent', 'paid', 'overdue', 'cancelled')", name='valid_status'),
        CheckConstraint("payment_status IN ('pending', 'partial', 'paid', 'overdue')", name='valid_payment_status'),
        Index('idx_invoices_tenant_status', 'tenant_id', 'status'),
        Index('idx_invoices_tenant_customer', 'tenant_id', 'customer_id'),
    )
    
    # Relationships
    customer = relationship("Customer", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    creator = relationship("User")

class InvoiceItem(Base):
    """
    Items de factura - Reemplaza dfactura + múltiples
    """
    __tablename__ = 'invoice_items'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey('invoices.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    
    # Producto
    description = Column(String(255), nullable=False)
    quantity = Column(Numeric(10, 3), nullable=False)
    unit_price = Column(Numeric(15, 4), nullable=False)
    discount_percentage = Column(Numeric(5, 2), default=0)
    tax_percentage = Column(Numeric(5, 2), default=0)
    
    # Cálculos
    line_total = Column(Numeric(15, 2), nullable=False)
    
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Product")

class Supplier(Base, TenantMixin, TimestampMixin):
    """
    Proveedores - Reemplaza proveedor + múltiples tablas legacy
    """
    __tablename__ = 'suppliers'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Identificación
    supplier_code = Column(String(25))
    tax_id = Column(String(20))
    legal_name = Column(String(255), nullable=False)
    commercial_name = Column(String(255))
    
    # Contacto
    email = Column(String(255))
    phone = Column(String(20))
    address = Column(Text)
    
    # Configuración comercial
    payment_terms = Column(Integer, default=30)
    
    # Estado
    status = Column(String(20), default='active')
    
    # Legacy mapping
    legacy_proveedor_id = Column(String(25))
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'supplier_code', name='unique_supplier_code'),
        UniqueConstraint('tenant_id', 'tax_id', name='unique_supplier_tax_id'),
        Index('idx_suppliers_tenant_status', 'tenant_id', 'status'),
    )
    
    # Relationships
    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")

class PurchaseOrder(Base, TenantMixin, TimestampMixin):
    """
    Órdenes de compra - Reemplaza compra + dcompra + múltiples
    """
    __tablename__ = 'purchase_orders'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    supplier_id = Column(UUID(as_uuid=True), ForeignKey('suppliers.id'), nullable=False)
    
    # Identificación
    po_number = Column(String(50), nullable=False)
    
    # Fechas
    order_date = Column(Date, nullable=False, default=func.current_date())
    expected_delivery_date = Column(Date)
    
    # Montos
    subtotal = Column(Numeric(15, 2), default=0)
    tax_amount = Column(Numeric(15, 2), default=0)
    total_amount = Column(Numeric(15, 2), default=0)
    
    # Estado
    status = Column(String(20), default='draft')
    
    # Metadata
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    # Legacy mapping
    legacy_compra_id = Column(Integer)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'po_number', name='unique_po_number'),
        Index('idx_po_tenant_supplier', 'tenant_id', 'supplier_id'),
    )
    
    # Relationships
    supplier = relationship("Supplier", back_populates="purchase_orders")
    creator = relationship("User")

# SCHEMA IA - Funcionalidades conversacionales

class AIConversation(Base, TenantMixin, TimestampMixin):
    """
    Conversaciones con IA - Nueva funcionalidad híbrida
    """
    __tablename__ = 'ai_conversations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    
    # Contexto
    context_module = Column(String(50))  # 'customers', 'inventory', 'invoicing'
    context_entity_id = Column(UUID(as_uuid=True))  # ID del cliente/producto/factura
    
    # Conversación
    title = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    # Relationships
    user = relationship("User")
    messages = relationship("AIMessage", back_populates="conversation", cascade="all, delete-orphan")

class AIMessage(Base):
    """
    Mensajes de las conversaciones IA
    """
    __tablename__ = 'ai_messages'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey('ai_conversations.id', ondelete='CASCADE'), nullable=False)
    
    # Mensaje
    role = Column(String(20), nullable=False)  # 'user', 'assistant', 'system'
    content = Column(Text, nullable=False)
    metadata = Column(JSON, default={})  # contexto adicional, acciones sugeridas
    
    created_at = Column(DateTime, default=func.now())
    
    # Constraints
    __table_args__ = (
        CheckConstraint("role IN ('user', 'assistant', 'system')", name='valid_role'),
    )
    
    # Relationships
    conversation = relationship("AIConversation", back_populates="messages")

class AIAutomation(Base, TenantMixin, TimestampMixin):
    """
    Automatizaciones con IA
    """
    __tablename__ = 'ai_automations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Trigger
    trigger_module = Column(String(50), nullable=False)
    trigger_condition = Column(JSON, nullable=False)
    
    # Action
    ai_prompt = Column(Text, nullable=False)
    action_type = Column(String(50), nullable=False)
    action_config = Column(JSON, default={})
    
    # Status
    is_active = Column(Boolean, default=True)
    execution_count = Column(Integer, default=0)
    last_executed = Column(DateTime)

class MigrationMapping(Base, TenantMixin):
    """
    Mapeo para migración automática desde legacy
    """
    __tablename__ = 'migration_mappings'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Legacy info
    legacy_table = Column(String(100), nullable=False)
    legacy_id = Column(String(50), nullable=False)
    
    # New info
    new_table = Column(String(100), nullable=False)
    new_id = Column(UUID(as_uuid=True), nullable=False)
    
    # Status
    migrated_at = Column(DateTime, default=func.now())
    migration_notes = Column(Text)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('tenant_id', 'legacy_table', 'legacy_id', name='unique_legacy_mapping'),
    )
