# app/api/v1/routers/routers.py - Versión modificada
from fastapi import APIRouter
from .auth.router import router as auth_router
from .facturacion.factura_lista import router as factura_lista_router
from .vendedores.vendedores_lista import router as vendedores_lista_router 
from .tipoDocumento.tipo_documento_lista import router as tipodocumento_lista_router
from .formaPago.forma_pago_lista import router as formapago_lista_router
from .clientes.clientes_lista import router as clientes_lista_router 
from .productos.productos_lista import router as productos_lista_router

# Crear router global
api_router = APIRouter()

# Incluir routers
api_router.include_router(factura_lista_router, prefix="/facturas", tags=["Facturas Lista"])
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(vendedores_lista_router, prefix="/vendedores", tags=["Vendedores"])
api_router.include_router(tipodocumento_lista_router, prefix="/tipodocumentos", tags=["Tipos de Documento"])
api_router.include_router(formapago_lista_router, prefix="/formaspago", tags=["Formas de Pago"])
api_router.include_router(clientes_lista_router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(productos_lista_router, prefix="/productos", tags="Productos")