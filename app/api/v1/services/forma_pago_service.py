from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.dbo.formpago import FormPago
from app.models.dbo.condpago import CondPago

class FormaPagoServiceORM:
    def __init__(self, db: Session):
        self.db = db
        # Deshabilitar la carga automática de relaciones
        self.db.autoflush = False
   
    def get_formas_pago_by_empresa(
        self,
        empresa_id: int,
        activo: Optional[bool] = None,
        frecuente: Optional[bool] = None
    ) -> List[FormPago]:
        """
        Obtiene todas las formas de pago de una empresa específica.
       
        Parámetros:
        - empresa_id: ID de la empresa
        - activo: Filtrar por formas de pago activas/inactivas
        - frecuente: Filtrar por formas de pago frecuentes
        """
        query = self.db.query(FormPago).filter(FormPago.empresa == empresa_id)
       
        # Filtrar por estado activo si se especifica
        if activo is not None:
            query = query.filter(FormPago.activo == activo)
       
        # Filtrar por frecuente si se especifica
        if frecuente is not None:
            query = query.filter(FormPago.frecuente == frecuente)
       
        # Ordenar por nombre
        query = query.order_by(FormPago.nformpago)
       
        return query.all()
   
    def get_forma_pago_by_id(self, formpago_id: int, empresa_id: int) -> Optional[FormPago]:
        """
        Obtiene una forma de pago específica por su ID, dentro de una empresa específica.
        """
        query = self.db.query(FormPago).filter(
            FormPago.formpago == formpago_id,
            FormPago.empresa == empresa_id
        )
       
        return query.first()
   
    def get_formas_pago_by_tipo(self, empresa_id: int) -> dict:
        """
        Obtiene formas de pago categorizadas por tipo.
        """
        # Formas de pago fijas
        fijas = self.db.query(FormPago).filter(
            FormPago.empresa == empresa_id,
            FormPago.activo == True,
            FormPago.FIJO == True
        ).order_by(FormPago.nformpago).all()
       
        # Formas de pago por obra
        por_obra = self.db.query(FormPago).filter(
            FormPago.empresa == empresa_id,
            FormPago.activo == True,
            FormPago.OBRA == True
        ).order_by(FormPago.nformpago).all()
       
        # Formas de pago por comisión
        comision = self.db.query(FormPago).filter(
            FormPago.empresa == empresa_id,
            FormPago.activo == True,
            FormPago.COMISION == True
        ).order_by(FormPago.nformpago).all()
       
        # Formas de pago frecuentes
        frecuentes = self.db.query(FormPago).filter(
            FormPago.empresa == empresa_id,
            FormPago.activo == True,
            FormPago.frecuente == True
        ).order_by(FormPago.nformpago).all()
       
        return {
            "fijas": fijas,
            "por_obra": por_obra,
            "comision": comision,
            "frecuentes": frecuentes
        }
    
    # Nuevos métodos para condiciones de pago
    def get_condiciones_pago(
        self,
        empresa_id: int,
        solo_contado: bool = False,
        solo_credito: bool = False
    ) -> List[CondPago]:
        """
        Obtiene las condiciones de pago según los filtros especificados.
        
        Parámetros:
        - empresa_id: ID de la empresa
        - solo_contado: Obtener solo condiciones de pago de contado (contado=1 or cheque=1 or tarjeta=1)
        - solo_credito: Obtener solo condiciones de pago de crédito (contado=0 and cheque=0 and tarjeta=0 and otro=0)
        """
        query = self.db.query(CondPago).filter(
            CondPago.empresa == empresa_id,
            CondPago.activo == True
        )
        
        # Aplicar filtros según el caso
        if solo_contado:
            # CASE 1: Solo condiciones de pago de contado
            query = query.filter(
                (CondPago.contado == True) | 
                (CondPago.cheque == True) | 
                (CondPago.tarjeta == True)
            )
        elif solo_credito:
            # CASE 2: Solo condiciones de pago de crédito
            query = query.filter(
                (CondPago.contado == False) &
                (CondPago.cheque == False) &
                (CondPago.tarjeta == False) &
                (CondPago.otro == False)
            )
        # OTHERWISE: Todas las condiciones de pago activas
        
        # Ordenar por nombre
        query = query.order_by(CondPago.ncondpago)
        
        return query.all()
    
    def get_condicion_pago_by_id(self, condpago_id: int, empresa_id: int) -> Optional[CondPago]:
        """
        Obtiene una condición de pago específica por su ID dentro de una empresa.
        """
        return self.db.query(CondPago).filter(
            CondPago.condpago == condpago_id,
            CondPago.empresa == empresa_id
        ).first()