# from fastapi import APIRouter
# from app.api.v1.endpoints import facturacion, maestros, compras, inventarios

# api_router = APIRouter()

# # Agrupamos los endpoints por funcionalidad
# api_router.include_router(
#     facturacion.router,
#     prefix="/facturacion",
#     tags=["Facturación"]
# )

# api_router.include_router(
#     maestros.router, 
#     prefix="/maestros",
#     tags=["Maestros"]
# )

# api_router.include_router(
#     compras.router,
#     prefix="/compras", 
#     tags=["Compras"]
# )

# api_router.include_router(
#     inventarios.router,
#     prefix="/inventarios",
#     tags=["Inventarios"]
# )