from fastapi import Depends, Query, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models.facturacion.facturaresponse import FacturaResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter(prefix="/api/v1")

# Define the endpoint to get factura information
@router.get("/", response_model=List[FacturaResponse], summary="Retrieve factura information", description="Fetch detailed factura information based on provided criteria.")
async def get_factura(
    factura: int = Query(..., description="Factura identifier"),
    db: AsyncSession = Depends(uget_db)
): 

    pempresa = global_vars.get_pempresa()

    query = text(
        """
        WITH vdescCTE AS (
            SELECT factura.factura, factura.vdesc
            FROM factura
            WHERE factura.factura = :factura
        ),
        envioCTE AS (
            SELECT TOP 1 cambodega.numedocu, envioFactura.factura
            FROM envioFactura
            INNER JOIN cambodega ON cambodega.cambodega = envioFactura.cambodega
            WHERE envioFactura.factura = :factura
            ORDER BY envioFactura.factura
        ),
        felCTE AS (
            SELECT TOP 1 factelec.selloRecibido, factelec.factura
            FROM factelec
            WHERE factelec.factura = :factura
            ORDER BY factelec.factura
        )
        SELECT factura.basesiniva, tipomov.coniva, factura.bnotas, factura.docunico, factura.nocheque,
               factura.notarjeta, factura.retencion, FACTURA.BODEGA, FACTURA.CLIENTES, FACTURA.CONDPAGO,
               FACTURA.FACTURA, FACTURA.FECHA, factura.fecha1, FACTURA.IMPRESA, FACTURA.IVA, FACTURA.MONEDA,
               FACTURA.MONTFACT, FACTURA.NOTAS, FACTURA.NULA, FACTURA.NUMEDOCU, FACTURA.PEDIDO,
               FACTURA.PRODPREC, FACTURA.TIPOMOV, FACTURA.TIPOVTA, FACTURA.TRANSPTE, FACTURA.VENDEDOR,
               FACTURA.vDESC, FACTURA.PDESC, factura.PROPINA, FACTURA.Afecta, FACTURA.Exenta, FACTURA.vIva,
               CASE WHEN factcont.factura IS NOT NULL THEN factcont.nclientes COLLATE Modern_Spanish_CI_AS ELSE clientes.nclientes COLLATE Modern_Spanish_CI_AS END AS nclientes,
               Vendedor.nVendedor, Clientes.Contado, CASE WHEN factcont.factura IS NOT NULL AND LEN(factcont.registro) != 0 THEN factcont.registro ELSE clientes.registro END AS Registro,
               factura.fovial, factura.cotrans, factura.efectivo, factura.nosujeto, factura.nombreref,
               factura.docref, FACTURA.PERCEPCION, factura.caja, factura.usuario, factura.horatiempo,
               clientes.dui, factura.empresa, factura.ordenno, factura.enfirme, factura.impbod, factura.estado,
               factura.cobrador, CASE WHEN factura.estado = 0 THEN '' ELSE CASE WHEN factura.estado = 1 THEN 'Preparar' ELSE CASE WHEN factura.estado = 2 THEN 'Terminado' ELSE CASE WHEN factura.estado = 4 THEN 'Dar Prioridad' ELSE CASE WHEN factura.estado = 3 THEN 'Cancelado' ELSE '' END END END END END AS Estatus,
               vdesc.vdesc AS dvdesc, CondPago.nCondPago, condpago.plazo, Clientes.Nit, clientes.email, depto.codpostal,
               sucursal.direccion AS dir, sucursal.prefijo, sucursal.prefijo1, sucursal.prefijo2, sucursal.prefijo3,
               sucursal.prefijo4, sucursal.quedan, CASE WHEN factcont.factura IS NOT NULL AND LEN(factcont.direccion) != 0 THEN factcont.Direccion ELSE Clientes.Direccion END AS Direccion,
               CASE WHEN dte.tabla IS NULL THEN RTRIM(municip.nmunicip) ELSE 'Distr. ' + RTRIM(municip.nmunicip) + ' - ' + RTRIM(dte.tabla) END AS nmunicip,
               Clientes.RazonSoc, Clientes.Giro, clientes.telefono1, clientes.email AS correo, tipomov.ntipomov,
               depto.ndepto, factura.dgratif, factura.tipopago, envio.numedocu AS notarem,
               (CASE WHEN condpago.contado = 1 OR condpago.cheque = 1 OR condpago.tarjeta = 1 OR condpago.remesa = 1 THEN 1 ELSE 0 END) AS contado,
               factura.clientes2, miclien.nclientes AS elCliente, factura.pagencia AS transferencia, clientes.dui AS iddoc,
               factura.cheque AS cambio, clientes.valorreferencia1, clientes.valorreferencia2, clientes.valorreferencia3,
               clientes.valorreferencia4, clientes.conPagare, clientes.referencia1, clientes.zona, clientes.municip,
               municip.depto, clientes.referencia2, CASE WHEN condpago.otro = 1 THEN 4 ELSE CASE WHEN condpago.contado = 1 THEN 1 ELSE CASE WHEN condpago.cheque = 1 THEN 3 ELSE CASE WHEN condpago.tarjeta = 1 THEN 2 ELSE 5 END END END END AS eltipo,
               empresa.notas AS misDatos, factura.tarjeta, factura.aprobado, factura.fecha2, factura.ordenno, '' AS lamesa,
               fel.selloRecibido AS sello, caja.ncaja, clientes.trabajo, tipcli.empleado, pais.npais, pais.elsalvador,
               factura.pesofactura AS cheque, tipcli.tipomiembro, factura.encomienda, factura.nomesa, clientes.tipcli
        FROM FACTURA
        LEFT JOIN clientes ON clientes.clientes = factura.clientes AND clientes.empresa = :pempresa
        LEFT JOIN felCTE fel ON fel.factura = factura.factura
        LEFT JOIN envioCTE envio ON envio.factura = factura.factura
        LEFT JOIN vdescCTE vdesc ON vdesc.factura = factura.factura
        LEFT JOIN vendedor ON vendedor.vendedor = factura.vendedor
        LEFT JOIN condpago ON condpago.condpago = factura.condpago
        LEFT JOIN tipomov ON tipomov.tipomov = factura.tipomov
        LEFT OUTER JOIN municip ON municip.municip = clientes.municip
        LEFT OUTER JOIN depto ON depto.depto = municip.depto
        LEFT JOIN pais ON pais.pais = depto.pais
        LEFT OUTER JOIN factcont ON factura.factura = factcont.factura
        LEFT JOIN bodega ON factura.bodega = bodega.bodega
        LEFT JOIN sucursal ON bodega.sucursal = sucursal.tipobodega
        LEFT OUTER JOIN clientes miclien ON miclien.clientes = factura.clientes2 AND miclien.empresa = :pempresa
        INNER JOIN empresa ON factura.empresa = empresa.empresa
        INNER JOIN tipcli ON tipcli.tipcli = clientes.tipcli
        LEFT JOIN caja ON caja.caja = factura.caja
        LEFT JOIN dte ON dte.municip = municip.municip
        WHERE factura.Factura = :factura
        """
    )

    # Execute query
    result = await db.execute(query, {"pempresa": pempresa, "factura": factura})
    rows = result.fetchall()

    # Convert Row objects to dictionaries and map to FacturaResponse
    factura_list = [FacturaResponse(**row._asdict()) for row in rows]

    return factura_list