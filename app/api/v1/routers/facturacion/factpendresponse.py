from fastapi import Depends, HTTPException, Query, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Literal, Optional
from app.models.facturacion.factpendresponse import FactPendResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[FactPendResponse])
async def get_facturas(
    qPedido: str = Query("", description="Número de pedido o documento"),
    qtipomov: str = Query("", description="Tipo de movimiento"),
    qncliente: str = Query("", description="Nombre o código de cliente"),
    psat_tipo: int = Query(..., description="Tipo de sello: 0 para ninguno, 1 o 2 para FEL, 3 para DTE", ge=0, le=3),
    db: AsyncSession = Depends(uget_db)
):
    
    pempresa = global_vars.get_pempresa()
    pmicaja = global_vars.get_pmicaja()

    # Determinar el sello según psat_tipo
    if psat_tipo in [1, 2]:
        sello_case = "(CASE WHEN factelec.factura is null THEN '' ELSE '*FEL*' END)"
    elif psat_tipo == 3:
        sello_case = "(CASE WHEN factelec.sellorecibido is null THEN '-SS-' ELSE '*DTE' END)"
    else:
        sello_case = "''"

    query = f"""
    WITH elquery as (
    select FACTURA.PEDIDO, 
        substring(tipomov.ntipomov,1,10) ntipomov,
        {sello_case} + FACTURA.NUMEDOCU numedocu, 
        FACTURA.FECHA, 
        FACTURA.MONTFACT, 
        FACTURA.IMPRESA, 
        FACTURA.NULA, 
        FACTURA.CLIENTES, 
        case when Clientes.Contado=1 then  ISNULL((select FactCont.nClientes from factcont where factcont.factura = factura.factura),clientes.nclientes) collate Modern_Spanish_CI_AS  else clientes.nclientes collate Modern_Spanish_CI_AS  end as nClientes, 
        case when Clientes.Contado=1 then (select FactCont.Registro from factcont where factcont.factura = factura.factura) else Clientes.REGISTRO end as Registro, 
        Depto.nDepto, 
        case when Clientes.Contado=1 AND isnull((select FactCont.nClientes from factcont where factcont.factura = factura.factura),'')!='' 
            then (select FactCont.nMunicip from factcont where factcont.factura = factura.factura) else Municip.nMunicip end as nMunicip, 
        Clientes.Telefono1, 
        factura.factura, 
        factura.caja, 
        factura.efectivo,
        factura.tipomov,  (select tipovta.ntipovta from tipovta where tipovta.tipovta = factura.tipovta) ntipovta,
        (select vendedor.nvendedor from vendedor where vendedor.vendedor = factura.vendedor) nvendedor,
        (select tipcli.ntipcli from tipcli where tipcli.tipcli = clientes.tipcli) ntipcli, 
        (select condpago.ncondpago from condpago where condpago.condpago = factura.condpago) ncondpago, 
        (case when factura.facturareferencia = 0 and factura.nula = 0 then 0 else 1 end) si,
        factura.notas,
        factura.afecta + factura.exenta neto
    from FACTURA 
        Left join Clientes on Clientes.Clientes = Factura.Clientes and clientes.empresa = :pempresa
        left join municip on clientes.municip = municip.municip 
        left join depto on municip.depto = depto.depto 
        left join tipomov on tipomov.tipomov = factura.tipomov
        left join factelec on factelec.factura = factura.factura
        left join factcont on factcont.factura = factura.factura
    where 
        factura.empresa = :pempresa and factura.impresa = 0 and factura.nula = 0
        and factura.tipomov in (select tipomov from tipomov where TipoMov.factura = 1 
        and tipomov.anticipo = 0 and tipomov.notacred = 0) and factura.empresa = :pempresa
        and (factura.pedido like :qPedido or factura.numedocu like :qPedido)
        and factura.tipomov like :qtipomov
        and factura.caja = :pmicaja
        and (clientes.nclientes like :qncliente or clientes.clientes like :qncliente
            or clientes.registro like :qncliente)    
        and factura.pedido not like '%corte%'
    )
    SELECT 
        PEDIDO, ntipomov, numedocu, FECHA, 
        MONTFACT, IMPRESA, NULA, 
        CLIENTES, nClientes, Registro,
        nDepto, nMunicip, Telefono1, 
        factura, caja, efectivo,
        tipomov, ntipovta,
        nvendedor,
        ntipcli, ncondpago, si,
        notas, neto
    from elquery    
    order by fecha, numedocu, ntipomov
    """
    
    try:
        result = await db.execute(
            text(query),
            {
                "pempresa": pempresa,
                "qPedido": f"%{qPedido}%" if qPedido else "%",
                "qtipomov": f"%{qtipomov}%" if qtipomov else "%",
                "pmicaja": pmicaja,
                "qncliente": f"%{qncliente}%" if qncliente else "%"
            }
        )
        
        facturas = result.mappings().all()
        return [FactPendResponse(**dict(factura)) for factura in facturas]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")