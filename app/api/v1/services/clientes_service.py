from sqlalchemy.orm import Session
from sqlalchemy import Tuple, select, and_, or_, func, desc
from typing import List, Optional, Dict, Any, Tuple as PyTuple
from app.models.dbo.clientes import Clientes
from datetime import datetime
import logging
import re
# Configurar logging
logger = logging.getLogger(__name__)

class ClientesServiceORM:
    def __init__(self, db: Session):
        self.db = db
        self.db.autoflush = False
        
    
    def _normalize_search_term(self, search_term: str) -> str:
        """
        Normaliza el término de búsqueda eliminando espacios extra,
        caracteres especiales y convirtiendo a minúsculas.
        """
        if not search_term:
            return ""
        
        # Eliminar espacios al inicio y final, convertir a minúsculas
        normalized = search_term.strip().lower()
        
        # Eliminar espacios múltiples y dejar solo uno
        normalized = re.sub(r'\s+', ' ', normalized)
        
        # Log para debugging
        if search_term != normalized:
            logger.debug(f"Término normalizado: '{search_term}' -> '{normalized}'")
        
        return normalized
    
    def get_clientes_by_empresa(
        self, 
        empresa_id: int, 
        activo: Optional[bool] = None,
        tipcli: Optional[int] = None,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 100,
        count_only: bool = False
    ) -> PyTuple[List[Dict[str, Any]], int]:
        """
        Obtiene todos los clientes de una empresa específica con filtros opcionales.
        Si count_only=True, solo retorna el conteo total sin datos.
        """
        try:
            # Normalizar término de búsqueda
            search_normalized = self._normalize_search_term(search) if search else None
            
            logger.info(f"Obteniendo clientes para empresa_id={empresa_id}, activo={activo}, tipcli={tipcli}, search='{search_normalized}'")
            
            # Crear la consulta base
            query = self.db.query(Clientes)
            
            # Aplicar filtro de empresa (siempre presente)
            query = query.filter(Clientes.empresa == empresa_id)
            
            # Filtrar por estado activo si se especifica
            if activo is not None:
                query = query.filter(Clientes.activo == activo)
            
            # Filtrar por tipo de cliente si se especifica
            if tipcli is not None:
                query = query.filter(Clientes.tipcli == tipcli)
            
            # Aplicar búsqueda mejorada si hay término
            if search_normalized and len(search_normalized) >= 2:  # Consistente: mínimo 2 caracteres
                # Dividir el término en palabras para búsqueda más flexible
                search_words = search_normalized.split()
                
                search_conditions = []
                
                # Para cada palabra, buscar en todos los campos relevantes
                for word in search_words:
                    word_pattern = f"%{word}%"
                    word_conditions = or_(
                        func.lower(Clientes.nclientes).like(word_pattern),
                        func.lower(Clientes.clientes).like(word_pattern),
                        func.lower(Clientes.nit).like(word_pattern),
                        func.lower(Clientes.registro).like(word_pattern),
                        func.lower(Clientes.telefono1).like(word_pattern),
                        func.lower(Clientes.telefono2).like(word_pattern),
                        func.lower(Clientes.celular).like(word_pattern),
                        func.lower(Clientes.razonsoc).like(word_pattern)
                    )
                    search_conditions.append(word_conditions)
                
                # Si hay múltiples palabras, todas deben coincidir (AND)
                if len(search_conditions) > 1:
                    query = query.filter(and_(*search_conditions))
                elif len(search_conditions) == 1:
                    query = query.filter(search_conditions[0])
                
                logger.debug(f"Aplicando búsqueda con {len(search_words)} palabra(s): {search_words}")
            
            # Obtener conteo total para paginación
            total = query.count()
            logger.info(f"Total de clientes encontrados: {total}")
            
            # Si solo queremos el conteo, retornamos temprano
            if count_only:
                return [], total
            
            # Aplicar ordenamiento y paginación
            if limit > 0:
                query = query.order_by(Clientes.nclientes, Clientes.clientes)
                query = query.offset(skip).limit(limit)
            
            # Ejecutar la consulta
            clientes_raw = query.all()
            logger.info(f"Obtenidos {len(clientes_raw)} clientes después de aplicar paginación")
            
            # Convertir a diccionarios
            clientes_list = []
            unique_clients = set()
            
            for cliente in clientes_raw:
                # Limpiar el ID del cliente de espacios
                cliente_id = cliente.clientes.strip() if isinstance(cliente.clientes, str) else cliente.clientes
                
                # Si este cliente ya fue procesado, omitirlo
                if cliente_id in unique_clients:
                    continue
                
                unique_clients.add(cliente_id)
                
                # Convertir a diccionario de manera segura
                cliente_dict = {}
                for column in cliente.__table__.columns:
                    value = getattr(cliente, column.name)
                    
                    # Limpiar espacios en valores string
                    if isinstance(value, str):
                        value = value.strip()
                    
                    # Establecer valores por defecto para valores None
                    if value is None:
                        if isinstance(column.type, (str)):
                            value = ""
                        elif isinstance(column.type, (bool)):
                            value = False
                        elif isinstance(column.type, (int, float)):
                            value = 0
                    
                    cliente_dict[column.name] = value
                
                # Asegurar que todos los campos booleanos están presentes
                boolean_fields = ["activo", "contado", "exento", "retencion", "nosujeto", 
                                "gobierno", "ivacero", "percepcion", "autoconsumo", 
                                "PROPIO", "ExcluirCredito"]
                
                for field in boolean_fields:
                    if field not in cliente_dict or cliente_dict[field] is None:
                        cliente_dict[field] = False
                
                clientes_list.append(cliente_dict)
            
            logger.info(f"Retornando {len(clientes_list)} clientes únicos")
            return clientes_list, total
            
        except Exception as e:
            logger.error(f"Error al obtener clientes: {str(e)}", exc_info=True)
            return [], 0
    
    def search_clientes_optimized(
        self, 
        empresa_id: int, 
        search_term: str, 
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Búsqueda optimizada de clientes para autocompletado.
        Usa el mismo motor de búsqueda que get_clientes_by_empresa para consistencia.
        """
        try:
            search_normalized = self._normalize_search_term(search_term)
            
            # Si el término es muy corto, no buscar
            if not search_normalized or len(search_normalized) < 2:
                logger.debug(f"Término de búsqueda muy corto: '{search_term}'")
                return []
            
            logger.debug(f"Búsqueda optimizada para: '{search_normalized}' (empresa: {empresa_id})")
            
            # Usar el método principal con parámetros optimizados para búsqueda
            clientes, total = self.get_clientes_by_empresa(
                empresa_id=empresa_id,
                activo=True,  # Solo clientes activos en búsquedas
                search=search_normalized,
                skip=0,
                limit=limit
            )
            
            logger.debug(f"Búsqueda devolvió {len(clientes)} resultados de {total} totales")
            return clientes
            
        except Exception as e:
            logger.error(f"Error en búsqueda optimizada: {str(e)}", exc_info=True)
            return []
    
    def get_cliente_by_id(self, cliente_id: str, empresa_id: int) -> Optional[Dict]:
        """
        Obtiene un cliente específico por su ID, dentro de una empresa específica.
        Incluye información de tablas relacionadas.
        """
        try:
            # Limpiar ID de cliente si es string
            if isinstance(cliente_id, str):
                cliente_id = cliente_id.strip()
            
            # Consulta básica con ORM
            cliente = self.db.query(Clientes).filter(
                Clientes.clientes == cliente_id,
                Clientes.empresa == empresa_id
            ).first()
            
            if not cliente:
                return None
            
            # Convertir a diccionario limpiando valores
            cliente_dict = {}
            for column in cliente.__table__.columns:
                value = getattr(cliente, column.name)
                
                # Limpiar espacios en strings
                if isinstance(value, str):
                    value = value.strip()
                
                cliente_dict[column.name] = value
            
            return cliente_dict
        
        except Exception as e:
            logger.error(f"Error al obtener cliente: {str(e)}", exc_info=True)
            return None
    
    def create_cliente(self, empresa_id: int, cliente_data: Dict[str, Any], usuario_id: int) -> Clientes:
        """
        Crea un nuevo cliente para una empresa específica.
        """
        # Generar código de cliente automático si no se proporciona
        if not cliente_data.get("clientes"):
            max_id = self.db.query(func.max(Clientes.idClientes)).filter(
                Clientes.empresa == empresa_id
            ).scalar() or 0
            
            nuevo_id = max_id + 1
            cliente_data["clientes"] = f"C{nuevo_id:07d}"
        
        # Agregar datos por defecto
        current_time = datetime.now()
        cliente_data.update({
            "empresa": empresa_id,
            "usuario": usuario_id,
            "horatiempo": current_time,
            # Valores por defecto para campos obligatorios que podrían no venir
            "activo": cliente_data.get("activo", True),
            "contado": cliente_data.get("contado", False),
            "direccion": cliente_data.get("direccion", ""),
            "telefono1": cliente_data.get("telefono1", ""),
            "telefono2": cliente_data.get("telefono2", ""),
            "celular": cliente_data.get("celular", ""),
            "fax": cliente_data.get("fax", ""),
            "registro": cliente_data.get("registro", ""),
            "nit": cliente_data.get("nit", ""),
            "dui": cliente_data.get("dui", ""),
            "giro": cliente_data.get("giro", ""),
            "propietario": cliente_data.get("propietario", ""),
            "contacto": cliente_data.get("contacto", ""),
            "recomendado": cliente_data.get("recomendado", ""),
            "razonsoc": cliente_data.get("razonsoc", ""),
            "notas": cliente_data.get("notas", ""),
            "saldo": cliente_data.get("saldo", "0"),
            "tipcli": cliente_data.get("tipcli", 1),  # Valor por defecto para tipo de cliente
            "municip": cliente_data.get("municip", 1),  # Valor por defecto para municipio
            "condpago": cliente_data.get("condpago", 1),  # Valor por defecto para condición de pago
            "prodprec": cliente_data.get("prodprec", 1),  # Valor por defecto para lista de precios
            "cliencatego": cliente_data.get("cliencatego", 1),  # Valor por defecto para categoría
            "moneda": cliente_data.get("moneda", 1),  # Valor por defecto para moneda
            "transpte": cliente_data.get("transpte", 0),
            "exento": cliente_data.get("exento", False),
            "descuento": cliente_data.get("descuento", 0),
            "promcomp": cliente_data.get("promcomp", 0),
            "prompago": cliente_data.get("prompago", 0),
            "limitecredito": cliente_data.get("limitecredito", 0),
            "retencion": cliente_data.get("retencion", False),
            "contrato": cliente_data.get("contrato", False),
            "casa": cliente_data.get("casa", ""),
            "telecasa": cliente_data.get("telecasa", ""),
            "trabajo": cliente_data.get("trabajo", ""),
            "cargo": cliente_data.get("cargo", ""),
            "profesion": cliente_data.get("profesion", ""),
            "teletrabajo": cliente_data.get("teletrabajo", ""),
            "direcciont": cliente_data.get("direcciont", ""),
            "fuente1": cliente_data.get("fuente1", ""),
            "ing1": cliente_data.get("ing1", ""),
            "firma": cliente_data.get("firma", ""),
            "gastos1": cliente_data.get("gastos1", ""),
            "conyuge": cliente_data.get("conyuge", ""),
            "sueldo2": cliente_data.get("sueldo2", ""),
            "trabajo2": cliente_data.get("trabajo2", ""),
            "teletrabajo2": cliente_data.get("teletrabajo2", ""),
            "gastos2": cliente_data.get("gastos2", ""),
            "tel1": cliente_data.get("tel1", ""),
            "referencia1": cliente_data.get("referencia1", ""),
            "relacion1": cliente_data.get("relacion1", ""),
            "referencia2": cliente_data.get("referencia2", ""),
            "tel2": cliente_data.get("tel2", ""),
            "relacion2": cliente_data.get("relacion2", ""),
            "referencia3": cliente_data.get("referencia3", ""),
            "tel3": cliente_data.get("tel3", ""),
            "relacion3": cliente_data.get("relacion3", ""),
            "referencia4": cliente_data.get("referencia4", ""),
            "tel4": cliente_data.get("tel4", ""),
            "relacion4": cliente_data.get("relacion4", ""),
            "notas2": cliente_data.get("notas2", ""),
            "ivacero": cliente_data.get("ivacero", False),
            "PROPIO": cliente_data.get("PROPIO", False),
            "PDESC": cliente_data.get("PDESC", 0),
            "ZONA": cliente_data.get("ZONA", 0),
            "bodega": cliente_data.get("bodega", 1),
            "direnvio": cliente_data.get("direnvio", ""),
            "agrupaclientes": cliente_data.get("agrupaclientes", 0),
            "vendedor": cliente_data.get("vendedor", 0),
            "preciovineta": cliente_data.get("preciovineta", 0),
            "percepcion": cliente_data.get("percepcion", False),
            "nosujeto": cliente_data.get("nosujeto", False),
            "comisionagencia": cliente_data.get("comisionagencia", 0),
            "CargoFULL": cliente_data.get("CargoFULL", False),
            "marchamo": cliente_data.get("marchamo", False),
            "vendedor2": cliente_data.get("vendedor2", 0),
            "pais": cliente_data.get("pais", 1),
            "autoconsumo": cliente_data.get("autoconsumo", False),
            "gobierno": cliente_data.get("gobierno", False),
            "cuenta": cliente_data.get("cuenta", 0),
            "cuentaProveedor": cliente_data.get("cuentaProveedor", 0),
            "ExcluirCredito": cliente_data.get("ExcluirCredito", False),
            "conPagare": cliente_data.get("conPagare", False),
            "Verificado": cliente_data.get("Verificado", False),
            "descEspecial": cliente_data.get("descEspecial", False),
            "valorreferencia1": cliente_data.get("valorreferencia1", 0),
            "valorreferencia2": cliente_data.get("valorreferencia2", 0),
            "valorreferencia3": cliente_data.get("valorreferencia3", 0),
            "valorreferencia4": cliente_data.get("valorreferencia4", 0),
            "noPagare": cliente_data.get("noPagare", ""),
            "montoref1": cliente_data.get("montoref1", 0),
            "montoref2": cliente_data.get("montoref2", 0),
            "montoref3": cliente_data.get("montoref3", 0),
            "montoref4": cliente_data.get("montoref4", 0),
            "pagarenotas": cliente_data.get("pagarenotas", ""),
            "pagareok": cliente_data.get("pagareok", False),
            "socio": cliente_data.get("socio", False),
            "prima": cliente_data.get("prima", 0),
            "cuota": cliente_data.get("cuota", 0),
            "fechacontrato": cliente_data.get("fechacontrato", current_time),
            "diapago": cliente_data.get("diapago", 0),
            "carnetactualizado": cliente_data.get("carnetactualizado", False),
            "suspendido": cliente_data.get("suspendido", False),
            "r1": cliente_data.get("r1", False),
            "r2": cliente_data.get("r2", False),
            "r3": cliente_data.get("r3", False),
            "r4": cliente_data.get("r4", False),
            "caja": cliente_data.get("caja", 0),
            "noCuotas": cliente_data.get("noCuotas", 0),
            "noContrato": cliente_data.get("noContrato", ""),
            "montoprima": cliente_data.get("montoprima", 0),
            "mesa": cliente_data.get("mesa", False),
            "nopropina": cliente_data.get("nopropina", False),
            "pprima": cliente_data.get("pprima", 0),
            "cuotas": cliente_data.get("cuotas", 0),
            "letras": cliente_data.get("letras", 0),
            "nomesa": cliente_data.get("nomesa", 0),
            "cuentamaestra": cliente_data.get("cuentamaestra", ""),
            "descautorizado": cliente_data.get("descautorizado", 0),
            "notaautorizado": cliente_data.get("notaautorizado", ""),
            "micolor": cliente_data.get("micolor", 0),
            "rangocliente": cliente_data.get("rangocliente", 0),
            "cobrodomicilio": cliente_data.get("cobrodomicilio", False),
            "factura": cliente_data.get("factura", True),
            "tiquet": cliente_data.get("tiquet", False),
            "efectivo": cliente_data.get("efectivo", True),
            "cheque": cliente_data.get("cheque", False),
            "otros": cliente_data.get("otros", False),
            "tarjeta": cliente_data.get("tarjeta", False),
            # No incluimos campos calculados o que deben ser nulos por defecto
        })
        
        # Crear el cliente
        nuevo_cliente = Clientes(**cliente_data)
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        
        return nuevo_cliente
    
    def update_cliente(self, cliente_id: str, empresa_id: int, cliente_data: Dict[str, Any], usuario_id: int) -> Optional[Clientes]:
        """
        Actualiza un cliente existente.
        """
        cliente = self.db.query(Clientes).filter(
            Clientes.clientes == cliente_id,
            Clientes.empresa == empresa_id
        ).first()
        
        if not cliente:
            return None
        
        # Actualizar información del cliente
        for key, value in cliente_data.items():
            # No actualizar claves primarias
            if key not in ['clientes', 'empresa', 'idClientes']:
                setattr(cliente, key, value)
        
        # Actualizar usuario y hora
        cliente.usuario = usuario_id
        cliente.horatiempo = datetime.now()
        
        self.db.commit()
        self.db.refresh(cliente)
        
        return cliente
    
    def delete_cliente(self, cliente_id: str, empresa_id: int) -> bool:
        """
        Elimina un cliente (marcándolo como inactivo).
        No realizamos eliminación física para mantener integridad referencial.
        """
        cliente = self.db.query(Clientes).filter(
            Clientes.clientes == cliente_id,
            Clientes.empresa == empresa_id
        ).first()
        
        if not cliente:
            return False
        
        # Marcar como inactivo en lugar de eliminar físicamente
        cliente.activo = False
        self.db.commit()
        
        return True
    
    def get_clientes_por_tipo(self, empresa_id: int) -> Dict[str, List[Clientes]]:
        """
        Obtiene clientes categorizados por tipo (individuales, corporativos, etc.)
        """
        # Consulta base para clientes activos de la empresa
        base_query = self.db.query(Clientes).filter(
            Clientes.empresa == empresa_id,
            Clientes.activo == True
        )
        
        # Clientes individuales (tipcli=1 es un ejemplo, ajusta según tu sistema)
        individuales = base_query.filter(Clientes.tipcli == 1).order_by(Clientes.nclientes).all()
        
        # Clientes corporativos (tipcli=2 es un ejemplo, ajusta según tu sistema)
        corporativos = base_query.filter(Clientes.tipcli == 2).order_by(Clientes.nclientes).all()
        
        # Clientes al contado
        contado = base_query.filter(Clientes.contado == True).order_by(Clientes.nclientes).all()
        
        # Clientes a crédito (no contado)
        credito = base_query.filter(Clientes.contado == False).order_by(Clientes.nclientes).all()
        
        return {
            "individuales": individuales,
            "corporativos": corporativos,
            "contado": contado,
            "credito": credito
        }