#!/bin/bash
# =============================================================================
# EJECUTOR COMPLETO DE MIGRACIÓN ERP
# SQL Server → PostgreSQL (559 tablas)
# =============================================================================

echo "🚀 INICIANDO MIGRACIÓN COMPLETA ERP"
echo "📊 Sistema: 559 tablas, 9,964 campos documentados"
echo "🎯 Objetivo: Schema completo PostgreSQL + migración datos"
echo "============================================================================="

# Variables de configuración
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="migration_complete_${TIMESTAMP}.log"
SCHEMA_FILE="complete_erp_schema_${TIMESTAMP}.sql"
DATA_LOG="data_migration_${TIMESTAMP}.log"

# Función de logging
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

# Verificar dependencias
check_dependencies() {
    log "🔍 Verificando dependencias..."
    
    # Python y librerías
    if ! command -v python3 &> /dev/null; then
        log "❌ Python3 no encontrado"
        exit 1
    fi
    
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

# Fase 1: Generar schema completo
generate_complete_schema() {
    log "🏗️  FASE 1: Generando schema completo (559 tablas)"
    
    python3 migration/generate_complete_schema.py > schema_generation.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Schema completo generado exitosamente"
        # El archivo se genera automáticamente por el script Python
        GENERATED_SCHEMA=$(ls complete_schema_*.sql 2>/dev/null | head -1)
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

# Fase 2: Ejecutar schema en PostgreSQL
execute_schema() {
    log "📋 FASE 2: Ejecutando schema en PostgreSQL"
    
    # Conectar a PostgreSQL y ejecutar schema
    docker exec -i postgres-erp-migration psql -U postgres -d erp_consolidasoft < $SCHEMA_FILE > schema_execution.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Schema ejecutado exitosamente en PostgreSQL"
        
        # Verificar cantidad de tablas creadas
        TABLE_COUNT=$(docker exec postgres-erp-migration psql -U postgres -d erp_consolidasoft -t -c "SELECT COUNT(*) FROM pg_tables WHERE schemaname = 'erp_main';" | tr -d ' ')
        log "📊 Tablas creadas en erp_main: $TABLE_COUNT"
        
        if [ "$TABLE_COUNT" -gt 500 ]; then
            log "🎉 Schema completo creado exitosamente"
        else
            log "⚠️  Advertencia: Solo $TABLE_COUNT tablas creadas (esperadas ~559)"
        fi
    else
        log "❌ Error ejecutando schema en PostgreSQL"
        log "📋 Revisar: schema_execution.log"
        exit 1
    fi
}

# Fase 3: Validar estructura
validate_schema() {
    log "🔍 FASE 3: Validando estructura creada"
    
    # Queries de validación
    VALIDATION_SQL="
    -- Contar tablas por schema
    SELECT 'erp_main' as schema, COUNT(*) as tablas FROM pg_tables WHERE schemaname = 'erp_main'
    UNION ALL
    SELECT 'erp_control', COUNT(*) FROM pg_tables WHERE schemaname = 'erp_control';
    
    -- Contar secuencias
    SELECT 'sequences' as tipo, COUNT(*) as total FROM pg_sequences WHERE schemaname = 'erp_main';
    
    -- Contar foreign keys
    SELECT 'foreign_keys' as tipo, COUNT(*) as total 
    FROM information_schema.table_constraints 
    WHERE constraint_type = 'FOREIGN KEY' AND table_schema = 'erp_main';
    
    -- Contar índices
    SELECT 'indexes' as tipo, COUNT(*) as total 
    FROM pg_indexes WHERE schemaname = 'erp_main';
    "
    
    echo "$VALIDATION_SQL" | docker exec -i postgres-erp-migration psql -U postgres -d erp_consolidasoft > validation_results.log 2>&1
    
    if [ $? -eq 0 ]; then
        log "✅ Validación de estructura completada"
        log "📊 Resultados guardados en: validation_results.log"
        cat validation_results.log | tail -20 >> $LOG_FILE
    else
        log "❌ Error en validación de estructura"
    fi
}

# Fase 4: Migración de datos (opcional)
migrate_data() {
    log "📦 FASE 4: ¿Migrar datos ahora? (s/N)"
    read -r MIGRATE_DATA
    
    if [[ $MIGRATE_DATA =~ ^[Ss]$ ]]; then
        log "🚀 Iniciando migración de datos..."
        
        python3 migration/migrate_erp_data.py > $DATA_LOG 2>&1 &
        MIGRATION_PID=$!
        
        log "📈 Migración de datos ejecutándose en background (PID: $MIGRATION_PID)"
        log "📋 Monitorear progreso: tail -f $DATA_LOG"
        log "🔍 Estado en PostgreSQL: SELECT * FROM erp_control.migration_status ORDER BY start_time DESC;"
        
        # Opción de esperar o continuar
        log "💡 Presionar ENTER para esperar completación, o Ctrl+C para continuar en background"
        read -r
        
        wait $MIGRATION_PID
        if [ $? -eq 0 ]; then
            log "🎉 Migración de datos completada exitosamente"
        else
            log "❌ Migración de datos falló - revisar $DATA_LOG"
        fi
    else
        log "⏭️  Migración de datos omitida"
        log "💡 Para migrar datos más tarde: python3 migration/migrate_erp_data.py"
    fi
}

# Función de reporte final
generate_report() {
    log "📋 GENERANDO REPORTE FINAL"
    
    REPORT_FILE="migration_report_${TIMESTAMP}.md"
    
    cat > $REPORT_FILE << EOF
# Reporte de Migración ERP - $(date)

## Resumen Ejecutivo
- **Fecha:** $(date '+%Y-%m-%d %H:%M:%S')
- **Duración total:** \$(($(date +%s) - START_TIME)) segundos
- **Archivos generados:** 
  - Schema: $SCHEMA_FILE
  - Logs: $LOG_FILE
  - Validación: validation_results.log

## Métricas de Migración
\`\`\`sql
-- Ejecutar en PostgreSQL para verificar estado
SELECT 
    'Tablas creadas' as metrica,
    COUNT(*) as valor
FROM pg_tables 
WHERE schemaname = 'erp_main'

UNION ALL SELECT 
    'Secuencias creadas',
    COUNT(*)
FROM pg_sequences 
WHERE schemaname = 'erp_main'

UNION ALL SELECT 
    'Foreign Keys',
    COUNT(*)
FROM information_schema.table_constraints 
WHERE constraint_type = 'FOREIGN KEY' 
  AND table_schema = 'erp_main'

UNION ALL SELECT 
    'Índices creados',
    COUNT(*)
FROM pg_indexes 
WHERE schemaname = 'erp_main';
\`\`\`

## Estado de Migración de Datos
\`\`\`sql
-- Progreso por tabla
SELECT 
    table_name,
    status,
    records_migrated,
    CASE status
        WHEN 'COMPLETED' THEN '✅'
        WHEN 'RUNNING' THEN '🔄'
        WHEN 'FAILED' THEN '❌'
        ELSE '⏳'
    END as status_icon,
    start_time,
    end_time
FROM erp_control.migration_status
ORDER BY start_time DESC
LIMIT 20;
\`\`\`

## Próximos Pasos

### Si el Schema fue Exitoso:
1. **Validar tipos críticos:**
   \`\`\`sql
   -- Verificar conversiones NUMERIC → DECIMAL
   SELECT table_name, column_name, data_type, numeric_precision, numeric_scale
   FROM information_schema.columns 
   WHERE table_schema = 'erp_main' 
     AND data_type = 'numeric'
   ORDER BY table_name, column_name;
   \`\`\`

2. **Verificar campos BIGINT críticos:**
   \`\`\`sql
   -- Verificar campos transaccionales → BIGINT
   SELECT table_name, column_name, data_type
   FROM information_schema.columns 
   WHERE table_schema = 'erp_main' 
     AND data_type = 'bigint'
     AND (table_name LIKE '%factura%' 
          OR table_name LIKE '%pedido%' 
          OR table_name LIKE '%venta%')
   ORDER BY table_name, column_name;
   \`\`\`

3. **Ejecutar migración de datos:**
   \`\`\`bash
   python3 migration/migrate_erp_data.py
   \`\`\`

### Si Hay Errores:
1. **Revisar logs:** $LOG_FILE
2. **Verificar conexiones:** docker-compose ps
3. **Validar estructura SQL Server:** Verificar que todas las 559 tablas estén accesibles

## Archivos de Referencia
- **Schema generado:** $SCHEMA_FILE
- **Log principal:** $LOG_FILE  
- **Validación:** validation_results.log
- **Datos (si aplica):** $DATA_LOG

## Comandos de Verificación
\`\`\`bash
# Ver tablas creadas
docker exec postgres-erp-migration psql -U postgres -d erp_consolidasoft -c "\\dt erp_main.*"

# Ver progreso de migración
docker exec postgres-erp-migration psql -U postgres -d erp_consolidasoft -c "SELECT * FROM erp_control.migration_status ORDER BY created_at DESC LIMIT 10;"

# Conectar directamente a PostgreSQL
docker exec -it postgres-erp-migration psql -U postgres -d erp_consolidasoft

# Conectar directamente a SQL Server
docker exec -it sqlserver-erp-origen /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "MigracionERP2025!" -C
\`\`\`

---
**Generado automáticamente por el sistema de migración ERP**
EOF
    
    log "📄 Reporte generado: $REPORT_FILE"
}

# Función de cleanup
cleanup() {
    log "🧹 Limpieza de archivos temporales..."
    # Mantener archivos importantes, limpiar temporales
    rm -f schema_generation.log schema_execution.log 2>/dev/null
    log "✅ Limpieza completada"
}

# Función principal
main() {
    START_TIME=$(date +%s)
    log "🚀 INICIANDO PROCESO COMPLETO DE MIGRACIÓN ERP"
    log "⏰ Hora de inicio: $(date)"
    
    # Ejecutar fases secuenciales
    check_dependencies
    generate_complete_schema
    execute_schema
    validate_schema
    migrate_data
    generate_report
    cleanup
    
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    
    log "🎉 PROCESO COMPLETO FINALIZADO"
    log "⏱️  Duración total: ${DURATION} segundos"
    log "📋 Reporte final: migration_report_${TIMESTAMP}.md"
    log "📊 Para verificar estado: docker exec -it postgres-erp-migration psql -U postgres -d erp_consolidasoft"
}

# Manejo de interrupciones
trap 'log "⚠️  Proceso interrumpido por usuario"; exit 1' INT

# Verificar si se ejecuta directamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi