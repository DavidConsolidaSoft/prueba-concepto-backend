#!/usr/bin/env python3
"""
schema_cli.py - Herramienta de línea de comandos para gestionar el esquema documentado de la base de datos

Esta herramienta permite extraer, documentar, buscar y mantener la documentación del esquema
de base de datos, optimizando el rendimiento de las consultas en lenguaje natural.

Uso:
  python schema_cli.py extract              # Extrae el esquema completo de la BD
  python schema_cli.py list                 # Lista todas las tablas documentadas
  python schema_cli.py view <tabla>         # Muestra detalles de una tabla
  python schema_cli.py import <archivo.json> # Importa documentación desde JSON
  python schema_cli.py search "consulta"    # Busca tablas relevantes para una consulta
  python schema_cli.py mark-important <tabla> # Marca una tabla como importante
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any
from dotenv import load_dotenv

# Asegurarse de que podemos importar desde el directorio raíz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar servicio de esquema
try:
    from app.api.v1.routers.ai.schema_metadata_service import SchemaMetadataService
except ImportError:
    print("Error: No se pudo importar SchemaMetadataService.")
    print("Asegúrate de ejecutar este script desde el directorio raíz del proyecto.")
    sys.exit(1)

# Cargar variables de entorno
load_dotenv()

def extract_schema(args):
    """Extrae el esquema de la base de datos."""
    schema_service = SchemaMetadataService()
    
    print("Extrayendo esquema de la base de datos...")
    table_count = schema_service.extract_and_store_schema(force_update=args.force)
    
    if table_count > 0:
        print(f"✅ Esquema extraído correctamente: {table_count} tablas procesadas")
    else:
        print("❌ Error al extraer esquema o no se encontraron tablas")

def list_tables(args):
    """Lista todas las tablas documentadas."""
    schema_service = SchemaMetadataService()
    
    if args.important:
        tables = schema_service.get_important_tables()
        print(f"\n📊 Tablas importantes documentadas ({len(tables)}):\n")
    else:
        tables = schema_service.get_all_tables()
        print(f"\n📊 Tablas documentadas ({len(tables)}):\n")
    
    if not tables:
        print("No hay tablas documentadas.")
        return
    
    # Obtener detalles de cada tabla
    for table_name in sorted(tables):
        table_data = schema_service.get_table_schema(table_name)
        if table_data:
            purpose = table_data.get("proposito", "Sin descripción")
            # Truncar descripción larga
            if len(purpose) > 70:
                purpose = purpose[:67] + "..."
            
            columns_count = len(table_data.get("columnas", []))
            relations_count = len(table_data.get("relaciones", []))
            
            print(f"- {table_name} ({columns_count} columnas, {relations_count} relaciones)")
            print(f"  {purpose}")
    
    print("\nUsa 'python schema_cli.py view <tabla>' para ver detalles de una tabla específica.")

def view_table(args):
    """Muestra detalles de una tabla específica."""
    schema_service = SchemaMetadataService()
    
    table_data = schema_service.get_table_schema(args.table)
    
    if not table_data:
        print(f"❌ La tabla '{args.table}' no está documentada.")
        return
    
    print(f"\n📋 Detalles de la tabla: {args.table}")
    print(f"🔍 Propósito: {table_data.get('proposito', 'Sin descripción')}")
    
    # Comprobar si es importante
    important_tables = schema_service.get_important_tables()
    is_important = args.table in important_tables
    print(f"⭐ Importante: {'Sí' if is_important else 'No'}")
    
    # Mostrar columnas
    columns = table_data.get("columnas", [])
    print(f"\n📊 Columnas ({len(columns)}):")
    
    for col in columns:
        col_type = col.get("type", "desconocido")
        col_desc = col.get("description", "Sin descripción")
        is_key = col.get("is_key", False)
        key_mark = "🔑 " if is_key else ""
        
        print(f"- {key_mark}{col['name']} ({col_type})")
        print(f"  {col_desc}")
    
    # Mostrar relaciones
    relations = table_data.get("relaciones", [])
    if relations:
        print(f"\n🔗 Relaciones ({len(relations)}):")
        
        for rel in relations:
            rel_type = rel.get("tipo_relacion", "desconocida")
            rel_table = rel.get("tabla_relacionada", "desconocida")
            local_col = rel.get("columna_local", "")
            external_col = rel.get("columna_externa", "")
            
            print(f"- {rel_type} con {rel_table}")
            print(f"  {local_col} -> {external_col}")

def import_table(args):
    """Importa o actualiza documentación de tabla desde un archivo JSON."""
    schema_service = SchemaMetadataService()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            table_data = json.load(f)
        
        # Verificar formato
        if "nombre_tabla" not in table_data or "columnas" not in table_data or "proposito" not in table_data:
            print("❌ El archivo JSON no tiene el formato correcto.")
            print("Debe contener al menos 'nombre_tabla', 'proposito' y 'columnas'.")
            return
        
        table_name = table_data["nombre_tabla"]
        is_important = table_data.get("is_important", False)
        
        # Actualizar tabla
        success = schema_service.update_table_metadata(
            table_name=table_name,
            purpose=table_data["proposito"],
            column_descriptions=table_data["columnas"],
            is_important=is_important
        )
        
        if success:
            print(f"✅ Tabla '{table_name}' importada correctamente.")
            if is_important:
                print("⭐ La tabla ha sido marcada como importante.")
        else:
            print(f"❌ Error al importar tabla '{table_name}'.")
        
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{args.file}' no existe.")
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo '{args.file}' no es un JSON válido.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def search_tables(args):
    """Busca tablas relevantes para una consulta en lenguaje natural."""
    schema_service = SchemaMetadataService()
    
    print(f"🔍 Buscando tablas relevantes para: \"{args.query}\"")
    
    relevant_tables = schema_service.find_relevant_tables(args.query, top_k=args.limit)
    
    if not relevant_tables:
        print("❌ No se encontraron tablas relevantes para esta consulta.")
        return
    
    print(f"\n📊 Tablas más relevantes ({len(relevant_tables)}):\n")
    
    for i, table in enumerate(relevant_tables, 1):
        table_name = table["nombre_tabla"]
        similarity = table["similarity"]
        purpose = table["proposito"]
        
        # Truncar descripción larga
        if len(purpose) > 70:
            purpose = purpose[:67] + "..."
        
        print(f"{i}. {table_name} ({similarity:.4f})")
        print(f"   {purpose}")
    
    if args.show_context:
        print("\n📝 Contexto que se incluiría en el prompt:\n")
        context = schema_service.generate_schema_context(args.query)
        print(context)

def mark_important(args):
    """Marca una tabla como importante."""
    schema_service = SchemaMetadataService()
    
    table_data = schema_service.get_table_schema(args.table)
    
    if not table_data:
        print(f"❌ La tabla '{args.table}' no está documentada.")
        return
    
    success = schema_service.mark_table_as_important(args.table)
    
    if success:
        print(f"⭐ Tabla '{args.table}' marcada como importante.")
    else:
        print(f"❌ Error al marcar la tabla '{args.table}' como importante.")

def export_table(args):
    """Exporta la documentación de una tabla a un archivo JSON."""
    schema_service = SchemaMetadataService()
    
    table_data = schema_service.get_table_schema(args.table)
    
    if not table_data:
        print(f"❌ La tabla '{args.table}' no está documentada.")
        return
    
    # Comprobar si es importante
    important_tables = schema_service.get_important_tables()
    is_important = args.table in important_tables
    
    # Añadir flag de importante
    table_data["is_important"] = is_important
    
    # Determinar nombre de archivo
    if args.output:
        filename = args.output
    else:
        filename = f"{args.table}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(table_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Tabla '{args.table}' exportada a '{filename}'.")
    except Exception as e:
        print(f"❌ Error al exportar tabla: {str(e)}")

def export_all(args):
    """Exporta todas las tablas documentadas a archivos JSON."""
    schema_service = SchemaMetadataService()
    
    if args.important:
        tables = schema_service.get_important_tables()
        print(f"Exportando {len(tables)} tablas importantes...")
    else:
        tables = schema_service.get_all_tables()
        print(f"Exportando {len(tables)} tablas...")
    
    if not tables:
        print("❌ No hay tablas para exportar.")
        return
    
    # Crear directorio si no existe
    output_dir = args.directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Lista de tablas importantes
    important_tables = schema_service.get_important_tables()
    
    # Exportar cada tabla
    success_count = 0
    for table_name in tables:
        try:
            table_data = schema_service.get_table_schema(table_name)
            
            if table_data:
                # Añadir flag de importante
                is_important = table_name in important_tables
                table_data["is_important"] = is_important
                
                # Guardar archivo
                filename = os.path.join(output_dir, f"{table_name}.json")
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(table_data, f, indent=2, ensure_ascii=False)
                
                success_count += 1
                print(f"✅ Exportada: {table_name}")
        except Exception as e:
            print(f"❌ Error al exportar '{table_name}': {str(e)}")
    
    print(f"\n📦 Exportación completada: {success_count} de {len(tables)} tablas exportadas a '{output_dir}'")

def main():
    """Función principal que procesa los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Herramienta para gestionar el esquema documentado de la base de datos"
    )
    
    subparsers = parser.add_subparsers(
        dest="command", 
        help="Comando a ejecutar",
        required=True
    )
    
    # Comando extract
    extract_parser = subparsers.add_parser(
        "extract", 
        help="Extrae el esquema de la base de datos"
    )
    extract_parser.add_argument(
        "-f", "--force", 
        action="store_true",
        help="Fuerza la actualización aunque exista un esquema reciente"
    )
    extract_parser.set_defaults(func=extract_schema)
    
    # Comando list
    list_parser = subparsers.add_parser(
        "list", 
        help="Lista todas las tablas documentadas"
    )
    list_parser.add_argument(
        "-i", "--important",
        action="store_true",
        help="Muestra solo tablas marcadas como importantes"
    )
    list_parser.set_defaults(func=list_tables)
    
    # Comando view
    view_parser = subparsers.add_parser(
        "view", 
        help="Muestra detalles de una tabla específica"
    )
    view_parser.add_argument(
        "table",
        help="Nombre de la tabla a visualizar"
    )
    view_parser.set_defaults(func=view_table)
    
    # Comando import
    import_parser = subparsers.add_parser(
        "import", 
        help="Importa documentación desde un archivo JSON"
    )
    import_parser.add_argument(
        "file",
        help="Ruta al archivo JSON"
    )
    import_parser.set_defaults(func=import_table)
    
    # Comando search
    search_parser = subparsers.add_parser(
        "search", 
        help="Busca tablas relevantes para una consulta"
    )
    search_parser.add_argument(
        "query",
        help="Consulta en lenguaje natural"
    )
    search_parser.add_argument(
        "-l", "--limit",
        type=int,
        default=5,
        help="Número máximo de tablas a mostrar"
    )
    search_parser.add_argument(
        "-c", "--show-context",
        action="store_true",
        help="Muestra el contexto que se incluiría en el prompt"
    )
    search_parser.set_defaults(func=search_tables)
    
    # Comando mark-important
    mark_parser = subparsers.add_parser(
        "mark-important", 
        help="Marca una tabla como importante"
    )
    mark_parser.add_argument(
        "table",
        help="Nombre de la tabla a marcar como importante"
    )
    mark_parser.set_defaults(func=mark_important)
    
    # Comando export
    export_parser = subparsers.add_parser(
        "export", 
        help="Exporta una tabla a un archivo JSON"
    )
    export_parser.add_argument(
        "table",
        help="Nombre de la tabla a exportar"
    )
    export_parser.add_argument(
        "-o", "--output",
        help="Nombre del archivo de salida"
    )
    export_parser.set_defaults(func=export_table)
    
    # Comando export-all
    export_all_parser = subparsers.add_parser(
        "export-all", 
        help="Exporta todas las tablas a archivos JSON"
    )
    export_all_parser.add_argument(
        "directory",
        help="Directorio donde guardar los archivos"
    )
    export_all_parser.add_argument(
        "-i", "--important",
        action="store_true",
        help="Exporta solo tablas marcadas como importantes"
    )
    export_all_parser.set_defaults(func=export_all)
    
    # Parsear argumentos y ejecutar función
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()