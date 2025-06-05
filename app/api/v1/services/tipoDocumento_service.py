from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, and_
from typing import List, Optional, Dict, Any
from app.models.dbo.tipomov import TipoMov
from app.models.dbo.pais import Pais
from app.models.dbo.empresa import Empresa
from app.models.dbo.caja import Caja
from app.models.dbo.condpago import CondPago

class TipoDocumentoServiceORM:
    def __init__(self, db: Session):
        self.db = db
        # Deshabilitar la carga automática de relaciones
        self.db.autoflush = False
   
    def get_documentos_by_empresa(
        self,
        empresa_id: int,
        activo: Optional[bool] = None,
        filtro_tipo: Optional[str] = None
    ) -> List[TipoMov]:
        """
        Obtiene todos los tipos de documento (movimiento) de una empresa específica.
       
        Parámetros:
        - empresa_id: ID de la empresa
        - activo: Filtrar por documentos activos/inactivos
        - filtro_tipo: Filtrar por tipo específico ('factura', 'notacred', 'compra', etc.)
        """
        query = self.db.query(TipoMov).filter(TipoMov.empresa == empresa_id)
       
        # Filtrar por estado activo si se especifica
        if activo is not None:
            query = query.filter(TipoMov.activo == activo)
       
        # Aplicar filtro por tipo de documento
        if filtro_tipo:
            if filtro_tipo == 'factura':
                query = query.filter(TipoMov.factura == True)
            elif filtro_tipo == 'notacred':
                query = query.filter(TipoMov.notacred == True)
            elif filtro_tipo == 'compra':
                query = query.filter(TipoMov.compra == True)
            elif filtro_tipo == 'anticipo':
                query = query.filter(TipoMov.ANTICIPO == True)
            elif filtro_tipo == 'notadebito':
                query = query.filter(TipoMov.notadebito == True)
            elif filtro_tipo == 'pedido':
                query = query.filter(TipoMov.pedido == True)
            elif filtro_tipo == 'inventario':
                query = query.filter(TipoMov.inventario == True)
       
        # Ordenar por código
        query = query.order_by(TipoMov.tipomov)
       
        return query.all()
   
    def get_documento_by_id(self, tipomov_id: int, empresa_id: int) -> Optional[TipoMov]:
        """
        Obtiene un tipo de documento específico por su ID, dentro de una empresa específica.
        """
        query = self.db.query(TipoMov).filter(
            TipoMov.tipomov == tipomov_id,
            TipoMov.empresa == empresa_id
        )
       
        return query.first()
   
    def get_tipos_documento(self, empresa_id: int) -> dict:
        """
        Obtiene categorías de tipos de documento para una empresa específica.
        Retorna un diccionario con diferentes listas de tipos de documento.
        """
        facturas = self.db.query(TipoMov).filter(
            TipoMov.empresa == empresa_id,
            TipoMov.factura == True,
            TipoMov.activo == True
        ).order_by(TipoMov.ntipomov).all()
       
        notas_credito = self.db.query(TipoMov).filter(
            TipoMov.empresa == empresa_id,
            TipoMov.notacred == True,
            TipoMov.activo == True
        ).order_by(TipoMov.ntipomov).all()
       
        compras = self.db.query(TipoMov).filter(
            TipoMov.empresa == empresa_id,
            TipoMov.compra == True,
            TipoMov.activo == True
        ).order_by(TipoMov.ntipomov).all()
       
        inventario = self.db.query(TipoMov).filter(
            TipoMov.empresa == empresa_id,
            TipoMov.inventario == True,
            TipoMov.activo == True
        ).order_by(TipoMov.ntipomov).all()
       
        pedidos = self.db.query(TipoMov).filter(
            TipoMov.empresa == empresa_id,
            TipoMov.pedido == True,
            TipoMov.activo == True
        ).order_by(TipoMov.ntipomov).all()
       
        return {
            "facturas": facturas,
            "notas_credito": notas_credito,
            "compras": compras,
            "inventario": inventario,
            "pedidos": pedidos
        }

    def get_facturas_by_empresa_pais(
        self,
        empresa_id: int,
        caja_id: int = None
    ) -> List[Dict[str, Any]]:
        """
        Replica la lógica original de la consulta SQL para obtener documentos de factura
        según el país y configuración de tiquetes.
        
        Parámetros:
        - empresa_id: ID de la empresa
        - caja_id: ID de la caja para determinar configuración de tiquetes
        """
        try:
            # Obtener información de país
            subquery_el_salvador = self.db.query(Pais.elsalvador).join(
                Empresa, Empresa.pais == Pais.pais
            ).filter(
                Pais.usuario == -100,
                Empresa.empresa == empresa_id
            ).scalar()
            
            es_el_salvador = 1 if subquery_el_salvador else 0
            
            subquery_guatemala = self.db.query(Pais.guatemala).join(
                Empresa, Empresa.pais == Pais.pais
            ).filter(
                Pais.usuario == -100,
                Empresa.empresa == empresa_id
            ).scalar()
            
            es_guatemala = 1 if subquery_guatemala else 0
            
            # Obtener configuración de tiquete si se proporciona caja_id
            tiquet = None
            if caja_id:
                tiquet = self.db.query(Caja.maximot).filter(
                    Caja.caja == caja_id,
                    Caja.empresa == empresa_id
                ).scalar() or 0
            
            # Consulta base
            query = self.db.query(
                TipoMov.ntipomov, 
                TipoMov.tipomov, 
                TipoMov.correl, 
                TipoMov.preferido,
                TipoMov.coniva, 
                TipoMov.tiquet, 
                TipoMov.nlineasmax, 
                TipoMov.informe,
                TipoMov.notacred, 
                TipoMov.exportacion, 
                TipoMov.noaplicariva, 
                CondPago.contado,
                TipoMov.prodprec, 
                TipoMov.condpago, 
                TipoMov.norestariva, 
                TipoMov.docunico,
                TipoMov.ptovta, 
                TipoMov.efectivo, 
                TipoMov.qmin, 
                TipoMov.correlpropio, 
                TipoMov.remision
            ).outerjoin(
                CondPago, CondPago.condpago == TipoMov.condpago
            ).filter(
                TipoMov.factura == True,
                TipoMov.activo == True,
                or_(TipoMov.ofactura == 0, TipoMov.ofactura != None),
                TipoMov.notacred == 0,
                TipoMov.empresa == empresa_id
            )
            
            # Aplicar ordenamiento según el país y configuración
            if es_el_salvador == 1:
                if tiquet == 1:
                    query = query.order_by(
                        TipoMov.exportacion,
                        TipoMov.noaplicariva,
                        TipoMov.tiquet.desc(),
                        TipoMov.preferido.desc(),
                        TipoMov.ntipomov
                    )
                else:
                    query = query.order_by(
                        TipoMov.exportacion,
                        TipoMov.preferido.desc(),
                        TipoMov.noaplicariva,
                        TipoMov.factura.desc(),
                        TipoMov.ntipomov
                    )
            elif es_guatemala == 1:
                query = query.order_by(
                    TipoMov.exportacion,
                    TipoMov.efectivo.desc(),
                    TipoMov.preferido.desc(),
                    TipoMov.noaplicariva,
                    TipoMov.factura.desc(),
                    TipoMov.ntipomov
                )
            else:
                query = query.order_by(
                    TipoMov.exportacion,
                    TipoMov.preferido.desc(),
                    TipoMov.noaplicariva,
                    TipoMov.factura.desc(),
                    TipoMov.ntipomov
                )
            
            # Ejecutar la consulta
            result = query.all()
            
            # Convertir a lista de diccionarios
            return [
                {
                    "ntipomov": row.ntipomov,
                    "tipomov": row.tipomov,
                    "correl": row.correl,
                    "Preferido": row.preferido,
                    "coniva": row.coniva,
                    "tiquet": row.tiquet,
                    "nlineasmax": row.nlineasmax,
                    "informe": row.informe,
                    "notacred": row.notacred,
                    "exportacion": row.exportacion,
                    "noaplicariva": row.noaplicariva,
                    "contado": row.contado,
                    "prodprec": row.prodprec,
                    "condpago": row.condpago,
                    "norestariva": row.norestariva,
                    "docunico": row.docunico,
                    "ptovta": row.ptovta,
                    "efectivo": row.efectivo,
                    "qmin": row.qmin,
                    "correlpropio": row.correlpropio,
                    "remision": row.remision
                }
                for row in result
            ]
        except Exception as e:
            # Registrar el error
            print(f"Error en get_facturas_by_empresa_pais: {str(e)}")
            # Puedes implementar un logger más robusto aquí
            return []