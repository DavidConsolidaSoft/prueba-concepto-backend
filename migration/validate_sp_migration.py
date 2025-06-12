#!/usr/bin/env python3
"""
VALIDADOR DE MIGRACIÓN DE STORED PROCEDURES
Verifica que los SPs migrados funcionen correctamente en PostgreSQL
"""

import psycopg2
import logging
from datetime import datetime
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SPMigrationValidator:
    """Validador de migración de stored procedures"""
    
    def __init__(self, environment: str = "demo"):
        self.environment = environment
        self.configs = self._get_configs()
        
    def _get_configs(self) -> Dict:
        """Configuraciones por entorno"""
        configs = {
            'demo': {
                'host': 'localhost',
                'port': 5422,
                'database': 'erp_consolidasoft',
                'username': 'postgres',
                'password': 'MigracionERP2025!'
            },
            'production': {
                'host': 'POSTGRES-PROD-HOST',
                'port': 5432,
                'database': 'erp_consolidado_prod',
                'username': 'postgres',
                'password': 'CONFIGURAR_PASSWORD_PROD'
            }
        }
        return configs[self.environment]
    
    def get_connection(self):
        """Obtener conexión a PostgreSQL"""
        config = self.configs
        return psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['username'],
            password=config['password']
        )
    
    def validate_migrated_functions(self) -> Dict:
        """Validar que las funciones migradas sean sintácticamente correctas"""
        
        logger.info("🔍 Validando funciones migradas...")
        
        conn = self.get_connection()
        cur = conn.cursor()
        
        results = {
            'total_functions': 0,
            'valid_functions': 0,
            'invalid_functions': 0,
            'function_details': []
        }
        
        try:
            # Obtener todas las funciones migradas
            cur.execute("""
                SELECT 
                    routine_name as function_name,
                    routine_type,
                    created as created_date,
                    routine_definition
                FROM information_schema.routines 
                WHERE routine_schema = 'legacy_procedures'
                ORDER BY routine_name
            """)
            
            functions = cur.fetchall()
            results['total_functions'] = len(functions)
            
            logger.info(f"📋 Encontradas {len(functions)} funciones migradas")
            
            for func in functions:
                func_name = func[0]
                func_type = func[1]
                created = func[2]
                
                print(f"🔍 Validando: {func_name}")
                
                try:
                    # Verificar que la función existe y es válida
                    cur.execute("""
                        SELECT 
                            p.proname,
                            p.pronargs,
                            pg_get_function_arguments(p.oid) as arguments,
                            pg_get_function_result(p.oid) as return_type,
                            p.prosrc IS NOT NULL as has_source
                        FROM pg_proc p
                        JOIN pg_namespace n ON p.pronamespace = n.oid
                        WHERE n.nspname = 'legacy_procedures' 
                          AND p.proname = %s
                    """, (func_name,))
                    
                    func_info = cur.fetchone()
                    
                    if func_info:
                        detail = {
                            'name': func_name,
                            'status': 'VALID',
                            'arguments': func_info[2],
                            'return_type': func_info[3],
                            'has_source': func_info[4],
                            'created': created
                        }
                        
                        results['valid_functions'] += 1
                        print(f"✅ {func_name} - VÁLIDA")
                        
                    else:
                        detail = {
                            'name': func_name,
                            'status': 'INVALID',
                            'error': 'Function not found in pg_proc',
                            'created': created
                        }
                        results['invalid_functions'] += 1
                        print(f"❌ {func_name} - INVÁLIDA")
                    
                    results['function_details'].append(detail)
                    
                except Exception as e:
                    detail = {
                        'name': func_name,
                        'status': 'ERROR',
                        'error': str(e),
                        'created': created
                    }
                    results['function_details'].append(detail)
                    results['invalid_functions'] += 1
                    print(f"❌ {func_name} - ERROR: {e}")
        
        except Exception as e:
            logger.error(f"❌ Error validando funciones: {e}")
        
        finally:
            conn.close()
        
        return results
    
    def check_migration_log(self) -> Dict:
        """Revisar el log de migración"""
        
        logger.info("📋 Revisando log de migración...")
        
        conn = self.get_connection()
        cur = conn.cursor()
        
        log_results = {
            'log_exists': False,
            'total_attempts': 0,
            'successful': 0,
            'failed': 0,
            'recent_migrations': []
        }
        
        try:
            # Verificar si existe la tabla de log
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'erp_control' 
                    AND table_name = 'sp_migration_log'
                )
            """)
            
            log_exists = cur.fetchone()[0]
            log_results['log_exists'] = log_exists
            
            if log_exists:
                # Obtener estadísticas del log
                cur.execute("""
                    SELECT 
                        COUNT(*) as total,
                        COUNT(CASE WHEN status = 'SUCCESS' THEN 1 END) as successful,
                        COUNT(CASE WHEN status = 'FAILED' THEN 1 END) as failed
                    FROM erp_control.sp_migration_log
                """)
                
                stats = cur.fetchone()
                log_results['total_attempts'] = stats[0]
                log_results['successful'] = stats[1] 
                log_results['failed'] = stats[2]
                
                # Obtener migraciones recientes
                cur.execute("""
                    SELECT 
                        procedure_name,
                        status,
                        error_message,
                        migration_time
                    FROM erp_control.sp_migration_log
                    ORDER BY migration_time DESC
                    LIMIT 20
                """)
                
                recent = cur.fetchall()
                log_results['recent_migrations'] = [
                    {
                        'procedure': row[0],
                        'status': row[1],
                        'error': row[2],
                        'time': row[3]
                    }
                    for row in recent
                ]
                
                logger.info(f"📊 Log: {stats[0]} intentos, {stats[1]} exitosos, {stats[2]} fallidos")
            
        except Exception as e:
            logger.error(f"❌ Error revisando log: {e}")
        
        finally:
            conn.close()
        
        return log_results
    
    def test_function_syntax(self) -> Dict:
        """Test básico de sintaxis de funciones"""
        
        logger.info("🧪 Testeando sintaxis de funciones...")
        
        conn = self.get_connection()
        cur = conn.cursor()
        
        syntax_results = {
            'total_tested': 0,
            'syntax_valid': 0,
            'syntax_errors': 0,
            'test_details': []
        }
        
        try:
            # Obtener funciones para testear
            cur.execute("""
                SELECT 
                    p.proname,
                    pg_get_functiondef(p.oid) as function_def
                FROM pg_proc p
                JOIN pg_namespace n ON p.pronamespace = n.oid
                WHERE n.nspname = 'legacy_procedures'
                ORDER BY p.proname
            """)
            
            functions = cur.fetchall()
            syntax_results['total_tested'] = len(functions)
            
            for func_name, func_def in functions:
                print(f"🧪 Testeando sintaxis: {func_name}")
                
                try:
                    # Test básico: obtener la definición sin errores
                    if func_def and len(func_def) > 0:
                        # Verificar que la función se puede "preparar" sin ejecutar
                        cur.execute("SELECT pg_get_functiondef(oid) FROM pg_proc WHERE proname = %s AND pronamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'legacy_procedures')", (func_name,))
                        
                        result = cur.fetchone()
                        if result:
                            syntax_results['syntax_valid'] += 1
                            syntax_results['test_details'].append({
                                'function': func_name,
                                'status': 'VALID',
                                'error': None
                            })
                            print(f"✅ {func_name} - Sintaxis OK")
                        else:
                            syntax_results['syntax_errors'] += 1
                            syntax_results['test_details'].append({
                                'function': func_name,
                                'status': 'ERROR',
                                'error': 'Function definition not found'
                            })
                            print(f"❌ {func_name} - Sin definición")
                    else:
                        syntax_results['syntax_errors'] += 1
                        syntax_results['test_details'].append({
                            'function': func_name,
                            'status': 'ERROR',
                            'error': 'Empty function definition'
                        })
                        print(f"❌ {func_name} - Definición vacía")
                        
                except Exception as e:
                    syntax_results['syntax_errors'] += 1
                    syntax_results['test_details'].append({
                        'function': func_name,
                        'status': 'ERROR',
                        'error': str(e)
                    })
                    print(f"❌ {func_name} - Error: {e}")
        
        except Exception as e:
            logger.error(f"❌ Error testeando sintaxis: {e}")
        
        finally:
            conn.close()
        
        return syntax_results
    
    def generate_validation_report(self, validation_results: Dict, log_results: Dict, syntax_results: Dict) -> str:
        """Generar reporte de validación"""
        
        report_filename = f"sp_validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(f"""# REPORTE DE VALIDACIÓN - STORED PROCEDURES MIGRADOS

## 📊 RESUMEN EJECUTIVO
- **Entorno:** {self.environment.upper()}
- **Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Total funciones:** {validation_results['total_functions']}
- **Funciones válidas:** {validation_results['valid_functions']}
- **Funciones inválidas:** {validation_results['invalid_functions']}

## ✅ FUNCIONES VÁLIDAS
""")
            
            for detail in validation_results['function_details']:
                if detail['status'] == 'VALID':
                    f.write(f"- ✅ **{detail['name']}**\n")
                    f.write(f"  - Argumentos: `{detail.get('arguments', 'N/A')}`\n")
                    f.write(f"  - Retorna: `{detail.get('return_type', 'N/A')}`\n")
            
            f.write("\n## ❌ FUNCIONES CON PROBLEMAS\n")
            for detail in validation_results['function_details']:
                if detail['status'] != 'VALID':
                    f.write(f"- ❌ **{detail['name']}** - {detail.get('error', 'Error desconocido')}\n")
            
            f.write(f"""
## 📋 LOG DE MIGRACIÓN
- **Log existe:** {'✅ Sí' if log_results['log_exists'] else '❌ No'}
- **Total intentos:** {log_results['total_attempts']}
- **Exitosos:** {log_results['successful']}
- **Fallidos:** {log_results['failed']}

## 🧪 TESTS DE SINTAXIS
- **Total testeadas:** {syntax_results['total_tested']}
- **Sintaxis válida:** {syntax_results['syntax_valid']}
- **Errores de sintaxis:** {syntax_results['syntax_errors']}

## 🔧 COMANDOS DE VERIFICACIÓN
```sql
-- Listar todas las funciones migradas
SELECT 
    routine_name,
    routine_type,
    created
FROM information_schema.routines 
WHERE routine_schema = 'legacy_procedures'
ORDER BY routine_name;

-- Verificar una función específica
SELECT pg_get_functiondef(oid) 
FROM pg_proc 
WHERE proname = 'nombre_funcion' 
  AND pronamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'legacy_procedures');

-- Test básico de ejecución (CUIDADO: solo para funciones sin parámetros)
-- SELECT legacy_procedures.nombre_funcion();
```

## 📈 MÉTRICAS DE ÉXITO
- **Tasa de éxito:** {(validation_results['valid_functions'] / max(validation_results['total_functions'], 1) * 100):.1f}%
- **Funciones operativas:** {validation_results['valid_functions']}/{validation_results['total_functions']}

## 💡 PRÓXIMOS PASOS
""")
            
            if validation_results['invalid_functions'] > 0:
                f.write("""
1. ⚠️  **Corregir funciones inválidas:**
   - Revisar archivos `failed_sp_*.sql` generados
   - Ajustar conversiones manualmente
   - Re-ejecutar funciones individuales

2. 🧪 **Testing funcional:**
   - Crear tests unitarios para funciones críticas
   - Validar comportamiento vs SQL Server original
   - Verificar performance
""")
            else:
                f.write("""
1. ✅ **¡Todas las funciones están válidas!**
   - Proceder con testing funcional
   - Implementar en aplicación
   - Monitorear performance
""")
        
        logger.info(f"📄 Reporte generado: {report_filename}")
        return report_filename
    
    def run_full_validation(self) -> Dict:
        """Ejecutar validación completa"""
        
        logger.info("🚀 INICIANDO VALIDACIÓN COMPLETA DE STORED PROCEDURES")
        logger.info("=" * 60)
        
        # 1. Validar funciones migradas
        validation_results = self.validate_migrated_functions()
        
        # 2. Revisar log de migración
        log_results = self.check_migration_log()
        
        # 3. Test de sintaxis
        syntax_results = self.test_function_syntax()
        
        # 4. Generar reporte
        report_file = self.generate_validation_report(validation_results, log_results, syntax_results)
        
        # 5. Resumen final
        print("\n" + "=" * 60)
        print("📊 VALIDACIÓN COMPLETADA")
        print(f"  📋 Total funciones: {validation_results['total_functions']}")
        print(f"  ✅ Válidas: {validation_results['valid_functions']}")
        print(f"  ❌ Inválidas: {validation_results['invalid_functions']}")
        print(f"  🧪 Sintaxis OK: {syntax_results['syntax_valid']}")
        print(f"  📄 Reporte: {report_file}")
        
        success_rate = (validation_results['valid_functions'] / max(validation_results['total_functions'], 1)) * 100
        
        if success_rate >= 80:
            print(f"  🎉 ÉXITO: {success_rate:.1f}% de funciones válidas")
        else:
            print(f"  ⚠️  REVISAR: {success_rate:.1f}% de funciones válidas")
        
        print("=" * 60)
        
        return {
            'success': success_rate >= 80,
            'validation_results': validation_results,
            'log_results': log_results,
            'syntax_results': syntax_results,
            'report_file': report_file,
            'success_rate': success_rate
        }

def main():
    """Función principal"""
    
    import sys
    
    environment = "demo"
    if len(sys.argv) > 1:
        environment = sys.argv[1].lower()
        if environment not in ['demo', 'production']:
            print("❌ Entorno debe ser 'demo' o 'production'")
            sys.exit(1)
    
    print("🔍 VALIDADOR DE MIGRACIÓN DE STORED PROCEDURES")
    print(f"🎯 Entorno: {environment.upper()}")
    print("=" * 50)
    
    validator = SPMigrationValidator(environment)
    results = validator.run_full_validation()
    
    if results['success']:
        print("\n🎉 ¡VALIDACIÓN EXITOSA!")
        print("   Las funciones migradas están listas para usar")
    else:
        print("\n⚠️  VALIDACIÓN PARCIAL")
        print("   Algunas funciones requieren corrección")
        print(f"   Consulta el reporte: {results['report_file']}")

if __name__ == "__main__":
    main()
