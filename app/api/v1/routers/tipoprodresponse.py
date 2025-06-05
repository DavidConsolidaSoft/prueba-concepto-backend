from fastapi import Depends, Query, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List
from app.models.tipoprodresponse import TipoProdResponse
from app.db.database import uget_db
from app.core import global_vars

router = APIRouter()

@router.get("/", response_model=List[TipoProdResponse], 
            summary="Retrieve product types", 
            description="Fetch product types based on search filters with pagination")
async def get_tipoprod(
    tipo: Optional[str] = Query(None, description="Search query for product type name"),
    limit: int = Query(4, description="Number of items to retrieve"),
    offset: int = Query(0, description="Number of items to skip"),
    db: AsyncSession = Depends(uget_db)
):
    pempresa = global_vars.get_pempresa()

    query = text("""
        SELECT TIPOPROD.NTIPOPROD, TIPOPROD.PREFERIDO, TIPOPROD.image,
            TIPOPROD.ACTIVO, TIPOPROD.TIPOPROD, TIPOPROD.EMPRESA, TIPOPROD.PARANCEL,
            TIPOPROD.puno, TIPOPROD.pdos, TIPOPROD.ptres, TIPOPROD.pcuatro, 
            TIPOPROD.pcinco, TIPOPROD.vol1, TIPOPROD.vol2, TIPOPROD.vol3, TIPOPROD.vol4, 
            TIPOPROD.vol5, TIPOPROD.fecha1, TIPOPROD.fecha2,
            TIPOPROD.factor1, TIPOPROD.factor2, TIPOPROD.factor3, 
            TIPOPROD.factor4, TIPOPROD.factor5,
            TIPOPROD.principal
        FROM TIPOPROD 
        WHERE empresa = :empresa
            AND ntipoprod LIKE :tipo
        ORDER BY TIPOPROD.nTipoProd
        OFFSET :offset ROWS FETCH NEXT :limit ROWS ONLY
    """)

    try:
        result = await db.execute(
            query,
            {
                "empresa": pempresa,
                "tipo": f"%{tipo}%" if tipo else "%",
                "limit": limit,
                "offset": offset,
            }
        )
        rows = result.fetchall()
        
        tipoprod_list = [TipoProdResponse(**dict(zip(result.keys(), row))) for row in rows]
        return tipoprod_list
        
    except Exception as e:
        await db.rollback()
        raise e