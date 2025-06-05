from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.api.v1.getParams import get_params
from app.schemas.sparams import ParamsResponse
from app.db.database import get_db

router = APIRouter()

@router.get("/{nombre_empresa}", response_model=List[ParamsResponse],
    summary="Get parameters by empresa"
)
async def get_parameters(
    nombre_empresa: str, 
    db: AsyncSession = Depends(get_db)
) -> List[ParamsResponse]:
    params = await get_params(db, nombre_empresa)
    if not params:
        raise HTTPException(status_code=404, detail="Parameters not found")
    return params