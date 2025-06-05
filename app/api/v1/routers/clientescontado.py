from fastapi import Depends, Query, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from app.models.clienteresponse import ClienteResponse

from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

# Define the endpoint to get clientes information
@router.get("/", response_model=List[ClienteResponse], summary="Retrieve Cliente Contado", description="Fetch cliente contado for the enterprise.")
async def get_cliente(
    db: AsyncSession = Depends(uget_db)
):
    # Obtener pempresa de las variables globales
    pempresa = global_vars.get_pempresa()
    
    query = text(
        """
        SELECT tipcli.ntipcli, clientes.clientes, clientes.nclientes, clientes.registro,
               pais.npais, clientes.direccion, clientes.telefono1, clientes.razonsoc,
               clientes.propietario, clientes.direnvio, LTRIM(RTRIM(depto.ndepto)) + ', ' +
               LTRIM(RTRIM(municip.nmunicip)) AS localidad,
               clientes.notas, clientes.retencion, clientes.percepcion, clientes.nosujeto, clientes.exento,
               RTRIM(clientes.telefono1) + ' ' + RTRIM(clientes.telefono2) + ' ' + RTRIM(clientes.telecasa) + ' ' + RTRIM(clientes.teletrabajo) AS telefono,
               condpago.ncondpago, clientes.limitecredito, clientes.dui
        FROM clientes
        LEFT JOIN tipcli ON clientes.tipcli = tipcli.tipcli
        LEFT JOIN pais ON clientes.pais = pais.pais
        LEFT JOIN municip ON municip.municip = clientes.municip
        LEFT JOIN depto ON depto.depto = municip.depto
        LEFT JOIN condpago ON condpago.condpago = clientes.condpago
        WHERE clientes.activo = 1
          AND clientes.contado = 1
          AND clientes.empresa = :pempresa
          AND clientes.mesa = 0
        """
    )

    try:
        # Execute query
        result = await db.execute(query, {"pempresa": pempresa})
        rows = result.fetchall()

        # Convert rows to dictionaries and map to ClienteResponse objects
        clientes_list = []
        for row in rows:
            cliente_dict = dict(zip(result.keys(), row))
            clientes_list.append(ClienteResponse(**cliente_dict))

        return clientes_list
    except Exception as e:
        await db.rollback()
        raise e