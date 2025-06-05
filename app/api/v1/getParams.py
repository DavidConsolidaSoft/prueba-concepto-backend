from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.mparams import ParamsDB
from app.schemas.sparams import ParamsResponse
from app.core import global_vars

async def get_params(
    db: AsyncSession, 
    empresa_nombre: str
) -> List[ParamsResponse]:
    query = select(ParamsDB).where(ParamsDB.nombre == empresa_nombre)
    result = await db.execute(query)
    params = result.scalars().all()

    if params:
        param = params[0]
        global_vars.set_pnempresa(empresa_nombre)
        # Actualizar variables globales
        global_vars.set_pempresa(param.empresa)
        global_vars.set_pnusuario(param.nusuario)
        global_vars.set_pempresa(param.empresa)
        global_vars.set_pmicaja(param.caja)
        global_vars.set_pbodega(param.bodega)
        global_vars.set_pvendedor(param.vendedor)
        global_vars.set_pprodprec(param.prodprec)
        global_vars.set_pdata(param.cc)

    return [ParamsResponse.model_validate(param) for param in params]
