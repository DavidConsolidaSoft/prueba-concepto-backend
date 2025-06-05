from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_, func
from typing import List, Optional
from app.models.dbo.vendedor import Vendedor
from app.models.dbo.empresa import Empresa

class VendedoresServiceORM:
    def __init__(self, db: Session):
        self.db = db
        # Deshabilitar la carga automática de relaciones
        self.db.autoflush = False
    
    def get_vendedores_by_empresa(self, empresa_id: int, activo: Optional[bool] = None) -> List[Vendedor]:
        """
        Obtiene todos los vendedores de una empresa específica, con opción de filtrar por estado activo.
        """
        query = self.db.query(Vendedor).filter(Vendedor.empresa == empresa_id)
        
        if activo is not None:
            query = query.filter(Vendedor.activo == activo)
        
        return query.all()
    
    def get_vendedor_by_id(self, vendedor_id: int, empresa_id: int) -> Optional[Vendedor]:
        """
        Obtiene un vendedor específico por su ID, dentro de una empresa específica.
        """
        query = self.db.query(Vendedor).filter(
            Vendedor.vendedor == vendedor_id,
            Vendedor.empresa == empresa_id
        )
        
        return query.first()
    
    def get_empresas_with_vendedores(self) -> List[Empresa]:
        """
        Obtiene la lista de empresas que tienen vendedores asignados.
        """
        # Consulta para obtener empresas que tienen al menos un vendedor
        query = self.db.query(Empresa).join(
            Vendedor,
            Empresa.empresa == Vendedor.empresa
        ).distinct()
        
        return query.all()