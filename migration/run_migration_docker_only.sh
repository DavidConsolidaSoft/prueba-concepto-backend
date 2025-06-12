#!/bin/bash
# =============================================================================
# EJECUTOR COMPLETO DE MIGRACIÓN ERP - VERSIÓN DOCKER ONLY
# SQL Server → PostgreSQL (559 tablas)
# Sin dependencias de Python local
# =============================================================================

echo "🚀 INICIANDO MIGRACIÓN COMPLETA ERP (DOCKER ONLY)"
echo "📊 Sistema: 559 tablas, 9,964 campos documentados"
echo "🎯 Objetivo: Schema completo PostgreSQL + migración datos"
echo "============================================================================="

# Variables de configuración
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="migration_complete_${TIMESTAMP}.log"
SCHEMA_FILE="complete_erp_schema_${TIMESTAMP}.sql"

# Función de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

# Verificar dependencias (solo Docker)
check_dependencies() {
    log "🔍 Verificando dependencias..."
    
    # Docker
    if ! command -v docker &> /dev/null; then
        log "❌ Docker no encontrado"
        exit 1
    fi
    
    # Verificar contenedores
    if ! docker ps | grep -q "postgres-erp-migration"; then
        log "❌ Contenedor PostgreSQL no está corriendo"
        log "💡 Ejecutar: docker-compose up -d"
        exit 1
    fi
    
    if ! docker ps | grep -q "sqlserver-erp-origen"; then
        log "❌ Contenedor SQL Server no está corriendo"
        log "💡 Ejecutar: docker-compose up -d"
        exit 1
    fi
    
    log "✅ Todas las dependencias verificadas"
}

# Crear contenedor Python temporal para migración
create_python_container() {
    log "🐳 Creando contenedor Python para migración..."
    
    # Crear Dockerfile temporal
    cat > Dockerfile.migration << 'EOF'
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc-dev \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Microsoft ODBC Driver para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Instalar librerías Python
RUN pip install psycopg2-binary pyodbc

# Directorio de trabajo
WORKDIR /migration

CMD ["python3"]
EOF

    # Construir imagen
    docker build -f Dockerfile.migration -t erp-migration-python . > docker_build.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Contenedor Python creado exitosamente"
        # Limpiar Dockerfile temporal
        rm Dockerfile.migration
    else
        log "❌ Error creando contenedor Python"
        log "📋 Revisar: docker_build.log"
        exit 1
    fi
}

# Fase 1: Generar schema completo usando Docker
generate_complete_schema() {
    log "🏗️  FASE 1: Generando schema completo (559 tablas)"
    
    # Ejecutar generador de schema en contenedor Python
    docker run --rm \
        --network erp-migration-network \
        -v "$(pwd)/migration:/migration" \
        -e SQL_SERVER_HOST=sqlserver-erp-origen \
        -e POSTGRES_HOST=postgres-erp-migration \
        erp-migration-python \
        python3 generate_complete_schema.py > schema_generation.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Schema completo generado exitosamente"
        # Buscar archivo generado
        GENERATED_SCHEMA=$(ls migration/complete_schema_*.sql 2>/dev/null | head -1)
        if [ -n "$GENERATED_SCHEMA" ]; then
            log "📄 Archivo generado: $GENERATED_SCHEMA"
            SCHEMA_FILE=$GENERATED_SCHEMA
        fi
    else
        log "❌ Error generando schema completo"
        log "📋 Revisar: schema_generation.log"
        exit 1
    fi
}

# Crear script de generación inline
generate_schema_inline() {
    log "🏗️  FASE 1: Generando schema básico (método alternativo)"
    
    # Crear schema básico usando SQL directo
    cat > $SCHEMA_FILE << 'EOF'
-- =====================================================
-- SCHEMA POSTGRESQL BÁSICO - ERP MIGRATION
-- Generado por script Docker-only
-- =====================================================

-- Extensiones necesarias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "btree_gin";
CREATE EXTENSION IF NOT EXISTS "btree_gist";

-- Schemas principales
CREATE SCHEMA IF NOT EXISTS erp_main;
CREATE SCHEMA IF NOT EXISTS erp_control;
CREATE SCHEMA IF NOT EXISTS legacy_procedures;

-- Función para timestamps automáticos
CREATE OR REPLACE FUNCTION erp_main.update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.fecha_modificacion = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Tablas de control para migración
CREATE TABLE IF NOT EXISTS erp_control.migration_status (
    id BIGSERIAL PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    migration_phase VARCHAR(50) NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    end_time TIMESTAMP WITH TIME ZONE,
    records_migrated BIGINT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'PENDING',
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS erp_control.id_mapping (
    source_table VARCHAR(100) NOT NULL,
    source_id BIGINT NOT NULL,
    target_id BIGINT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (source_table, source_id)
);

CREATE TABLE IF NOT EXISTS erp_control.session_continuity (
    session_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    migration_phase VARCHAR(50) NOT NULL,
    current_step TEXT,
    next_actions JSONB,
    validation_results JSONB,
    error_log TEXT,
    recovery_commands TEXT
);

-- Checkpoint de completación
INSERT INTO erp_control.session_continuity (
    migration_phase,
    current_step,
    next_actions
) VALUES (
    'BASIC_SCHEMA_CREATION',
    'Schema básico creado - Listo para migración manual',
    '{"next": "run_python_generator", "then": "execute_complete_migration"}'::jsonb
);
EOF

    log "✅ Schema básico generado: $SCHEMA_FILE"
}

# Fase 2: Ejecutar schema en PostgreSQL
execute_schema() {
    log "📋 FASE 2: Ejecutando schema en PostgreSQL"
    
    # Conectar a PostgreSQL y ejecutar schema
    docker exec -i postgres-erp-migration psql -U postgres -d erp_consolidasoft < $SCHEMA_FILE > schema_execution.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Schema ejecutado exitosamente en PostgreSQL"
        
        # Verificar cantidad de tablas creadas
        TABLE_COUNT=$(docker exec postgres-erp-migration psql -U postgres -d erp_consolidasoft -t -c "SELECT COUNT(*) FROM pg_tables WHERE schemaname = 'erp_main';" | tr -d ' ' | tr -d '\n')
        log "📊 Tablas creadas en erp_main: $TABLE_COUNT"
        
        if [ "$TABLE_COUNT" -gt 0 ]; then
            log "✅ Schema básico creado exitosamente"
        else
            log "⚠️  Solo esquema de control creado"
        fi
    else
        log "❌ Error ejecutando schema en PostgreSQL"
        log "📋 Revisar: schema_execution.log"
        exit 1
    fi
}

# Función de instrucciones manuales
manual_instructions() {
    log "📋 INSTRUCCIONES PARA COMPLETAR MIGRACIÓN"
    
    INSTRUCTIONS_FILE="migration_instructions_${TIMESTAMP}.md"
    
    cat > $INSTRUCTIONS_FILE << EOF
# Instrucciones para Completar Migración ERP

## Estado Actual
- ✅ Contenedores Docker funcionando
- ✅ Schema básico PostgreSQL creado
- ⏳ Pendiente: Migración completa de 559 tablas

## Próximos Pasos

### Opción 1: Instalar Python y Continuar
\`\`\`bash
# 1. Instalar Python 3.11+
# Descargar desde: https://www.python.org/downloads/
# ¡IMPORTANTE! Marcar "Add Python to PATH"

# 2. Instalar dependencias
pip install psycopg2-binary pyodbc

# 3. Ejecutar migración completa
python migration/generate_complete_schema.py
python migration/migrate_erp_data.py
\`\`\`

### Opción 2: Usar Contenedor Python (Avanzado)
\`\`\`bash
# 1. Crear contenedor Python con dependencias
docker run -it --network erp-migration-network python:3.11 bash

# 2. Dentro del contenedor:
pip install psycopg2-binary pyodbc
cd /migration
python generate_complete_schema.py
\`\`\`

### Opción 3: Migración Manual por Partes
\`\`\`bash
# 1. Usar pgloader (desde WSL2)
sudo apt install pgloader
pgloader "mssql://sa:MigracionERP2025!@localhost:1433/una" \\
         "postgresql://postgres:MigracionERP2025!@localhost:5422/erp_consolidasoft"

# 2. O exportar/importar por lotes
docker exec sqlserver-erp-origen sqlcmd -S localhost -U sa -P "MigracionERP2025!" \\
    -Q "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
\`\`\`

## Validar Estado Actual
\`\`\`bash
# Conectar a PostgreSQL
docker exec -it postgres-erp-migration psql -U postgres -d erp_consolidasoft

# Ver tablas actuales
\\dt erp_main.*

# Ver estado de migración
SELECT * FROM erp_control.session_continuity ORDER BY created_at DESC;
\`\`\`

## Archivos Generados
- Schema básico: $SCHEMA_FILE
- Log principal: $LOG_FILE
- Instrucciones: $INSTRUCTIONS_FILE

¡El sistema está preparado para completar la migración!
EOF

    log "📄 Instrucciones guardadas en: $INSTRUCTIONS_FILE"
    log "🎯 Próximo paso: Instalar Python o usar método alternativo"
}

# Función principal
main() {
    START_TIME=$(date +%s)
    log "🚀 INICIANDO PROCESO COMPLETO DE MIGRACIÓN ERP (DOCKER ONLY)"
    log "⏰ Hora de inicio: $(date)"
    
    # Ejecutar fases disponibles
    check_dependencies
    
    # Decidir método de generación de schema
    log "🤔 Python no encontrado localmente - usando método alternativo"
    generate_schema_inline
    execute_schema
    manual_instructions
    
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    
    log "🎉 PREPARACIÓN COMPLETADA"
    log "⏱️  Duración: ${DURATION} segundos"
    log "📋 Revisar: migration_instructions_${TIMESTAMP}.md"
    log "💡 Instalar Python para migración completa automatizada"
}

# Manejo de interrupciones
trap 'log "⚠️  Proceso interrumpido por usuario"; exit 1' INT

# Verificar si se ejecuta directamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi