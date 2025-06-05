# app/utils/comment_all_relationships.py
"""
Script para comentar TODAS las relaciones en TODOS los modelos
"""
import os
import re

def comment_all_relationships(models_dir='app/models/dbo'):
    """
    Comenta todas las relaciones en todos los archivos de modelos
    """
    fixed_count = 0
    
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(models_dir, filename)
            modified = False
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Comentar import de relationship
                if 'from sqlalchemy.orm import relationship' in content:
                    content = re.sub(
                        r'from sqlalchemy\.orm import relationship',
                        '# from sqlalchemy.orm import relationship  # Comentado temporalmente',
                        content
                    )
                    modified = True
                
                # Encontrar y comentar todas las relaciones
                relationship_pattern = r'(\s*)(\w+)\s*=\s*relationship\([^)]+\)'
                matches = list(re.finditer(relationship_pattern, content))
                
                for match in reversed(matches):  # Procesar de atrás hacia adelante
                    indent = match.group(1)
                    line = match.group(0)
                    # Reemplazar la línea completa con una versión comentada
                    commented_line = f'{indent}# {line.strip()}  # Comentado automáticamente'
                    content = content[:match.start()] + commented_line + content[match.end():]
                    modified = True
                
                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_count += 1
                    print(f"✓ Arreglado: {filename}")
                    
            except Exception as e:
                print(f"❌ Error en {filename}: {str(e)}")
    
    print(f"\nTotal de archivos modificados: {fixed_count}")
    return fixed_count

def verify_models(models_dir='app/models/dbo'):
    """
    Verifica que no queden relaciones sin comentar
    """
    problems = []
    
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(models_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Buscar relaciones no comentadas
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if 'relationship(' in line and not line.strip().startswith('#'):
                        problems.append(f"{filename}:{i+1} - {line.strip()}")
                
            except Exception as e:
                problems.append(f"{filename}: Error al leer - {str(e)}")
    
    if problems:
        print("\n⚠️  Relaciones no comentadas encontradas:")
        for problem in problems:
            print(f"  {problem}")
    else:
        print("\n✅ Todas las relaciones están comentadas correctamente")
    
    return len(problems) == 0

if __name__ == "__main__":
    print("=== Comentando TODAS las relaciones en los modelos ===")
    
    # Comentar todas las relaciones
    count = comment_all_relationships()
    
    # Verificar que todo esté bien
    print("\n=== Verificando modelos ===")
    if verify_models():
        print("\n🎉 ¡Éxito! Todos los modelos están listos para usar sin relaciones.")
        print("Reinicia el servidor con: uvicorn main:app --reload")
    else:
        print("\n⚠️  Aún hay problemas. Revisa manualmente los archivos indicados.")