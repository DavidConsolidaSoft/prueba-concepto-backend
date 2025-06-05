
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from typing import List
from app.models.facturacion.factimpresa import FactImpresaResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[FactImpresaResponse])
async def get_facturas_impresas(
    qfecha1: datetime = Query(..., description="Fecha inicial"),
    qfecha2: datetime = Query(..., description="Fecha final"),
    qmvendedor: str = Query("", description="Código del vendedor"),
    qmtipomov: str = Query("", description="Tipo de movimiento"),
    qdocumento: str = Query("", description="Número de documento"), 
    qcliente: str = Query("", description="Código o nombre o registro del cliente"),
    db: AsyncSession = Depends(uget_db)
):
    pempresa = global_vars.get_pempresa()
    pmicaja = global_vars.get_pmicaja()

    # print(qmtipomov, pmicaja, pempresa, qfecha1, qfecha2, qmvendedor, qmtipomov, qdocumento, qcliente)

    query = """
    SELECT distinct 
        factura.fecha, 
        factura.numedocu, 
        substring(tipomov.ntipomov,1,10) ntipomov, 
        factura.factura, 
        factura.montfact,
        substring(case when factcont.nclientes is not null then factcont.nclientes else Clientes.nClientes end,1,30) nclientes,
        vendedor.nvendedor, 
        condpago.ncondpago, 
        factura.tipomov, 
        factura.condpago
    from factura 
        inner join clientes on factura.clientes = clientes.clientes and clientes.empresa = :pempresa
        inner join tipomov on tipomov.tipomov = factura.tipomov and tipomov.notacred = 0
        left outer join factcont on factura.factura = factcont.factura
        inner join vendedor on vendedor.vendedor = factura.vendedor
        inner join condpago on condpago.condpago = factura.condpago
    where factura.impresa = 1
        and factura.PEDIDO != FACTURA.NUMEDOCU
        and Factura.fecha >= :qfecha1 and factura.fecha <= :qfecha2
        and clientes.empresa = :pempresa
        and (factura.caja like '%' or factura.caja like :pmicaja)
        and factura.empresa = :pempresa
        and factura.vendedor like :qmvendedor
        and factura.tipomov like :qmtipomov
        and factura.numedocu like :qdocumento
        and (clientes.nclientes like :qcliente 
            or factcont.nclientes like :qcliente
            or clientes.clientes like :qcliente
            or clientes.registro like :qcliente)
        and tipomov.factura = 1 
        and tipomov.notacred = 0 
        and tipomov.devolucion = 0
        and tipomov.empresa = :pempresa
    order by factura.fecha desc, factura.numedocu desc
    """
    
    try:
        result = await db.execute(
            text(query),
            {
                "pempresa": pempresa,
                "pmicaja": pmicaja,
                "qfecha1": f"{qfecha1}" if qfecha1 else datetime.today(),
                "qfecha2": f"{qfecha2}" if qfecha2 else datetime.today(),
                "qmvendedor": f"%{qmvendedor}%" if qmvendedor else "%",
                "qmtipomov": f"%{qmtipomov}%" if qmtipomov else "%",
                "qdocumento": f"%{qdocumento}%" if qdocumento else "%",
                "qcliente": f"%{qcliente}%" if qcliente else "%",
            }
        )
        
        facturas = result.mappings().all()
        return [FactImpresaResponse(**dict(factura)) for factura in facturas]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")