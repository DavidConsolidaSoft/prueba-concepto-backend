
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from typing import List
from app.models.facturacion.carteracliente import CarteraClienteResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[CarteraClienteResponse])
async def get_cartera_cliente(
    qfecha2: datetime = Query(..., description="Fecha final"),
    Cliente: str = Query("", description="Código del cliente"),
    Vendedor: str = Query("", description="Código del vendedor"),
    qtipcli: str = Query("", description="Tipo de cliente"),
    db: AsyncSession = Depends(uget_db)
):
    pempresa = global_vars.get_pempresa()

    query = """
    SET nocount on;
    DECLARE @suma table (
        clientes varchar(25), tipomov int, condpago int, vendedor int, fecha datetime,
        numedocu varchar(15), documento varchar(15), nula bit, invcliente int, factura int, 
        pagos int, dpagos int, monto numeric(12,2), caja int, cargo numeric(12,2), 
        abono numeric(12,2), contrato bit, fechaquedan datetime, saldo numeric(12,2)
    );

    insert into @suma (clientes, tipomov, condpago, vendedor, fecha,   
        numedocu, documento, nula, invcliente, pagos, monto, contrato, caja, 
        fechaquedan, saldo, cargo, abono)
    SELECT invcliente.clientes, invcliente.tipomov, invcliente.condpago, invcliente.vendedor,
        invcliente.fecha, invcliente.numedocu, invcliente.numedocu as documento,  
        invcliente.nula, invcliente.invcliente, 0 pagos, 
        case when invcliente.nula=1 then 0000.00 else invcliente.montfact end as montfact, 
        tipomov.contrato, invcliente.caja, invcliente.fechaquedan, 
        invcliente.montfact + invcliente.cargo - invcliente.abono,
        invcliente.cargo, invcliente.abono
    from invcliente inner join tipomov on tipomov.tipomov = invcliente.tipomov
    where invcliente.fecha <= :fecha
        and invcliente.clientes like :cliente  
        and tipomov.anticipo = 0 
        and tipomov.bodega like '%'
        and invcliente.empresa = :empresa 
        and invcliente.montfact + invcliente.cargo - invcliente.abono != 0
        and not exists
            (select 1 from factura where facturareferencia != 0 and fecha < :fecha 
             and empresa = :empresa and factura.factura = invcliente.factura);

    select tipcli.ntipcli tipocliente, cSum.clientes codigo, 
        '' grupocliente, 
        clientes.nclientes NombreCliente, cSum.fecha fecha, 
        dateadd(dd, condpago.plazo, 
            case when cSum.fechaquedan is not null then cSum.fechaquedan 
            else cSum.fecha end) fechavencimiento,
        tipomov.ntipomov tipodocumento, cSum.numedocu documento, 
        cSum.monto monto, cSum.cargo cargo, cSum.abono abono, cSum.saldo saldo, 
        datediff(dd,dateadd(dd,condpago.plazo,cSum.fecha),getdate()) vencida,
        datediff(dd, cSum.fecha, getdate()) antiguedad, vendedor.nvendedor vendedor, 
        clientes.telefono1 telefono, pais.npais pais, depto.ndepto departamento, 
        municip.nmunicip municipio, clientes.direccion,
        clientes.limitecredito, clientes.razonsoc razonsocial, clientes.registro, 
        cSum.contrato, condpago.plazo,
        '' caja 
    from @suma cSum 
    inner join clientes on clientes.clientes collate Modern_Spanish_CI_AS = cSum.clientes 
        collate Modern_Spanish_CI_AS and clientes.empresa = :empresa
    inner join tipcli on tipcli.tipcli = clientes.tipcli
    inner join condpago on condpago.condpago = cSum.condpago
    inner join tipomov on tipomov.tipomov = cSum.tipomov
    inner join vendedor on vendedor.vendedor = cSum.vendedor
    left outer join municip on municip.municip = clientes.municip
    left outer join depto on depto.depto = municip.depto
    left outer join pais on pais.pais = depto.pais 
    left join caja on caja.caja = cSum.caja
    where vendedor.vendedor like :vendedor
        and tipcli.tipcli like :tipcli
        and (clientes.nclientes like :cliente
            or clientes.clientes like :cliente
            or clientes.registro like :cliente
            or clientes.nit like :cliente
            or clientes.dui like :cliente)
    """

    try:
        result = await db.execute(
            text(query),
            {
                "empresa": pempresa,
                "fecha": f"{qfecha2}",
                "cliente": f"%{Cliente}%" if Cliente else "%",
                "vendedor": f"%{Vendedor}%" if Vendedor else "%",
                "tipcli": f"%{qtipcli}%" if qtipcli else "%"
            }
        )
        
        cartera = result.mappings().all()
        return [CarteraClienteResponse(**dict(item)) for item in cartera]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {str(e)}")