
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.facturacion.dfactura import DFacturaResponse
from app.db.database import uget_db

router = APIRouter()

@router.get("/{factura}", response_model=List[DFacturaResponse])
async def get_detalle_factura(
    factura: int,
    db: AsyncSession = Depends(uget_db)
):
    query = """
    select 
        tipoprod.ntipoprod tipoproducto, 
        producto.icdbarra codigo,
        CASE when producto.exento = 1 then '(Ex) ' else '' end + producto.nproducto as nombreProducto,
        (select top 1 bodega.nbodega from bodega where bodega.bodega = kardex.bodega) as bodega,
        (select top 1 lote.nolote from lote where lote.lote = kardex.lote) as numLote,
        dfactura.cantidad, dfactura.reservado, dfactura.bonificado, dfactura.pdesc, 
        dfactura.precio, dfactura.kardex, dfactura.gratificado as gratificado, dfactura.gratif,
        dfactura.exenta, dfactura.afecta, dfactura.viva as impuesto, dfactura.vdesc,
        dfactura.montfact monto, dfactura.dfactura, dfactura.factura, dfactura.fovial, 
        dfactura.cotrans, dfactura.vgdesc as descglobal, dfactura.talonario,
        dfactura.apliquemora, dfactura.oprecio, dfactura.nosujeto,
        dfactura.horatiempo, dfactura.linea, dfactura.empresa, dfactura.nombre,
        dfactura.vinculado, producto.mformula, dfactura.pcomision, dfactura.estado,
        dfactura.fraccion, dfactura.dregciclo, dfactura.preciolista, dfactura.uvendidas,
        (select top 1 lote.fecvence from lote where lote.lote = kardex.lote) as fecvence,
        producto.nosujeto bitnosujeto, producto.exento, producto.condicion1,
        producto.nosujeto, producto.recargo, producto.parte, producto.peso,
        kardex.producto, producto.codbarra,
        (select top 1 umedida.numedida from umedida where umedida.umedida = producto.umedida) numedida,
        producto.umedida,
        case when dfactura.afecta = 0 or dfactura.montfact = 0 then dfactura.vdesc 
            else round(dfactura.vdesc*dfactura.afecta/dfactura.montfact,2) end yvdesc,
        (select top 1 umedida.factor from umedida where umedida.umedida = producto.umedida1) factor,
        dfactura.texto, producto.servicios, dfactura.costo,
        (producto.apdesc | tipoprod.adescp) apdesc, dfactura.factalm,
        dfactura.vendedor, producto.costo tallak, producto.cicloanterior,
        dfactura.gratificadouventa
    from 
        dfactura inner join kardex on kardex.kardex = dfactura.kardex
        inner join producto on kardex.producto = producto.producto
        inner join tipoprod on tipoprod.tipoprod = producto.tipoprod
    where dfactura.factura = :factura
        and dfactura.preciolista = 0
    order by dfactura.dfactura
    """
    
    try:
        result = await db.execute(
            text(query),
            {"factura": factura}
        )
        
        detalles = result.mappings().all()
        return [DFacturaResponse(**dict(detalle)) for detalle in detalles]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")