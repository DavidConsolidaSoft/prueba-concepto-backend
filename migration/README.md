# Migración ERP: SQL Server → PostgreSQL

## 🎯 Objetivo del Proyecto

Consolidar múltiples bases SQL Server distribuidas en una sola instancia PostgreSQL, migrando **559 tablas** con **9,964 campos** documentados, manteniendo 100% de integridad y mejorando performance.

### Beneficios Esperados
- ✅ **70% reducción** en costos de hosting
- ✅ **80% reducción** en mantenimiento
- ✅ **200% mejora** en performance
- ✅ **Preparación** para integración con IA

---

## 📊 Métricas del Sistema

| Métrica | Valor | Criticidad |
|---------|--------|------------|
| **Total Tablas** | 559 | 🔴 Alta |
| **Total Campos** | 9,964 | 🔴 Alta |
| **Campos NUMERIC** | 1,928 | 🟡 Media |
| **Campos DATETIME** | 966 | 🟡 Media |
| **Campos AutoIncrement** | 513 (36 transaccionales) | 🔴 Alta |
| **Campos MONEY** | 19 | 🟢 Baja |
| **Usuarios Activos** | 1,000 distribuidos | 🔴 Alta |
| **Volumen Mensual** | ~80,000 facturas | 🔴 Alta |

---

## 🏗️ Arquitectura de Migración

### Entornos de Trabajo
```yaml
SQL Server (Origen):
  Host: localhost
  Port: 1433
  Database: una
  Usuario: sa
  
PostgreSQL (Destino):
  Host: localhost  
  Port: 5422
  Database: erp_consolidasoft
  Usuario: postgres
  Schemas: erp_main, erp_control
```

### Decisiones Técnicas Críticas

| Tipo SQL Server | PostgreSQL | Justificación |
|------------------|------------|---------------|
| `INT` (transaccional) | `BIGINT` | Escalabilidad 1M usuarios |
| `NUMERIC(18,6)` | `DECIMAL(18,6)` | Sin pérdida precisión |
| `DATETIME` | `TIMESTAMP WITH TIME ZONE` | Compatibilidad global |
| `BIT` | `BOOLEAN` | Estándar PostgreSQL |
| `MONEY` | `DECIMAL(19,4)` | Precisión financiera |

---

## 🚀 Ejecución Rápida

### Prerequisitos
```bash
# 1. Docker y Docker Compose instalados
docker --version
docker-compose --version

# 2. Python 3.x con librerías
pip install psycopg2-binary pyodbc

# 3. Levantar contenedores
docker-compose up -d

# 4. Verificar que estén corriendo
docker-compose ps
```

### Migración Completa (Un Solo Comando)
```bash
# Clonar repositorio
git clone https://github.com/DavidConsolidaSoft/prueba-concepto-backend.git
cd prueba-concepto-backend

# Ejecutar migración completa
chmod +x migration/run_complete_migration.sh
./migration/run_complete_migration.sh
```

### Migración Manual (Paso a Paso)
```bash
# 1. Generar schema completo
python3 migration/generate_complete_schema.py

# 2. Ejecutar schema en PostgreSQL  
docker exec -i postgres-erp-migration psql -U postgres -d erp_consolidasoft < complete_schema_*.sql

# 3. Migrar datos
python3 migration/migrate_erp_data.py

# 4. Validar resultados
docker exec -it postgres-erp-migration psql -U postgres -d erp_consolidasoft
```

---

## 📁 Estructura del Proyecto

```
migration/
├── run_complete_migration.sh      # 🚀 Ejecutor principal
├── generate_complete_schema.py    # 🏗️  Generador schema 559 tablas
├── migrate_erp_data.py            # 📦 Migrador de datos
├── docker-compose.yml             # 🐳 Contenedores SQL Server + PostgreSQL
└── README.md                      # 📖 Esta documentación
```

---

## 🔍 Validaciones y Monitoreo

### Verificar Schema Creado
```sql
-- Contar tablas creadas
SELECT COUNT(*) as total_tablas 
FROM pg_tables 
WHERE schemaname = 'erp_main';

-- Verificar tipos críticos
SELECT table_name, column_name, data_type, numeric_precision 
FROM information_schema.columns 
WHERE table_schema = 'erp_main' 
  AND data_type IN ('bigint', 'decimal', 'timestamp with time zone')
ORDER BY table_name, column_name;
```

### Monitorear Migración de Datos
```sql
-- Estado general de migración
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
ORDER BY start_time DESC;

-- Progreso en tiempo real
SELECT 
    SUM(CASE WHEN status = 'COMPLETED' THEN 1 ELSE 0 END) as completadas,
    SUM(CASE WHEN status = 'RUNNING' THEN 1 ELSE 0 END) as en_progreso,
    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) as fallidas,
    COUNT(*) as total
FROM erp_control.migration_status;
```

---

## 🎛️ Configuración Docker

### docker-compose.yml Actual
```yaml
version: '3.8'
services:
  postgres-migration:
    image: postgres:15-alpine
    container_name: postgres-erp-migration
    environment:
      POSTGRES_DB: erp_consolidasoft
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: MigracionERP2025!
    ports:
      - "5422:5432"
    volumes:
      - postgres_migration_data:/var/lib/postgresql/data/pgdata
    networks:
      - erp-migration-network

  sqlserver-origen:
    image: mcr.microsoft.com/mssql/server:2019-latest
    container_name: sqlserver-erp-origen
    environment:
      ACCEPT_EULA: "Y"
      MSSQL_SA_PASSWORD: "MigracionERP2025!"
      MSSQL_PID: "Express"
    ports:
      - "1433:1433"
    volumes:
      - sqlserver_data:/var/opt/mssql
    networks:
      - erp-migration-network

volumes:
  postgres_migration_data:
  sqlserver_data:

networks:
  erp-migration-network:
    driver: bridge
```

---

## 🚨 Resolución de Problemas

### Error: Contenedores no están corriendo
```bash
# Verificar estado
docker-compose ps

# Levantar servicios
docker-compose up -d

# Ver logs si hay problemas
docker-compose logs postgres-migration
docker-compose logs sqlserver-origen
```

### Error: No se puede conectar a SQL Server
```bash
# Test de conexión
docker exec sqlserver-erp-origen \
  /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "MigracionERP2025!" -C -Q "SELECT @@VERSION"

# Si falla, reiniciar contenedor
docker restart sqlserver-erp-origen
```

### Error: PostgreSQL no acepta conexiones
```bash
# Test de conexión
docker exec postgres-erp-migration \
  psql -U postgres -d erp_consolidasoft -c "SELECT version();"

# Ver logs PostgreSQL
docker logs postgres-erp-migration
```

### Error: Migración de datos falla
```bash
# Ver progreso detallado
docker exec postgres-erp-migration \
  psql -U postgres -d erp_consolidasoft \
  -c "SELECT * FROM erp_control.migration_status WHERE status = 'FAILED';"

# Reiniciar migración de tabla específica
python3 -c "
from migration.migrate_erp_data import ERPMigrator
migrator = ERPMigrator()
migrator.migrate_table_data('nombre_tabla')
"
```

---

## 📈 Métricas de Performance

### Baseline Esperado
| Métrica | SQL Server Actual | PostgreSQL Objetivo | Mejora |
|---------|-------------------|---------------------|--------|
| **Consultas/segundo** | ~1,000 | ~2,000 | 100% |
| **Tiempo consulta promedio** | 150ms | 75ms | 50% |
| **Uso de memoria** | 8GB | 4GB | 50% |
| **Costo mensual hosting** | $1,000 | $300 | 70% |

### Queries de Benchmark
```sql
-- Test performance consulta simple
EXPLAIN ANALYZE SELECT COUNT(*) FROM erp_main.clientes;

-- Test performance consulta compleja
EXPLAIN ANALYZE 
SELECT c.nombre, COUNT(f.factura) as total_facturas, SUM(f.total) as total_ventas
FROM erp_main.clientes c
LEFT JOIN erp_main.facturas f ON c.clientes = f.cliente_id
WHERE c.activo = true
GROUP BY c.clientes, c.nombre
ORDER BY total_ventas DESC
LIMIT 100;
```

---

## 🔄 Estrategia de Rollback

### Plan de Contingencia
1. **Backup completo** antes de iniciar
2. **Snapshots incrementales** por fase
3. **Scripts de reversión** automáticos
4. **Procedimiento de emergencia** documentado

### Comandos de Rollback
```bash
# 1. Detener migración en progreso
pkill -f "migrate_erp_data.py"

# 2. Backup de estado actual
docker exec postgres-erp-migration \
  pg_dump -U postgres erp_consolidasoft > rollback_backup_$(date +%Y%m%d_%H%M%S).sql

# 3. Restaurar snapshot anterior (si existe)
# docker exec -i postgres-erp-migration \
#   psql -U postgres -d erp_consolidasoft < backup_anterior.sql

# 4. Verificar integridad post-rollback
docker exec postgres-erp-migration \
  psql -U postgres -d erp_consolidasoft \
  -c "SELECT COUNT(*) FROM pg_tables WHERE schemaname = 'erp_main';"
```

---

## 🎯 Criterios de Éxito

### No Negociables
- ✅ **0% downtime** no planificado
- ✅ **100% integridad** de datos históricos
- ✅ **0 regresiones** funcionales
- ✅ **Performance** igual o superior al sistema actual

### Validaciones Críticas
```sql
-- 1. Integridad de conteos
SELECT 'SQL Server' as origen, COUNT(*) FROM [SQL_SERVER].dbo.clientes
UNION ALL
SELECT 'PostgreSQL', COUNT(*) FROM erp_main.clientes;

-- 2. Integridad referencial
SELECT COUNT(*) as registros_huerfanos
FROM erp_main.clientedatos cd
WHERE NOT EXISTS (SELECT 1 FROM erp_main.clientes c WHERE c.clientes = cd.cliente_id);

-- 3. Precisión numérica
SELECT 
    ABS(SUM(limite_credito) - (SELECT SUM(limite_credito) FROM [SQL_SERVER].dbo.clientes)) as diferencia_numerica
FROM erp_main.clientes;
```

---

## 📞 Soporte y Contacto

### En Caso de Problemas Críticos
1. **Revisar logs:** `migration_complete_*.log`
2. **Verificar estado:** Tablas de control en `erp_control`
3. **Validar conexiones:** `docker-compose ps`
4. **Ejecutar diagnósticos:** Scripts de validación incluidos

### Información Técnica
- **Estrategia:** Strangler Fig Pattern
- **Método:** Migración gradual sin downtime
- **Tecnologías:** Python 3, PostgreSQL 15, SQL Server 2019
- **Contenedores:** Docker Compose

---

## 🏆 Estado del Proyecto

### ✅ Completado
- [x] Análisis completo de 559 tablas
- [x] Mapeo de 9,964 campos
- [x] Identificación de campos problemáticos
- [x] Generador automático de schema
- [x] Migrador de datos con validación
- [x] Scripts de automatización completa
- [x] Documentación técnica

### 🔄 En Progreso
- [ ] Migración de 15 stored procedures
- [ ] Testing con volumen completo de datos
- [ ] Optimización de queries específicas
- [ ] Configuración de replicación

### 📋 Pendiente
- [ ] Migración a producción
- [ ] Capacitación de usuarios
- [ ] Monitoreo en tiempo real
- [ ] Integración con sistemas de IA

---

**¡El schema completo de 559 tablas está listo para ejecución!** 

🚀 **Ejecutar ahora:** `./migration/run_complete_migration.sh`
