from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.facturacion.tipomov import TipoMovResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[TipoMovResponse])
async def get_tipos_movimiento(
    db: AsyncSession = Depends(uget_db)
):
    pempresa = global_vars.get_pempresa()
    pmicaja = global_vars.get_pmicaja()

    query = """
    DECLARE @tiquet int;
    DECLARE @elSalvador int;
    DECLARE @guatemala int;

    select @guatemala = pais.guatemala 
    from pais INNER JOIN empresa ON empresa.pais = pais.pais 
    where pais.usuario = -100 and empresa.guatemala = 1;

    select @elSalvador = pais.elsalvador 
    from pais INNER JOIN empresa ON empresa.pais = pais.pais 
    where pais.usuario = -100 and empresa.elSalvador = 1;

    SELECT @tiquet = caja.maximot FROM caja WHERE caja = :pmicaja AND empresa = :pempresa;

    IF @elSalvador = 1
        IF @tiquet = 1 
            SELECT 
                Tipomov.ntipomov, 
                Tipomov.tipomov, 
                Tipomov.correl, 
                Tipomov.Preferido,  /* Note the capital P */
                Tipomov.coniva, 
                Tipomov.tiquet, 
                Tipomov.nlineasmax, 
                Tipomov.informe,
                Tipomov.notacred, 
                Tipomov.exportacion, 
                Tipomov.noaplicariva, 
                condpago.contado,
                tipomov.prodprec, 
                tipomov.condpago, 
                tipomov.norestariva, 
                tipomov.docunico,
                tipomov.ptovta, 
                tipomov.efectivo, 
                tipomov.qmin, 
                tipomov.correlpropio, 
                tipomov.remision
            FROM tipomov left outer join condpago on condpago.condpago = tipomov.condpago
            WHERE Tipomov.factura = 1 and Tipomov.activo = 1 
                and (Tipomov.ofactura = 0 or tipomov.ofactura is not null)
                AND tipomov.notacred = 0 and tipomov.empresa = :pempresa
            ORDER BY Tipomov.exportacion, tipomov.noaplicariva, tipomov.tiquet desc, 
                tipomov.preferido desc, Tipomov.ntipomov
        ELSE
            SELECT 
                Tipomov.ntipomov, 
                Tipomov.tipomov, 
                Tipomov.correl, 
                Tipomov.Preferido,  /* Note the capital P */
                Tipomov.coniva, 
                Tipomov.tiquet, 
                Tipomov.nlineasmax, 
                Tipomov.informe,
                Tipomov.notacred, 
                Tipomov.exportacion, 
                Tipomov.noaplicariva, 
                condpago.contado,
                tipomov.prodprec, 
                tipomov.condpago, 
                tipomov.norestariva, 
                tipomov.docunico,
                tipomov.ptovta, 
                tipomov.efectivo, 
                tipomov.qmin, 
                tipomov.correlpropio, 
                tipomov.remision
            FROM tipomov left outer join condpago on condpago.condpago = tipomov.condpago
            WHERE Tipomov.factura = 1 and Tipomov.activo = 1 
                and (Tipomov.ofactura = 0 or tipomov.ofactura is not null)
                AND tipomov.notacred = 0 and tipomov.empresa = :pempresa
            ORDER BY tipomov.exportacion, tipomov.preferido desc, tipomov.noaplicariva, 
                tipomov.factura desc, Tipomov.ntipomov;
    ELSE 
        IF @guatemala = 1
            SELECT 
                Tipomov.ntipomov, 
                Tipomov.tipomov, 
                Tipomov.correl, 
                Tipomov.Preferido,  /* Note the capital P */
                Tipomov.coniva, 
                Tipomov.tiquet, 
                Tipomov.nlineasmax, 
                Tipomov.informe,
                Tipomov.notacred, 
                Tipomov.exportacion, 
                Tipomov.noaplicariva, 
                condpago.contado,
                tipomov.prodprec, 
                tipomov.condpago, 
                tipomov.norestariva, 
                tipomov.docunico,
                tipomov.ptovta, 
                tipomov.efectivo, 
                tipomov.qmin, 
                tipomov.correlpropio, 
                tipomov.remision
            FROM tipomov left outer join condpago on condpago.condpago = tipomov.condpago
            WHERE Tipomov.factura  = 1 and Tipomov.activo = 1 and (Tipomov.ofactura = 0 or tipomov.ofactura is not null)
                AND tipomov.notacred = 0 and tipomov.empresa = :pempresa
            ORDER BY Tipomov.exportacion, tipomov.efectivo desc, tipomov.preferido desc, tipomov.noaplicariva, tipomov.factura desc, Tipomov.ntipomov
        ELSE 
            SELECT 
                Tipomov.ntipomov, 
                Tipomov.tipomov, 
                Tipomov.correl, 
                Tipomov.Preferido,  /* Note the capital P */
                Tipomov.coniva, 
                Tipomov.tiquet, 
                Tipomov.nlineasmax, 
                Tipomov.informe,
                Tipomov.notacred, 
                Tipomov.exportacion, 
                Tipomov.noaplicariva, 
                condpago.contado,
                tipomov.prodprec, 
                tipomov.condpago, 
                tipomov.norestariva, 
                tipomov.docunico,
                tipomov.ptovta, 
                tipomov.efectivo, 
                tipomov.qmin, 
                tipomov.correlpropio, 
                tipomov.remision
            FROM tipomov left outer join condpago on condpago.condpago = tipomov.condpago
            WHERE Tipomov.factura  = 1 and Tipomov.activo = 1 and (Tipomov.ofactura = 0 or tipomov.ofactura is not null)
                AND tipomov.notacred = 0 and tipomov.empresa = :pempresa
            ORDER BY tipomov.exportacion,  tipomov.preferido desc, tipomov.noaplicariva, tipomov.factura desc, Tipomov.ntipomov

       """

    try:
        result = await db.execute(
            text(query),
            {
                "pempresa": pempresa,
                "pmicaja": pmicaja
            }
        )
        
        tipos = result.mappings().all()
        return [TipoMovResponse(**dict(tipo)) for tipo in tipos]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")