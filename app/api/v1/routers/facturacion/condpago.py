from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.facturacion.condpago import CondPagoResponse, FilterType
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[CondPagoResponse])
async def get_condiciones_pago(
    filter_type: FilterType = Query(FilterType.TODOS, description="Tipo de filtro para condiciones de pago"),
    db: AsyncSession = Depends(uget_db)
):
    pempresa = global_vars.get_pempresa()

    # Base query structure
    base_query = """
        select 
            CONDPAGO.NCONDPAGO as ncondpago,
            CONDPAGO.PLAZO as plazo,
            CONDPAGO.CONTADO as contado,
            CONDPAGO.CONDPAGO as condpago,
            CONDPAGO.PREFERIDO as preferido,
            CONDPAGO.tarjeta as tarjeta,
            CONDPAGO.cheque as cheque,
            CONDPAGO.vueltaviaje as vueltaviaje,
            CONDPAGO.remesa as remesa,
            CONDPAGO.otro as otro
        from CONDPAGO 
        where condpago.empresa = :pempresa
            and activo = 1
    """

    if filter_type == FilterType.CONTADO:
        query = base_query + " and (contado = 1 or cheque = 1 or tarjeta = 1)"
    elif filter_type == FilterType.CREDITO:
        query = base_query + " and (contado = 0 and cheque = 0 and tarjeta = 0 and otro = 0)"
    else:
        query = base_query

    query += " order by condpago.nCondPago"
    
    try:
        result = await db.execute(
            text(query),
            {"pempresa": pempresa}
        )
        
        condiciones = result.mappings().all()
        return [CondPagoResponse(**dict(condicion)) for condicion in condiciones]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")