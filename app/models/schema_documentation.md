# Documentación del Esquema de Base de Datos

Generado: 2025-05-13 16:44:58

## Resumen
- Total de esquemas: 1
- Total de tablas: 559

## Esquema: dbo
- Tablas: 559

### Tabla: AddingsClientes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipomov | INTEGER | ✓ |  |
| caja | INTEGER | ✓ |  |
| serie | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| resolucion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME | ✓ |  |
| activo | BIT |  |  |
| AddingsClientes | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| descrip | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: AddingsProveedor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| proveedor | INTEGER | ✓ |  |
| ccuenta | INTEGER | ✓ |  |
| serie | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| resolucion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| AddingsProveedor | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: BodegaPais
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| bodegapais | BIGINT |  | ✓ |
| pais | INTEGER |  |  |
| Orden | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: Bodeguero
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nBodeguero | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Bodeguero | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_Bodeguero_Bodeguero: ['Bodeguero'] 
- IX_Bodeguero_nBodeguero: ['nBodeguero'] 
- IX_Bodeguero_usuario: ['usuario'] 

### Tabla: Candidato
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| codisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nempleado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| aempleado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nombisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| foto | IMAGE | ✓ |  |
| sexo | INTEGER | ✓ |  |
| nacional | INTEGER | ✓ |  |
| pais | INTEGER | ✓ |  |
| depto | INTEGER | ✓ |  |
| municip | INTEGER | ✓ |  |
| fechnac | DATETIME | ✓ |  |
| lugarnac | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| estcivil | INTEGER | ✓ |  |
| profesion | INTEGER | ✓ |  |
| direccemp | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tiposan | INTEGER | ✓ |  |
| fechacont | DATETIME | ✓ |  |
| vencontra | DATETIME | ✓ |  |
| fecharet | DATETIME | ✓ |  |
| seccion | INTEGER | ✓ |  |
| cargo | INTEGER | ✓ |  |
| ntarjeta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| jornada | INTEGER | ✓ |  |
| sueldiario | NUMERIC(18, 6) | ✓ |  |
| suelmen | NUMERIC(18, 6) | ✓ |  |
| formpago | INTEGER | ✓ |  |
| nit | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cip | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| carelect | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| carmino | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| permintr | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| liccond | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pasaport | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nup | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cuentab | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipocta | INTEGER | ✓ |  |
| banco | INTEGER | ✓ |  |
| afp | INTEGER | ✓ |  |
| procurad | BIT | ✓ |  |
| horasext | BIT | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| cuenta | INTEGER | ✓ |  |
| ctrocosto | INTEGER | ✓ |  |
| afpv | NUMERIC(18, 6) | ✓ |  |
| afpvp | NUMERIC(18, 6) | ✓ |  |
| Empleado | INTEGER | ✓ |  |
| Candidato | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empcubanco | INTEGER | ✓ |  |
| sueldiarioseg | NUMERIC(18, 6) | ✓ |  |
| suelmenseg | NUMERIC(18, 6) | ✓ |  |
| afpvseg | NUMERIC(18, 6) | ✓ |  |
| afpvpseg | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| tipoplaza | INTEGER | ✓ |  |
| jubilado | BIT | ✓ |  |
| codreloj | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| contrato | BIT | ✓ |  |
| gerente | BIT | ✓ |  |
| jefe | BIT | ✓ |  |
| supervisor | BIT | ✓ |  |
| autoriza | BIT | ✓ |  |
| miImagen | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| aprobadorrhh | BIT |  |  |
| aprobadojefe | BIT |  |  |
| faprobadorrhh | DATETIME | ✓ |  |
| faprobadojefe | DATETIME | ✓ |  |

### Tabla: CategoriaBien
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nCategoriaBien | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Codigo | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| CategoriaBien | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: CategoriaNomina
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| CategoriaNomina | INTEGER |  |  |
| nCategoriaNomina | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Sancion | BIT |  |  |
| Reconocimiento | BIT |  |  |
| capacitacion | BIT |  |  |
| Titulos | BIT |  |  |
| asensos | BIT |  |  |
| permisos | BIT |  |  |
| inacistencias | BIT |  |  |
| accidentes | BIT |  |  |
| solicitudEmpleo | BIT |  |  |
| despido | BIT |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_CategoriaNomina: ['CategoriaNomina'] 

### Tabla: ClientesDocs
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ClientesDocs | INTEGER |  |  |
| nClientesDocs | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ClientesDocsRef | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_ClientesDocs: ['ClientesDocs'] 

### Tabla: Clientes_caja
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| caja | INTEGER |  |  |
| clientes | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clientes_caja | INTEGER |  | ✓ |

### Tabla: ComisionAgencia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| pDesc | NUMERIC(5, 2) |  |  |
| Encomienda | NUMERIC(16, 6) |  |  |
| Comision | NUMERIC(16, 6) |  |  |
| Retencion | NUMERIC(16, 6) |  |  |
| contabilidad | BIT |  |  |
| ComisionAgencia | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| umail | INTEGER |  |  |
| vmail | NUMERIC(18, 6) |  |  |
| viatico | NUMERIC(18, 6) |  |  |
| otros | NUMERIC(18, 6) |  |  |
| noremesado | NUMERIC(18, 6) |  |  |
| unulas | INTEGER |  |  |
| nulas | NUMERIC(18, 6) |  |  |
| otrosdesc | NUMERIC(18, 6) |  |  |
| banco | INTEGER |  |  |
| condpago | INTEGER |  |  |
| mes | DATETIME |  |  |
| minimo | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Maximo | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| remesado | NUMERIC(18, 6) |  |  |
| renta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| impresa | BIT |  |  |
| noitems | INTEGER |  |  |
| montfact | NUMERIC(18, 6) |  |  |

#### Índices
- IX_ComisionAgencia_banco: ['banco'] 
- IX_ComisionAgencia_clientes: ['clientes'] 
- IX_ComisionAgencia_ComisionAgencia: ['ComisionAgencia'] 
- IX_ComisionAgencia_condpago: ['condpago'] 
- IX_ComisionAgencia_empresa: ['empresa'] 
- IX_ComisionAgencia_Maximo: ['Maximo'] 
- IX_ComisionAgencia_minimo: ['minimo'] 
- IX_ComisionAgencia_noitems: ['noitems'] 
- IX_ComisionAgencia_umail: ['umail'] 
- IX_ComisionAgencia_unulas: ['unulas'] 
- IX_ComisionAgencia_usuario: ['usuario'] 

### Tabla: ConceptoDiezmo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ConceptoDiezmo | INTEGER |  |  |
| nConceptoDiezmo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| diezmo | BIT |  |  |
| ofrenda | BIT |  |  |
| primicia | BIT |  |  |
| evento | BIT |  |  |
| festividad | BIT |  |  |
| siembra | BIT |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_ConceptoDiezmo: ['ConceptoDiezmo'] 

### Tabla: ConciliaBancos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ConciliaBancos | INTEGER |  | ✓ |
| tipopart | INTEGER |  |  |
| partida | INTEGER |  |  |
| cuentaBanco | INTEGER |  |  |
| FechaBanco | DATETIME |  |  |
| noEstadoCuenta | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Debe | NUMERIC(18, 6) |  |  |
| haber | NUMERIC(18, 6) |  |  |
| conciliado | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: ControlRegistro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ControlRegistro | INTEGER |  | ✓ |
| modulo | INTEGER |  |  |
| netdata | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| Empresa | INTEGER |  |  |
| Usuario | INTEGER |  |  |

#### Índices
- IX_ControlRegistro_ControlRegistro: ['ControlRegistro'] 
- IX_ControlRegistro_Empresa: ['Empresa'] 
- IX_ControlRegistro_modulo: ['modulo'] 
- IX_ControlRegistro_netdata: ['netdata'] 
- IX_ControlRegistro_Usuario: ['Usuario'] 

### Tabla: ControlSolicitud
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| OrdenTrabajo | INTEGER |  |  |
| nControlSolicitud | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaSolicitud | DATETIME | ✓ |  |
| fechaEntrega | DATETIME | ✓ |  |
| fechaInicial | DATETIME | ✓ |  |
| fechaTermino | DATETIME | ✓ |  |
| empleado | INTEGER |  |  |
| PrecioBudget | NUMERIC(16, 6) |  |  |
| PrecioReal | NUMERIC(16, 6) |  |  |
| Observaciones | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| ControlSolicitud | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ControlSolicitud_Clientes: ['Clientes'] 
- IX_ControlSolicitud_ControlSolicitud: ['ControlSolicitud'] 
- IX_ControlSolicitud_empleado: ['empleado'] 
- IX_ControlSolicitud_empresa: ['empresa'] 
- IX_ControlSolicitud_nControlSolicitud: ['nControlSolicitud'] 
- IX_ControlSolicitud_Observaciones: ['Observaciones'] 
- IX_ControlSolicitud_OrdenTrabajo: ['OrdenTrabajo'] 
- IX_ControlSolicitud_usuario: ['usuario'] 

### Tabla: CostoTipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nCostoTipo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Codigo | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| CostoTipo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: Diezmo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Diezmo | INTEGER |  |  |
| Numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| distrito | INTEGER |  |  |
| lider | INTEGER |  |  |
| entrega | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| conceptodiezmo | INTEGER |  |  |

#### Índices
- ci_azure_fixup_dbo_Diezmo: ['Diezmo'] 

### Tabla: Distrito
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Distrito | INTEGER |  |  |
| nDistrito | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_Distrito: ['Distrito'] 

### Tabla: Documentoviaje
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| DocumentoViaje | INTEGER |  | ✓ |
| nDocumentoViaje | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: Entrega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| entrega | INTEGER |  |  |
| nEntrega | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_Entrega: ['entrega'] 

### Tabla: Fabricacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fabricacion | INTEGER |  | ✓ |
| nfabricacion | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: Factdelivery
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfactura | INTEGER | ✓ |  |
| cant1 | NUMERIC(9, 2) | ✓ |  |
| cant2 | NUMERIC(9, 2) | ✓ |  |
| cant3 | NUMERIC(9, 2) | ✓ |  |
| cant4 | NUMERIC(9, 2) | ✓ |  |
| cant5 | NUMERIC(9, 2) | ✓ |  |
| cant6 | NUMERIC(9, 2) | ✓ |  |
| cant7 | NUMERIC(9, 2) | ✓ |  |
| cant8 | NUMERIC(9, 2) | ✓ |  |
| cant9 | NUMERIC(9, 2) | ✓ |  |
| cant10 | NUMERIC(9, 2) | ✓ |  |
| cant11 | NUMERIC(9, 2) | ✓ |  |
| cant12 | NUMERIC(9, 2) | ✓ |  |
| cant13 | NUMERIC(9, 2) | ✓ |  |
| cant14 | NUMERIC(9, 2) | ✓ |  |
| cant15 | NUMERIC(9, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| Factdelivery | INTEGER |  | ✓ |

### Tabla: FacturaPago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| Monto | NUMERIC(12, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| FacturaPago | INTEGER |  | ✓ |

### Tabla: FormatoNominas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| FormatoNomina | INTEGER |  |  |
| nFormatoNomina | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fFormatoNomina | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_FormatoNominas: ['FormatoNomina'] 

### Tabla: FranjaHoraria
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nFranjaHoraria | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Hora1 | NUMERIC(5, 2) |  |  |
| Hora2 | NUMERIC(5, 2) |  |  |
| MesInvierno | INTEGER |  |  |
| HoraMesInvierno | INTEGER |  |  |
| FranjaHoraria | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: GastoAnticipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nGastoAnticipo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| GastoAnticipo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: GestionTaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| GestionTaller | INTEGER |  | ✓ |
| tipomov | INTEGER |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| lote | INTEGER |  |  |
| fase | INTEGER |  |  |
| numedocu | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fecvence | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| suspendida | BIT |  |  |
| aReservado | BIT |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| adicion | BIT |  |  |
| devolucion | BIT |  |  |
| perdida | NUMERIC(18, 6) |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rupstatus | INTEGER |  |  |
| camion | INTEGER |  |  |
| rupfase | INTEGER |  |  |
| RTFrontNew | BIT |  |  |
| RTFrontRecord | BIT |  |  |
| RTFrontFlat | BIT |  |  |
| LTFrontNew | BIT |  |  |
| LTFrontRecord | BIT |  |  |
| LTFrontFlat | BIT |  |  |
| STNew | BIT |  |  |
| STRecord | BIT |  |  |
| STFlat | BIT |  |  |
| RTBackNew | BIT |  |  |
| RTBackRecord | BIT |  |  |
| RTBackFlat | BIT |  |  |
| LTBackNew | BIT |  |  |
| LTBackRecord | BIT |  |  |
| LTBackFlat | BIT |  |  |
| Mica | BIT |  |  |
| Spanner | BIT |  |  |
| Tools | BIT |  |  |
| extinguisher | BIT |  |  |
| triangles | BIT |  |  |
| GasCap | BIT |  |  |
| CCard | BIT |  |  |
| fuelTank | VARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| LMirror | BIT |  |  |
| RMirror | BIT |  |  |
| RVMirror | BIT |  |  |
| Stereo | BIT |  |  |
| lighter | BIT |  |  |
| TSlock | BIT |  |  |
| PadLock | BIT |  |  |
| GoodSeat | BIT |  |  |
| BrokenSeat | BIT |  |  |
| DirtySeat | BIT |  |  |
| BSFront | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| BSLeft | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| BSRight | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| BSBack | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| kilometraje | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| formulataller | INTEGER |  |  |
| motorista | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| comments | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| facturado | BIT |  |  |
| fechafin | DATETIME | ✓ |  |

#### Foreign Keys
- ['camion'] → camion.['camion']
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']

### Tabla: HistoricoNomina
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| HistoricoNomina | INTEGER |  |  |
| categoriaNomina | INTEGER |  |  |
| fecha | DATETIME |  |  |
| empleado | INTEGER |  |  |
| fHistoricoNomina | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_HistoricoNomina: ['HistoricoNomina'] 

### Tabla: Incapacidad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Incapacidad | INTEGER |  | ✓ |
| inicio | DATETIME | ✓ |  |
| fin | DATETIME | ✓ |  |
| nIncapacidad | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| TipoIncapacidad | INTEGER | ✓ |  |
| Planilla | INTEGER | ✓ |  |
| empleado | INTEGER |  |  |
| activo | BIT |  |  |
| ndias | INTEGER | ✓ |  |
| montopago | NUMERIC(18, 6) | ✓ |  |
| fechareg | DATETIME | ✓ |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_Incapacidad_empleado: ['empleado'] 
- IX_Incapacidad_empresa: ['empresa'] 
- IX_Incapacidad_Incapacidad: ['Incapacidad'] 
- IX_Incapacidad_nIncapacidad: ['nIncapacidad'] 
- IX_Incapacidad_Planilla: ['Planilla'] 
- IX_Incapacidad_TipoIncapacidad: ['TipoIncapacidad'] 
- IX_Incapacidad_usuario: ['usuario'] 

### Tabla: IntervalDesc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| IntervalDesc | INTEGER |  | ✓ |
| interval1 | INTEGER | ✓ |  |
| interval2 | INTEGER | ✓ |  |
| interval3 | INTEGER | ✓ |  |
| interval4 | INTEGER | ✓ |  |
| interval5 | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| diasgracia | INTEGER |  |  |

### Tabla: IntervaloPauta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nIntervaloPauta | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Lunes | BIT |  |  |
| Martes | BIT |  |  |
| Miercoles | BIT |  |  |
| Jueves | BIT |  |  |
| viernes | BIT |  |  |
| sabado | BIT |  |  |
| domingo | BIT |  |  |
| IntervaloPauta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: JornadaRuta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| JornadaRuta | INTEGER |  |  |
| nJornadaRuta | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| residuos | BIT |  |  |

#### Índices
- ci_azure_fixup_dbo_JornadaRuta: ['JornadaRuta'] 

### Tabla: Lider
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Lider | INTEGER |  |  |
| nLider | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_Lider: ['Lider'] 

### Tabla: MIPERIODO
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| FECHA | DATETIME |  |  |
| PERIODO | INTEGER |  |  |
| ACTIVO | BIT |  |  |

#### Índices
- IX_MIPERIODO_FECHA: ['FECHA'] 
- IX_MIPERIODO_PERIODO: ['PERIODO'] 

### Tabla: MiFlujoProy
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| MiFlujoProy | INTEGER |  | ✓ |
| Anio | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| descripcion | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Enero | NUMERIC(18, 6) |  |  |
| Febrero | NUMERIC(18, 6) |  |  |
| Marzo | NUMERIC(18, 6) |  |  |
| Abril | NUMERIC(18, 6) |  |  |
| Mayo | NUMERIC(18, 6) |  |  |
| Junio | NUMERIC(18, 6) |  |  |
| Julio | NUMERIC(18, 6) |  |  |
| Agosto | NUMERIC(18, 6) |  |  |
| Septiembre | NUMERIC(18, 6) |  |  |
| Octubre | NUMERIC(18, 6) |  |  |
| Noviembre | NUMERIC(18, 6) |  |  |
| Diciembre | NUMERIC(18, 6) |  |  |
| TipoFlujo | INTEGER |  |  |
| nocuenta | INTEGER |  |  |

### Tabla: MiMensaje
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| MiMensaje | INTEGER |  | ✓ |
| nMiMensaje | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| longitud | INTEGER |  |  |
| Preferido | BIT |  |  |
| Activo | BIT |  |  |
| Empresa | INTEGER |  |  |
| Usuario | INTEGER |  |  |

#### Índices
- IX_MiMensaje_Empresa: ['Empresa'] 
- IX_MiMensaje_longitud: ['longitud'] 
- IX_MiMensaje_MiMensaje: ['MiMensaje'] 
- IX_MiMensaje_nMiMensaje: ['nMiMensaje'] 
- IX_MiMensaje_Usuario: ['Usuario'] 

### Tabla: Naturaleza
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Naturaleza | INTEGER |  | ✓ |
| nNaturaleza | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| Notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| rubro | INTEGER | ✓ |  |
| grupo | INTEGER | ✓ |  |
| nrubro | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: OcultaBodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| OcultaBodega | INTEGER |  | ✓ |
| bodega | INTEGER |  |  |
| caja | INTEGER |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: OrdenTrabajo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| OrdenTrabajo | INTEGER |  | ✓ |
| tipomov | INTEGER |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| lote | INTEGER |  |  |
| fase | INTEGER |  |  |
| numedocu | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fecvence | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| suspendida | BIT |  |  |
| aReservado | BIT |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| adicion | BIT |  |  |
| devolucion | BIT |  |  |
| perdida | NUMERIC(18, 6) |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rupstatus | INTEGER |  |  |
| rupfase | INTEGER |  |  |
| deltaTiempo | NUMERIC(18, 6) |  |  |
| Batch | NUMERIC(18, 6) |  |  |
| BatchNo | INTEGER |  |  |
| producido | NUMERIC(18, 6) |  |  |
| fechaplan | DATETIME |  |  |
| bodegaInsumos | INTEGER |  |  |
| totalbatch | INTEGER |  |  |
| fechapesada | DATETIME |  |  |
| ControlSolicitud | INTEGER |  |  |

### Tabla: PerfilUsuario
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| PerfilUsuario | INTEGER |  | ✓ |
| nPerfilUsuario | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| supervisor | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| nivel | INTEGER |  |  |
| uno | BIT |  |  |
| dos | BIT |  |  |
| tres | BIT |  |  |
| cuatro | BIT |  |  |
| cinco | BIT |  |  |
| seis | BIT |  |  |
| siete | BIT |  |  |
| ocho | BIT |  |  |
| nueve | BIT |  |  |
| diez | BIT |  |  |
| veCostos | BIT |  |  |
| puedeBackup | BIT |  |  |
| PuedePrecio | BIT |  |  |
| puedepermiso | BIT |  |  |
| conta1 | BIT |  |  |
| conta2 | BIT |  |  |
| conta3 | BIT |  |  |
| conta4 | BIT |  |  |
| conta5 | BIT |  |  |
| conta6 | BIT |  |  |
| vecxc | BIT |  |  |
| puedecantidad | BIT |  |  |
| saltaPrecio | BIT |  |  |
| superventas | BIT |  |  |
| precio1 | BIT |  |  |
| precio2 | BIT |  |  |
| precio3 | BIT |  |  |
| precio4 | BIT |  |  |
| precio5 | BIT |  |  |

### Tabla: Perfilaccesos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| PerfilUsuario | INTEGER |  |  |
| proceso | INTEGER |  |  |
| acceso | BIT |  |  |
| crear | BIT |  |  |
| modificar | BIT |  |  |
| eliminar | BIT |  |  |
| imprimir | BIT |  |  |
| excel | BIT |  |  |
| PERFILaccesos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| monto | NUMERIC(18, 6) |  |  |

### Tabla: PreparaJornada
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| PreparaJornada | INTEGER |  |  |
| JornadaRuta | INTEGER | ✓ |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| fecha | DATETIME |  |  |
| notas | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Precio | NUMERIC(18, 6) | ✓ |  |
| numtiquet | INTEGER | ✓ |  |
| fnumtiquet | INTEGER | ✓ |  |
| producto | INTEGER | ✓ |  |
| bodega | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_PreparaJornada: ['PreparaJornada'] 

### Tabla: PreparaPedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| PreparaPedido | INTEGER |  |  |
| Prioridad | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| factura | INTEGER | ✓ |  |
| bodeguero | INTEGER | ✓ |  |
| rupStatus | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cambodega | INTEGER |  |  |
| preparar | BIT |  |  |
| Preparado | BIT |  |  |
| bultos | INTEGER |  |  |
| terminarpedido | DATETIME | ✓ |  |
| prepararpedido | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_PreparaPedido: ['PreparaPedido'] 

### Tabla: PreparaRemision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| PreparaRemision | INTEGER |  |  |
| Prioridad | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| cambodega | INTEGER | ✓ |  |
| bodeguero | INTEGER | ✓ |  |
| rupStatus | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: ProductoUnidadVenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Producto | INTEGER |  |  |
| UnidadVenta | INTEGER |  |  |
| Factor | NUMERIC(16, 6) |  |  |
| Preferido | BIT |  |  |
| Activo | BIT |  |  |
| ProductoUnidadVenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| Precio | NUMERIC(16, 6) |  |  |

#### Índices
- IX_ProductoUnidadVenta_empresa: ['empresa'] 
- IX_ProductoUnidadVenta_Producto: ['Producto'] 
- IX_ProductoUnidadVenta_ProductoUnidadVenta: ['ProductoUnidadVenta'] 
- IX_ProductoUnidadVenta_UnidadVenta: ['UnidadVenta'] 
- IX_ProductoUnidadVenta_usuario: ['usuario'] 

### Tabla: ProvisionGasto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| provisionGasto | INTEGER |  | ✓ |
| numedocu | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| Afecta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| fovial | NUMERIC(18, 6) |  |  |
| excluidos | NUMERIC(18, 6) |  |  |
| partida | INTEGER |  |  |
| renta | NUMERIC(18, 6) | ✓ |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| iva | INTEGER |  |  |
| cotrans | NUMERIC(16, 6) | ✓ |  |
| declarable | BIT |  |  |
| PERCEPCION | NUMERIC(18, 6) |  |  |
| deduccion1 | NUMERIC(18, 6) |  |  |
| deduccion2 | NUMERIC(18, 6) |  |  |
| linea | INTEGER |  |  |
| Cuenta | INTEGER | ✓ |  |
| cesc | NUMERIC(12, 2) | ✓ |  |
| serie | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['iva'] → iva.['iva']

#### Índices
- IX_ProvisionGasto_empresa: ['empresa'] 
- IX_ProvisionGasto_fecha: ['fecha'] 
- IX_ProvisionGasto_iva: ['iva'] 
- IX_ProvisionGasto_partida: ['partida'] 
- IX_ProvisionGasto_provisionGasto: ['provisionGasto'] 
- IX_ProvisionGasto_usuario: ['usuario'] 

### Tabla: REMESA
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| remesa | INTEGER |  | ✓ |
| fecha | DATETIME | ✓ |  |
| monto | NUMERIC(19, 8) | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| numero | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| banco | INTEGER | ✓ |  |
| saldo | NUMERIC(19, 8) | ✓ |  |
| contado | BIT | ✓ |  |
| noReserva | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| escheque | BIT |  |  |
| venta | BIT |  |  |
| credito | NUMERIC(18, 6) |  |  |
| tarjeta | NUMERIC(18, 6) |  |  |
| cheque | NUMERIC(18, 6) |  |  |
| valor | NUMERIC(18, 6) |  |  |
| tipomov | INTEGER |  |  |
| noitems | INTEGER |  |  |
| caja | INTEGER |  |  |
| saldocaja | BIT |  |  |
| estarjeta | BIT |  |  |
| fechadoc | DATETIME |  |  |

#### Índices
- IX_REMESA_banco: ['banco'] 
- IX_REMESA_caja: ['caja'] 
- IX_REMESA_empresa: ['empresa'] 
- IX_REMESA_fecha: ['fecha'] 
- IX_REMESA_noitems: ['noitems'] 
- IX_REMESA_noReserva: ['noReserva'] 
- IX_REMESA_numero: ['numero'] 
- IX_REMESA_remesa: ['remesa'] 
- IX_REMESA_tipomov: ['tipomov'] 
- IX_REMESA_usuario: ['usuario'] 

### Tabla: RangoCliente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRangoCliente | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| RangoCliente | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |

### Tabla: RazonFinan
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nRazonFinan | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| monto | NUMERIC(18, 6) |  |  |
| RazonFinan | INTEGER |  | ✓ |
| proyectado | NUMERIC(18, 6) |  |  |
| grupo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| orden | INTEGER |  |  |
| fecha | DATETIME | ✓ |  |
| tipo | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: RecintoFiscal
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nRecintoFiscal | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| RecintoFiscal | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| contacto | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cuotam3 | NUMERIC(18, 6) |  |  |
| cuotam3seg | NUMERIC(18, 6) |  |  |

### Tabla: RegistroGarantia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME | ✓ |  |
| Clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodeguero | INTEGER |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| registroGarantia | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_RegistroGarantia_bodeguero: ['bodeguero'] 
- IX_RegistroGarantia_Clientes: ['Clientes'] 
- IX_RegistroGarantia_fecha: ['fecha'] 
- IX_RegistroGarantia_notas: ['notas'] 
- IX_RegistroGarantia_Numedocu: ['Numedocu'] 
- IX_RegistroGarantia_registroGarantia: ['registroGarantia'] 
- IX_RegistroGarantia_usuario: ['usuario'] 

### Tabla: RegistroProducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| compra | INTEGER |  |  |
| producto | INTEGER |  |  |
| serie | NCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| fechaVence | DATETIME | ✓ |  |
| bodega | INTEGER |  |  |
| registoProducto | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |

#### Foreign Keys
- ['producto'] → producto.['producto']

#### Índices
- IX_RegistroProducto_bodega: ['bodega'] 
- IX_RegistroProducto_compra: ['compra'] 
- IX_RegistroProducto_producto: ['producto'] 
- IX_RegistroProducto_registoProducto: ['registoProducto'] 
- IX_RegistroProducto_usuario: ['usuario'] 

### Tabla: RemesaAgencia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Banco | INTEGER |  |  |
| Remesa | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME | ✓ |  |
| Monto | NUMERIC(16, 6) |  |  |
| Activo | BIT |  |  |
| RemesaAgencia | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RemesaAgencia_Banco: ['Banco'] 
- IX_RemesaAgencia_Clientes: ['Clientes'] 
- IX_RemesaAgencia_empresa: ['empresa'] 
- IX_RemesaAgencia_fecha: ['fecha'] 
- IX_RemesaAgencia_Remesa: ['Remesa'] 
- IX_RemesaAgencia_RemesaAgencia: ['RemesaAgencia'] 
- IX_RemesaAgencia_usuario: ['usuario'] 

### Tabla: RupActividad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RupFase | INTEGER |  |  |
| nRupActividad | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Orden | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| RupActividad | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rupResponsable | INTEGER | ✓ |  |

#### Índices
- IX_RupActividad_empresa: ['empresa'] 
- IX_RupActividad_nRupActividad: ['nRupActividad'] 
- IX_RupActividad_Orden: ['Orden'] 
- IX_RupActividad_RupActividad: ['RupActividad'] 
- IX_RupActividad_RupFase: ['RupFase'] 
- IX_RupActividad_usuario: ['usuario'] 

### Tabla: RupComponente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RupEntregable | INTEGER |  |  |
| RupCompResponsable | INTEGER |  |  |
| nRupComponente | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ParaCuandoComp | DATETIME | ✓ |  |
| Activo | BIT |  |  |
| RupComponente | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupComponente_empresa: ['empresa'] 
- IX_RupComponente_nRupComponente: ['nRupComponente'] 
- IX_RupComponente_RupComponente: ['RupComponente'] 
- IX_RupComponente_RupCompResponsable: ['RupCompResponsable'] 
- IX_RupComponente_RupEntregable: ['RupEntregable'] 
- IX_RupComponente_usuario: ['usuario'] 

### Tabla: RupEntregable
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RupOT | INTEGER |  |  |
| RupEntResponsable | INTEGER |  |  |
| nRupEntregable | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ParaCuandoEnt | DATETIME | ✓ |  |
| Activo | BIT |  |  |
| RupEntregable | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupEntregable_empresa: ['empresa'] 
- IX_RupEntregable_nRupEntregable: ['nRupEntregable'] 
- IX_RupEntregable_RupEntregable: ['RupEntregable'] 
- IX_RupEntregable_RupEntResponsable: ['RupEntResponsable'] 
- IX_RupEntregable_RupOT: ['RupOT'] 
- IX_RupEntregable_usuario: ['usuario'] 

### Tabla: RupFase
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupFase | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Orden | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| RupFase | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| Preparacion | BIT |  |  |
| MaterialEmpaque | BIT |  |  |
| MateriaPrima | BIT |  |  |
| Adicion | BIT |  |  |
| Devolucion | BIT |  |  |
| Produccion | BIT |  |  |
| Revision | BIT |  |  |
| productoTerminado | BIT |  |  |
| repuesto | BIT |  |  |
| TALLER | BIT |  |  |
| informe | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| imprimeInforme | BIT |  |  |
| nivel | INTEGER | ✓ |  |

#### Índices
- IX_RupFase_empresa: ['empresa'] 
- IX_RupFase_nRupFase: ['nRupFase'] 
- IX_RupFase_Orden: ['Orden'] 
- IX_RupFase_RupFase: ['RupFase'] 
- IX_RupFase_usuario: ['usuario'] 

### Tabla: RupOT
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RupSolicitud | INTEGER |  |  |
| RupOTResponsable | INTEGER |  |  |
| nRupOT | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ParaCuandoOT | DATETIME | ✓ |  |
| Activo | BIT |  |  |
| RupOT | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| producto | INTEGER | ✓ |  |
| almacen | INTEGER | ✓ |  |
| cantidad | NUMERIC(9, 2) | ✓ |  |
| fentrega | DATETIME | ✓ |  |
| rupactividad | INTEGER | ✓ |  |

#### Índices
- IX_RupOT_empresa: ['empresa'] 
- IX_RupOT_nRupOT: ['nRupOT'] 
- IX_RupOT_RupOT: ['RupOT'] 
- IX_RupOT_RupOTResponsable: ['RupOTResponsable'] 
- IX_RupOT_RupSolicitud: ['RupSolicitud'] 
- IX_RupOT_usuario: ['usuario'] 

### Tabla: RupPersonal
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupPersonal | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaIngreso | DATETIME | ✓ |  |
| fechaRetiro | DATETIME | ✓ |  |
| HoraHombre | NUMERIC(16, 6) |  |  |
| Observaciones | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Renta | BIT |  |  |
| Factura | BIT |  |  |
| Activo | BIT |  |  |
| RupPersonal | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupPersonal_empresa: ['empresa'] 
- IX_RupPersonal_nRupPersonal: ['nRupPersonal'] 
- IX_RupPersonal_Observaciones: ['Observaciones'] 
- IX_RupPersonal_RupPersonal: ['RupPersonal'] 
- IX_RupPersonal_usuario: ['usuario'] 

### Tabla: RupSolicitud
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nRupSolicitud | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechaSolicitud | DATETIME | ✓ |  |
| ParaCuando | DATETIME | ✓ |  |
| RupResponsable | INTEGER |  |  |
| Precio | NUMERIC(16, 6) |  |  |
| PrecioReal | NUMERIC(16, 6) |  |  |
| Observaciones | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| RupSolicitud | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupSolicitud_Clientes: ['Clientes'] 
- IX_RupSolicitud_empresa: ['empresa'] 
- IX_RupSolicitud_nRupSolicitud: ['nRupSolicitud'] 
- IX_RupSolicitud_Observaciones: ['Observaciones'] 
- IX_RupSolicitud_RupResponsable: ['RupResponsable'] 
- IX_RupSolicitud_RupSolicitud: ['RupSolicitud'] 
- IX_RupSolicitud_usuario: ['usuario'] 

### Tabla: RupStandar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupStandar | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| HorasStandar | NUMERIC(9, 2) |  |  |
| Activo | BIT |  |  |
| RupStandar | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupStandar_empresa: ['empresa'] 
- IX_RupStandar_nRupStandar: ['nRupStandar'] 
- IX_RupStandar_RupStandar: ['RupStandar'] 
- IX_RupStandar_usuario: ['usuario'] 

### Tabla: RupStandarControl
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupStandarControl | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| HorasStandar | NUMERIC(9, 2) |  |  |
| Activo | BIT |  |  |
| RupStandarControl | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupStandarControl_empresa: ['empresa'] 
- IX_RupStandarControl_nRupStandarControl: ['nRupStandarControl'] 
- IX_RupStandarControl_RupStandarControl: ['RupStandarControl'] 
- IX_RupStandarControl_usuario: ['usuario'] 

### Tabla: RupStatus
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupStatus | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Activo | BIT |  |  |
| RupStatus | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| suspendido | BIT |  |  |
| terminado | BIT |  |  |
| cancelado | BIT |  |  |
| enproceso | BIT |  |  |
| noiniciado | BIT |  |  |

#### Índices
- IX_RupStatus_empresa: ['empresa'] 
- IX_RupStatus_nRupStatus: ['nRupStatus'] 
- IX_RupStatus_RupStatus: ['RupStatus'] 
- IX_RupStatus_usuario: ['usuario'] 

### Tabla: RupSubActivitie
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RupOTActividad | INTEGER |  |  |
| nRupSubActividad | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Rupstandar | INTEGER |  |  |
| Orden | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empleado | INTEGER |  |  |
| fechaEntrega | DATETIME | ✓ |  |
| fechaTerminado | DATETIME | ✓ |  |
| HorasBudget | NUMERIC(16, 6) |  |  |
| HorasReal | NUMERIC(16, 6) |  |  |
| ValorHorahombre | NUMERIC(16, 6) |  |  |
| Activo | BIT |  |  |
| Terminado | BIT |  |  |
| RupSubActividad | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupSubActivitie_empleado: ['empleado'] 
- IX_RupSubActivitie_empresa: ['empresa'] 
- IX_RupSubActivitie_nRupSubActividad: ['nRupSubActividad'] 
- IX_RupSubActivitie_Orden: ['Orden'] 
- IX_RupSubActivitie_RupOTActividad: ['RupOTActividad'] 
- IX_RupSubActivitie_Rupstandar: ['Rupstandar'] 
- IX_RupSubActivitie_RupSubActividad: ['RupSubActividad'] 
- IX_RupSubActivitie_usuario: ['usuario'] 

### Tabla: RupTipoActividad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupTipoActividad | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| RupTipoActividad | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_RupTipoActividad_empresa: ['empresa'] 
- IX_RupTipoActividad_nRupTipoActividad: ['nRupTipoActividad'] 
- IX_RupTipoActividad_RupTipoActividad: ['RupTipoActividad'] 
- IX_RupTipoActividad_usuario: ['usuario'] 

### Tabla: RupTipoProceso
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nRupTipoProceso | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| RupTipoProceso | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| nivel | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| rupactividad | INTEGER | ✓ |  |
| rupot | INTEGER | ✓ |  |
| cantidad | NUMERIC(9, 2) | ✓ |  |
| insumo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| producto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_RupTipoProceso_empresa: ['empresa'] 
- IX_RupTipoProceso_nRupTipoProceso: ['nRupTipoProceso'] 
- IX_RupTipoProceso_RupTipoProceso: ['RupTipoProceso'] 
- IX_RupTipoProceso_usuario: ['usuario'] 

### Tabla: RutaCamion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rutaCamion | INTEGER |  |  |
| nRutaCamion | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_RutaCamion: ['rutaCamion'] 

### Tabla: TIPOPLAZA
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| TIPOPLAZA | INTEGER |  |  |
| DESCRIPCION | VARCHAR(80) COLLATE "Modern_Spanish_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| temporal | BIT | ✓ |  |
| permanente | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- IX_TIPOPLAZA_DESCRIPCION: ['DESCRIPCION'] 
- IX_TIPOPLAZA_empresa: ['empresa'] 
- IX_TIPOPLAZA_TIPOPLAZA: ['TIPOPLAZA'] 
- IX_TIPOPLAZA_usuario: ['usuario'] 

### Tabla: Talla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| talla | INTEGER |  | ✓ |
| talla1 | NUMERIC(5, 2) |  |  |
| talla2 | NUMERIC(5, 2) |  |  |
| talla3 | NUMERIC(5, 2) |  |  |
| tallatipo | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: TamanoPauta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nTamanoPauta | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sizePauta | INTEGER |  |  |
| TamanoPauta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: Temporada
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Temporada | INTEGER |  | ✓ |
| nTemporada | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: TipoCargo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| TipoCargo | INTEGER |  | ✓ |
| nTipoCargo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Naturaleza | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| operador | INTEGER | ✓ |  |

### Tabla: TipoEfectivo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| valor | NUMERIC(18, 6) |  |  |
| TipoEfectivo | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| pais | INTEGER |  |  |

#### Índices
- IX_TipoEfectivo_empresa: ['empresa'] 
- IX_TipoEfectivo_TipoEfectivo: ['TipoEfectivo'] 
- IX_TipoEfectivo_usuario: ['usuario'] 

### Tabla: TipoEscala
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| TipoEscala | INTEGER |  | ✓ |
| nTipoEscala | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| corridaz1 | NUMERIC(4, 1) |  |  |
| corridaz2 | NUMERIC(4, 1) |  |  |
| corridaz3 | NUMERIC(4, 1) |  |  |
| corridaz4 | NUMERIC(4, 1) |  |  |
| corridaz5 | NUMERIC(4, 1) |  |  |
| corridaz6 | NUMERIC(4, 1) |  |  |
| corridaz7 | NUMERIC(4, 1) |  |  |
| corridaz8 | NUMERIC(4, 1) |  |  |
| corridaA1 | INTEGER |  |  |
| corridaA2 | INTEGER |  |  |
| corridaA3 | INTEGER |  |  |
| corridaA4 | INTEGER |  |  |
| corridaA5 | INTEGER |  |  |
| corridaA6 | INTEGER |  |  |
| corridaA7 | INTEGER |  |  |
| corridaA8 | INTEGER |  |  |
| TotalEscala | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| subescala | BIT |  |  |
| tiposubescala | INTEGER |  |  |
| tipo_uer | BIT |  |  |
| tipo_us | BIT |  |  |
| tipo_uk | BIT |  |  |
| sexo | INTEGER |  |  |

### Tabla: TipoPago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipopago | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TipoPago | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: Todos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| TodoID | UNIQUEIDENTIFIER |  | ✓ |
| Author | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TodoDate | DATETIME |  |  |
| TodoDescription | VARCHAR(4000) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TodoState | SMALLINT |  |  |

### Tabla: UnidadVenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| UnidadBase | INTEGER |  |  |
| UVenta | INTEGER |  |  |
| Factor | NUMERIC(16, 6) |  |  |
| Activo | BIT |  |  |
| UnidadVenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_UnidadVenta_empresa: ['empresa'] 
- IX_UnidadVenta_UnidadBase: ['UnidadBase'] 
- IX_UnidadVenta_UnidadVenta: ['UnidadVenta'] 
- IX_UnidadVenta_usuario: ['usuario'] 
- IX_UnidadVenta_UVenta: ['UVenta'] 

### Tabla: ZonaVendedor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nzonaVendedor | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| zonaVendedor | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: __EFMigrationsHistory
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| MigrationId | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  | ✓ |
| ProductVersion | NVARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: aAutorizar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| accesos | INTEGER |  |  |
| documentoid | INTEGER |  |  |
| esperfil | BIT |  |  |
| pedidoVenta | BIT |  |  |
| pedidoCompra | BIT |  |  |
| factura | BIT |  |  |
| compra | BIT |  |  |
| almacen | BIT |  |  |
| otros | BIT |  |  |
| tipomov | INTEGER |  |  |
| datos | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| autorizado | INTEGER |  |  |
| fecha | DATETIME |  |  |
| autoriza | INTEGER |  |  |
| fechaautorizado | DATETIME | ✓ |  |
| aAutorizar | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| original | INTEGER |  |  |
| nueva | INTEGER |  |  |

### Tabla: accesos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| proceso | INTEGER |  |  |
| acceso | BIT |  |  |
| crear | BIT |  |  |
| modificar | BIT |  |  |
| eliminar | BIT |  |  |
| imprimir | BIT |  |  |
| excel | BIT |  |  |
| accesos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| monto | NUMERIC(18, 6) |  |  |

#### Índices
- IX_accesos_accesos: ['accesos'] 
- IX_accesos_empresa: ['empresa'] 
- IX_accesos_proceso: ['proceso'] 
- IX_accesos_rusuario: ['rusuario'] 
- IX_accesos_usuario: ['usuario'] 

### Tabla: acomision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| miembro | CHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ccopias | NUMERIC(15, 6) |  |  |
| cal1 | NUMERIC(4, 2) |  |  |
| compnivel1 | NUMERIC(15, 6) |  |  |
| comsdirectos | NUMERIC(15, 6) |  |  |
| calc2 | NUMERIC(15, 6) |  |  |
| compnivel2 | NUMERIC(15, 6) |  |  |
| comsdirectos2 | NUMERIC(15, 6) |  |  |
| pnivel | NUMERIC(15, 6) |  |  |
| snivel | NUMERIC(15, 6) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| acomision | INTEGER |  | ✓ |

#### Índices
- IX_acomision_acomision: ['acomision'] 
- IX_acomision_clientes: ['clientes'] 
- IX_acomision_empresa: ['empresa'] 
- IX_acomision_usuario: ['usuario'] 

### Tabla: adepreciacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | INTEGER |  |  |
| montodepreciado | NUMERIC(18, 6) |  |  |
| aproducto | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| adepreciacion | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| anio | INTEGER |  |  |
| fecha | DATETIME | ✓ |  |

#### Índices
- IX_adepreciacion_aproducto: ['aproducto', 'mes', 'anio'] (UNIQUE)
- IX_anio_mes_aproducto: ['aproducto', 'anio', 'mes'] (UNIQUE)

### Tabla: adistr
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| miembro | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| anivel | INTEGER |  |  |
| topacio | BIT |  |  |
| zafiro | BIT |  |  |
| esmeralda | BIT |  |  |
| adistr | INTEGER |  | ✓ |
| membresia | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fingreso | DATETIME | ✓ |  |
| bonopag | BIT | ✓ |  |
| bono | NUMERIC(7, 3) |  |  |

#### Índices
- IX_adistr_adistr: ['adistr'] 
- IX_adistr_anivel: ['anivel'] 
- IX_adistr_clientes: ['clientes'] 
- IX_adistr_empresa: ['empresa'] 
- IX_adistr_usuario: ['usuario'] 

### Tabla: admoncaja
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| admoncaja | INTEGER |  | ✓ |
| tipoEscala | INTEGER | ✓ |  |
| nocaja | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME | ✓ |  |
| fcheck | DATETIME | ✓ |  |
| fseall | DATETIME | ✓ |  |
| q1 | INTEGER | ✓ |  |
| q2 | INTEGER | ✓ |  |
| q3 | INTEGER | ✓ |  |
| q4 | INTEGER | ✓ |  |
| q5 | INTEGER | ✓ |  |
| q6 | INTEGER | ✓ |  |
| q7 | INTEGER | ✓ |  |
| q8 | INTEGER | ✓ |  |
| t1 | NUMERIC(3, 1) | ✓ |  |
| t2 | NUMERIC(3, 1) | ✓ |  |
| t3 | NUMERIC(3, 1) | ✓ |  |
| t4 | NUMERIC(3, 1) | ✓ |  |
| t5 | NUMERIC(3, 1) | ✓ |  |
| t6 | NUMERIC(3, 1) | ✓ |  |
| t7 | NUMERIC(3, 1) | ✓ |  |
| t8 | NUMERIC(3, 1) | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| bodega | NUMERIC(6, 2) | ✓ |  |
| producto | NUMERIC(6, 2) | ✓ |  |
| docompra | INTEGER | ✓ |  |
| enfirme | NUMERIC(9, 2) | ✓ |  |
| Tenfirme | DATETIME | ✓ |  |

### Tabla: afp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nafp | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| simafp | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pais | INTEGER | ✓ |  |
| activo | BIT |  |  |
| afp | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| tipo | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_afp_afp: ['afp'] 
- IX_afp_empresa: ['empresa'] 
- IX_afp_nafp: ['nafp'] 
- IX_afp_pais: ['pais'] 
- IX_afp_simafp: ['simafp'] 
- IX_afp_usuario: ['usuario'] 

### Tabla: agencia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nagencia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| propietario | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tipcli | INTEGER |  |  |
| municip | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| cliencatego | INTEGER |  |  |
| contado | BIT |  |  |
| contacto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| recomendado | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| razonsoc | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| giro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fax | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| exento | BIT |  |  |
| descuento | INTEGER |  |  |
| email | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| promcomp | NUMERIC(16, 6) |  |  |
| prompago | NUMERIC(16, 6) |  |  |
| limitecredito | NUMERIC(16, 6) |  |  |
| saldo | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hora | DATETIME | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| agencia | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | BIT |  |  |
| contrato | BIT |  |  |
| nacimiento | DATETIME | ✓ |  |
| ivacero | BIT |  |  |
| PROPIO | BIT |  |  |
| PDESC | NUMERIC(5, 2) |  |  |
| ZONA | INTEGER |  |  |
| pApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| sApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Nombres | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| bodega | INTEGER |  |  |
| MESA | BIT | ✓ |  |
| NOPROPINA | BIT | ✓ |  |
| referido | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direnvio | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| agrupaagencia | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| preciovineta | INTEGER | ✓ |  |
| percepcion | BIT |  |  |
| nosujeto | BIT |  |  |

### Tabla: agrupaclientes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nagrupaclientes | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| agrupaClientes | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: almacen
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| almacen | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dfactura | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| bodega | INTEGER |  |  |
| camion | INTEGER |  |  |
| pfactura | INTEGER |  |  |
| transpte | INTEGER |  |  |
| OrdenTrabajo | INTEGER |  |  |
| rupfase | INTEGER |  |  |
| gestiontaller | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| motorista | INTEGER |  |  |
| factura | INTEGER |  |  |
| compra | INTEGER |  |  |
| PrecioActualizado | BIT |  |  |
| tienecambiobodega | BIT |  |  |
| almacenReferencia | INTEGER |  |  |
| caja | INTEGER |  |  |
| IngxDevolucion | BIT |  |  |
| NcAplicada | INTEGER |  |  |
| equipoprocess | INTEGER | ✓ |  |
| fentrega | DATETIME | ✓ |  |
| fechacierre | DATETIME | ✓ |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- almacen_empresa_fecha: ['empresa', 'fecha'] 
- almacen_nula_empresa: ['nula', 'empresa'] 
- almacen_tipomov_empresa_fecha: ['tipomov', 'empresa', 'fecha'] 
- compra_nula_empresa: ['nula', 'empresa'] 
- IX_almacen_almacen: ['almacen'] 
- IX_almacen_CAJA: ['caja'] 
- IX_almacen_clientes: ['clientes'] 
- IX_almacen_dfactura: ['dfactura'] 
- IX_almacen_empresa: ['empresa'] 
- IX_almacen_fecha: ['fecha'] 
- IX_almacen_moneda: ['moneda'] 
- IX_almacen_notas: ['notas'] 
- IX_almacen_tipomov: ['tipomov'] 
- IX_almacen_usuario: ['usuario'] 

### Tabla: almnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| almacen | INTEGER |  |  |
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| almnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['almacen'] → almacen.['almacen']

#### Índices
- IX_almnula_almacen: ['almacen'] 
- IX_almnula_almnula: ['almnula'] 
- IX_almnula_empresa: ['empresa'] 
- IX_almnula_fecha: ['fecha'] 
- IX_almnula_motivo: ['motivo'] 
- IX_almnula_usuario: ['usuario'] 

### Tabla: almtaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fechaentrega | DATETIME | ✓ |  |
| almacen | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| almtaller | INTEGER |  | ✓ |

### Tabla: anivel
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nanivel | CHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nomiembros | INTEGER |  |  |
| orden | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| porctje | NUMERIC(4, 2) |  |  |
| compramin | NUMERIC(15, 6) |  |  |
| acompramin | NUMERIC(15, 6) |  |  |
| montobono | NUMERIC(15, 6) |  |  |
| nivel1 | BIT |  |  |
| nivel2 | BIT |  |  |
| topacio | BIT |  |  |
| zafiro | BIT |  |  |
| esmeralda | BIT |  |  |
| anivel | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| membresia | BIT |  |  |
| bono | BIT | ✓ |  |

#### Índices
- IX_anivel_anivel: ['anivel'] 
- IX_anivel_empresa: ['empresa'] 
- IX_anivel_nomiembros: ['nomiembros'] 
- IX_anivel_usuario: ['usuario'] 

### Tabla: anticipofactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| anticipofactura | INTEGER |  | ✓ |
| anticipos | INTEGER |  |  |
| pagos | INTEGER |  |  |
| monto | NUMERIC(18, 6) |  |  |
| fecha | DATETIME |  |  |
| empresa | INTEGER |  |  |
| activo | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |
| liquidada | BIT | ✓ |  |

### Tabla: anticipos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| contabilidad | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| difcambio | NUMERIC(16, 6) |  |  |
| mora | NUMERIC(16, 6) |  |  |
| anticipos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| iva | INTEGER |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| caja | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipopago | INTEGER |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| rutacobro | INTEGER |  |  |
| ENFIRME | BIT |  |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| aplicado | BIT |  |  |
| habono | NUMERIC(18, 6) |  |  |
| hafecta | NUMERIC(18, 6) |  |  |
| hexenta | NUMERIC(18, 6) |  |  |
| hviva | NUMERIC(18, 6) |  |  |
| pagos | INTEGER |  |  |

### Tabla: aproducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| naproducto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| valoradquisicion | NUMERIC(18, 6) |  |  |
| atipo | INTEGER |  |  |
| sucursal | INTEGER |  |  |
| seccion | INTEGER |  |  |
| serie | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codigo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| residual | NUMERIC(18, 6) |  |  |
| cuota | NUMERIC(18, 6) |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horatiempo | DATETIME |  |  |
| aproducto | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| fechaadquisicion | DATETIME | ✓ |  |
| aplicado | BIT |  |  |

### Tabla: asegurad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nasegurad | VARCHAR(80) COLLATE "Modern_Spanish_CI_AS" |  |  |
| activo | BIT |  |  |
| asegurad | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_asegurad_asegurad: ['asegurad'] 
- IX_asegurad_empresa: ['empresa'] 
- IX_asegurad_nasegurad: ['nasegurad'] 
- IX_asegurad_usuario: ['usuario'] 

### Tabla: asignafull
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER |  |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factor | NUMERIC(18, 6) |  |  |
| asignaFull | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| prodprec | INTEGER |  |  |

### Tabla: atipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| descripcion | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tasaresidual | NUMERIC(18, 6) |  |  |
| tasardepreciacion | NUMERIC(18, 6) |  |  |
| anios | INTEGER |  |  |
| criterio | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| atipo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

### Tabla: autfact
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER |  |  |
| autusr | INTEGER |  |  |
| concepto | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| valor | INTEGER |  |  |
| autorizada | BIT |  |  |
| autfact | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_autfact_autfact: ['autfact'] 
- IX_autfact_autusr: ['autusr'] 
- IX_autfact_concepto: ['concepto'] 
- IX_autfact_empresa: ['empresa'] 
- IX_autfact_factura: ['factura'] 
- IX_autfact_usuario: ['usuario'] 
- IX_autfact_valor: ['valor'] 

### Tabla: autocheque
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| autocheque | INTEGER |  | ✓ |
| partida | INTEGER |  |  |
| chpartida | INTEGER |  |  |
| activo | BIT |  |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| abono | NUMERIC(18, 6) |  |  |

#### Índices
- IX_autocheque_autocheque: ['autocheque'] 
- IX_autocheque_chpartida: ['chpartida'] 
- IX_autocheque_partida: ['partida'] 

### Tabla: autorizar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| autorizar | BIGINT |  | ✓ |
| autorizo | INTEGER |  |  |
| proceso | INTEGER |  |  |
| fechasolicitud | DATETIME |  |  |
| fecharevision | DATETIME | ✓ |  |
| autorizado | BIT |  |  |
| negado | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: banco
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nbanco | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| banco | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| simbanco | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condpago | INTEGER |  |  |
| TARJETA | BIT |  |  |
| sqlPLANILLA | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| largocuenta | INTEGER |  |  |
| campo1 | INTEGER |  |  |
| campo2 | INTEGER |  |  |
| campo3 | INTEGER |  |  |
| campo4 | INTEGER |  |  |
| campo5 | INTEGER |  |  |
| campo6 | INTEGER |  |  |
| campo7 | INTEGER |  |  |
| gastoAdmon | BIT |  |  |
| gastoFinan | BIT |  |  |
| gastoVenta | BIT |  |  |
| esbanco | BIT |  |  |

#### Índices
- IX_banco_banco: ['banco'] 
- IX_banco_clientes: ['clientes'] 
- IX_banco_condpago: ['condpago'] 
- IX_banco_empresa: ['empresa'] 
- IX_banco_nbanco: ['nbanco'] 
- IX_banco_simbanco: ['simbanco'] 
- IX_banco_usuario: ['usuario'] 
- IX_banco_vendedor: ['vendedor'] 

### Tabla: bodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nbodega | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| preferido | BIT |  |  |
| bodega | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| serie | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipobodega | INTEGER |  |  |
| ruteo | BIT |  |  |
| general | BIT |  |  |
| SUCURSAL | INTEGER | ✓ |  |
| venta | BIT |  |  |
| devolucion | BIT |  |  |
| bipdescuento | BIT |  |  |
| remision | BIT |  |  |
| recarga | BIT |  |  |
| Supermercado | BIT |  |  |
| combustible | BIT |  |  |
| taller | INTEGER |  |  |
| complementofactura | BIT | ✓ |  |
| rutacamion | INTEGER |  |  |
| bodegaproduccion | BIT |  |  |
| consignacion | BIT |  |  |
| servicios | BIT |  |  |
| entransito | BIT |  |  |
| noexcel | BIT |  |  |
| noprint | BIT |  |  |
| caja | INTEGER |  |  |
| recintofiscal | BIT |  |  |
| showroom | BIT |  |  |
| puedofacturar | BIT |  |  |
| puedeSupervisor | BIT |  |  |
| plazos | BIT |  |  |
| cuotam3 | NUMERIC(6, 2) | ✓ |  |
| cuotam3seg | NUMERIC(6, 2) | ✓ |  |
| reservado | BIT |  |  |
| m_in | INTEGER |  |  |
| h_in | INTEGER |  |  |
| mout | INTEGER |  |  |
| hout | INTEGER |  |  |

#### Índices
- IX_bodega_bodega: ['bodega'] 
- IX_bodega_empresa: ['empresa'] 
- IX_bodega_nbodega: ['nbodega'] 
- IX_bodega_serie: ['serie'] 
- IX_bodega_SUCURSAL: ['SUCURSAL'] 
- IX_bodega_tipobodega: ['tipobodega'] 
- IX_bodega_usuario: ['usuario'] 

### Tabla: bomba
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nbomba | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| Bomba | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: bombatanque
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| bomba | INTEGER |  |  |
| bodega | INTEGER |  |  |
| producto | INTEGER |  |  |
| Bombatanque | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: caccesos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncaccesos | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| proceso | INTEGER |  |  |
| micolor | INTEGER |  |  |
| nivel0 | NUMERIC(18, 6) |  |  |
| nivel1 | NUMERIC(18, 6) |  |  |
| nivel2 | NUMERIC(18, 6) |  |  |
| nivel3 | NUMERIC(18, 6) |  |  |
| nivel4 | NUMERIC(18, 6) |  |  |
| tipoNivel | INTEGER |  |  |
| diasgracia | INTEGER |  |  |
| caccesos | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| nproceso | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| acceso | BIT |  |  |
| descrip | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| puedecambiar | BIT |  |  |
| minimo | INTEGER |  |  |

#### Índices
- IX_caccesos_caccesos: ['caccesos'] 

### Tabla: caja
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| caja | INTEGER |  | ✓ |
| ncaja | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| EQUIPO | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Corrf | INTEGER |  |  |
| MaximoF | INTEGER |  |  |
| CorrC | INTEGER |  |  |
| MaximoC | INTEGER |  |  |
| CorrP | INTEGER |  |  |
| MaximoP | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| CorrT | INTEGER |  |  |
| MaximoT | INTEGER |  |  |
| controlcorrel | INTEGER |  |  |
| bodega | INTEGER |  |  |
| controlbodega | BIT |  |  |
| controlcorrelnc | INTEGER |  |  |
| sucursal | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| corrnc | INTEGER |  |  |
| controlsucursal | BIT |  |  |
| puntoventa | BIT |  |  |
| prodprec | INTEGER |  |  |
| micaja | INTEGER |  |  |
| puedeImprimir | BIT |  |  |
| MUESTRAEXIST | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ingreso | INTEGER |  |  |
| salida | INTEGER |  |  |
| cambodega | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| prodprec2 | INTEGER |  |  |
| notaremision | INTEGER |  |  |
| supervisor | BIT |  |  |
| serialprinter | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| puerto | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cashdrawer | BIT |  |  |
| soloImprime | BIT |  |  |
| REGMOSTRADOS | INTEGER |  |  |
| notacredito | INTEGER |  |  |
| notadebito | INTEGER |  |  |
| impf | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| impc | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| impt | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodegaConsigna | INTEGER |  |  |
| cocina | BIT |  |  |
| mibar | BIT |  |  |
| abono | INTEGER |  |  |
| pedido | INTEGER |  |  |
| lotengo | BIT |  |  |
| corrno | INTEGER |  |  |
| calculosiniva | BIT |  |  |
| ventadiferida | BIT |  |  |
| correxp | INTEGER |  |  |
| corrotro | INTEGER |  |  |
| ocompra | INTEGER | ✓ |  |
| esmostrador | BIT |  |  |
| variaspc | BIT |  |  |
| compra | INTEGER |  |  |
| micorr | INTEGER |  |  |
| devnc | INTEGER |  |  |
| offline | BIT | ✓ |  |
| precioconIva | BIT | ✓ |  |

#### Índices
- IX_caja_caja: ['caja'] 
- IX_caja_CorrC: ['CorrC'] 
- IX_caja_Corrf: ['Corrf'] 
- IX_caja_CorrP: ['CorrP'] 
- IX_caja_CorrT: ['CorrT'] 
- IX_caja_empresa: ['empresa'] 
- IX_caja_EQUIPO: ['EQUIPO'] 
- IX_caja_IMPC: ['impc'] 
- IX_caja_IMPF: ['impf'] 
- IX_caja_IMPT: ['impt'] 
- IX_caja_MaximoC: ['MaximoC'] 
- IX_caja_MaximoF: ['MaximoF'] 
- IX_caja_MaximoP: ['MaximoP'] 
- IX_caja_MaximoT: ['MaximoT'] 
- IX_caja_ncaja: ['ncaja'] 
- IX_caja_usuario: ['usuario'] 

### Tabla: cajaNotas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| caja | INTEGER | ✓ |  |
| Notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: cajatipomov
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cajatipomov | INTEGER |  | ✓ |
| caja | INTEGER | ✓ |  |
| tipomov | INTEGER | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: cajavendedor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cajavendedor | INTEGER |  | ✓ |
| caja | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_cajavendedor_caja: ['caja'] 
- IX_cajavendedor_cajavendedor: ['cajavendedor'] 
- IX_cajavendedor_empresa: ['empresa'] 
- IX_cajavendedor_usuario: ['usuario'] 
- IX_cajavendedor_vendedor: ['vendedor'] 

### Tabla: cambioempleado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Activo | BIT |  |  |
| empleado | INTEGER |  |  |
| grupo | INTEGER |  |  |
| fecha | DATETIME |  |  |
| cambioempleado | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: cambiogrupo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| grupo | INTEGER |  |  |
| descripcion | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empleado | INTEGER |  |  |
| cambiogrupo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fechacambio | DATETIME |  |  |
| grupo2 | INTEGER |  |  |

### Tabla: cambiojornada
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Activo | BIT |  |  |
| empleado | INTEGER |  |  |
| jornada | INTEGER |  |  |
| fecha | DATETIME |  |  |
| cambiojornada | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: cambiojornadaemp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| jornada | INTEGER |  |  |
| jornada2 | INTEGER |  |  |
| descripcion | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empleado | INTEGER |  |  |
| cambiojornadaemp | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fechacambio | DATETIME | ✓ |  |

### Tabla: cambnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cambodega | INTEGER |  |  |
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| cambnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['cambodega'] → cambodega.['cambodega']

#### Índices
- IX_cambnula_cambnula: ['cambnula'] 
- IX_cambnula_cambodega: ['cambodega'] 
- IX_cambnula_empresa: ['empresa'] 
- IX_cambnula_fecha: ['fecha'] 
- IX_cambnula_motivo: ['motivo'] 
- IX_cambnula_usuario: ['usuario'] 

### Tabla: cambodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| cambodega | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| EXENTA | NUMERIC(18, 6) |  |  |
| AFECTA | NUMERIC(18, 6) |  |  |
| VIVA | NUMERIC(18, 6) |  |  |
| MONTFACT | NUMERIC(18, 6) |  |  |
| RETENCION | NUMERIC(18, 6) |  |  |
| condpago | INTEGER |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| bodegas | INTEGER |  |  |
| bodega | INTEGER |  |  |
| fdevolucion1 | DATETIME | ✓ |  |
| fdevolucion2 | DATETIME | ✓ |  |
| fdevolucion3 | DATETIME | ✓ |  |
| fdevolucion4 | DATETIME | ✓ |  |
| fdevolucion5 | DATETIME | ✓ |  |
| entregado | BIT |  |  |
| factura | INTEGER |  |  |
| camion | INTEGER |  |  |
| transpte | INTEGER |  |  |
| motorista | INTEGER |  |  |
| precio | NUMERIC(18, 6) |  |  |
| producto | INTEGER |  |  |
| numtiquet | INTEGER |  |  |
| preparaJornada | INTEGER |  |  |
| fnumtiquet | INTEGER |  |  |
| nInicial | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nFinal | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| liquidada | BIT |  |  |
| factorInteres | INTEGER |  |  |
| pprima | NUMERIC(18, 6) |  |  |
| letras | INTEGER |  |  |
| cuotas | NUMERIC(18, 6) |  |  |
| diapago | INTEGER |  |  |
| fechainicial | DATETIME |  |  |
| montocredito | NUMERIC(18, 6) |  |  |
| procesado | BIT |  |  |
| pais | INTEGER | ✓ |  |
| PrecioActualizado | BIT |  |  |
| prodprec | INTEGER |  |  |
| caja | INTEGER |  |  |
| ofactura | INTEGER |  |  |
| cambodegareferencia | INTEGER |  |  |
| enfirme | BIT |  |  |
| enruta | BIT |  |  |
| impBod | BIT |  |  |
| estado | INTEGER |  |  |
| dev1 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev2 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev3 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev4 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev5 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vendedor1 | INTEGER | ✓ |  |
| vendedor2 | INTEGER | ✓ |  |
| vendedor3 | INTEGER | ✓ |  |
| vendedor4 | INTEGER | ✓ |  |
| vendedor5 | INTEGER | ✓ |  |
| motivo1 | INTEGER |  |  |
| motivo2 | INTEGER |  |  |
| motivo3 | INTEGER |  |  |
| motivo4 | INTEGER |  |  |
| motivo5 | INTEGER |  |  |
| fdevolucion6 | DATETIME | ✓ |  |
| fdevolucion7 | DATETIME | ✓ |  |
| fdevolucion8 | DATETIME | ✓ |  |
| fdevolucion9 | DATETIME | ✓ |  |
| fdevolucion10 | DATETIME | ✓ |  |
| fdevolucion11 | DATETIME | ✓ |  |
| fdevolucion12 | DATETIME | ✓ |  |
| fdevolucion13 | DATETIME | ✓ |  |
| fdevolucion14 | DATETIME | ✓ |  |
| fdevolucion15 | DATETIME | ✓ |  |
| dev6 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev7 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev8 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev9 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev10 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev11 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev12 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev13 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev14 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dev15 | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vendedor6 | INTEGER | ✓ |  |
| vendedor7 | INTEGER | ✓ |  |
| vendedor8 | INTEGER | ✓ |  |
| vendedor9 | INTEGER | ✓ |  |
| vendedor10 | INTEGER | ✓ |  |
| vendedor11 | INTEGER | ✓ |  |
| vendedor12 | INTEGER | ✓ |  |
| vendedor13 | INTEGER | ✓ |  |
| vendedor14 | INTEGER | ✓ |  |
| vendedor15 | INTEGER | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| fechacancela | DATETIME | ✓ |  |
| propina | FLOAT | ✓ |  |
| nombre | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| casaprod | INTEGER | ✓ |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- cambodega_empresa_fecha: ['empresa', 'fecha'] 
- cambodega_nula_empresa: ['nula', 'empresa'] 
- IX_cambodega_CAJA: ['caja'] 
- IX_cambodega_cambodega: ['cambodega'] 
- IX_cambodega_clientes: ['clientes'] 
- IX_cambodega_empresa: ['empresa'] 
- IX_cambodega_fecha: ['fecha'] 
- IX_cambodega_moneda: ['moneda'] 
- IX_cambodega_notas: ['notas'] 
- IX_cambodega_prodprec: ['prodprec'] 
- IX_cambodega_tipomov: ['tipomov'] 
- IX_cambodega_usuario: ['usuario'] 

### Tabla: camion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncamion | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| chasis | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| motor | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| mantenimiento | BIT |  |  |
| caracteristica | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| camion | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| propio | BIT |  |  |
| ejes | INTEGER |  |  |
| marca | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| year | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nacionalidad | INTEGER |  |  |
| placa | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| motorista | INTEGER |  |  |
| bodega | INTEGER |  |  |
| transpte | INTEGER |  |  |
| tipovehiculo | INTEGER |  |  |

### Tabla: cargaAnticipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| camion | INTEGER |  |  |
| motorista | INTEGER |  |  |
| empleado | INTEGER |  |  |
| fecha | DATETIME | ✓ |  |
| cargo | NUMERIC(18, 6) |  |  |
| anticipo | NUMERIC(18, 6) |  |  |
| autorizo | INTEGER |  |  |
| liquido | INTEGER |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| cargaAnticipo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pagado | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecharetorno | DATETIME | ✓ |  |
| fechasalida | DATETIME | ✓ |  |
| clasecarga | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dplanilla | INTEGER |  |  |
| destino | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dpfactura | INTEGER |  |  |

#### Foreign Keys
- ['camion'] → camion.['camion']
- ['motorista'] → motorista.['motorista']

### Tabla: cargo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncargo | VARCHAR(60) COLLATE "Modern_Spanish_CI_AS" |  |  |
| activo | BIT |  |  |
| cargo | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- cargo_cargo: ['cargo', 'empresa'] 
- IX_cargo_cargo: ['cargo'] 
- IX_cargo_empresa: ['empresa'] 
- IX_cargo_ncargo: ['ncargo'] 
- IX_cargo_usuario: ['usuario'] 

### Tabla: cargoscomp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncargoscomp | VARCHAR(52) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| cargoscomp | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_cargoscomp_cargoscomp: ['cargoscomp'] 
- IX_cargoscomp_empresa: ['empresa'] 
- IX_cargoscomp_ncargoscomp: ['ncargoscomp'] 
- IX_cargoscomp_usuario: ['usuario'] 

### Tabla: cargosfact
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| compra | INTEGER |  |  |
| cargoscomp | INTEGER |  |  |
| moneda | INTEGER |  |  |
| fecha | DATETIME |  |  |
| monto | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| cargosfact | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |

#### Foreign Keys
- ['cargoscomp'] → cargoscomp.['cargoscomp']
- ['compra'] → compra.['compra']

#### Índices
- IX_cargosfact_cargoscomp: ['cargoscomp'] 
- IX_cargosfact_cargosfact: ['cargosfact'] 
- IX_cargosfact_compra: ['compra'] 
- IX_cargosfact_empresa: ['empresa'] 
- IX_cargosfact_fecha: ['fecha'] 
- IX_cargosfact_moneda: ['moneda'] 
- IX_cargosfact_usuario: ['usuario'] 

### Tabla: cargosocomp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ocompra | INTEGER |  |  |
| cargoscomp | INTEGER |  |  |
| moneda | INTEGER |  |  |
| fecha | DATETIME |  |  |
| monto | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| cargosocomp | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |

### Tabla: casaprod
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncasaprod | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| casaprod | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| contacto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| correo | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| porc1 | NUMERIC(18, 6) |  |  |
| porc2 | NUMERIC(18, 6) |  |  |
| porc3 | NUMERIC(18, 6) |  |  |
| porc4 | NUMERIC(18, 6) |  |  |
| porc5 | NUMERIC(18, 6) |  |  |
| lim1 | NUMERIC(18, 6) |  |  |
| lim2 | NUMERIC(18, 6) |  |  |
| lim3 | NUMERIC(18, 6) |  |  |
| lim4 | NUMERIC(18, 6) |  |  |
| lim5 | NUMERIC(18, 6) |  |  |
| comisionfija | BIT |  |  |
| porclogro | NUMERIC(18, 6) |  |  |
| porcNoLogro | NUMERIC(18, 6) |  |  |
| umedida | INTEGER |  |  |
| factor1 | INTEGER |  |  |
| factor2 | INTEGER |  |  |
| factor3 | INTEGER |  |  |
| factor4 | INTEGER |  |  |
| factor5 | INTEGER |  |  |

#### Índices
- IX_casaprod_casaprod: ['casaprod'] 
- IX_casaprod_empresa: ['empresa'] 
- IX_casaprod_ncasaprod: ['ncasaprod'] 
- IX_casaprod_usuario: ['usuario'] 

### Tabla: categori
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncategori | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| categori | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| margenminimo | NUMERIC(16, 6) |  |  |
| margen | NUMERIC(16, 6) |  |  |
| materiaprima | BIT |  |  |
| MaterialEmpaque | BIT |  |  |
| ProductoTerminado | BIT |  |  |
| liquido | BIT |  |  |
| solido | BIT |  |  |
| Preventivo | BIT |  |  |
| Correctivo | BIT |  |  |

#### Índices
- IX_categori_categori: ['categori'] 
- IX_categori_empresa: ['empresa'] 
- IX_categori_ncategori: ['ncategori'] 
- IX_categori_usuario: ['usuario'] 

### Tabla: categoritaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncategoritaller | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| categoritaller | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| margenminimo | NUMERIC(16, 6) |  |  |
| margen | NUMERIC(16, 6) |  |  |
| Preventivo | BIT |  |  |
| Correctivo | BIT |  |  |
| diesel | BIT |  |  |
| Recepcion | BIT |  |  |

### Tabla: ccontrato
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| nula | BIT |  |  |
| impresa | BIT |  |  |
| vendedor | INTEGER |  |  |
| condpago | INTEGER |  |  |
| numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cancelada | BIT |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| pprima | NUMERIC(18, 6) |  |  |
| letras | INTEGER |  |  |
| factorinteres | NUMERIC(18, 6) |  |  |
| abono | NUMERIC(18, 6) |  |  |
| cargo | NUMERIC(18, 6) |  |  |
| ccontrato | INTEGER |  |  |
| empresa | INTEGER |  |  |
| fechainicial | DATETIME |  |  |
| montocredito | NUMERIC(18, 6) |  |  |
| diaPago | INTEGER |  |  |
| cuota | NUMERIC(18, 6) |  |  |
| tipomov | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_ccontrato: ['ccontrato'] 

### Tabla: ccosto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nopartida | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATE | ✓ |  |
| noctrocosto | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocuenta | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: checkcontrol
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| checkcontrol | INTEGER |  | ✓ |
| partida | INTEGER | ✓ |  |
| nocheque_o | INTEGER | ✓ |  |
| nocheque_f | INTEGER |  |  |
| usuario_r | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| fecha_o | DATETIME | ✓ |  |
| fecha_f | DATETIME | ✓ |  |

### Tabla: checkroom
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| checkroom | INTEGER |  | ✓ |
| room | INTEGER |  |  |
| fecha | DATETIME |  |  |
| activo | BIT |  |  |
| horain | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horaout | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| valor | NUMERIC(16, 6) |  |  |
| categori | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| vendedor1 | INTEGER |  |  |
| rato | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_checkroom_categori: ['categori'] 
- IX_checkroom_checkroom: ['checkroom'] 
- IX_checkroom_empresa: ['empresa'] 
- IX_checkroom_fecha: ['fecha'] 
- IX_checkroom_horain: ['horain'] 
- IX_checkroom_horaout: ['horaout'] 
- IX_checkroom_room: ['room'] 
- IX_checkroom_usuario: ['usuario'] 
- IX_checkroom_vendedor: ['vendedor'] 
- IX_checkroom_vendedor1: ['vendedor1'] 

### Tabla: chequeRechazado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ChequeRechazado | INTEGER |  |  |
| nocheque | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| chrechazado | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaPago | DATETIME | ✓ |  |
| Fecha | DATETIME |  |  |
| Fechacheque | DATETIME |  |  |
| FechaAnulacion | DATETIME | ✓ |  |
| banco | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_chequeRechazado: ['ChequeRechazado'] 

### Tabla: ciclo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ano | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cerrado | BIT |  |  |
| activo | BIT |  |  |
| ciclo | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ciclo_ano: ['ano'] 
- IX_ciclo_ciclo: ['ciclo'] 
- IX_ciclo_mes: ['mes'] 
- IX_ciclo_usuario: ['usuario'] 

### Tabla: cintaAuditoria
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| qfecha2 | DATETIME | ✓ |  |
| pmicaja | INTEGER | ✓ |  |
| valor | INTEGER | ✓ |  |
| reporte | INTEGER | ✓ |  |
| horaImpresion | DATETIME | ✓ |  |
| qusuario | INTEGER | ✓ |  |
| cintaAuditoria | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| CORREL | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_cintaAuditoria_cintaAuditoria: ['cintaAuditoria'] 
- IX_cintaAuditoria_empresa: ['empresa'] 
- IX_cintaAuditoria_pmicaja: ['pmicaja'] 
- IX_cintaAuditoria_qusuario: ['qusuario'] 
- IX_cintaAuditoria_reporte: ['reporte'] 
- IX_cintaAuditoria_usuario: ['usuario'] 
- IX_cintaAuditoria_valor: ['valor'] 

### Tabla: clase
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clase | INTEGER |  | ✓ |
| nClase | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: clasificacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Clasificacion | INTEGER |  | ✓ |
| nclasificacion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| riesgoA | BIT |  |  |
| riesgoB | BIT |  |  |
| riesgoC | BIT |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_clasificacion_Clasificacion: ['Clasificacion'] 
- IX_clasificacion_empresa: ['empresa'] 
- IX_clasificacion_nclasificacion: ['nclasificacion'] 
- IX_clasificacion_usuario: ['usuario'] 

### Tabla: clidprodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clidprodprec | INTEGER |  | ✓ |
| cliprodprec | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| condpago | INTEGER | ✓ |  |
| usuario | INTEGER |  |  |
| monto | NUMERIC(18, 9) | ✓ |  |

#### Índices
- IX_clidprodprec_clidprodprec: ['clidprodprec'] 
- IX_clidprodprec_cliprodprec: ['cliprodprec'] 
- IX_clidprodprec_condpago: ['condpago'] 
- IX_clidprodprec_empresa: ['empresa'] 
- IX_clidprodprec_prodprec: ['prodprec'] 
- IX_clidprodprec_usuario: ['usuario'] 

### Tabla: cliencatego
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncliencatego | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| preferido | BIT |  |  |
| cliencatego | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_cliencatego_cliencatego: ['cliencatego'] 
- IX_cliencatego_empresa: ['empresa'] 
- IX_cliencatego_ncliencatego: ['ncliencatego'] 
- IX_cliencatego_usuario: ['usuario'] 

### Tabla: clientedatos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientedatos | INTEGER |  | ✓ |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nclientedatos | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| placa | VARCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| chasis | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechamatricula | DATETIME | ✓ |  |
| nolicencia | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| motor | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| color | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ano | DATETIME | ✓ |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |

#### Índices
- IX_clientedatos_chasis: ['chasis'] 
- IX_clientedatos_clientedatos: ['clientedatos'] 
- IX_clientedatos_clientes: ['clientes'] 
- IX_clientedatos_color: ['color'] 
- IX_clientedatos_empresa: ['empresa'] 
- IX_clientedatos_motor: ['motor'] 
- IX_clientedatos_nclientedatos: ['nclientedatos'] 
- IX_clientedatos_nolicencia: ['nolicencia'] 
- IX_clientedatos_placa: ['placa'] 
- IX_clientedatos_usuario: ['usuario'] 

### Tabla: clienteformula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| preferido | BIT |  |  |
| mformula | INTEGER |  |  |
| producto | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clienteformula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_clienteformula_clienteformula: ['clienteformula'] 
- IX_clienteformula_clientes: ['clientes'] 
- IX_clienteformula_empresa: ['empresa'] 
- IX_clienteformula_mformula: ['mformula'] 
- IX_clienteformula_producto: ['producto'] 
- IX_clienteformula_usuario: ['usuario'] 

### Tabla: clientes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nclientes | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| propietario | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tipcli | INTEGER |  |  |
| municip | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| cliencatego | INTEGER |  |  |
| contado | BIT |  |  |
| contacto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| recomendado | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| razonsoc | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| giro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fax | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| exento | BIT |  |  |
| descuento | INTEGER |  |  |
| email | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| promcomp | NUMERIC(16, 6) |  |  |
| prompago | NUMERIC(16, 6) |  |  |
| limitecredito | NUMERIC(16, 6) |  |  |
| saldo | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hora | DATETIME | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  | ✓ |
| empresa | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | BIT |  |  |
| contrato | BIT |  |  |
| nacimiento | DATETIME | ✓ |  |
| casa | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telecasa | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| trabajo | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| profesion | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| teletrabajo | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direcciont | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fuente1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ing1 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| firma | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sueldo1 | TEXT(2147483647) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| gastos1 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| conyuge | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dui | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sueldo2 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| trabajo2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| teletrabajo2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gastos2 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia1 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion2 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia3 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion3 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia4 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel4 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion4 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas2 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ivacero | BIT |  |  |
| PROPIO | BIT |  |  |
| PDESC | NUMERIC(5, 2) |  |  |
| ZONA | INTEGER |  |  |
| pApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| sApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Nombres | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| bodega | INTEGER |  |  |
| direnvio | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| agrupaclientes | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| preciovineta | INTEGER |  |  |
| percepcion | BIT |  |  |
| nosujeto | BIT |  |  |
| comisionagencia | NUMERIC(18, 6) |  |  |
| CargoFULL | BIT |  |  |
| marchamo | BIT |  |  |
| vendedor2 | INTEGER |  |  |
| pais | INTEGER |  |  |
| idClientes | INTEGER |  |  |
| autoconsumo | BIT |  |  |
| gobierno | BIT |  |  |
| cuenta | INTEGER |  |  |
| cuentaProveedor | INTEGER |  |  |
| ExcluirCredito | BIT |  |  |
| conPagare | BIT |  |  |
| Verificado | BIT |  |  |
| descEspecial | BIT |  |  |
| valorreferencia1 | INTEGER |  |  |
| valorreferencia2 | INTEGER |  |  |
| valorreferencia3 | INTEGER |  |  |
| valorreferencia4 | INTEGER |  |  |
| noPagare | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaPagare | DATETIME | ✓ |  |
| vencePagare | DATETIME | ✓ |  |
| montoPagare | NUMERIC(18, 6) | ✓ |  |
| PagareAbierto | INTEGER | ✓ |  |
| firmaFactura | BIT | ✓ |  |
| endipcom | BIT | ✓ |  |
| tweeter | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| facebook | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccioncobro | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ordenRuta | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montoref1 | NUMERIC(18, 6) |  |  |
| montoref2 | NUMERIC(18, 6) |  |  |
| montoref3 | NUMERIC(18, 6) |  |  |
| montoref4 | NUMERIC(18, 6) |  |  |
| foda | VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pagarenotas | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pagareok | BIT |  |  |
| fecharef1 | DATETIME | ✓ |  |
| fecharef2 | DATETIME | ✓ |  |
| fecharef3 | DATETIME | ✓ |  |
| fecharef4 | DATETIME | ✓ |  |
| socio | BIT |  |  |
| prima | NUMERIC(18, 6) |  |  |
| cuota | NUMERIC(18, 6) |  |  |
| fechacontrato | DATETIME |  |  |
| diapago | INTEGER |  |  |
| carnetactualizado | BIT |  |  |
| suspendido | BIT |  |  |
| r1 | BIT |  |  |
| r2 | BIT |  |  |
| r3 | BIT |  |  |
| r4 | BIT |  |  |
| caja | INTEGER |  |  |
| noCuotas | INTEGER |  |  |
| noContrato | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montoprima | NUMERIC(18, 6) |  |  |
| mesa | BIT |  |  |
| nopropina | BIT |  |  |
| pprima | NUMERIC(18, 6) |  |  |
| cuotas | NUMERIC(18, 6) |  |  |
| letras | NUMERIC(18, 6) |  |  |
| nomesa | INTEGER |  |  |
| cuentamaestra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descautorizado | INTEGER |  |  |
| notaautorizado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| micolor | INTEGER |  |  |
| rangocliente | INTEGER |  |  |
| cobrodomicilio | BIT |  |  |
| foda1 | VARCHAR(450) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| firmaIncorrecta | BIT | ✓ |  |
| lineaIncorrecta | BIT | ✓ |  |
| duivencido | BIT | ✓ |  |
| factura | BIT |  |  |
| tiquet | BIT |  |  |
| efectivo | BIT |  |  |
| cheque | BIT |  |  |
| otros | BIT |  |  |
| tarjeta | BIT |  |  |

#### Foreign Keys
- ['prodprec'] → cliencatego.['cliencatego']
- ['municip'] → municip.['municip']
- ['prodprec'] → prodprec.['prodprec']
- ['tipcli'] → tipcli.['tipcli']

#### Índices
- cliente_empresa: ['empresa'] 
- clientes_tipcli: ['tipcli'] 
- IX_clientes_bodega: ['bodega'] 
- IX_clientes_cargo: ['cargo'] 
- IX_clientes_casa: ['casa'] 
- IX_clientes_celular: ['celular'] 
- IX_clientes_cliencatego: ['cliencatego'] 
- IX_clientes_clientes: ['clientes'] 
- IX_clientes_condpago: ['condpago'] 
- IX_clientes_contacto: ['contacto'] 
- IX_clientes_conyuge: ['conyuge'] 
- IX_clientes_descuento: ['descuento'] 
- IX_clientes_direccion: ['direccion'] 
- IX_clientes_direcciont: ['direcciont'] 
- IX_clientes_dui: ['dui'] 
- IX_clientes_empresa: ['empresa'] 
- IX_clientes_fax: ['fax'] 
- IX_clientes_firma: ['firma'] 
- IX_clientes_fuente1: ['fuente1'] 
- IX_clientes_gastos1: ['gastos1'] 
- IX_clientes_gastos2: ['gastos2'] 
- IX_clientes_giro: ['giro'] 
- IX_clientes_ing1: ['ing1'] 
- IX_clientes_moneda: ['moneda'] 
- IX_clientes_municip: ['municip'] 
- IX_clientes_nclientes: ['nclientes'] 
- IX_clientes_nit: ['nit'] 
- IX_clientes_Nombres: ['Nombres'] 
- IX_clientes_notas: ['notas'] 
- IX_clientes_notas2: ['notas2'] 
- IX_clientes_pApellido: ['pApellido'] 
- IX_clientes_prodprec: ['prodprec'] 
- IX_clientes_profesion: ['profesion'] 
- IX_clientes_propietario: ['propietario'] 
- IX_clientes_razonsoc: ['razonsoc'] 
- IX_clientes_recomendado: ['recomendado'] 
- IX_clientes_referencia1: ['referencia1'] 
- IX_clientes_referencia2: ['referencia2'] 
- IX_clientes_referencia3: ['referencia3'] 
- IX_clientes_referencia4: ['referencia4'] 
- IX_clientes_registro: ['registro'] 
- IX_clientes_relacion1: ['relacion1'] 
- IX_clientes_relacion2: ['relacion2'] 
- IX_clientes_relacion3: ['relacion3'] 
- IX_clientes_relacion4: ['relacion4'] 
- IX_clientes_saldo: ['saldo'] 
- IX_clientes_sApellido: ['sApellido'] 
- IX_clientes_sueldo2: ['sueldo2'] 
- IX_clientes_tel1: ['tel1'] 
- IX_clientes_tel2: ['tel2'] 
- IX_clientes_tel3: ['tel3'] 
- IX_clientes_tel4: ['tel4'] 
- IX_clientes_telecasa: ['telecasa'] 
- IX_clientes_telefono1: ['telefono1'] 
- IX_clientes_telefono2: ['telefono2'] 
- IX_clientes_teletrabajo: ['teletrabajo'] 
- IX_clientes_teletrabajo2: ['teletrabajo2'] 
- IX_clientes_tipcli: ['tipcli'] 
- IX_clientes_trabajo: ['trabajo'] 
- IX_clientes_trabajo2: ['trabajo2'] 
- IX_clientes_transpte: ['transpte'] 
- IX_clientes_usuario: ['usuario'] 
- IX_clientes_ZONA: ['ZONA'] 

### Tabla: clientesGrupo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nClientesGrupo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| pareja | BIT |  |  |
| hijo | BIT |  |  |
| pariente | BIT |  |  |
| Nota | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ClientesGrupo | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: clientesmod
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nclientes | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| propietario | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tipcli | INTEGER |  |  |
| municip | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| cliencatego | INTEGER |  |  |
| contado | BIT |  |  |
| contacto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| recomendado | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| razonsoc | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| giro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fax | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| exento | BIT |  |  |
| descuento | INTEGER |  |  |
| email | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| promcomp | NUMERIC(16, 6) |  |  |
| prompago | NUMERIC(16, 6) |  |  |
| limitecredito | NUMERIC(16, 6) |  |  |
| saldo | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hora | DATETIME |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | BIT |  |  |
| contrato | BIT |  |  |
| nacimiento | DATETIME | ✓ |  |
| casa | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telecasa | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| trabajo | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| profesion | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| teletrabajo | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direcciont | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fuente1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ing1 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| firma | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sueldo1 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gastos1 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| conyuge | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dui | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sueldo2 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| trabajo2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| teletrabajo2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gastos2 | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia1 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion2 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia3 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion3 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia4 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tel4 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| relacion4 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas2 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ivacero | BIT |  |  |
| PROPIO | BIT |  |  |
| PDESC | NUMERIC(5, 2) |  |  |
| ZONA | INTEGER |  |  |
| pApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| sApellido | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Nombres | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| bodega | INTEGER |  |  |
| MESA | BIT | ✓ |  |
| NOPROPINA | BIT | ✓ |  |
| referido | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direnvio | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| agrupaclientes | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| preciovineta | INTEGER |  |  |
| percepcion | BIT |  |  |
| nosujeto | BIT |  |  |
| comisionagencia | NUMERIC(18, 6) |  |  |
| CargoFULL | BIT |  |  |
| marchamo | BIT |  |  |
| vendedor2 | INTEGER |  |  |
| pais | INTEGER |  |  |
| idClientes | INTEGER |  |  |
| autoconsumo | BIT |  |  |
| gobierno | BIT |  |  |
| cuenta | INTEGER |  |  |
| cuentaProveedor | INTEGER |  |  |
| ExcluirCredito | BIT |  |  |
| conPagare | BIT |  |  |
| Verificado | BIT |  |  |
| descEspecial | BIT |  |  |
| valorreferencia1 | INTEGER |  |  |
| valorreferencia2 | INTEGER |  |  |
| valorreferencia3 | INTEGER |  |  |
| valorreferencia4 | INTEGER |  |  |
| noPagare | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaPagare | DATETIME | ✓ |  |
| vencePagare | DATETIME | ✓ |  |
| montoPagare | NUMERIC(18, 6) | ✓ |  |
| PagareAbierto | INTEGER | ✓ |  |
| firmaFactura | BIT | ✓ |  |
| endipcom | BIT | ✓ |  |
| tweeter | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| facebook | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| celular3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccioncobro | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ordenRuta | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montoref1 | NUMERIC(18, 6) |  |  |
| montoref2 | NUMERIC(18, 6) |  |  |
| montoref3 | NUMERIC(18, 6) |  |  |
| montoref4 | NUMERIC(18, 6) |  |  |
| foda | VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['prodprec'] → cliencatego.['cliencatego']
- ['prodprec'] → prodprec.['prodprec']
- ['tipcli'] → tipcli.['tipcli']

### Tabla: cliprodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cliprodprec | INTEGER |  | ✓ |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| lcobro | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vendedor | INTEGER |  |  |
| fechapertura | DATETIME | ✓ |  |
| LugarCobro | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fcobro | DATETIME | ✓ |  |
| factura | INTEGER |  |  |

#### Índices
- IX_cliprodprec_clientes: ['clientes'] 
- IX_cliprodprec_cliprodprec: ['cliprodprec'] 
- IX_cliprodprec_empresa: ['empresa'] 
- IX_cliprodprec_factura: ['factura'] 
- IX_cliprodprec_lcobro: ['lcobro'] 
- IX_cliprodprec_LugarCobro: ['LugarCobro'] 
- IX_cliprodprec_vendedor: ['vendedor'] 

### Tabla: coddepto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncoddepto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| depto | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| coddepto | INTEGER |  | ✓ |

### Tabla: codmunicip
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncodmunicip | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| municip | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| codmunicip | INTEGER |  | ✓ |

### Tabla: comision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| p1 | NUMERIC(16, 6) |  |  |
| l1 | INTEGER |  |  |
| p2 | NUMERIC(16, 6) |  |  |
| l2 | INTEGER |  |  |
| p3 | NUMERIC(16, 6) |  |  |
| l3 | INTEGER |  |  |
| p4 | NUMERIC(16, 6) |  |  |
| l4 | INTEGER |  |  |
| p5 | NUMERIC(16, 6) |  |  |
| l5 | INTEGER |  |  |
| activo | BIT |  |  |
| comision | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tipovendedor | INTEGER |  |  |
| efectivo | NUMERIC(18, 6) |  |  |

#### Índices
- IX_comision_comision: ['comision'] 
- IX_comision_empresa: ['empresa'] 
- IX_comision_l1: ['l1'] 
- IX_comision_l2: ['l2'] 
- IX_comision_l3: ['l3'] 
- IX_comision_l4: ['l4'] 
- IX_comision_l5: ['l5'] 
- IX_comision_usuario: ['usuario'] 

### Tabla: comisiontienda
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| comisiontienda | INTEGER |  | ✓ |
| tienda | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| valores | NUMERIC(16, 6) |  |  |
| vcomision | NUMERIC(16, 6) |  |  |
| rangospagados | INTEGER |  |  |
| anio | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| mes | INTEGER | ✓ |  |
| comision | NUMERIC(14, 2) | ✓ |  |
| fecha | DATETIME | ✓ |  |

### Tabla: comisionventas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| comisionventas | INTEGER |  | ✓ |
| vendedor | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| valores | NUMERIC(16, 6) |  |  |
| vcomision | NUMERIC(16, 6) |  |  |
| rangospagados | INTEGER |  |  |
| anio | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| mes | INTEGER | ✓ |  |
| comision | NUMERIC(14, 2) | ✓ |  |
| fecha | DATETIME | ✓ |  |

### Tabla: compnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| compra | INTEGER |  |  |
| compnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['compra'] → compra.['compra']

#### Índices
- IX_compnula_compnula: ['compnula'] 
- IX_compnula_compra: ['compra'] 
- IX_compnula_empresa: ['empresa'] 
- IX_compnula_fecha: ['fecha'] 
- IX_compnula_motivo: ['motivo'] 
- IX_compnula_usuario: ['usuario'] 

### Tabla: compra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| impresa | BIT |  |  |
| aplicaexistencia | BIT |  |  |
| contabilidad | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| tipovta | INTEGER |  |  |
| encompra | INTEGER |  |  |
| proveedor | INTEGER |  |  |
| proveedor2 | INTEGER |  |  |
| condpago | INTEGER |  |  |
| iva | INTEGER |  |  |
| cprodprec | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(18, 6) |  |  |
| tasacambioseg | NUMERIC(18, 6) |  |  |
| tasacambiotres | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| tax | NUMERIC(18, 6) |  |  |
| descuentos | NUMERIC(18, 6) |  |  |
| descaplica | BIT |  |  |
| flete | NUMERIC(18, 6) |  |  |
| fob | NUMERIC(18, 6) |  |  |
| seguro | NUMERIC(18, 6) |  |  |
| monto | NUMERIC(18, 6) |  |  |
| montcomp | NUMERIC(18, 6) |  |  |
| montgasto | NUMERIC(18, 6) |  |  |
| montbonif | NUMERIC(18, 6) |  |  |
| pdesc | NUMERIC(18, 6) |  |  |
| vdesc | NUMERIC(18, 6) |  |  |
| notas | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| compra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| basesiniva | BIT |  |  |
| cargo | NUMERIC(18, 6) |  |  |
| abono | NUMERIC(18, 6) |  |  |
| nproveedor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nocuenta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| noPoliza | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| GASTOS | NUMERIC(18, 6) |  |  |
| Partida | INTEGER |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| bodega | INTEGER |  |  |
| taller | BIT |  |  |
| tiquetinicial | INTEGER |  |  |
| tiquetfinal | INTEGER |  |  |
| numtiquet | INTEGER |  |  |
| canttiquet | INTEGER |  |  |
| precioUnitario | NUMERIC(18, 6) |  |  |
| producto | INTEGER |  |  |
| caja | INTEGER |  |  |
| cotrans | NUMERIC(18, 6) |  |  |
| preventa | BIT |  |  |
| poliza | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gestiontaller | INTEGER | ✓ |  |

#### Foreign Keys
- ['iva'] → iva.['iva']
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- compra_nula_empresa: ['nula', 'empresa'] 
- IX_compra_bodega: ['bodega'] 
- IX_compra_CAJA: ['caja'] 
- IX_compra_compra: ['compra'] 
- IX_compra_condpago: ['condpago'] 
- IX_compra_cprodprec: ['cprodprec'] 
- IX_compra_empresa: ['empresa'] 
- IX_compra_encompra: ['encompra'] 
- IX_compra_fecha: ['fecha'] 
- IX_compra_iva: ['iva'] 
- IX_compra_moneda: ['moneda'] 
- IX_compra_nocuenta: ['nocuenta'] 
- IX_compra_noPoliza: ['noPoliza'] 
- IX_compra_notas: ['notas'] 
- IX_compra_nproveedor: ['nproveedor'] 
- IX_compra_pedido: ['pedido'] 
- IX_compra_proveedor: ['proveedor'] 
- IX_compra_proveedor2: ['proveedor2'] 
- IX_compra_registro: ['registro'] 
- IX_compra_tipomov: ['tipomov'] 
- IX_compra_tipovta: ['tipovta'] 
- IX_compra_usuario: ['usuario'] 

### Tabla: comprafirme
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| comprafirme | INTEGER |  | ✓ |
| numedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME | ✓ |  |
| fechaOut | DATETIME | ✓ |  |
| fechain | DATETIME | ✓ |  |
| impresa | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| notasPago | VARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| flete | NUMERIC(9, 2) | ✓ |  |
| seguro | NUMERIC(9, 2) | ✓ |  |
| montgasto | NUMERIC(9, 2) | ✓ |  |
| cartacredito | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| poliza | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| encompra | INTEGER | ✓ |  |
| embarque | INTEGER | ✓ |  |
| cembarque | INTEGER | ✓ |  |
| loadingcontainer | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| billloading | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| containerno | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| marchamo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| loadingPort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| DischargePort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| DeliveryPort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| hechoen | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| deliveryterms | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ctracking | INTEGER | ✓ |  |
| recinto | BIT | ✓ |  |
| fecharecinto | DATETIME | ✓ |  |
| metros3 | NUMERIC(9, 2) | ✓ |  |
| metros3p | NUMERIC(9, 2) | ✓ |  |
| impuesto | NUMERIC(9, 2) | ✓ |  |
| impuestop | NUMERIC(9, 2) | ✓ |  |
| arancel | NUMERIC(9, 2) | ✓ |  |
| arancelp | NUMERIC(9, 2) | ✓ |  |
| cif | NUMERIC(9, 2) | ✓ |  |
| montoiva | NUMERIC(9, 2) | ✓ |  |
| ndeposito | INTEGER | ✓ |  |
| recintofiscal | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| Tipomov | INTEGER | ✓ |  |
| Gastos | NUMERIC(9, 2) | ✓ |  |

### Tabla: compras
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| periodoiva | INTEGER |  |  |
| fecha | DATETIME |  |  |
| nocheque | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numedocu | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| proveedor | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| excluido | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| importacion | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| compras | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| otro | NUMERIC(16, 6) |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| nProveedor | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocuenta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| REGISTRO | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| cotrans | NUMERIC(18, 6) |  |  |
| tipobodega | INTEGER |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| partida | INTEGER |  |  |
| compra | INTEGER |  |  |
| PAGOS | INTEGER |  |  |
| idretencion | INTEGER |  |  |
| importado | BIT |  |  |
| cuenta | INTEGER | ✓ |  |
| tipomov | INTEGER | ✓ |  |
| cuenta1 | INTEGER | ✓ |  |
| CESC | NUMERIC(9, 2) |  |  |
| serie | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pais | INTEGER | ✓ |  |
| servicio | INTEGER |  |  |
| tipo | INTEGER |  |  |
| clasificacion | INTEGER |  |  |
| sector | INTEGER |  |  |
| costo | INTEGER |  |  |

#### Foreign Keys
- ['periodoiva'] → periodoiva.['periodoiva']

#### Índices
- IX_compras_compras: ['compras'] 
- IX_compras_empresa: ['empresa'] 
- IX_compras_fecha: ['fecha'] 
- IX_compras_moneda: ['moneda'] 
- IX_compras_nocheque: ['nocheque'] 
- IX_compras_nocuenta: ['nocuenta'] 
- IX_compras_nProveedor: ['nProveedor'] 
- IX_compras_periodoiva: ['periodoiva'] 
- IX_compras_proveedor: ['proveedor'] 
- IX_compras_tipobodega: ['tipobodega'] 
- IX_compras_usuario: ['usuario'] 

### Tabla: conciliado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| conciliado | INTEGER |  | ✓ |
| saldo | NUMERIC(9, 2) | ✓ |  |
| Fecha | DATETIME | ✓ |  |
| diferencia | NUMERIC(9, 2) | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: condpago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncondpago | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| plazo | INTEGER |  |  |
| contado | BIT |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| condpago | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| cheque | BIT |  |  |
| tarjeta | BIT |  |  |
| remesa | BIT |  |  |
| otro | BIT |  |  |
| vueltaviaje | BIT |  |  |
| canjepuntos | BIT |  |  |
| contrato | BIT |  |  |
| transferencia | BIT |  |  |
| bitcoin | BIT |  |  |
| activarPromo | BIT |  |  |
| pdesc | NUMERIC(5, 2) |  |  |
| d1 | BIT |  |  |
| d2 | BIT |  |  |
| d3 | BIT |  |  |
| d4 | BIT |  |  |
| d5 | BIT |  |  |
| d6 | BIT |  |  |
| d7 | BIT |  |  |
| h1 | INTEGER |  |  |
| h2 | INTEGER |  |  |
| m1 | INTEGER |  |  |
| m2 | INTEGER |  |  |

#### Índices
- IX_condpago_condpago: ['condpago'] 
- IX_condpago_empresa: ['empresa'] 
- IX_condpago_ncondpago: ['ncondpago'] 
- IX_condpago_plazo: ['plazo'] 
- IX_condpago_usuario: ['usuario'] 

### Tabla: consigna
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| compra | INTEGER |  |  |
| almacen | INTEGER |  |  |
| consigna | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_consigna_almacen: ['almacen'] 
- IX_consigna_compra: ['compra'] 
- IX_consigna_consigna: ['consigna'] 
- IX_consigna_empresa: ['empresa'] 
- IX_consigna_usuario: ['usuario'] 

### Tabla: contingencia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER | ✓ |  |
| uuid | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| serie | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numero | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

### Tabla: contnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| contrato | INTEGER |  |  |
| contnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['contrato'] → contrato.['contrato']

#### Índices
- IX_contnula_contnula: ['contnula'] 
- IX_contnula_contrato: ['contrato'] 
- IX_contnula_empresa: ['empresa'] 
- IX_contnula_fecha: ['fecha'] 
- IX_contnula_motivo: ['motivo'] 
- IX_contnula_usuario: ['usuario'] 

### Tabla: contrato
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| cancelada | BIT |  |  |
| impresa | BIT |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacanc | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| iva | INTEGER |  |  |
| condpago | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| factoriva | NUMERIC(16, 6) |  |  |
| factorinteres | NUMERIC(16, 6) |  |  |
| factormora | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| contrato | INTEGER |  | ✓ |
| cargo | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| pprima | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| letras | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| basesiniva | BIT |  |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']
- ['vendedor'] → vendedor.['vendedor']

#### Índices
- IX_contrato_bodega: ['bodega'] 
- IX_contrato_clientes: ['clientes'] 
- IX_contrato_condpago: ['condpago'] 
- IX_contrato_contrato: ['contrato'] 
- IX_contrato_empresa: ['empresa'] 
- IX_contrato_fecha: ['fecha'] 
- IX_contrato_iva: ['iva'] 
- IX_contrato_letras: ['letras'] 
- IX_contrato_moneda: ['moneda'] 
- IX_contrato_notas: ['notas'] 
- IX_contrato_pedido: ['pedido'] 
- IX_contrato_prodprec: ['prodprec'] 
- IX_contrato_tipomov: ['tipomov'] 
- IX_contrato_usuario: ['usuario'] 
- IX_contrato_vendedor: ['vendedor'] 

### Tabla: contratoPagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| invcliente | INTEGER |  |  |
| factura | INTEGER |  |  |
| pagos | INTEGER |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| contratoPagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['factura'] → factura.['factura']
- ['invcliente'] → invcliente.['invcliente']
- ['pagos'] → pagos.['pagos']

### Tabla: contratoabono
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| invcliente | INTEGER |  |  |
| factura | INTEGER |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| contratoabono | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pagos | INTEGER |  |  |

### Tabla: controlCosto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME | ✓ |  |
| cerrado | BIT | ✓ |  |
| ControlCosto | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_controlCosto_ControlCosto: ['ControlCosto'] 
- IX_controlCosto_empresa: ['empresa'] 
- IX_controlCosto_fecha: ['fecha'] 
- IX_controlCosto_usuario: ['usuario'] 

### Tabla: controlTramo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dpfactura | INTEGER |  |  |
| tramo | INTEGER |  |  |
| nTramo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME | ✓ |  |
| controlTramo | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| precio | NUMERIC(18, 6) |  |  |
| facturar | BIT |  |  |
| facturado | BIT |  |  |
| TIRExport | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TIRImport | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| OrdenPago | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| producto | INTEGER |  |  |
| bl | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| precioAgregado | NUMERIC(18, 6) |  |  |
| fechaQuedan | DATETIME | ✓ |  |
| precioParte | NUMERIC(18, 6) |  |  |
| factura | INTEGER |  |  |
| PRECIOPROV | NUMERIC(18, 6) |  |  |
| FECHAPROV | DATETIME | ✓ |  |
| OTROSCPROV | NUMERIC(18, 6) |  |  |

### Tabla: controla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tabla | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| equipo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hora | DATETIME | ✓ |  |
| Activo | BIT |  |  |
| controla | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| caja | INTEGER |  |  |

#### Índices
- IX_controla_controla: ['controla'] 
- IX_controla_empresa: ['empresa'] 
- IX_controla_equipo: ['equipo'] 
- IX_controla_tabla: ['tabla'] 
- IX_controla_usuario: ['usuario'] 

### Tabla: controlcaja
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| controlcaja | INTEGER |  | ✓ |
| producto | INTEGER | ✓ |  |
| fecha | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| caja | INTEGER | ✓ |  |
| t1 | INTEGER | ✓ |  |
| t2 | INTEGER | ✓ |  |
| t3 | INTEGER | ✓ |  |
| t4 | INTEGER | ✓ |  |
| t5 | INTEGER | ✓ |  |
| t6 | INTEGER | ✓ |  |
| t7 | INTEGER | ✓ |  |
| t8 | INTEGER | ✓ |  |
| opagada | INTEGER | ✓ |  |
| docompra | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: controlcarga
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Numedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| estatus | INTEGER |  |  |
| tipovta | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| condpago | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| enfirme | INTEGER |  |  |
| bodega | INTEGER |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| controlcarga | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| moneda | INTEGER |  |  |
| iva | INTEGER |  |  |
| siniva | INTEGER |  |  |

### Tabla: controlcitas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mitiempo | INTEGER | ✓ |  |
| midsemana | INTEGER | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vendedor | INTEGER | ✓ |  |
| Notas | VARCHAR(500) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| diasemana | INTEGER | ✓ |  |
| dia | DATETIME | ✓ |  |
| hora1 | NCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| hora2 | NCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| controlcitas | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| horasefectivas | NUMERIC(18, 6) | ✓ |  |
| producto | INTEGER | ✓ |  |
| recordar | INTEGER | ✓ |  |
| drecordar | DATETIME | ✓ |  |
| ordentrabajo | INTEGER | ✓ |  |
| rupfase | INTEGER | ✓ |  |
| rupsolicitud | INTEGER | ✓ |  |
| ruptipoproceso | INTEGER | ✓ |  |
| monto | NUMERIC(10, 2) | ✓ |  |
| actividad | INTEGER | ✓ |  |

### Tabla: controlcorrel
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| correl | INTEGER |  |  |
| qmin | INTEGER |  |  |
| qmax | INTEGER |  |  |
| ingreso | BIT |  |  |
| salida | BIT |  |  |
| notacredito | BIT |  |  |
| notadebito | BIT |  |  |
| pagos | BIT |  |  |
| docunico | BIT |  |  |
| nconcepto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| controlcorrel | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| ventas | BIT |  |  |
| warningcorrel | INTEGER |  |  |
| fwarning | DATETIME | ✓ |  |
| produccion | BIT |  |  |
| empaque | BIT |  |  |
| Taller | BIT |  |  |

### Tabla: controldia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME | ✓ |  |
| cdia | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| controldia | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: controles
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| controles | INTEGER |  | ✓ |
| ncontroles | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| clasificacion | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_controles_clasificacion: ['clasificacion'] 
- IX_controles_controles: ['controles'] 
- IX_controles_empresa: ['empresa'] 
- IX_controles_ncontroles: ['ncontroles'] 
- IX_controles_usuario: ['usuario'] 

### Tabla: controlperiodo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME | ✓ |  |
| cerrado | BIT | ✓ |  |
| controlPeriodo | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| caja | INTEGER | ✓ |  |
| sincro | BIT |  |  |

#### Índices
- IX_controlperiodo_caja: ['caja'] 
- IX_controlperiodo_controlPeriodo: ['controlPeriodo'] 
- IX_controlperiodo_empresa: ['empresa'] 
- IX_controlperiodo_fecha: ['fecha'] 
- IX_controlperiodo_usuario: ['usuario'] 

### Tabla: controlvence
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| controlvence | INTEGER |  | ✓ |
| miusuario | INTEGER |  |  |
| notas1 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas2 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| atendio | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: controlvineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfactura | INTEGER |  |  |
| vvineta | NUMERIC(18, 6) |  |  |
| producto | INTEGER |  |  |
| danoimpresa | BIT |  |  |
| danopegado | BIT |  |  |
| contador | INTEGER |  |  |
| bobina | INTEGER |  |  |
| impresa | BIT |  |  |
| facturanula | BIT |  |  |
| controlvineta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: corrDiezmo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Corrdiezmo | INTEGER |  |  |
| nopedido | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_corrDiezmo: ['Corrdiezmo'] 

### Tabla: corrcotiza
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Corrcotiza | INTEGER |  |  |
| nopedido | INTEGER | ✓ |  |
| caja | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- IX_corrcotiza_corrcotiza: ['Corrcotiza'] 

### Tabla: correlativos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| correlativos | INTEGER |  |  |
| dato | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: cotifactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cotifactura | INTEGER |  | ✓ |
| factura | INTEGER | ✓ |  |
| oventa | INTEGER | ✓ |  |
| afacturar | NUMERIC(18, 6) | ✓ |  |
| facturado | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| doventa | INTEGER |  |  |

### Tabla: cotiremision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cotiremision | INTEGER |  | ✓ |
| cambodega | INTEGER | ✓ |  |
| oventa | INTEGER | ✓ |  |
| aremisionar | NUMERIC(18, 6) | ✓ |  |
| remisionado | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| doventa | INTEGER |  |  |

### Tabla: cotizacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| proyecto | INTEGER |  |  |
| cotizacion | INTEGER |  | ✓ |
| proveedor | INTEGER |  |  |
| fecha | DATETIME |  |  |
| activo | BIT |  |  |
| monto | NUMERIC(16, 6) |  |  |
| cprodprec | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| nula | BIT |  |  |
| fentrega | DATETIME | ✓ |  |
| condpago | INTEGER |  |  |
| garantia | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_cotizacion_condpago: ['condpago'] 
- IX_cotizacion_cotizacion: ['cotizacion'] 
- IX_cotizacion_cprodprec: ['cprodprec'] 
- IX_cotizacion_empresa: ['empresa'] 
- IX_cotizacion_fecha: ['fecha'] 
- IX_cotizacion_proveedor: ['proveedor'] 
- IX_cotizacion_proyecto: ['proyecto'] 
- IX_cotizacion_usuario: ['usuario'] 

### Tabla: cpagocompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cpagocompra | INTEGER |  |  |
| pagocompra | INTEGER |  | ✓ |
| npagocompra | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Fecha | DATETIME | ✓ |  |
| monto | NUMERIC(9, 2) | ✓ |  |
| montoOriginal | NUMERIC(9, 2) | ✓ |  |
| pagado | NUMERIC(9, 2) | ✓ |  |
| factor | NUMERIC(9, 2) | ✓ |  |
| moneda | INTEGER | ✓ |  |
| tasacambio | NUMERIC(9, 6) | ✓ |  |
| compraFirme | INTEGER | ✓ |  |
| ocompra | INTEGER | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: cpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nopartida | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocheque | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nofacturas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| noquedan | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| concepto | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| nula | BIT |  |  |
| quedan | BIT |  |  |
| impresa | BIT |  |  |
| cheqimp | BIT |  |  |
| conciliado | BIT |  |  |
| contabilidad | BIT |  |  |
| automatico | BIT |  |  |
| fecha | DATETIME |  |  |
| fechapago | DATETIME | ✓ |  |
| reffecha | DATETIME | ✓ |  |
| tipopart | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| periodo | INTEGER |  |  |
| ccuenta | INTEGER |  |  |
| chpartida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| debe | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| cpartida | INTEGER |  | ✓ |
| partida | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| abono | NUMERIC(16, 6) |  |  |
| CDEBE | NUMERIC(18, 6) |  |  |
| CHABER | NUMERIC(18, 6) |  |  |
| IMPRIMECHEQUE | BIT |  |  |
| CMONTO | NUMERIC(18, 6) |  |  |
| TASACAMBIOTRES | NUMERIC(18, 6) |  |  |
| pagado | BIT |  |  |

#### Índices
- IX_cpartida_ccuenta: ['ccuenta'] 
- IX_cpartida_chpartida: ['chpartida'] 
- IX_cpartida_concepto: ['concepto'] 
- IX_cpartida_cpartida: ['cpartida'] 
- IX_cpartida_cuenta: ['cuenta'] 
- IX_cpartida_empresa: ['empresa'] 
- IX_cpartida_fecha: ['fecha'] 
- IX_cpartida_moneda: ['moneda'] 
- IX_cpartida_nocheque: ['nocheque'] 
- IX_cpartida_nofacturas: ['nofacturas'] 
- IX_cpartida_nopartida: ['nopartida'] 
- IX_cpartida_noquedan: ['noquedan'] 
- IX_cpartida_partida: ['partida'] 
- IX_cpartida_periodo: ['periodo'] 
- IX_cpartida_referencia: ['referencia'] 
- IX_cpartida_tipopart: ['tipopart'] 
- IX_cpartida_usuario: ['usuario'] 

### Tabla: cprodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| ncprodprec | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainicial | DATETIME | ✓ |  |
| fechafinal | DATETIME | ✓ |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| cprodprec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_cprodprec_cprodprec: ['cprodprec'] 
- IX_cprodprec_empresa: ['empresa'] 
- IX_cprodprec_moneda: ['moneda'] 
- IX_cprodprec_ncprodprec: ['ncprodprec'] 
- IX_cprodprec_usuario: ['usuario'] 

### Tabla: ctactrocto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| ctactrocto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['cuenta'] → cuenta.['cuenta']

#### Índices
- IX_ctactrocto_ctactrocto: ['ctactrocto'] 
- IX_ctactrocto_ctrocosto: ['ctrocosto'] 
- IX_ctactrocto_cuenta: ['cuenta'] 
- IX_ctactrocto_empresa: ['empresa'] 
- IX_ctactrocto_usuario: ['usuario'] 

### Tabla: ctalong
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nctalong | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| longitud | INTEGER |  |  |
| mayor | BIT |  |  |
| activo | BIT |  |  |
| ctalong | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| simctalong | CHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rubro | BIT |  |  |
| grupo | BIT |  |  |
| nivel1 | BIT |  |  |
| nivel2 | BIT |  |  |
| nivelGasto | BIT |  |  |
| sub01 | BIT |  |  |
| sub02 | BIT |  |  |
| longoriginal | INTEGER |  |  |
| nwLong | INTEGER |  |  |

#### Índices
- IX_ctalong_ctalong: ['ctalong'] 
- IX_ctalong_empresa: ['empresa'] 
- IX_ctalong_longitud: ['longitud'] 
- IX_ctalong_nctalong: ['nctalong'] 
- IX_ctalong_nwlong: ['nwLong'] 
- IX_ctalong_usuario: ['usuario'] 

### Tabla: ctcategori
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncategori | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| ctcategori | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ctcategori_ctcategori: ['ctcategori'] 
- IX_ctcategori_empresa: ['empresa'] 
- IX_ctcategori_ncategori: ['ncategori'] 
- IX_ctcategori_usuario: ['usuario'] 

### Tabla: ctracking
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| getcompra | BIT |  |  |
| enfirme | BIT |  |  |
| nctracking | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ctracking | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: ctrocosto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| noctrocosto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nctrocosto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ctrolong | INTEGER |  |  |
| activo | BIT |  |  |
| ctrocosto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| provision | INTEGER |  |  |
| Partida | INTEGER |  |  |
| sucursal | INTEGER |  |  |
| informeRetencion | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Nombre | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Nit | VARCHAR(18) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Direccion | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono | VARCHAR(18) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Celular | VARCHAR(18) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| email | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Notas | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hijos | INTEGER |  |  |
| fechaIngreso | DATETIME |  |  |
| lider | INTEGER |  |  |
| Nacionalidad | INTEGER |  |  |
| Distrito | INTEGER |  |  |
| Domiciliado | BIT |  |  |
| porc | NUMERIC(5, 2) | ✓ |  |

#### Foreign Keys
- ['ctrolong'] → ctrolong.['ctrolong']

#### Índices
- IX_ctrocosto_ctrocosto: ['ctrocosto'] 
- IX_ctrocosto_ctrolong: ['ctrolong'] 
- IX_ctrocosto_empresa: ['empresa'] 
- IX_ctrocosto_nctrocosto: ['nctrocosto'] 
- IX_ctrocosto_noctrocosto: ['noctrocosto'] 
- IX_ctrocosto_usuario: ['usuario'] 

### Tabla: ctrolong
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nctrolong | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| longitud | INTEGER |  |  |
| activo | BIT |  |  |
| ctrolong | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rubro | BIT |  |  |
| grupo | BIT |  |  |
| nivel1 | BIT |  |  |

#### Índices
- IX_ctrolong_ctrolong: ['ctrolong'] 
- IX_ctrolong_empresa: ['empresa'] 
- IX_ctrolong_longitud: ['longitud'] 
- IX_ctrolong_nctrolong: ['nctrolong'] 
- IX_ctrolong_usuario: ['usuario'] 

### Tabla: cuenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nocuenta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ncuenta | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nocheque | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| miformato | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ctalong | INTEGER |  |  |
| rubro | INTEGER |  |  |
| banco | BIT |  |  |
| activo | BIT |  |  |
| cuenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| proveedor | BIT |  |  |
| provbol | BIT |  |  |
| Iva | BIT |  |  |
| Ret | BIT |  |  |
| Excl | BIT |  |  |
| Fovial | BIT |  |  |
| Renta | BIT |  |  |
| factor | NUMERIC(18, 6) |  |  |
| debe | BIT |  |  |
| micheque | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| AplicaRete | BIT |  |  |
| REGISTRO | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| IMPORTACION | BIT |  |  |
| misformato | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cotrans | BIT | ✓ |  |
| lineascheque | INTEGER |  |  |
| nit | VARCHAR(17) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| giro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| razonsoc | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| email | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sitioweb | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| PERCEPCION | BIT |  |  |
| CxCProveedor | BIT |  |  |
| cuentaCxC | INTEGER |  |  |
| nivelGasto | BIT |  |  |
| telefono | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| deduccion1 | BIT |  |  |
| deduccion2 | BIT |  |  |
| AplicaPercepcion | BIT |  |  |
| ActivoCirculante | BIT |  |  |
| ActivoFijo | BIT |  |  |
| PasivoCirculante | BIT |  |  |
| PasivoLargoPlazo | BIT |  |  |
| RubroProveedores | BIT |  |  |
| ObligacionesBancarias | BIT |  |  |
| ImpuestosxPagar | BIT |  |  |
| RubroBancos | BIT |  |  |
| CuentasxCobrar | BIT |  |  |
| Inventarios | BIT |  |  |
| Compras | BIT |  |  |
| RebajasyDevoluciones | BIT |  |  |
| GastosAdom | BIT |  |  |
| GastosVentas | BIT |  |  |
| GastosFinancieros | BIT |  |  |
| GastosOtros | BIT |  |  |
| GastosOperacion | BIT |  |  |
| RubroActivo | BIT |  |  |
| RubroPasivo | BIT |  |  |
| RubroCapital | BIT |  |  |
| RubroIngresos | BIT |  |  |
| RubroGastos | BIT |  |  |
| CostoVentas | BIT |  |  |
| ProductosFinancieros | BIT |  |  |
| Intereses | BIT |  |  |
| ReservaLegal | BIT |  |  |
| OtrosProdFinancieros | BIT |  |  |
| GastosNoDeducc | BIT |  |  |
| caja | BIT |  |  |
| costoVariable | BIT |  |  |
| costoFijo | BIT |  |  |
| resultados | BIT |  |  |
| nonegociable | BIT |  |  |
| cuentaclave | INTEGER |  |  |
| saldobanco | NUMERIC(18, 6) |  |  |
| ingreso | INTEGER | ✓ |  |
| nosujeto | INTEGER | ✓ |  |
| isr10 | INTEGER | ✓ |  |
| tarjeta | INTEGER | ✓ |  |
| debitofiscal | INTEGER | ✓ |  |
| creditofiscal | INTEGER | ✓ |  |
| automatica | BIT |  |  |
| cesc | BIT |  |  |
| entransito | BIT |  |  |
| tipo | INTEGER |  |  |
| clasificacion | INTEGER |  |  |
| sector | INTEGER |  |  |
| costo | INTEGER |  |  |

#### Foreign Keys
- ['ctalong'] → ctalong.['ctalong']
- ['rubro'] → rubro.['rubro']

#### Índices
- CUENTA_EMPRESA: ['empresa'] 
- IX_cuenta_ctalong: ['ctalong'] 
- IX_cuenta_cuenta: ['cuenta'] 
- IX_cuenta_empresa: ['empresa'] 
- IX_cuenta_miformato: ['miformato'] 
- IX_cuenta_misformato: ['misformato'] 
- IX_cuenta_ncuenta: ['ncuenta'] 
- IX_cuenta_nocheque: ['nocheque'] 
- IX_cuenta_nocuenta: ['nocuenta'] 
- IX_cuenta_rubro: ['rubro'] 
- IX_cuenta_usuario: ['usuario'] 

### Tabla: cuentaclave
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cuentaclave | INTEGER |  | ✓ |
| ncuentaclave | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ActivoCirculante | BIT |  |  |
| ActivoFijo | BIT |  |  |
| PasivoCirculante | BIT |  |  |
| PasivoLargoPlazo | BIT |  |  |
| RubroProveedores | BIT |  |  |
| ObligacionesBancarias | BIT |  |  |
| ImpuestosxPagar | BIT |  |  |
| RubroBancos | BIT |  |  |
| CuentasxCobrar | BIT |  |  |
| Inventarios | BIT |  |  |
| Compras | BIT |  |  |
| RebajasyDevoluciones | BIT |  |  |
| GastosAdom | BIT |  |  |
| GastosVentas | BIT |  |  |
| GastosFinancieros | BIT |  |  |
| GastosOtros | BIT |  |  |
| GastosOperacion | BIT |  |  |
| RubroActivo | BIT |  |  |
| RubroPasivo | BIT |  |  |
| RubroCapital | BIT |  |  |
| RubroIngresos | BIT |  |  |
| RubroGastos | BIT |  |  |
| CostoVentas | BIT |  |  |
| ProductosFinancieros | BIT |  |  |
| Intereses | BIT |  |  |
| ReservaLegal | BIT |  |  |
| OtrosProdFinancieros | BIT |  |  |
| GastosNoDeducc | BIT |  |  |
| RubroIntereses | BIT |  |  |
| caja | BIT |  |  |
| costoVariable | BIT |  |  |
| costoFijo | BIT |  |  |
| resultados | BIT |  |  |
| nonegociable | BIT |  |  |
| activo | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| CuentaXPagar | BIT |  |  |
| Anticipo | BIT |  |  |

### Tabla: cuentapuente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cuenta | INTEGER |  |  |
| cuentapuente | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_cuentapuente_cuenta: ['cuenta'] 
- IX_cuentapuente_cuentapuente: ['cuentapuente'] 
- IX_cuentapuente_empresa: ['empresa'] 
- IX_cuentapuente_usuario: ['usuario'] 

### Tabla: cuentatipomov
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Activo | BIT |  |  |
| tipomov | INTEGER |  |  |
| sucursal | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| cuentatipomov | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| cuentaiva | INTEGER |  |  |

### Tabla: cxp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATE | ✓ |  |
| debe | FLOAT | ✓ |  |
| haber | FLOAT | ✓ |  |
| cdebe | FLOAT | ✓ |  |
| cmonto | FLOAT | ✓ |  |
| chaber | FLOAT | ✓ |  |
| nopartida | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| noquedan | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocheque | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha2 | DATE | ✓ |  |
| debe2 | FLOAT | ✓ |  |
| haber2 | FLOAT | ✓ |  |
| cdebe2 | FLOAT | ✓ |  |
| cmonto2 | FLOAT | ✓ |  |
| chaber2 | FLOAT | ✓ |  |
| nopartida2 | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| noquedan2 | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocheque2 | NCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| abono | FLOAT | ✓ |  |

### Tabla: dDiezmo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dDiezmo | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| monto | NUMERIC(18, 6) |  |  |
| diezmo | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |
| numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| remesa | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- ci_azure_fixup_dbo_dDiezmo: ['dDiezmo'] 

### Tabla: dGestionTaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dGestionTaller | INTEGER |  | ✓ |
| GestionTaller | INTEGER |  |  |
| rupfase | INTEGER |  |  |
| ausuario | INTEGER |  |  |
| susuario | INTEGER |  |  |
| finicio | DATETIME | ✓ |  |
| ffin | DATETIME | ✓ |  |
| perdida | NUMERIC(18, 6) |  |  |
| devolucion | BIT |  |  |
| adicion | BIT |  |  |
| nula | BIT |  |  |
| suspendida | BIT |  |  |
| impresa | BIT |  |  |
| Operadores | INTEGER |  |  |
| estatus | INTEGER |  |  |
| bodega | INTEGER |  |  |
| ingreso | BIT |  |  |
| salida | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rupstatus | INTEGER |  |  |
| costo | NUMERIC(18, 6) |  |  |
| dias | INTEGER |  |  |
| horas | INTEGER |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| mitiempo | NUMERIC(18, 6) |  |  |
| resttiempo | NUMERIC(18, 6) |  |  |
| factura | INTEGER |  |  |

#### Foreign Keys
- ['GestionTaller'] → GestionTaller.['GestionTaller']
- ['rupfase'] → RupFase.['RupFase']

### Tabla: dOrdenTrabajo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dOrdenTrabajo | INTEGER |  | ✓ |
| ordenTrabajo | INTEGER |  |  |
| rupfase | INTEGER |  |  |
| ausuario | INTEGER |  |  |
| susuario | INTEGER |  |  |
| finicio | DATETIME |  |  |
| ffin | DATETIME | ✓ |  |
| perdida | NUMERIC(18, 6) |  |  |
| devolucion | BIT |  |  |
| adicion | BIT |  |  |
| nula | BIT |  |  |
| suspendida | BIT |  |  |
| impresa | BIT |  |  |
| Operadores | INTEGER |  |  |
| estatus | INTEGER |  |  |
| bodega | INTEGER |  |  |
| ingreso | BIT |  |  |
| salida | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| rupstatus | INTEGER |  |  |
| costo | NUMERIC(18, 6) |  |  |
| dias | INTEGER |  |  |
| horas | INTEGER |  |  |
| Informe | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| almacen | INTEGER |  |  |

### Tabla: dafp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| minimo | NUMERIC(18, 9) | ✓ |  |
| maximo | NUMERIC(18, 9) | ✓ |  |
| totdev | NUMERIC(18, 9) | ✓ |  |
| oper1 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| condicion1 | NUMERIC(18, 6) | ✓ |  |
| oper2 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| patronal | NUMERIC(18, 6) | ✓ |  |
| activo | BIT | ✓ |  |
| pension | NUMERIC(18, 6) | ✓ |  |
| comision | NUMERIC(18, 6) | ✓ |  |
| afp | INTEGER | ✓ |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| minimoseg | NUMERIC(18, 6) |  |  |
| maximoseg | NUMERIC(18, 6) |  |  |
| dafp | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| CUOTAEMPLEADO | NUMERIC(18, 6) |  |  |
| CUOTAPATRONO | NUMERIC(18, 6) |  |  |

#### Índices
- IX_dafp_afp: ['afp'] 
- IX_dafp_dafp: ['dafp'] 
- IX_dafp_empresa: ['empresa'] 
- IX_dafp_oper1: ['oper1'] 
- IX_dafp_oper2: ['oper2'] 
- IX_dafp_usuario: ['usuario'] 

### Tabla: dalmacen
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| kardex | INTEGER |  |  |
| almacen | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| cuarentena | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hcuarentena | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| dalmacen | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| PRECIO | NUMERIC(18, 6) |  |  |
| nula | BIT |  |  |
| dfactura | INTEGER |  |  |
| nombre | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dordentrabajo | INTEGER |  |  |
| presenta | INTEGER |  |  |
| facturar | BIT |  |  |
| facturado | BIT |  |  |
| factura | INTEGER |  |  |
| linea | INTEGER |  |  |
| tipoescala | INTEGER |  |  |
| producto | INTEGER |  |  |
| lote | INTEGER |  |  |
| bodega | INTEGER |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecvence | DATETIME | ✓ |  |

#### Foreign Keys
- ['almacen'] → almacen.['almacen']
- ['kardex'] → kardex.['kardex']

#### Índices
- dalmacen_kardex: ['kardex'] 
- IX_dalmacen_almacen: ['almacen'] 
- IX_dalmacen_dalmacen: ['dalmacen'] 
- IX_dalmacen_dfactura: ['dfactura'] 
- IX_dalmacen_empresa: ['empresa'] 
- IX_dalmacen_kardex: ['kardex'] 
- IX_dalmacen_usuario: ['usuario'] 

### Tabla: dalmacennc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dalmacen | INTEGER | ✓ |  |
| descuento | NUMERIC(9, 2) | ✓ |  |
| fecha | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dalmacennc | INTEGER |  | ✓ |

### Tabla: datosComision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| datoscomision | INTEGER |  | ✓ |
| codigo | INTEGER |  |  |
| casaprod | INTEGER |  |  |
| comision | NUMERIC(18, 6) |  |  |
| factorcomision | NUMERIC(18, 6) |  |  |
| porcnologro | NUMERIC(18, 6) |  |  |
| AntiguedadCobro | NUMERIC(18, 6) |  |  |
| FactorLogro | NUMERIC(18, 6) |  |  |
| Logrocuota | NUMERIC(18, 6) |  |  |
| MontoVendido | NUMERIC(18, 6) |  |  |
| cuotaVendedor | NUMERIC(18, 6) |  |  |
| MontoCobrado | NUMERIC(18, 6) |  |  |
| ComisionFija | BIT |  |  |
| periodocomision | INTEGER |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: dbudget
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME | ✓ |  |
| cuenta | INTEGER | ✓ |  |
| monto | NUMERIC(12, 2) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| dbudget | INTEGER |  | ✓ |

### Tabla: dcambio
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cambio | NUMERIC(18, 6) | ✓ |  |
| cambio2 | NUMERIC(18, 6) | ✓ |  |
| fecha | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dcambio | INTEGER |  | ✓ |

### Tabla: dcambodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| cuarentena | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hcuarentena | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| kardex | INTEGER |  |  |
| kardex1 | INTEGER |  |  |
| cambodega | INTEGER |  |  |
| dcambodega | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| precio | NUMERIC(16, 6) |  |  |
| nula | BIT |  |  |
| nombre | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| original | NUMERIC(18, 6) |  |  |
| devolucion1 | NUMERIC(18, 6) |  |  |
| devolucion2 | NUMERIC(18, 6) |  |  |
| devolucion3 | NUMERIC(18, 6) |  |  |
| devolucion4 | NUMERIC(18, 6) |  |  |
| devolucion5 | NUMERIC(18, 6) |  |  |
| fProducto | INTEGER |  |  |
| afacturar | BIT |  |  |
| facturado | BIT |  |  |
| fkardex | INTEGER |  |  |
| fcantidad | NUMERIC(18, 6) |  |  |
| precio1 | NUMERIC(18, 6) |  |  |
| precio2 | NUMERIC(18, 6) |  |  |
| facturar | BIT |  |  |
| factura | INTEGER |  |  |
| fisico | INTEGER |  |  |
| fechaliq | DATETIME | ✓ |  |
| venta | INTEGER |  |  |
| efectivo | NUMERIC(18, 6) |  |  |
| linea | INTEGER |  |  |
| tipoescala | INTEGER |  |  |
| mformula | INTEGER | ✓ |  |
| gratif | NUMERIC(9, 2) |  |  |
| devolucion6 | NUMERIC(18, 6) |  |  |
| devolucion7 | NUMERIC(18, 6) |  |  |
| devolucion8 | NUMERIC(18, 6) |  |  |
| devolucion9 | NUMERIC(18, 6) |  |  |
| devolucion10 | NUMERIC(18, 6) |  |  |
| devolucion11 | NUMERIC(18, 6) |  |  |
| devolucion12 | NUMERIC(18, 6) |  |  |
| devolucion13 | NUMERIC(18, 6) |  |  |
| devolucion14 | NUMERIC(18, 6) |  |  |
| devolucion15 | NUMERIC(18, 6) |  |  |

#### Foreign Keys
- ['cambodega'] → cambodega.['cambodega']
- ['kardex'] → kardex.['kardex']
- ['kardex1'] → kardex.['kardex']

#### Índices
- IX_dcambodega_cambodega: ['cambodega'] 
- IX_dcambodega_dcambodega: ['dcambodega'] 
- IX_dcambodega_empresa: ['empresa'] 
- IX_dcambodega_kardex: ['kardex'] 
- IX_dcambodega_kardex1: ['kardex1'] 
- IX_dcambodega_usuario: ['usuario'] 

### Tabla: dcargaAnticipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| CargaAnticipo | INTEGER |  |  |
| GastoAnticipo | INTEGER |  |  |
| cargo | NUMERIC(18, 6) |  |  |
| dcargaAnticipo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fecha | DATETIME | ✓ |  |

### Tabla: dcompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| reservado | NUMERIC(18, 6) |  |  |
| bonificado | NUMERIC(18, 6) |  |  |
| hcantidad | NUMERIC(18, 6) |  |  |
| hreservado | NUMERIC(18, 6) |  |  |
| hbonificado | NUMERIC(18, 6) |  |  |
| precio | NUMERIC(18, 6) |  |  |
| preciolista | NUMERIC(18, 6) |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| costo | NUMERIC(18, 6) |  |  |
| tax | NUMERIC(18, 6) |  |  |
| cprecio | NUMERIC(18, 6) | ✓ |  |
| vtax | NUMERIC(18, 6) | ✓ |  |
| gasto | NUMERIC(18, 6) | ✓ |  |
| kardex | INTEGER |  |  |
| compra | INTEGER |  |  |
| dcompra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pdesc | NUMERIC(18, 6) |  |  |
| vdesc | NUMERIC(18, 6) |  |  |
| vgdesc | NUMERIC(18, 6) |  |  |
| fovial | NUMERIC(18, 6) |  |  |
| ncmonto | NUMERIC(18, 6) |  |  |
| ncafecta | NUMERIC(18, 6) |  |  |
| ncexenta | NUMERIC(18, 6) |  |  |
| ncviva | NUMERIC(18, 6) |  |  |
| nula | BIT |  |  |
| resolucion1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| resolucion2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| resolFecha | DATETIME | ✓ |  |
| linea | INTEGER |  |  |
| cotrans | NUMERIC(18, 6) |  |  |
| resolucion | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ptax | NUMERIC(18, 6) |  |  |
| tipoescala | INTEGER |  |  |
| costoprom | NUMERIC(16, 6) | ✓ |  |
| gratificado | NUMERIC(9, 2) |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecvence | DATETIME | ✓ |  |
| producto | INTEGER |  |  |
| lote | INTEGER | ✓ |  |
| bodega | INTEGER |  |  |
| precio1 | NUMERIC(12, 6) | ✓ |  |
| precio2 | NUMERIC(12, 6) | ✓ |  |
| precio3 | NUMERIC(12, 6) | ✓ |  |
| precio4 | NUMERIC(12, 6) | ✓ |  |
| precio5 | NUMERIC(12, 6) | ✓ |  |
| dordentrabajo | INTEGER | ✓ |  |

#### Foreign Keys
- ['kardex'] → kardex.['kardex']

#### Índices
- IX_dcompra_compra: ['compra'] 
- IX_dcompra_dcompra: ['dcompra'] 
- IX_dcompra_empresa: ['empresa'] 
- IX_dcompra_kardex: ['kardex'] 
- IX_dcompra_usuario: ['usuario'] 

### Tabla: dcompranc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dcompra | INTEGER | ✓ |  |
| descuento | NUMERIC(9, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dcompranc | INTEGER |  | ✓ |
| difcambio | NUMERIC(5, 2) | ✓ |  |

### Tabla: dconciliado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dconciliado | INTEGER |  | ✓ |
| conciliado | NUMERIC(9, 2) | ✓ |  |
| partida | INTEGER | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: dcontrato
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| gratificado | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hbonificado | NUMERIC(16, 6) |  |  |
| hgratificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolista | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| texto | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| factorinteres | NUMERIC(16, 6) |  |  |
| factormora | NUMERIC(16, 6) |  |  |
| contrato | INTEGER |  |  |
| dcontrato | INTEGER |  | ✓ |
| kardex | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| costo | NUMERIC(16, 6) |  |  |
| pprima | NUMERIC(16, 6) |  |  |
| letras | NUMERIC(16, 6) |  |  |
| nula | BIT |  |  |

#### Foreign Keys
- ['contrato'] → contrato.['contrato']
- ['kardex'] → kardex.['kardex']

#### Índices
- IX_dcontrato_contrato: ['contrato'] 
- IX_dcontrato_dcontrato: ['dcontrato'] 
- IX_dcontrato_empresa: ['empresa'] 
- IX_dcontrato_kardex: ['kardex'] 
- IX_dcontrato_texto: ['texto'] 
- IX_dcontrato_usuario: ['usuario'] 

### Tabla: dcontrola
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tabla | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| equipo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Nuevo | BIT |  |  |
| modificar | BIT |  |  |
| eliminar | BIT |  |  |
| dcontrola | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| aplicacion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: dcontrolcarga
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| BLNumero | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| camion | INTEGER |  |  |
| tipoviaje | INTEGER |  |  |
| motorista | INTEGER |  |  |
| estatus | INTEGER |  |  |
| munipickat | INTEGER |  |  |
| munientrega | INTEGER |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaentrega | DATETIME | ✓ |  |
| fechasalida | DATETIME | ✓ |  |
| fechallegada | DATETIME | ✓ |  |
| impresa | BIT |  |  |
| montfact | NUMERIC(18, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| addcharge | NUMERIC(18, 6) |  |  |
| controlcarga | INTEGER |  |  |
| dcontrolcarga | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: dcontrolvence
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dcontrolvence | INTEGER |  | ✓ |
| dfactura | INTEGER |  |  |
| uvendidas | NUMERIC(18, 6) |  |  |
| vendida | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| venta | NUMERIC(16, 8) |  |  |
| controlvence | INTEGER |  |  |
| diasvence | INTEGER |  |  |
| saldo | NUMERIC(18, 6) |  |  |

### Tabla: dcpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| orden | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| banco | BIT |  |  |
| cheque | BIT |  |  |
| cheqnulo | BIT |  |  |
| aquien | BIT |  |  |
| cheqimp | BIT |  |  |
| concepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| debe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| hdebe | NUMERIC(16, 6) |  |  |
| hhaber | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| hphaber | NUMERIC(16, 6) |  |  |
| hpdebe | NUMERIC(16, 6) |  |  |
| partida | INTEGER |  |  |
| Cpartida | INTEGER |  |  |
| Dpartida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| dcpartida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| hconcepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Automatico | BIT |  |  |

#### Índices
- IX_dcpartida_concepto: ['concepto'] 
- IX_dcpartida_Cpartida: ['Cpartida'] 
- IX_dcpartida_ctrocosto: ['ctrocosto'] 
- IX_dcpartida_cuenta: ['cuenta'] 
- IX_dcpartida_dcpartida: ['dcpartida'] 
- IX_dcpartida_Dpartida: ['Dpartida'] 
- IX_dcpartida_empresa: ['empresa'] 
- IX_dcpartida_hconcepto: ['hconcepto'] 
- IX_dcpartida_moneda: ['moneda'] 
- IX_dcpartida_orden: ['orden'] 
- IX_dcpartida_partida: ['partida'] 
- IX_dcpartida_usuario: ['usuario'] 

### Tabla: dcprodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| pfecha | DATETIME | ✓ |  |
| pminimo | NUMERIC(16, 6) |  |  |
| precioa | NUMERIC(16, 6) |  |  |
| preciob | NUMERIC(16, 6) |  |  |
| precioc | NUMERIC(16, 6) |  |  |
| cantidada | INTEGER |  |  |
| cantidadb | INTEGER |  |  |
| cantidadc | INTEGER |  |  |
| mprecio | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| fprecio | NUMERIC(16, 6) |  |  |
| cfecha | DATETIME | ✓ |  |
| factor | NUMERIC(16, 6) |  |  |
| producto | INTEGER |  |  |
| cprodprec | INTEGER |  |  |
| dcprodprec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tprecio | NUMERIC(16, 6) |  |  |

#### Foreign Keys
- ['producto'] → producto.['producto']

#### Índices
- IX_dcprodprec_cantidada: ['cantidada'] 
- IX_dcprodprec_cantidadb: ['cantidadb'] 
- IX_dcprodprec_cantidadc: ['cantidadc'] 
- IX_dcprodprec_cprodprec: ['cprodprec'] 
- IX_dcprodprec_dcprodprec: ['dcprodprec'] 
- IX_dcprodprec_empresa: ['empresa'] 
- IX_dcprodprec_producto: ['producto'] 
- IX_dcprodprec_usuario: ['usuario'] 

### Tabla: dcuenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| debe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| adebe | NUMERIC(16, 6) |  |  |
| ahaber | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| apdebe | NUMERIC(16, 6) |  |  |
| aphaber | NUMERIC(16, 6) |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| periodo | INTEGER |  |  |
| dcuenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fecha | DATETIME |  |  |
| tienemov | BIT |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |

#### Índices
- dcuenta_cuuenta_empresa_ctrocosto: ['cuenta', 'empresa', 'ctrocosto'] 
- dcuenta_empresa: ['empresa'] 
- dcuenta_empresa_ctrocosto: ['empresa', 'ctrocosto'] 
- IX_dcuenta_ctrocosto: ['ctrocosto'] 
- IX_dcuenta_cuenta: ['cuenta'] 
- IX_dcuenta_empresa: ['empresa'] 
- IX_dcuenta_fecha: ['fecha'] 
- IX_dcuenta_moneda: ['moneda'] 
- IX_dcuenta_periodo: ['periodo'] 
- IX_dcuenta_usuario: ['usuario'] 

### Tabla: decimotercero
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipopla | INTEGER |  |  |
| empleado | INTEGER |  |  |
| finicio | DATETIME |  |  |
| ffin | DATETIME |  |  |
| sueldo | NUMERIC(18, 6) |  |  |
| spromedio | NUMERIC(18, 6) |  |  |
| comision | NUMERIC(18, 6) |  |  |
| cpromedio | NUMERIC(18, 6) |  |  |
| pagos | INTEGER |  |  |
| fcontrato | DATETIME |  |  |
| fmaxima | DATETIME |  |  |
| dias | INTEGER |  |  |
| facotr | NUMERIC(18, 6) |  |  |
| valor | NUMERIC(18, 6) |  |  |
| horatiempo | DATETIME |  |  |
| decimotercero | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

### Tabla: depend
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ndepend | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| edad | INTEGER |  |  |
| parentes | INTEGER | ✓ |  |
| activo | BIT |  |  |
| empleado | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER | ✓ |  |
| depend | INTEGER |  | ✓ |

#### Índices
- IX_depend_depend: ['depend'] 
- IX_depend_edad: ['edad'] 
- IX_depend_empleado: ['empleado'] 
- IX_depend_empresa: ['empresa'] 
- IX_depend_ndepend: ['ndepend'] 
- IX_depend_parentes: ['parentes'] 
- IX_depend_usuario: ['usuario'] 

### Tabla: depto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ndepto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| preferido | BIT |  |  |
| pais | INTEGER |  |  |
| depto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| codpostal | VARCHAR(7) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| codigo | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cod_postal | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['pais'] → pais.['pais']

#### Índices
- IX_depto_depto: ['depto'] 
- IX_depto_empresa: ['empresa'] 
- IX_depto_ndepto: ['ndepto'] 
- IX_depto_pais: ['pais'] 
- IX_depto_usuario: ['usuario'] 

### Tabla: descmax
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| porcmax | NUMERIC(16, 6) |  |  |
| descmax | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_descmax_descmax: ['descmax'] 
- IX_descmax_empresa: ['empresa'] 
- IX_descmax_usuario: ['usuario'] 

### Tabla: detallecotizacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cotizacion | INTEGER |  |  |
| producto | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| aceptado | BIT |  |  |
| entregado | BIT |  |  |
| comprado | BIT |  |  |
| activo | BIT |  |  |
| fechaentrega | DATETIME | ✓ |  |
| precioentrega | NUMERIC(16, 6) |  |  |
| detallecotizacion | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_detallecotizacion_cotizacion: ['cotizacion'] 
- IX_detallecotizacion_detallecotizacion: ['detallecotizacion'] 
- IX_detallecotizacion_empresa: ['empresa'] 
- IX_detallecotizacion_producto: ['producto'] 
- IX_detallecotizacion_usuario: ['usuario'] 

### Tabla: detallepago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| detallepago | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| Banco1 | INTEGER |  |  |
| cheque1 | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| MontBanco1 | NUMERIC(18, 6) |  |  |
| Banco2 | INTEGER |  |  |
| cheque2 | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| MontBanco2 | NUMERIC(18, 6) |  |  |
| TarjetaCredito | INTEGER |  |  |
| notarjeta | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montTarjeta | NUMERIC(18, 6) |  |  |
| Efectivo | NUMERIC(18, 6) |  |  |

#### Índices
- IX_detallepago_Banco1: ['Banco1'] 
- IX_detallepago_Banco2: ['Banco2'] 
- IX_detallepago_cheque1: ['cheque1'] 
- IX_detallepago_cheque2: ['cheque2'] 
- IX_detallepago_detallepago: ['detallepago'] 
- IX_detallepago_factura: ['factura'] 
- IX_detallepago_notarjeta: ['notarjeta'] 
- IX_detallepago_TarjetaCredito: ['TarjetaCredito'] 

### Tabla: dfactmes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfactura | INTEGER |  |  |
| dregciclo | INTEGER |  |  |
| mes | DATETIME | ✓ |  |
| activo | BIT | ✓ |  |
| dfactmes | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_dfactmes_dfactmes: ['dfactmes'] 
- IX_dfactmes_dfactura: ['dfactura'] 
- IX_dfactmes_dregciclo: ['dregciclo'] 
- IX_dfactmes_empresa: ['empresa'] 
- IX_dfactmes_usuario: ['usuario'] 

### Tabla: dfactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| gratificado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hgratificado | NUMERIC(16, 6) |  |  |
| hbonificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolista | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| texto | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| factura | INTEGER |  |  |
| kardex | INTEGER |  |  |
| costo | NUMERIC(16, 6) |  |  |
| dfactura | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| ncmonto | NUMERIC(16, 6) |  |  |
| ncafecta | NUMERIC(16, 6) |  |  |
| ncexenta | NUMERIC(16, 6) |  |  |
| ncviva | NUMERIC(16, 6) |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| nombre | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nula | BIT |  |  |
| talonario | INTEGER | ✓ |  |
| mes | DATETIME | ✓ |  |
| apliquemora | BIT |  |  |
| unidadVenta | INTEGER |  |  |
| PrecioUVenta | NUMERIC(16, 6) |  |  |
| CantidadUVenta | NUMERIC(16, 6) |  |  |
| ReservadoUVenta | NUMERIC(16, 6) |  |  |
| BonificadoUVenta | NUMERIC(16, 6) |  |  |
| GratificadoUVenta | NUMERIC(16, 6) |  |  |
| Cotrans | NUMERIC(16, 8) |  |  |
| vendedor | INTEGER |  |  |
| prioridad | INTEGER |  |  |
| estado | INTEGER |  |  |
| factalm | INTEGER |  |  |
| dregciclo | INTEGER |  |  |
| dgratif | NUMERIC(18, 6) |  |  |
| gratif | NUMERIC(18, 6) |  |  |
| vineta | BIT |  |  |
| bomba | INTEGER |  |  |
| concaja | BIT |  |  |
| bonifreservado | BIT |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| pcomision | NUMERIC(5, 2) |  |  |
| uvendidas | NUMERIC(16, 8) |  |  |
| vinculado | BIT |  |  |
| fraccion | NUMERIC(18, 6) |  |  |
| nbonif | INTEGER |  |  |
| resolucion1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| resolfecha | DATETIME | ✓ |  |
| linea | INTEGER |  |  |
| oPrecio | NUMERIC(18, 6) |  |  |
| tipoescala | INTEGER |  |  |
| cotiza | INTEGER |  |  |

#### Foreign Keys
- ['factura'] → factura.['factura']
- ['kardex'] → kardex.['kardex']

#### Índices
- dfactura_dregciclo_empresa: ['dregciclo', 'empresa'] 
- dfactura_factura_cantidad: ['factura', 'empresa'] 
- IX_dfactura_dfactura: ['dfactura'] 
- IX_dfactura_dregciclo: ['dregciclo'] 
- IX_dfactura_empresa: ['empresa'] 
- IX_dfactura_estado: ['estado'] 
- IX_dfactura_factalm: ['factalm'] 
- IX_dfactura_factura: ['factura'] 
- IX_dfactura_kardex: ['kardex'] 
- IX_dfactura_nombre: ['nombre'] 
- IX_dfactura_prioridad: ['prioridad'] 
- IX_dfactura_talonario: ['talonario'] 
- IX_dfactura_texto: ['texto'] 
- IX_dfactura_unidadVenta: ['unidadVenta'] 
- IX_dfactura_usuario: ['usuario'] 
- IX_dfactura_vendedor: ['vendedor'] 

### Tabla: dfliquida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfliquida | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| kardex | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| rliquida | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montliquida | NUMERIC(16, 6) |  |  |
| prodprec | INTEGER |  |  |
| fecha | DATETIME |  |  |

#### Índices
- IX_dfliquida_clientes: ['clientes'] 
- IX_dfliquida_dfliquida: ['dfliquida'] 
- IX_dfliquida_empresa: ['empresa'] 
- IX_dfliquida_factura: ['factura'] 
- IX_dfliquida_fecha: ['fecha'] 
- IX_dfliquida_kardex: ['kardex'] 
- IX_dfliquida_numedocu: ['numedocu'] 
- IX_dfliquida_prodprec: ['prodprec'] 
- IX_dfliquida_rliquida: ['rliquida'] 
- IX_dfliquida_usuario: ['usuario'] 
- IX_dfliquida_vendedor: ['vendedor'] 

### Tabla: dformulataller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| km3 | BIT |  |  |
| km5 | BIT |  |  |
| km6 | BIT |  |  |
| km9 | BIT |  |  |
| km10 | BIT |  |  |
| km12 | BIT |  |  |
| km15 | BIT |  |  |
| km18 | BIT |  |  |
| km20 | BIT |  |  |
| km21 | BIT |  |  |
| km24 | BIT |  |  |
| km25 | BIT |  |  |
| km27 | BIT |  |  |
| km30 | BIT |  |  |
| km33 | BIT |  |  |
| km35 | BIT |  |  |
| km36 | BIT |  |  |
| km40 | BIT |  |  |
| km150 | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| producto | INTEGER |  |  |
| formulaTaller | INTEGER |  |  |
| dformulataller | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| descripcion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| orden | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rupfase | INTEGER |  |  |

#### Foreign Keys
- ['rupfase'] → RupFase.['RupFase']
- ['formulaTaller'] → formulataller.['formulataller']

### Tabla: dfpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| concepto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tcondicion1 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tcondicion2 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tcondicion3 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tcondicion4 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tcondicion5 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| debe | BIT |  |  |
| fpartida | INTEGER |  |  |
| dfpartida | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['fpartida'] → fpartida.['fpartida']

#### Índices
- IX_dfpartida_concepto: ['concepto'] 
- IX_dfpartida_ctrocosto: ['ctrocosto'] 
- IX_dfpartida_cuenta: ['cuenta'] 
- IX_dfpartida_dfpartida: ['dfpartida'] 
- IX_dfpartida_empresa: ['empresa'] 
- IX_dfpartida_fpartida: ['fpartida'] 
- IX_dfpartida_tcondicion1: ['tcondicion1'] 
- IX_dfpartida_tcondicion2: ['tcondicion2'] 
- IX_dfpartida_tcondicion3: ['tcondicion3'] 
- IX_dfpartida_tcondicion4: ['tcondicion4'] 
- IX_dfpartida_tcondicion5: ['tcondicion5'] 
- IX_dfpartida_usuario: ['usuario'] 

### Tabla: dgetcompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| docompra | INTEGER |  |  |
| precio | NUMERIC(18, 6) |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| bonificado | NUMERIC(18, 6) |  |  |
| montcomp | NUMERIC(18, 6) |  |  |
| hcantidad | NUMERIC(18, 6) |  |  |
| hbonificado | NUMERIC(18, 6) |  |  |
| hprecio | NUMERIC(18, 6) |  |  |
| vcantidad | NUMERIC(18, 6) |  |  |
| hmontcomp | NUMERIC(18, 6) |  |  |
| pdesc | NUMERIC(5, 2) |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| lote | INTEGER |  |  |
| kardex | INTEGER |  |  |
| dgetcompra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| getcompra | INTEGER |  |  |

### Tabla: diaferiado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| ndiaferiado | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| diaferiado | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| nhoraspago | NUMERIC(18, 6) | ✓ |  |

### Tabla: diasLaborados
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dia | DATETIME |  |  |
| esdomingo | BIT |  |  |
| esasueto | BIT |  |  |
| espermanente | BIT |  |  |
| diaslaborados | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: dimpuesto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| compra | INTEGER |  | ✓ |
| impuesto | INTEGER |  | ✓ |
| valor | FLOAT | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

### Tabla: dlinea1
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| linea1 | INTEGER |  |  |
| dlinea1 | INTEGER |  | ✓ |
| tarea | INTEGER |  |  |
| entregable | INTEGER |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| estatus | INTEGER |  |  |
| hora1 | DATETIME | ✓ |  |
| hora2 | DATETIME | ✓ |  |
| costohora | NUMERIC(18, 2) |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_dlinea1_dlinea1: ['dlinea1'] 
- IX_dlinea1_empresa: ['empresa'] 
- IX_dlinea1_entregable: ['entregable'] 
- IX_dlinea1_estatus: ['estatus'] 
- IX_dlinea1_linea1: ['linea1'] 
- IX_dlinea1_notas: ['notas'] 
- IX_dlinea1_tarea: ['tarea'] 
- IX_dlinea1_usuario: ['usuario'] 

### Tabla: dlinea2
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dlinea2 | INTEGER |  | ✓ |
| dlinea1 | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| estatus | INTEGER |  |  |
| hora1 | DATETIME | ✓ |  |
| hora2 | DATETIME | ✓ |  |
| Notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_dlinea2_dlinea1: ['dlinea1'] 
- IX_dlinea2_dlinea2: ['dlinea2'] 
- IX_dlinea2_empresa: ['empresa'] 
- IX_dlinea2_estatus: ['estatus'] 
- IX_dlinea2_Notas: ['Notas'] 
- IX_dlinea2_rusuario: ['rusuario'] 
- IX_dlinea2_usuario: ['usuario'] 

### Tabla: dlpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| orden | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| concepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| debemont | NUMERIC(16, 6) |  |  |
| habermont | NUMERIC(16, 6) |  |  |
| lpartida | INTEGER |  |  |
| dfpartida | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| dlpartida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['cuenta'] → cuenta.['cuenta']
- ['lpartida'] → lpartida.['lpartida']

#### Índices
- IX_dlpartida_concepto: ['concepto'] 
- IX_dlpartida_ctrocosto: ['ctrocosto'] 
- IX_dlpartida_cuenta: ['cuenta'] 
- IX_dlpartida_dfpartida: ['dfpartida'] 
- IX_dlpartida_dlpartida: ['dlpartida'] 
- IX_dlpartida_empresa: ['empresa'] 
- IX_dlpartida_lpartida: ['lpartida'] 
- IX_dlpartida_moneda: ['moneda'] 
- IX_dlpartida_orden: ['orden'] 
- IX_dlpartida_usuario: ['usuario'] 

### Tabla: dmaestro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tabla | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dmaestros | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dmaestro | INTEGER |  | ✓ |

#### Índices
- IX_dmaestro_dmaestro: ['dmaestro'] 
- IX_dmaestro_dmaestros: ['dmaestros'] 
- IX_dmaestro_empresa: ['empresa'] 
- IX_dmaestro_tabla: ['tabla'] 
- IX_dmaestro_usuario: ['usuario'] 

### Tabla: docRecibido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| docRecibido | INTEGER |  | ✓ |
| DocumentoViaje | INTEGER |  |  |
| dpfactura | INTEGER |  |  |
| Recibido | BIT |  |  |
| Notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: docliente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| docompra | INTEGER | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| docliente | INTEGER |  | ✓ |

### Tabla: docompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolist | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| tax | NUMERIC(16, 6) |  |  |
| cprecio | NUMERIC(16, 6) |  |  |
| vtax | NUMERIC(16, 6) |  |  |
| gasto | NUMERIC(16, 6) |  |  |
| producto | INTEGER |  |  |
| lote | INTEGER |  |  |
| bodega | INTEGER |  |  |
| ocompra | INTEGER |  |  |
| compra | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| rcantidad | NUMERIC(16, 6) |  |  |
| rreservado | NUMERIC(16, 6) |  |  |
| rbonificado | NUMERIC(16, 6) |  |  |
| rprecio | NUMERIC(16, 6) |  |  |
| rmontfact | NUMERIC(16, 6) |  |  |
| rpdesc | NUMERIC(16, 6) |  |  |
| rvdesc | NUMERIC(16, 6) |  |  |
| ccantidad | NUMERIC(16, 6) |  |  |
| presenta | INTEGER |  |  |
| docompra | INTEGER |  | ✓ |
| unidades | NUMERIC(16, 6) |  |  |
| cbonificado | NUMERIC(18, 6) |  |  |
| linea | INTEGER | ✓ |  |
| fechaDespacho | DATETIME | ✓ |  |
| fechaRecepcion | DATETIME | ✓ |  |
| umedida | INTEGER |  |  |
| ocantidad | NUMERIC(18, 6) |  |  |
| cusuario | INTEGER |  |  |
| cenvio | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| kardex | INTEGER |  |  |
| original | NUMERIC(18, 6) |  |  |
| devolucion1 | NUMERIC(18, 6) |  |  |
| devolucion2 | NUMERIC(18, 6) |  |  |
| devolucion3 | NUMERIC(18, 6) |  |  |
| devolucion4 | NUMERIC(18, 6) |  |  |
| devolucion5 | NUMERIC(18, 6) |  |  |
| entrega1 | NUMERIC(18, 6) |  |  |
| entrega2 | NUMERIC(18, 6) |  |  |
| entrega3 | NUMERIC(18, 6) |  |  |
| entrega4 | NUMERIC(18, 6) |  |  |
| entrega5 | NUMERIC(18, 6) |  |  |
| nproducto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso | NUMERIC(18, 6) |  |  |
| minimo | NUMERIC(18, 6) |  |  |
| maximo | NUMERIC(18, 6) |  |  |
| miimagen | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipoprod | INTEGER |  |  |
| tipoescala | INTEGER |  |  |
| micolor | INTEGER |  |  |
| sexo | INTEGER |  |  |
| clase | INTEGER |  |  |
| temporada | INTEGER |  |  |
| fabricacion | INTEGER |  |  |
| casaprod | INTEGER |  |  |
| categori | INTEGER |  |  |
| envio | INTEGER |  |  |
| icdbarra1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra3 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra4 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra5 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra6 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra7 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra8 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipoescala_cm3 | NUMERIC(18, 6) |  |  |
| recibido | BIT |  |  |
| vcantidad | NUMERIC(18, 6) |  |  |
| impuesto | NUMERIC(18, 6) |  |  |
| parancel | NUMERIC(18, 6) |  |  |
| arancel | NUMERIC(18, 6) |  |  |
| varancel | NUMERIC(18, 6) |  |  |
| crecinto | NUMERIC(18, 6) |  |  |
| m3 | NUMERIC(18, 6) |  |  |
| vcip | NUMERIC(18, 6) |  |  |

#### Índices
- IX_docompra_bodega: ['bodega'] 
- IX_docompra_compra: ['compra'] 
- IX_docompra_docompra: ['docompra'] 
- IX_docompra_empresa: ['empresa'] 
- IX_docompra_lote: ['lote'] 
- IX_docompra_ocompra: ['ocompra'] 
- IX_docompra_presenta: ['presenta'] 
- IX_docompra_producto: ['producto'] 
- IX_docompra_usuario: ['usuario'] 

### Tabla: docompra1
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER |  |  |
| docompra | INTEGER |  |  |
| ocompra | INTEGER |  |  |
| recibido | NUMERIC(18, 6) |  |  |
| pendiente | NUMERIC(18, 6) |  |  |
| nuevoingreso | NUMERIC(18, 6) |  |  |
| lote | INTEGER |  |  |
| bodega | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| docompra1 | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| dcompra | INTEGER |  |  |
| recibidorecinto | NUMERIC(18, 6) |  |  |
| pendienterecinto | NUMERIC(18, 6) |  |  |
| nuevoingresorecinto | NUMERIC(18, 6) |  |  |
| compra | INTEGER |  |  |
| kardex | INTEGER |  |  |

### Tabla: document
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| document | INTEGER |  | ✓ |
| ndocument | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| departamento | INTEGER |  |  |
| adjunto | IMAGE | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_document_departamento: ['departamento'] 
- IX_document_document: ['document'] 
- IX_document_empresa: ['empresa'] 
- IX_document_ndocument: ['ndocument'] 
- IX_document_usuario: ['usuario'] 

### Tabla: dofactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| gratificado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hgratificado | NUMERIC(16, 6) |  |  |
| hbonificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolista | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| texto | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| ofactura | INTEGER |  |  |
| kardex | INTEGER |  |  |
| costo | NUMERIC(16, 6) |  |  |
| dofactura | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| ncmonto | NUMERIC(16, 6) |  |  |
| ncafecta | NUMERIC(16, 6) |  |  |
| ncexenta | NUMERIC(16, 6) |  |  |
| ncviva | NUMERIC(16, 6) |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| nombre | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nula | BIT |  |  |
| talonario | INTEGER | ✓ |  |
| mes | DATETIME | ✓ |  |
| apliquemora | BIT |  |  |
| unidadVenta | INTEGER |  |  |
| PrecioUVenta | NUMERIC(16, 6) |  |  |
| CantidadUVenta | NUMERIC(16, 6) |  |  |
| ReservadoUVenta | NUMERIC(16, 6) |  |  |
| BonificadoUVenta | NUMERIC(16, 6) |  |  |
| GratificadoUVenta | NUMERIC(16, 6) |  |  |
| Cotrans | NUMERIC(16, 8) |  |  |
| vendedor | INTEGER |  |  |
| prioridad | INTEGER |  |  |
| estado | INTEGER |  |  |
| factalm | INTEGER |  |  |
| dregciclo | INTEGER |  |  |
| dgratif | NUMERIC(18, 6) |  |  |
| gratif | NUMERIC(18, 6) |  |  |
| vineta | BIT |  |  |
| bomba | INTEGER |  |  |
| concaja | BIT |  |  |
| bonifreservado | BIT |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| pcomision | NUMERIC(5, 2) |  |  |
| uvendidas | NUMERIC(16, 8) |  |  |
| vinculado | BIT |  |  |
| fraccion | NUMERIC(18, 6) |  |  |
| nbonif | INTEGER |  |  |
| resolucion1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| resolfecha | DATETIME | ✓ |  |
| linea | INTEGER |  |  |
| oPrecio | NUMERIC(18, 6) |  |  |
| tipoescala | INTEGER |  |  |
| UConfirmada | NUMERIC(18, 6) |  |  |
| Ufacturada | NUMERIC(18, 6) |  |  |
| cambodega | INTEGER |  |  |
| condicion1 | BIT |  |  |
| ocompra | INTEGER |  |  |
| producto | INTEGER |  |  |
| confirmado | BIT |  |  |

#### Foreign Keys
- ['ofactura'] → ofactura.['ofactura']
- ['producto'] → producto.['producto']

### Tabla: donacion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dte | INTEGER | ✓ |  |
| monto | FLOAT | ✓ |  |
| referencia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| almacen | INTEGER | ✓ |  |
| donacion | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: doventa
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolist | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| tax | NUMERIC(16, 6) |  |  |
| cprecio | NUMERIC(16, 6) |  |  |
| vtax | NUMERIC(16, 6) |  |  |
| gasto | NUMERIC(16, 6) |  |  |
| producto | INTEGER |  |  |
| lote | INTEGER |  |  |
| bodega | INTEGER |  |  |
| oventa | INTEGER |  |  |
| venta | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| rcantidad | NUMERIC(16, 6) |  |  |
| rreservado | NUMERIC(16, 6) |  |  |
| rbonificado | NUMERIC(16, 6) |  |  |
| rprecio | NUMERIC(16, 6) |  |  |
| rmontfact | NUMERIC(16, 6) |  |  |
| rpdesc | NUMERIC(16, 6) |  |  |
| rvdesc | NUMERIC(16, 6) |  |  |
| ccantidad | NUMERIC(16, 6) |  |  |
| presenta | INTEGER |  |  |
| doventa | INTEGER |  |  |
| unidades | NUMERIC(16, 6) |  |  |
| cbonificado | NUMERIC(18, 6) |  |  |
| linea | INTEGER | ✓ |  |
| fechaDespacho | DATETIME | ✓ |  |
| fechaRecepcion | DATETIME | ✓ |  |
| disponible | NUMERIC(18, 6) |  |  |
| kardex | INTEGER |  |  |
| bodega1 | INTEGER | ✓ |  |
| oprecio | NUMERIC(12, 2) |  |  |
| pcomision | NUMERIC(6, 2) |  |  |
| derecinto | NUMERIC(12, 2) |  |  |
| detransito | NUMERIC(12, 2) |  |  |
| comprar | NUMERIC(12, 2) |  |  |
| autorizado | NUMERIC(12, 2) |  |  |
| nombre | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nosujeto | NUMERIC(12, 2) |  |  |
| gratif | NUMERIC(12, 2) |  |  |

#### Índices
- doventa_oventa_empresa: ['oventa', 'empresa'] 
- IX_doventa_doventa: ['doventa'] 

### Tabla: doventafact
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfactura | INTEGER | ✓ |  |
| doventa | INTEGER | ✓ |  |
| cantidad | NUMERIC(18, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| doventafact | INTEGER |  | ✓ |
| dcambodega | INTEGER | ✓ |  |

### Tabla: dpEntrega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dpEntrega | INTEGER |  |  |
| Entrega | INTEGER |  |  |
| monto | NUMERIC(18, 6) |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_dpEntrega: ['dpEntrega'] 

### Tabla: dpagooing
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dpagooing | NUMERIC(18, 0) |  | ✓ |
| dplanilla | INTEGER | ✓ |  |
| ingreso | INTEGER | ✓ |  |
| poldesc | INTEGER | ✓ |  |
| esingreso | BIT | ✓ |  |
| monto | NUMERIC(18, 9) | ✓ |  |

#### Índices
- IX_dpagooing_dplanilla: ['dplanilla'] 
- IX_dpagooing_dplanilla1: ['dplanilla', 'ingreso', 'poldesc'] (UNIQUE)
- IX_dpagooing_ingreso: ['ingreso'] 
- IX_dpagooing_poldesc: ['poldesc'] 

### Tabla: dpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cargo | NUMERIC(15, 6) |  |  |
| abono | NUMERIC(15, 6) |  |  |
| pagos | INTEGER |  |  |
| invcliente | INTEGER |  |  |
| dpagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| hcargo | NUMERIC(15, 6) |  |  |
| habono | NUMERIC(15, 6) |  |  |
| vendedor | INTEGER |  |  |
| condpago | INTEGER |  |  |
| recibo | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| exenta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| nocheque | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechacheque | DATETIME | ✓ |  |
| rechazado | BIT |  |  |
| nula | BIT |  |  |
| chcobrado | BIT |  |  |
| FechaCobrado | DATETIME | ✓ |  |
| enfirme | BIT |  |  |
| pagada | BIT |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| chrechazado | BIT |  |  |
| chpagado | BIT |  |  |
| noRemesa | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bancoRemesa | INTEGER |  |  |
| fechadeposito | DATETIME | ✓ |  |
| qlinea | INTEGER |  |  |
| montopost | NUMERIC(18, 6) |  |  |
| nocuenta | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Foreign Keys
- ['invcliente'] → invcliente.['invcliente']
- ['pagos'] → pagos.['pagos']

#### Índices
- CXC_DPAGOS_INVCLIENTE: ['invcliente'] 
- IX_dpagos_dpagos: ['dpagos'] 
- IX_dpagos_empresa: ['empresa'] 
- IX_dpagos_invcliente: ['invcliente'] 
- IX_dpagos_pagos: ['pagos'] 
- IX_dpagos_usuario: ['usuario'] 

### Tabla: dpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| orden | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| banco | BIT |  |  |
| cheque | BIT |  |  |
| cheqnulo | BIT |  |  |
| aquien | BIT |  |  |
| cheqimp | BIT |  |  |
| concepto | VARCHAR(800) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| debe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| hdebe | NUMERIC(16, 6) |  |  |
| hhaber | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| hphaber | NUMERIC(16, 6) |  |  |
| hpdebe | NUMERIC(16, 6) |  |  |
| partida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| dpartida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| hconcepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| linea | INTEGER |  |  |
| conciliado | BIT |  |  |
| comparativo | NUMERIC(18, 6) |  |  |
| automov | BIT |  |  |
| fconc | DATETIME | ✓ |  |

#### Foreign Keys
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['cuenta'] → cuenta.['cuenta']
- ['partida'] → partida.['partida']

#### Índices
- dpartida_empresa: ['empresa'] 
- IX_dpartida_concepto: ['concepto'] 
- IX_dpartida_ctrocosto: ['ctrocosto'] 
- IX_dpartida_cuenta: ['cuenta'] 
- IX_dpartida_empresa: ['empresa'] 
- IX_dpartida_hconcepto: ['hconcepto'] 
- IX_dpartida_moneda: ['moneda'] 
- IX_dpartida_orden: ['orden'] 
- IX_dpartida_partida: ['partida'] 
- IX_dpartida_usuario: ['usuario'] 

### Tabla: dpedidoalmacen
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| pedidoalmacen | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| cantidadsurtida | NUMERIC(16, 6) |  |  |
| hcantidadsurtida | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| dpedidoalmacen | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| PRECIO | NUMERIC(18, 6) |  |  |
| nula | BIT |  |  |
| nosuplir | BIT |  |  |
| entregado | BIT |  |  |

#### Foreign Keys
- ['pedidoalmacen'] → pedidoalmacen.['pedidoalmacen']
- ['producto'] → producto.['producto']

### Tabla: dperiodo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cerrado | BIT |  |  |
| activo | BIT |  |  |
| periodo | INTEGER |  |  |
| dperiodo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fecha | DATETIME |  |  |
| ano | INTEGER |  |  |
| mes | INTEGER |  |  |

#### Foreign Keys
- ['periodo'] → periodo.['periodo']

#### Índices
- IX_dperiodo_ano: ['ano'] 
- IX_dperiodo_dperiodo: ['dperiodo'] 
- IX_dperiodo_empresa: ['empresa'] 
- IX_dperiodo_fecha: ['fecha'] 
- IX_dperiodo_mes: ['mes'] 
- IX_dperiodo_periodo: ['periodo'] 
- IX_dperiodo_usuario: ['usuario'] 

### Tabla: dpfactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| gratificado | NUMERIC(16, 6) |  |  |
| bonificado | NUMERIC(16, 6) |  |  |
| hcantidad | NUMERIC(16, 6) |  |  |
| hreservado | NUMERIC(16, 6) |  |  |
| hgratificado | NUMERIC(16, 6) |  |  |
| hbonificado | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| preciolist | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| texto | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| vgdesc | NUMERIC(16, 6) |  |  |
| factura | INTEGER |  |  |
| kardex | INTEGER |  |  |
| costo | NUMERIC(16, 6) |  |  |
| dpfactura | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| pfactura | INTEGER |  |  |
| cantidadfact | NUMERIC(16, 6) |  |  |
| enfirme | BIT |  |  |
| nombre | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nula | BIT |  |  |
| oPrecio | NUMERIC(18, 6) |  |  |
| motorista | INTEGER |  |  |
| camion | INTEGER |  |  |
| estatus | INTEGER |  |  |
| fechaentrega | DATETIME | ✓ |  |
| fechainicio | DATETIME | ✓ |  |
| fechatermino | DATETIME | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bl | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| FUERAPUERTO | BIT |  |  |
| FACTURADO | BIT |  |  |
| FACTURAR | BIT |  |  |
| efechatermino | DATETIME | ✓ |  |
| pfechainicio | DATETIME | ✓ |  |
| pfechatermino | DATETIME | ✓ |  |
| ifechainicio | DATETIME | ✓ |  |
| TIRExport | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TIRImport | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| OrdenPago | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| FechaQuedan | DATETIME | ✓ |  |
| PrecioAgregado | NUMERIC(18, 6) |  |  |
| cuenta | INTEGER |  |  |
| pagado | BIT |  |  |
| pagar | BIT |  |  |
| costopago | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| d1 | INTEGER | ✓ |  |
| d2 | INTEGER | ✓ |  |
| d3 | INTEGER | ✓ |  |
| d4 | INTEGER | ✓ |  |
| d5 | INTEGER | ✓ |  |
| d6 | INTEGER | ✓ |  |
| d7 | INTEGER | ✓ |  |
| d8 | INTEGER | ✓ |  |
| d9 | INTEGER | ✓ |  |
| d10 | INTEGER | ✓ |  |
| d11 | INTEGER | ✓ |  |
| d12 | INTEGER | ✓ |  |
| d13 | INTEGER | ✓ |  |
| d14 | INTEGER | ✓ |  |
| d15 | INTEGER | ✓ |  |
| d16 | INTEGER | ✓ |  |
| d17 | INTEGER | ✓ |  |
| d18 | INTEGER | ✓ |  |
| d19 | INTEGER | ✓ |  |
| d20 | INTEGER | ✓ |  |
| d21 | INTEGER | ✓ |  |
| d22 | INTEGER | ✓ |  |
| d23 | INTEGER | ✓ |  |
| d24 | INTEGER | ✓ |  |
| d25 | INTEGER | ✓ |  |
| d26 | INTEGER | ✓ |  |
| d27 | INTEGER | ✓ |  |
| d28 | INTEGER | ✓ |  |
| d29 | INTEGER | ✓ |  |
| d30 | INTEGER | ✓ |  |
| d31 | INTEGER | ✓ |  |
| mes | INTEGER |  |  |
| ano | INTEGER |  |  |
| nproducto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pauta | INTEGER |  |  |
| PRECIOPROV | NUMERIC(18, 6) |  |  |
| FECHAPROV | DATETIME | ✓ |  |
| OTROSCPROV | NUMERIC(18, 6) |  |  |
| intervalopauta | INTEGER |  |  |
| midpfactura | INTEGER |  |  |
| vinculado | BIT |  |  |
| ocCantidad | NUMERIC(18, 6) |  |  |
| CantidadFalta | NUMERIC(18, 6) |  |  |
| viajeterminado | BIT |  |  |
| NoDocumentoViaje | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechaliquida | DATETIME | ✓ |  |
| gasto | NUMERIC(12, 2) | ✓ |  |
| notagasto | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prodprec | INTEGER | ✓ |  |
| usuariogasto | INTEGER | ✓ |  |

#### Foreign Keys
- ['kardex'] → kardex.['kardex']
- ['pfactura'] → pfactura.['pfactura']

#### Índices
- IX_dpfactura_dpfactura: ['dpfactura'] 
- IX_dpfactura_empresa: ['empresa'] 
- IX_dpfactura_factura: ['factura'] 
- IX_dpfactura_kardex: ['kardex'] 
- IX_dpfactura_nombre: ['nombre'] 
- IX_dpfactura_pfactura: ['pfactura'] 
- IX_dpfactura_texto: ['texto'] 
- IX_dpfactura_usuario: ['usuario'] 

### Tabla: dplanilla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| empleado | INTEGER | ✓ |  |
| tipoprest | INTEGER | ✓ |  |
| poldesc | INTEGER | ✓ |  |
| afp | INTEGER | ✓ |  |
| afpcomision | NUMERIC(18, 9) | ✓ |  |
| afppension | NUMERIC(18, 9) | ✓ |  |
| totdedvp | NUMERIC(18, 9) | ✓ |  |
| totdedv | NUMERIC(18, 9) | ✓ |  |
| ingreso | INTEGER | ✓ |  |
| totded | NUMERIC(18, 9) | ✓ |  |
| totdev | NUMERIC(18, 9) | ✓ |  |
| totdedp | NUMERIC(18, 9) | ✓ |  |
| activo | BIT | ✓ |  |
| prestemp | INTEGER | ✓ |  |
| planilla | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| totdevseg | NUMERIC(18, 6) | ✓ |  |
| totdedseg | NUMERIC(18, 6) | ✓ |  |
| dplanilla | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| HEDiurnas | NUMERIC(18, 9) | ✓ |  |
| HENocturna | NUMERIC(18, 9) | ✓ |  |
| hedprecio | NUMERIC(18, 9) | ✓ |  |
| henprecio | NUMERIC(18, 9) | ✓ |  |
| viaticos | NUMERIC(18, 9) | ✓ |  |
| tisss | NUMERIC(18, 9) | ✓ |  |
| tafp | NUMERIC(18, 9) | ✓ |  |
| trenta | NUMERIC(18, 9) | ✓ |  |
| totros | NUMERIC(18, 9) | ✓ |  |
| montoapagar | NUMERIC(18, 9) | ✓ |  |
| dias | INTEGER | ✓ |  |
| comision | NUMERIC(18, 6) | ✓ |  |
| suelmen | NUMERIC(18, 6) | ✓ |  |
| otrosing | NUMERIC(18, 6) | ✓ |  |
| prestamos | NUMERIC(18, 6) | ✓ |  |
| despensa | NUMERIC(18, 9) | ✓ |  |
| sueldiario | NUMERIC(18, 8) | ✓ |  |
| FAGUIPAGADO | DATETIME | ✓ |  |
| AGUINALDO | NUMERIC(18, 9) | ✓ |  |
| vacacion | NUMERIC(18, 6) | ✓ |  |
| AGUIPAGADO | NUMERIC(18, 9) | ✓ |  |
| pisss | NUMERIC(18, 9) | ✓ |  |
| pafp | NUMERIC(18, 9) | ✓ |  |
| indemnizacion | NUMERIC(16, 6) |  |  |
| INCAPACIDAD | INTEGER |  |  |
| VINCAPACIDAD | NUMERIC(16, 6) |  |  |
| TRABAJADOS | BIT |  |  |
| originaldias | INTEGER |  |  |
| Alimentacion | NUMERIC(18, 9) | ✓ |  |
| gratificacion | NUMERIC(18, 9) | ✓ |  |
| HEF | NUMERIC(18, 9) | ✓ |  |
| Segurov | NUMERIC(18, 9) | ✓ |  |
| Transporte | NUMERIC(18, 9) | ✓ |  |
| hevprecio | NUMERIC(18, 9) | ✓ |  |
| hev | NUMERIC(18, 9) | ✓ |  |
| hedomprecio | NUMERIC(18, 9) | ✓ |  |
| hedom | NUMERIC(18, 9) | ✓ |  |
| valHE | NUMERIC(18, 6) |  |  |
| seccion | INTEGER |  |  |
| DTOTROS | NUMERIC(18, 6) |  |  |
| totalaguinaldo | NUMERIC(18, 6) |  |  |
| totalvacaciones | NUMERIC(18, 6) |  |  |
| totalindemnizacion | NUMERIC(18, 6) |  |  |
| cooperativa | NUMERIC(18, 6) |  |  |
| horasjornada | INTEGER |  |  |
| COBISSS | INTEGER |  |  |
| anios | INTEGER | ✓ |  |
| rentajunio | NUMERIC(18, 6) |  |  |
| rentadiciembre | NUMERIC(18, 6) |  |  |

#### Foreign Keys
- ['planilla'] → planilla.['planilla']
- ['planilla'] → planilla.['planilla']
- ['seccion'] → seccion.['seccion']

#### Índices
- IX_dplanilla_afp: ['afp'] 
- IX_dplanilla_dias: ['dias'] 
- IX_dplanilla_dplanilla: ['dplanilla'] 
- IX_dplanilla_empleado: ['empleado'] 
- IX_dplanilla_empresa: ['empresa'] 
- IX_dplanilla_INCAPACIDAD: ['INCAPACIDAD'] 
- IX_dplanilla_ingreso: ['ingreso'] 
- IX_dplanilla_originaldias: ['originaldias'] 
- IX_dplanilla_planilla: ['planilla'] 
- IX_dplanilla_poldesc: ['poldesc'] 
- IX_dplanilla_prestemp: ['prestemp'] 
- IX_dplanilla_seccion: ['seccion'] 
- IX_dplanilla_tipoprest: ['tipoprest'] 
- IX_dplanilla_usuario: ['usuario'] 
- IX_planilla_empleado: ['planilla', 'empleado'] (UNIQUE)

### Tabla: dpoldesc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| sueldmen | BIT |  |  |
| totdev | BIT |  |  |
| deducafp | BIT |  |  |
| minimo | MONEY |  |  |
| maximo | MONEY |  |  |
| oper0 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper1 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic1 | NUMERIC(9, 4) |  |  |
| oper2 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic2 | NUMERIC(9, 4) |  |  |
| oper3 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic3 | NUMERIC(9, 4) |  |  |
| oper4 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic4 | NUMERIC(9, 4) |  |  |
| oper5 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic5 | NUMERIC(9, 4) |  |  |
| oper6 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper7 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper8 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper9 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper10 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper11 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper12 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper13 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| poldesc | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| minimoseg | MONEY |  |  |
| maximoseg | MONEY |  |  |
| condic1seg | NUMERIC(9, 4) |  |  |
| condic2seg | NUMERIC(9, 4) |  |  |
| condic3seg | NUMERIC(9, 4) |  |  |
| condic4seg | NUMERIC(9, 4) |  |  |
| condic5seg | NUMERIC(9, 4) |  |  |
| dpoldesc | INTEGER |  | ✓ |
| dias | INTEGER | ✓ |  |

#### Índices
- IX_dpoldesc_dpoldesc: ['dpoldesc'] 
- IX_dpoldesc_poldesc: ['poldesc'] 
- IX_dpoldesc_usuario: ['usuario'] 

### Tabla: dpolingpla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| sueldodiario | BIT |  |  |
| diaslaborados | BIT |  |  |
| diasanuales | INTEGER |  |  |
| diascalculo | INTEGER |  |  |
| minimo | MONEY |  |  |
| maximo | MONEY |  |  |
| oper0 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper1 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic1 | NUMERIC(9, 4) |  |  |
| oper2 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic2 | NUMERIC(9, 4) |  |  |
| oper3 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic3 | NUMERIC(9, 4) |  |  |
| oper4 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic4 | NUMERIC(9, 4) |  |  |
| oper5 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic5 | NUMERIC(9, 4) |  |  |
| oper6 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper7 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper8 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper9 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper10 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper11 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper12 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper13 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| polingpla | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| minimoseg | MONEY |  |  |
| maximoseg | MONEY |  |  |
| condic1seg | NUMERIC(9, 4) |  |  |
| condic2seg | NUMERIC(9, 4) |  |  |
| condic3seg | NUMERIC(9, 4) |  |  |
| condic4seg | NUMERIC(9, 4) |  |  |
| condic5seg | NUMERIC(9, 4) |  |  |
| dpolingpla | INTEGER |  | ✓ |

#### Índices
- IX_dpolingpla_diasanuales: ['diasanuales'] 
- IX_dpolingpla_diascalculo: ['diascalculo'] 
- IX_dpolingpla_dpolingpla: ['dpolingpla'] 
- IX_dpolingpla_polingpla: ['polingpla'] 
- IX_dpolingpla_usuario: ['usuario'] 

### Tabla: dpolpladeduc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Minimo | INTEGER |  |  |
| Maximo | INTEGER |  |  |
| oper0 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper1 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper2 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| SueldoDiario | BIT |  |  |
| oper3 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic0 | NUMERIC(9, 4) |  |  |
| oper4 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper5 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper6 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic1 | NUMERIC(9, 4) |  |  |
| oper7 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic2 | NUMERIC(9, 4) |  |  |
| oper8 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper9 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper10 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper11 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic3 | NUMERIC(9, 4) |  |  |
| oper12 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condic4 | NUMERIC(9, 4) |  |  |
| oper13 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper14 | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| polpladeduc | INTEGER |  |  |
| dpolpladeduc | INTEGER |  | ✓ |
| diastrabajo | BIT |  |  |
| dias | NUMERIC(5, 1) |  |  |
| ndias | BIT |  |  |

### Tabla: dppagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cargo | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| ppagos | INTEGER |  |  |
| compra | INTEGER |  |  |
| dppagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| hcargo | NUMERIC(16, 6) |  |  |
| habono | NUMERIC(16, 6) |  |  |
| partida | INTEGER | ✓ |  |
| retencion | INTEGER | ✓ |  |

#### Índices
- IX_dppagos_compra: ['compra'] 
- IX_dppagos_dppagos: ['dppagos'] 
- IX_dppagos_empresa: ['empresa'] 
- IX_dppagos_ppagos: ['ppagos'] 
- IX_dppagos_usuario: ['usuario'] 

### Tabla: dppartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dppartida | INTEGER |  | ✓ |
| orden | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| banco | BIT |  |  |
| cheque | BIT |  |  |
| cheqnulo | BIT |  |  |
| aquien | BIT |  |  |
| cheqimp | BIT |  |  |
| concepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| debe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| hdebe | NUMERIC(16, 6) |  |  |
| hhaber | NUMERIC(16, 6) |  |  |
| hpdebe | NUMERIC(16, 6) |  |  |
| hphaber | NUMERIC(16, 6) |  |  |
| hconcepto | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ppartida | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| moneda | INTEGER |  |  |

#### Foreign Keys
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['cuenta'] → cuenta.['cuenta']
- ['ppartida'] → ppartida.['ppartida']

#### Índices
- IX_dppartida_concepto: ['concepto'] 
- IX_dppartida_ctrocosto: ['ctrocosto'] 
- IX_dppartida_cuenta: ['cuenta'] 
- IX_dppartida_dppartida: ['dppartida'] 
- IX_dppartida_empresa: ['empresa'] 
- IX_dppartida_hconcepto: ['hconcepto'] 
- IX_dppartida_moneda: ['moneda'] 
- IX_dppartida_orden: ['orden'] 
- IX_dppartida_ppartida: ['ppartida'] 
- IX_dppartida_usuario: ['usuario'] 

### Tabla: dprePed
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER | ✓ |  |
| lote | INTEGER | ✓ |  |
| prePed | INTEGER | ✓ |  |
| cantidad | NUMERIC(18, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dprePed | INTEGER |  | ✓ |

### Tabla: dpreciovineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER |  |  |
| codigo | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| precio1 | NUMERIC(18, 6) |  |  |
| precio2 | NUMERIC(18, 6) |  |  |
| precio3 | NUMERIC(18, 6) |  |  |
| preciovineta | INTEGER |  |  |
| dpreciovineta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| precio4 | NUMERIC(18, 6) |  |  |
| precio5 | NUMERIC(18, 6) |  |  |

### Tabla: dpreparar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfactura | INTEGER | ✓ |  |
| fecha | DATETIME |  |  |
| dpreparar | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| dcambodega | INTEGER |  |  |

### Tabla: dprestamo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| planilla | INTEGER | ✓ |  |
| cuotanum | NUMERIC(5, 0) |  |  |
| fpagocuota | DATETIME |  |  |
| montocuota | NUMERIC(18, 6) |  |  |
| activo | BIT |  |  |
| prestemp | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| dprestamo | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| pagado | BIT | ✓ |  |
| noincluir | BIT |  |  |

#### Índices
- IX_dprestamo_dprestamo: ['dprestamo'] 
- IX_dprestamo_empresa: ['empresa'] 
- IX_dprestamo_planilla: ['planilla'] 
- IX_dprestamo_prestemp: ['prestemp'] 
- IX_dprestamo_usuario: ['usuario'] 

### Tabla: dprodDevolucion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dprodDevolucion | INTEGER |  | ✓ |
| dProdEntregado | INTEGER |  |  |
| Serie | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechagarantia | DATETIME | ✓ |  |
| garantia | NUMERIC(6, 2) | ✓ |  |
| Vencida | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |

#### Índices
- IX_dprodDevolucion_dprodDevolucion: ['dprodDevolucion'] 
- IX_dprodDevolucion_dProdEntregado: ['dProdEntregado'] 
- IX_dprodDevolucion_Serie: ['Serie'] 
- IX_dprodDevolucion_usuario: ['usuario'] 

### Tabla: dprodentregado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dprodentregado | INTEGER |  | ✓ |
| ProdEntregado | INTEGER |  |  |
| Producto | INTEGER |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| Serie | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechagarantia | DATETIME | ✓ |  |
| garantia | NUMERIC(6, 2) | ✓ |  |
| Devolucion | BIT |  |  |
| Vencida | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| registrogarantia | INTEGER |  |  |

#### Índices
- IX_dprodentregado_dprodentregado: ['dprodentregado'] 
- IX_dprodentregado_ProdEntregado: ['ProdEntregado'] 
- IX_dprodentregado_Producto: ['Producto'] 
- IX_dprodentregado_registrogarantia: ['registrogarantia'] 
- IX_dprodentregado_Serie: ['Serie'] 
- IX_dprodentregado_usuario: ['usuario'] 

### Tabla: dprodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| pfecha | DATETIME | ✓ |  |
| pminimo | NUMERIC(16, 6) |  |  |
| precioa | NUMERIC(16, 6) |  |  |
| preciob | NUMERIC(16, 6) |  |  |
| precioc | NUMERIC(16, 6) |  |  |
| cantidada | INTEGER |  |  |
| cantidadb | INTEGER |  |  |
| cantidadc | INTEGER |  |  |
| mprecio | NUMERIC(16, 6) |  |  |
| precio | NUMERIC(16, 6) |  |  |
| fprecio | NUMERIC(16, 6) |  |  |
| cfecha | DATETIME | ✓ |  |
| factor | NUMERIC(16, 6) |  |  |
| producto | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| dprodprec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tprecio | NUMERIC(16, 6) |  |  |
| TIPCLI | INTEGER |  |  |
| Margen | NUMERIC(18, 6) | ✓ |  |
| MargenMinimo | NUMERIC(18, 6) | ✓ |  |
| vineta | NUMERIC(18, 6) |  |  |
| pprecio | NUMERIC(18, 6) |  |  |
| fPrecioPromo | NUMERIC(18, 6) |  |  |
| tPrecioPromo | NUMERIC(18, 6) |  |  |
| pfechaini | DATETIME | ✓ |  |
| pfechafin | DATETIME | ✓ |  |
| precio1 | NUMERIC(18, 6) |  |  |
| precio2 | NUMERIC(18, 6) |  |  |
| precio3 | NUMERIC(18, 6) |  |  |
| precio4 | NUMERIC(18, 6) |  |  |
| precio5 | NUMERIC(18, 6) |  |  |
| precio6 | NUMERIC(18, 6) |  |  |
| precio7 | NUMERIC(18, 6) |  |  |
| precio8 | NUMERIC(18, 6) |  |  |
| precioagregado | NUMERIC(18, 6) |  |  |
| parte | BIT |  |  |
| cargofull | NUMERIC(18, 6) |  |  |
| qlinea | INTEGER |  |  |
| preciomax | NUMERIC(18, 6) |  |  |

#### Foreign Keys
- ['producto'] → producto.['producto']

#### Índices
- IX_dprodprec_cantidada: ['cantidada'] 
- IX_dprodprec_cantidadb: ['cantidadb'] 
- IX_dprodprec_cantidadc: ['cantidadc'] 
- IX_dprodprec_dprodprec: ['dprodprec'] 
- IX_dprodprec_empresa: ['empresa'] 
- IX_dprodprec_prodprec: ['prodprec'] 
- IX_dprodprec_producto: ['producto'] 
- IX_dprodprec_TIPCLI: ['TIPCLI'] 
- IX_dprodprec_usuario: ['usuario'] 
- producto_prodprec: ['prodprec', 'producto'] (UNIQUE)

### Tabla: dproducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dalmacen | INTEGER | ✓ |  |
| cantrequerida | NUMERIC(12, 6) | ✓ |  |
| cantpendiente | NUMERIC(12, 6) | ✓ |  |
| cantsolicita | NUMERIC(12, 6) | ✓ |  |
| devolucion | NUMERIC(12, 6) | ✓ |  |
| averia | NUMERIC(12, 6) | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| dproducto | INTEGER |  | ✓ |

### Tabla: drecvineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dfactura | INTEGER |  |  |
| recvineta | INTEGER |  |  |
| vvineta | NUMERIC(18, 6) |  |  |
| precioa | NUMERIC(18, 6) |  |  |
| preciob | NUMERIC(18, 6) |  |  |
| drecvineta | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| pagada | BIT |  |  |
| factura | INTEGER |  |  |
| vinetanum | INTEGER |  |  |
| icdbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: dregciclo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| regciclo | INTEGER |  |  |
| dregciclo | INTEGER |  | ✓ |
| cBarra | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| precio1 | NUMERIC(16, 6) |  |  |
| precio2 | NUMERIC(16, 6) |  |  |
| precio3 | NUMERIC(16, 6) |  |  |
| precio4 | NUMERIC(16, 6) |  |  |
| factura | INTEGER |  |  |
| impresa | BIT |  |  |
| pagos | INTEGER |  |  |
| automatico | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| mes | DATETIME | ✓ |  |
| GENERADO | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| empresa | INTEGER |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['regciclo'] → regciclo.['regciclo']

#### Índices
- IX_dregciclo_cBarra: ['cBarra'] 
- IX_dregciclo_clientes: ['clientes'] 
- IX_dregciclo_dregciclo: ['dregciclo'] 
- IX_dregciclo_factura: ['factura'] 
- IX_dregciclo_pagos: ['pagos'] 
- IX_dregciclo_regciclo: ['regciclo'] 

### Tabla: dregfactnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dregfactnula | INTEGER |  | ✓ |
| dregciclo | INTEGER |  |  |
| empresa | INTEGER |  |  |
| factura | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_dregfactnula_dregciclo: ['dregciclo'] 
- IX_dregfactnula_dregfactnula: ['dregfactnula'] 
- IX_dregfactnula_empresa: ['empresa'] 
- IX_dregfactnula_factura: ['factura'] 
- IX_dregfactnula_usuario: ['usuario'] 

### Tabla: dregllave
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dregllave | INTEGER |  | ✓ |
| pais | INTEGER |  |  |
| Producto | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dclientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| moneda | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| equipo | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(65) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| reinstall | INTEGER |  |  |
| sucursal | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| email | VARCHAR(65) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| noProducto | VARCHAR(65) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Llave | VARCHAR(65) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| IFORMATO | INTEGER |  |  |

### Tabla: dregpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cargo | NUMERIC(15, 6) | ✓ |  |
| abono | NUMERIC(15, 6) | ✓ |  |
| regpagos | INTEGER | ✓ |  |
| invcliente | INTEGER | ✓ |  |
| dregpagos | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| hcargo | NUMERIC(15, 6) | ✓ |  |
| habono | NUMERIC(15, 6) | ✓ |  |
| pagos | INTEGER |  |  |

#### Índices
- IX_dregpagos_dregpagos: ['dregpagos'] 
- IX_dregpagos_empresa: ['empresa'] 
- IX_dregpagos_invcliente: ['invcliente'] 
- IX_dregpagos_pagos: ['pagos'] 
- IX_dregpagos_regpagos: ['regpagos'] 
- IX_dregpagos_usuario: ['usuario'] 

### Tabla: dreporte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| filas | NUMERIC(16, 6) |  |  |
| impnumc | BIT |  |  |
| nombre | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| saldant | NUMERIC(16, 6) |  |  |
| saldmen | NUMERIC(16, 6) |  |  |
| saldacu | NUMERIC(16, 6) |  |  |
| anterior | BIT |  |  |
| mensual | BIT |  |  |
| acum | BIT |  |  |
| fila1 | NUMERIC(16, 6) |  |  |
| oper1 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fila2 | NUMERIC(16, 6) |  |  |
| oper2 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fila3 | NUMERIC(16, 6) |  |  |
| oper3 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fila4 | NUMERIC(16, 6) |  |  |
| oper4 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| expresion1 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| oper5 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| expresion2 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nivel | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| columna | NUMERIC(16, 6) |  |  |
| inventa | BIT |  |  |
| activo | BIT |  |  |
| raya | BIT |  |  |
| reporte | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| dreporte | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| oreporte | INTEGER |  |  |
| mimoneda | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipo | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fila5 | INTEGER |  |  |
| raya1 | BIT |  |  |
| raya2 | BIT |  |  |
| raya3 | BIT |  |  |
| factor | NUMERIC(6, 2) |  |  |

#### Foreign Keys
- ['ctrocosto'] → ctrocosto.['ctrocosto']
- ['cuenta'] → cuenta.['cuenta']
- ['reporte'] → reporte.['reporte']

#### Índices
- IX_dreporte_ctrocosto: ['ctrocosto'] 
- IX_dreporte_cuenta: ['cuenta'] 
- IX_dreporte_dreporte: ['dreporte'] 
- IX_dreporte_empresa: ['empresa'] 
- IX_dreporte_expresion1: ['expresion1'] 
- IX_dreporte_expresion2: ['expresion2'] 
- IX_dreporte_nivel: ['nivel'] 
- IX_dreporte_nombre: ['nombre'] 
- IX_dreporte_oper1: ['oper1'] 
- IX_dreporte_oper2: ['oper2'] 
- IX_dreporte_oper3: ['oper3'] 
- IX_dreporte_oper4: ['oper4'] 
- IX_dreporte_oper5: ['oper5'] 
- IX_dreporte_oreporte: ['oreporte'] 
- IX_dreporte_reporte: ['reporte'] 
- IX_dreporte_usuario: ['usuario'] 

### Tabla: drliquida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| drliquida | INTEGER |  | ✓ |
| rliquida | INTEGER |  |  |
| precio | NUMERIC(16, 6) |  |  |
| kardex | INTEGER |  |  |
| almacen | INTEGER |  |  |
| pagos | INTEGER |  |  |
| devolucion | NUMERIC(16, 6) |  |  |
| venta | NUMERIC(16, 6) |  |  |
| vfaltante | NUMERIC(16, 6) |  |  |
| saldoliquida | NUMERIC(16, 6) |  |  |
| montliquida | NUMERIC(16, 6) |  |  |
| recarga | NUMERIC(16, 6) |  |  |
| usuario | INTEGER |  |  |
| activo | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| vefectivo | NUMERIC(16, 6) |  |  |
| tvventa | NUMERIC(16, 6) |  |  |
| inicial | NUMERIC(18, 6) |  |  |
| fisico | NUMERIC(18, 6) |  |  |

#### Índices
- IX_drliquida_activo: ['activo'] 
- IX_drliquida_almacen: ['almacen'] 
- IX_drliquida_drliquida: ['drliquida'] 
- IX_drliquida_empresa: ['empresa'] 
- IX_drliquida_kardex: ['kardex'] 
- IX_drliquida_pagos: ['pagos'] 
- IX_drliquida_rliquida: ['rliquida'] 
- IX_drliquida_usuario: ['usuario'] 

### Tabla: drutacobro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| invcliente | INTEGER |  |  |
| factura | INTEGER |  |  |
| rutacobro | INTEGER |  |  |
| saldo | NUMERIC(18, 6) |  |  |
| drutacobro | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| liquidada | BIT |  |  |
| vence | INTEGER |  |  |
| ANTIGUEDAD | INTEGER |  |  |
| cobrada | BIT |  |  |
| dpagos | INTEGER | ✓ |  |
| monto | NUMERIC(9, 2) | ✓ |  |
| quedan | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechaquedan | DATETIME | ✓ |  |
| noRemesa | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Recibo | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FechaDeposito | DATETIME | ✓ |  |
| CondPago | INTEGER | ✓ |  |
| noCheque | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FechaCheque | DATETIME | ✓ |  |
| cambodega | INTEGER | ✓ |  |
| vdesc | NUMERIC(9, 2) | ✓ |  |
| nocuenta | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: dte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ncatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| catalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| scatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dte | INTEGER |  | ✓ |
| tabla | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| zona | NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| depto | INTEGER | ✓ |  |
| municip | INTEGER | ✓ |  |

### Tabla: dtipobudget
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dtipobudget | INTEGER |  | ✓ |
| tipobudget | INTEGER |  |  |
| producto | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| depto | INTEGER |  |  |
| municip | INTEGER |  |  |
| budget | NUMERIC(18, 6) |  |  |
| mes | DATETIME | ✓ |  |
| horatiempo | DATETIME |  |  |
| Activo | BIT |  |  |
| Empresa | INTEGER |  |  |
| Usuario | INTEGER |  |  |

#### Índices
- IX_dtipobudget_clientes: ['clientes'] 
- IX_dtipobudget_depto: ['depto'] 
- IX_dtipobudget_dtipobudget: ['dtipobudget'] 
- IX_dtipobudget_Empresa: ['Empresa'] 
- IX_dtipobudget_municip: ['municip'] 
- IX_dtipobudget_producto: ['producto'] 
- IX_dtipobudget_tipobudget: ['tipobudget'] 
- IX_dtipobudget_Usuario: ['Usuario'] 
- IX_dtipobudget_vendedor: ['vendedor'] 

### Tabla: dtomafisica
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| kardex | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| cuarentena | NUMERIC(16, 6) |  |  |
| fcantidad | NUMERIC(16, 6) |  |  |
| freservado | NUMERIC(16, 6) |  |  |
| fcuarentena | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| fcosto | NUMERIC(16, 6) |  |  |
| ajustar | BIT |  |  |
| tomafisica | INTEGER |  |  |
| dtomafisica | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['kardex'] → kardex.['kardex']
- ['tomafisica'] → tomafisica.['tomafisica']

#### Índices
- IX_dtomafisica_dtomafisica: ['dtomafisica'] 
- IX_dtomafisica_empresa: ['empresa'] 
- IX_dtomafisica_kardex: ['kardex'] 
- IX_dtomafisica_tomafisica: ['tomafisica'] 
- IX_dtomafisica_usuario: ['usuario'] 

### Tabla: dtranspte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| fecha | DATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| transpte | INTEGER |  |  |
| factura | INTEGER |  |  |
| enfirme | BIT |  |  |
| impresa | BIT |  |  |
| tdespacho | INTEGER |  |  |
| dtranspte | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| entregada | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bultos | INTEGER |  |  |
| imprimir | BIT |  |  |

#### Índices
- IX_dtranspte_dtranspte: ['dtranspte'] 
- IX_dtranspte_empresa: ['empresa'] 
- IX_dtranspte_factura: ['factura'] 
- IX_dtranspte_fecha: ['fecha'] 
- IX_dtranspte_tdespacho: ['tdespacho'] 
- IX_dtranspte_transpte: ['transpte'] 
- IX_dtranspte_usuario: ['usuario'] 

### Tabla: empleado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| codisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nempleado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| aempleado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nombisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| foto | IMAGE | ✓ |  |
| sexo | INTEGER | ✓ |  |
| nacional | INTEGER | ✓ |  |
| pais | INTEGER | ✓ |  |
| depto | INTEGER | ✓ |  |
| municip | INTEGER | ✓ |  |
| fechnac | DATETIME | ✓ |  |
| lugarnac | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| estcivil | INTEGER | ✓ |  |
| profesion | INTEGER | ✓ |  |
| direccemp | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tiposan | INTEGER | ✓ |  |
| fechacont | DATETIME | ✓ |  |
| vencontra | DATETIME | ✓ |  |
| fecharet | DATETIME | ✓ |  |
| seccion | INTEGER | ✓ |  |
| cargo | INTEGER | ✓ |  |
| ntarjeta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| jornada | INTEGER | ✓ |  |
| sueldiario | NUMERIC(18, 6) | ✓ |  |
| suelmen | NUMERIC(18, 6) | ✓ |  |
| formpago | INTEGER | ✓ |  |
| nit | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cip | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| carelect | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| carmino | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| permintr | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| liccond | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pasaport | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numisss | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nup | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cuentab | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipocta | INTEGER | ✓ |  |
| banco | INTEGER | ✓ |  |
| afp | INTEGER | ✓ |  |
| procurad | BIT | ✓ |  |
| horasext | BIT | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| cuenta | INTEGER | ✓ |  |
| ctrocosto | INTEGER | ✓ |  |
| afpv | NUMERIC(18, 6) | ✓ |  |
| afpvp | NUMERIC(18, 6) | ✓ |  |
| empleado | INTEGER |  |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| empcubanco | INTEGER | ✓ |  |
| sueldiarioseg | NUMERIC(18, 6) | ✓ |  |
| suelmenseg | NUMERIC(18, 6) | ✓ |  |
| afpvseg | NUMERIC(18, 6) | ✓ |  |
| afpvpseg | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| tipoplaza | INTEGER | ✓ |  |
| jubilado | BIT | ✓ |  |
| codreloj | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| contrato | BIT |  |  |
| gerente | BIT |  |  |
| jefe | BIT |  |  |
| supervisor | BIT |  |  |
| autoriza | BIT |  |  |
| miImagen | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ingesp | INTEGER |  |  |
| asegurad | INTEGER |  |  |
| tiposeg | INTEGER |  |  |
| camion | INTEGER |  |  |
| rutacamion | INTEGER | ✓ |  |
| sectorlaboral | INTEGER |  |  |
| tiempo | INTEGER | ✓ |  |
| licNRemu | BIT | ✓ |  |
| IBC | BIT | ✓ |  |
| pensionvejezanti | BIT | ✓ |  |
| pensionadosinobli | BIT | ✓ |  |
| penriesgospro | BIT | ✓ |  |
| docentepub | BIT | ✓ |  |
| cotivoluntariaafi | NUMERIC(16, 8) | ✓ |  |
| cotivoluntariaemp | INTEGER | ✓ |  |
| codigobpen | INTEGER | ✓ |  |
| citrab | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| codigocentrabajo | NUMERIC(16, 8) | ✓ |  |
| ingesp1 | INTEGER | ✓ |  |
| ingesp2 | INTEGER | ✓ |  |
| ingesp3 | INTEGER | ✓ |  |
| ingesp4 | INTEGER | ✓ |  |
| ingesp5 | INTEGER | ✓ |  |
| ingesp6 | INTEGER | ✓ |  |
| ingesp7 | INTEGER | ✓ |  |
| nempleado1 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| napellido1 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| napellido2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| clave | INTEGER |  |  |
| sprofesional | BIT |  |  |
| email | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['seccion'] → seccion.['seccion']

#### Índices
- empleado_empleado: ['empleado', 'empresa'] 
- empleado_nempleado: ['empresa', 'nempleado'] 
- IX_empleado_aempleado: ['aempleado'] 
- IX_empleado_afp: ['afp'] 
- IX_empleado_banco: ['banco'] 
- IX_empleado_carelect: ['carelect'] 
- IX_empleado_cargo: ['cargo'] 
- IX_empleado_carmino: ['carmino'] 
- IX_empleado_cip: ['cip'] 
- IX_empleado_codisss: ['codisss'] 
- IX_empleado_codreloj: ['codreloj'] 
- IX_empleado_ctrocosto: ['ctrocosto'] 
- IX_empleado_cuenta: ['cuenta'] 
- IX_empleado_cuentab: ['cuentab'] 
- IX_empleado_depto: ['depto'] 
- IX_empleado_direccemp: ['direccemp'] 
- IX_empleado_empcubanco: ['empcubanco'] 
- IX_empleado_empleado: ['empleado'] 
- IX_empleado_empresa: ['empresa'] 
- IX_empleado_estcivil: ['estcivil'] 
- IX_empleado_formpago: ['formpago'] 
- IX_empleado_jornada: ['jornada'] 
- IX_empleado_liccond: ['liccond'] 
- IX_empleado_lugarnac: ['lugarnac'] 
- IX_empleado_municip: ['municip'] 
- IX_empleado_nacional: ['nacional'] 
- IX_empleado_nempleado: ['nempleado'] 
- IX_empleado_nit: ['nit'] 
- IX_empleado_nombisss: ['nombisss'] 
- IX_empleado_notas: ['notas'] 
- IX_empleado_ntarjeta: ['ntarjeta'] 
- IX_empleado_numisss: ['numisss'] 
- IX_empleado_nup: ['nup'] 
- IX_empleado_pais: ['pais'] 
- IX_empleado_pasaport: ['pasaport'] 
- IX_empleado_permintr: ['permintr'] 
- IX_empleado_profesion: ['profesion'] 
- IX_empleado_seccion: ['seccion'] 
- IX_empleado_sexo: ['sexo'] 
- IX_empleado_telefon1: ['telefon1'] 
- IX_empleado_telefon2: ['telefon2'] 
- IX_empleado_tipocta: ['tipocta'] 
- IX_empleado_tipoplaza: ['tipoplaza'] 
- IX_empleado_tiposan: ['tiposan'] 
- IX_empleado_usuario: ['usuario'] 

### Tabla: empleadoregistro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| empleado | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empleadoregistro | INTEGER |  | ✓ |
| hora | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: empresa
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| numissspat | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nempresa | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| direccion | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono1 | VARCHAR(14) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono2 | VARCHAR(14) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fax | VARCHAR(14) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dui | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| representa | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| giro | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| municip | INTEGER |  |  |
| empresa | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| PAIS | INTEGER |  |  |
| MONEDA | INTEGER |  |  |
| elSalvador | BIT |  |  |
| Guatemala | BIT |  |  |
| nicaragua | BIT |  |  |
| honduras | BIT |  |  |
| costarica | BIT |  |  |
| panama | BIT |  |  |
| estadosunidos | BIT |  |  |
| mexico | BIT |  |  |
| chile | BIT |  |  |
| ecuador | BIT |  |  |
| peru | BIT |  |  |
| venezuela | BIT |  |  |
| correlativoQuedan | INTEGER |  |  |
| soloExistencias | BIT |  |  |
| sidomingo | BIT |  |  |
| puertoDescarga | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| puertoEntrega | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| email | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| docunico | BIT |  |  |
| autorizacion | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cajanumero | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vendedorbodega | BIT |  |  |
| escogerprinter | BIT |  |  |
| preciocaja | BIT |  |  |
| activapermisos | BIT |  |  |
| planilla30 | BIT |  |  |
| isr | NUMERIC(18, 6) |  |  |
| aportacionsoli | NUMERIC(18, 6) |  |  |
| vistaprevia | BIT |  |  |
| confirmaprint | BIT |  |  |
| justprint | BIT |  |  |
| pcloud | BIT |  |  |
| prefijarcantuno | INTEGER |  |  |
| rembodcaja | BIT | ✓ |  |
| preparapedido | BIT |  |  |
| rutareloj | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sipreciocosto | BIT |  |  |
| autosinctipomov | BIT |  |  |
| cuantasListasPrecio | INTEGER | ✓ |  |
| fPercepcion | INTEGER |  |  |
| pPercepcion | BIT |  |  |
| fRetencion | INTEGER |  |  |
| pRetencion | BIT |  |  |
| sinInternet | BIT |  |  |
| sinImpuesto | BIT |  |  |
| fseguridad | BIT |  |  |
| variosprecios | BIT |  |  |
| noselectPrint | INTEGER |  |  |
| precioenCompra | BIT |  |  |
| manejaLote | BIT |  |  |
| ppistola | BIT |  |  |
| escoje_precio | BIT |  |  |
| busca_por_registro | BIT |  |  |
| bonifica | BIT |  |  |
| descxvol | BIT |  |  |
| escalzado | BIT |  |  |
| PrecioCompcIva | BIT |  |  |
| esdefinitiva | BIT |  |  |
| cuantosPrint | INTEGER |  |  |
| vretencion | BIT |  |  |
| vpercepcion | BIT |  |  |
| siCantidad | BIT |  |  |
| blockcprecio | BIT |  |  |
| blockCliRapido | BIT |  |  |
| llevacxp | BIT |  |  |
| cambiaPrecios | BIT |  |  |
| pcontrolexist | BIT |  |  |
| descxval | BIT |  |  |
| offline | BIT |  |  |
| consigna | BIT |  |  |
| solocontado | BIT |  |  |
| solocredito | BIT |  |  |
| solof2 | BIT |  |  |
| cambiaLprecio | BIT |  |  |
| cdespacho | BIT |  |  |
| lockvendedor | BIT |  |  |
| obligaclave | BIT |  |  |
| mesobligaclave | INTEGER |  |  |
| tasaInteres | NUMERIC(5, 2) |  |  |
| preservado | BIT |  |  |
| factor_fob | NUMERIC(5, 2) |  |  |
| a90 | BIT |  |  |
| boniplus | BIT |  |  |
| iglesia | BIT |  |  |
| cambioacero | BIT |  |  |
| esfactor | BIT |  |  |
| gestionventa | INTEGER |  |  |
| dirFactura | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| margenPrecio | BIT |  |  |
| tipo | INTEGER | ✓ |  |
| conemail | BIT |  |  |

#### Índices
- IX_empresa_CAJANUMERO: ['cajanumero'] 
- IX_empresa_direccion: ['direccion'] 
- IX_empresa_dui: ['dui'] 
- IX_empresa_empresa: ['empresa'] 
- IX_empresa_fax: ['fax'] 
- IX_empresa_giro: ['giro'] 
- IX_empresa_municip: ['municip'] 
- IX_empresa_nempresa: ['nempresa'] 
- IX_empresa_nit: ['nit'] 
- IX_empresa_notas: ['notas'] 
- IX_empresa_numissspat: ['numissspat'] 
- IX_empresa_registro: ['registro'] 
- IX_empresa_representa: ['representa'] 
- IX_empresa_telefono1: ['telefono1'] 
- IX_empresa_telefono2: ['telefono2'] 
- IX_empresa_usuario: ['usuario'] 

### Tabla: emptipla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| empleado | INTEGER |  |  |
| tipopla | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| emptipla | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |

#### Foreign Keys
- ['tipopla'] → tipopla.['tipopla']

#### Índices
- IX_emptipla_empleado: ['empleado'] 
- IX_emptipla_empresa: ['empresa'] 
- IX_emptipla_emptipla: ['emptipla'] 
- IX_emptipla_tipopla: ['tipopla'] 
- IX_emptipla_usuario: ['usuario'] 
- IX_tipopla_empleado: ['tipopla', 'empleado'] (UNIQUE)

### Tabla: encompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nencompra | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fecingreso | DATETIME | ✓ |  |
| fecretiro | DATETIME | ✓ |  |
| lencompra | BIT |  |  |
| lpagador | BIT |  |  |
| encompra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_encompra_empresa: ['empresa'] 
- IX_encompra_encompra: ['encompra'] 
- IX_encompra_nencompra: ['nencompra'] 
- IX_encompra_usuario: ['usuario'] 

### Tabla: entradabodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| entradabodega | INTEGER |  | ✓ |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rf | DATETIME | ✓ |  |
| n | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rnum | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| npre | CHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rc | NUMERIC(15, 6) |  |  |
| np | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rp | NUMERIC(15, 6) |  |  |
| rt | MONEY |  |  |
| notas | CHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_entradabodega_entradabodega: ['entradabodega'] 

### Tabla: entregable
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| etapa | INTEGER |  |  |
| entregable | INTEGER |  | ✓ |
| nentregable | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_entregable_empresa: ['empresa'] 
- IX_entregable_entregable: ['entregable'] 
- IX_entregable_etapa: ['etapa'] 
- IX_entregable_nentregable: ['nentregable'] 
- IX_entregable_usuario: ['usuario'] 

### Tabla: envio
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| envio | INTEGER |  | ✓ |
| nEnvio | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: envioCotiza
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Activo | BIT |  |  |
| dcambodega | INTEGER |  |  |
| dfactura | INTEGER |  |  |
| doventa | INTEGER |  |  |
| envioCotiza | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: envioFactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER |  |  |
| cambodega | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| envioFactura | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| dfactura | INTEGER | ✓ |  |
| dcambodega | INTEGER | ✓ |  |

### Tabla: equipo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nequipo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| orden | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tiempo | NUMERIC(6, 2) | ✓ |  |
| cantidad | NUMERIC(12, 2) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| equipo | INTEGER |  | ✓ |

### Tabla: equipoprocess
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| equipo | INTEGER | ✓ |  |
| almacen | INTEGER | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tiempo | NUMERIC(6, 2) | ✓ |  |
| fecha | DATETIME | ✓ |  |
| fechainicio | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| estatus | INTEGER | ✓ |  |
| rupfase | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| equipoprocess | INTEGER |  | ✓ |
| rupstatus | INTEGER | ✓ |  |
| fentrega | DATETIME | ✓ |  |
| hcuanto | INTEGER | ✓ |  |
| rupot | INTEGER | ✓ |  |
| mcuanto | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| orden | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| f1 | DATETIME | ✓ |  |

### Tabla: estado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| estado | INTEGER |  | ✓ |
| nestado | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| preferido | BIT |  |  |
| usuario | INTEGER |  |  |

#### Índices
- IX_estado_empresa: ['empresa'] 
- IX_estado_estado: ['estado'] 
- IX_estado_nestado: ['nestado'] 
- IX_estado_usuario: ['usuario'] 

### Tabla: estatus
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| estatus | INTEGER |  | ✓ |
| nestatus | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| noiniciado | BIT |  |  |
| proceso | BIT |  |  |
| terminado | BIT |  |  |
| cancela | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| cimport | BIT |  |  |
| cexport | BIT |  |  |
| portimport | BIT |  |  |
| portexport | BIT |  |  |

#### Índices
- IX_estatus_empresa: ['empresa'] 
- IX_estatus_estatus: ['estatus'] 
- IX_estatus_nestatus: ['nestatus'] 
- IX_estatus_usuario: ['usuario'] 

### Tabla: estcivil
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nestcivil | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| estcivil | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| simbolo | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_estcivil_empresa: ['empresa'] 
- IX_estcivil_estcivil: ['estcivil'] 
- IX_estcivil_nestcivil: ['nestcivil'] 
- IX_estcivil_usuario: ['usuario'] 

### Tabla: estilo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nestilo | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| estilo | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: etapa
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fase | INTEGER |  |  |
| etapa | INTEGER |  | ✓ |
| netapa | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_etapa_empresa: ['empresa'] 
- IX_etapa_etapa: ['etapa'] 
- IX_etapa_fase: ['fase'] 
- IX_etapa_netapa: ['netapa'] 
- IX_etapa_usuario: ['usuario'] 

### Tabla: existen
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| icdbarra | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cantidad | NUMERIC(15, 6) |  |  |
| ncategori | CHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ntipoprod | CHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipoprod | INTEGER |  |  |

#### Índices
- IX_existen_tipoprod: ['tipoprod'] 

### Tabla: factElec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER |  |  |
| uuid | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| serie | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numero | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factelec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pagos | INTEGER |  |  |
| lafecha | DATETIME | ✓ |  |
| compra | INTEGER | ✓ |  |
| remision | INTEGER | ✓ |  |
| retencion | INTEGER | ✓ |  |
| conting | INTEGER | ✓ |  |
| invalida | INTEGER | ✓ |  |
| fhProcesamiento | DATETIME | ✓ |  |
| selloRecibido | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| eljson | VARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factnew | INTEGER | ✓ |  |
| contingencia | INTEGER | ✓ |  |
| contingenvio | INTEGER | ✓ |  |
| anulacion | INTEGER | ✓ |  |
| anulada | INTEGER | ✓ |  |
| _correo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| _clave | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| donacion | BIT |  |  |
| almacen | INTEGER | ✓ |  |
| exclunula | INTEGER | ✓ |  |
| donanula | INTEGER | ✓ |  |
| retennula | INTEGER | ✓ |  |
| exponula | INTEGER | ✓ |  |
| reminula | INTEGER | ✓ |  |
| ppagos | INTEGER | ✓ |  |
| ncreten_nula | INTEGER | ✓ |  |

### Tabla: factcont
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nclientes | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nmunicip | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factura | INTEGER |  |  |
| factcont | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dui | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ofactura | INTEGER |  |  |
| telefono | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['factura'] → factura.['factura']

#### Índices
- IX_factcont_direccion: ['direccion'] 
- IX_factcont_empresa: ['empresa'] 
- IX_factcont_factcont: ['factcont'] 
- IX_factcont_factura: ['factura'] 
- IX_factcont_nclientes: ['nclientes'] 
- IX_factcont_nit: ['nit'] 
- IX_factcont_nmunicip: ['nmunicip'] 
- IX_factcont_registro: ['registro'] 
- IX_factcont_usuario: ['usuario'] 

### Tabla: factnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| factura | INTEGER |  |  |
| factnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| impresa | BIT |  |  |
| facturareferencia | INTEGER | ✓ |  |

#### Foreign Keys
- ['factura'] → factura.['factura']

#### Índices
- IX_factnula_empresa: ['empresa'] 
- IX_factnula_factnula: ['factnula'] 
- IX_factnula_factura: ['factura'] 
- IX_factnula_fecha: ['fecha'] 
- IX_factnula_motivo: ['motivo'] 
- IX_factnula_usuario: ['usuario'] 

### Tabla: factorxcli
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| presenta | INTEGER |  |  |
| producto | INTEGER |  |  |
| factor | NUMERIC(16, 6) |  |  |
| factorxcli | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']

#### Índices
- IX_factorxcli_clientes: ['clientes'] 
- IX_factorxcli_empresa: ['empresa'] 
- IX_factorxcli_factorxcli: ['factorxcli'] 
- IX_factorxcli_presenta: ['presenta'] 
- IX_factorxcli_producto: ['producto'] 
- IX_factorxcli_usuario: ['usuario'] 

### Tabla: factorxfact
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER |  |  |
| dfactura | INTEGER |  |  |
| kardex | INTEGER |  |  |
| muestras | NUMERIC(16, 6) |  |  |
| factor | NUMERIC(16, 6) |  |  |
| factorprecio | NUMERIC(16, 6) |  |  |
| factorxfact | INTEGER |  | ✓ |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_factorxfact_dfactura: ['dfactura'] 
- IX_factorxfact_empresa: ['empresa'] 
- IX_factorxfact_factorxfact: ['factorxfact'] 
- IX_factorxfact_factura: ['factura'] 
- IX_factorxfact_kardex: ['kardex'] 
- IX_factorxfact_usuario: ['usuario'] 

### Tabla: factpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factpagos | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| pagos | INTEGER |  |  |
| facturanula | INTEGER |  |  |
| pagosnula | INTEGER |  |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_factpagos_factpagos: ['factpagos'] 
- IX_factpagos_factura: ['factura'] 
- IX_factpagos_facturanula: ['facturanula'] 
- IX_factpagos_pagos: ['pagos'] 
- IX_factpagos_pagosnula: ['pagosnula'] 

### Tabla: factura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| cancelada | BIT |  |  |
| impbod | BIT |  |  |
| impresa | BIT |  |  |
| numedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| comentario | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| expcomen | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacanc | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| iva | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipovta | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| factoriva | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| factura | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| pesofactura | NUMERIC(16, 6) |  |  |
| pagos | INTEGER |  |  |
| basesiniva | BIT |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| efectivo | NUMERIC(16, 6) |  |  |
| cheque | NUMERIC(16, 6) |  |  |
| tarjeta | NUMERIC(16, 6) |  |  |
| nocheque | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notarjeta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| caja | INTEGER |  |  |
| combustible | NUMERIC(18, 6) |  |  |
| encomienda | NUMERIC(18, 6) |  |  |
| ivaCombustible | NUMERIC(18, 6) |  |  |
| ivaencomienda | NUMERIC(18, 6) |  |  |
| Cotrans | NUMERIC(16, 8) |  |  |
| fechafin | DATETIME | ✓ |  |
| estado | INTEGER |  |  |
| prioridad | INTEGER |  |  |
| terminado | BIT |  |  |
| turno | INTEGER |  |  |
| rliquida | INTEGER |  |  |
| aprobado | BIT |  |  |
| impempaque | BIT |  |  |
| impvineta | BIT |  |  |
| vineta | INTEGER |  |  |
| enfirme | BIT |  |  |
| dgratif | NUMERIC(18, 6) |  |  |
| tipopago | INTEGER |  |  |
| bnotas | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cobrador | INTEGER |  |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| concaja | BIT |  |  |
| clientes2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pais | INTEGER |  |  |
| pagencia | NUMERIC(12, 2) | ✓ |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| ordenno | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nombreref | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| docref | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| camion | INTEGER |  |  |
| FacturaReferencia | BIGINT |  |  |
| enruta | BIT |  |  |
| anulada | BIT |  |  |
| propina | NUMERIC(18, 6) |  |  |
| nopropina | BIT |  |  |
| mesa | BIT |  |  |
| nomesa | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| equipo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['condpago'] → condpago.['condpago']
- ['iva'] → iva.['iva']
- ['tipomov'] → tipomov.['tipomov']
- ['vendedor'] → vendedor.['vendedor']

#### Índices
- <Name of Missing Index, sysname,>: ['nula', 'empresa'] 
- CXC_FACTURA_PAGOS: ['pagos', 'fecha'] 
- factura_empresa_caja_fecha: ['empresa', 'caja'] 
- factura_fecha_tiopago: ['empresa', 'fecha', 'tipopago'] 
- factura_nula_empresa: ['nula', 'empresa'] 
- factura_nula_impresa_clientes: ['nula', 'impresa'] 
- factura_nula_impresa_factura: ['nula', 'impresa'] 
- Factura_nula_impresa_montfact: ['nula', 'impresa'] 
- factura_nula_impresa_vendedor: ['nula', 'impresa'] 
- facturaReferencia1: ['FacturaReferencia'] 
- invkardex_28122012: ['nula'] 
- IX_factura_bodega: ['bodega'] 
- IX_factura_caja: ['caja'] 
- IX_factura_clientes: ['clientes'] 
- IX_factura_comentario: ['comentario'] 
- IX_factura_condpago: ['condpago'] 
- IX_factura_empresa: ['empresa'] 
- IX_factura_estado: ['estado'] 
- IX_factura_expcomen: ['expcomen'] 
- IX_factura_factura: ['factura'] 
- IX_factura_fecha: ['fecha'] 
- IX_factura_iva: ['iva'] 
- IX_factura_moneda: ['moneda'] 
- IX_factura_nocheque: ['nocheque'] 
- IX_factura_NOMESA: ['nomesa'] 
- IX_factura_notarjeta: ['notarjeta'] 
- IX_factura_notas: ['notas'] 
- IX_factura_pagos: ['pagos'] 
- IX_factura_pedido: ['pedido'] 
- IX_factura_prioridad: ['prioridad'] 
- IX_factura_prodprec: ['prodprec'] 
- IX_factura_rliquida: ['rliquida'] 
- IX_factura_tipomov: ['tipomov'] 
- IX_factura_tipovta: ['tipovta'] 
- IX_factura_transpte: ['transpte'] 
- IX_factura_turno: ['turno'] 
- IX_factura_usuario: ['usuario'] 
- IX_factura_vendedor: ['vendedor'] 

### Tabla: facturapagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| factura | INTEGER |  |  |
| pagos | INTEGER |  |  |
| pagosnula | BIT |  |  |
| facturapagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: facturasexpress
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| facturasexpress | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| proveedor | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bl | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripgods | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| piezas | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| volumen | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| contenedor | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| exportcarrier | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| foreingport | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marksnum1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marksnum2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marksnum3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marksnum4 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marksnum5 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numbers1 | NUMERIC(18, 6) |  |  |
| numbers2 | NUMERIC(18, 6) |  |  |
| numbers3 | NUMERIC(18, 6) |  |  |
| numbers4 | NUMERIC(18, 6) |  |  |
| numbers5 | NUMERIC(18, 6) |  |  |
| descripcomm1 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcomm2 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcomm3 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcomm4 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcomm5 | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gross1 | NUMERIC(18, 6) |  |  |
| gross2 | NUMERIC(18, 6) |  |  |
| gross3 | NUMERIC(18, 6) |  |  |
| gross4 | NUMERIC(18, 6) |  |  |
| gross5 | NUMERIC(18, 6) |  |  |
| measureme1 | NUMERIC(18, 6) |  |  |
| measureme2 | NUMERIC(18, 6) |  |  |
| measureme3 | NUMERIC(18, 6) |  |  |
| measureme4 | NUMERIC(18, 6) |  |  |
| measureme5 | NUMERIC(18, 6) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| peso1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso4 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso5 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso6 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso7 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso8 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso9 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| peso10 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| carriageby | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| placeofrecipient | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| portofloadingexport | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fortrans | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: factvehiculo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factvehiculo | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| clientedatos | INTEGER |  |  |

#### Índices
- IX_factvehiculo_clientedatos: ['clientedatos'] 
- IX_factvehiculo_factura: ['factura'] 
- IX_factvehiculo_factvehiculo: ['factvehiculo'] 

### Tabla: faltofacturar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| kardex | INTEGER |  |  |
| fecha | DATETIME |  |  |
| cantidad | NUMERIC(18, 6) | ✓ |  |
| precio | NUMERIC(18, 6) | ✓ |  |
| faltofacturar | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |

#### Índices
- IX_faltofacturar_clientes: ['clientes'] 
- IX_faltofacturar_empresa: ['empresa'] 
- IX_faltofacturar_faltofacturar: ['faltofacturar'] 
- IX_faltofacturar_fecha: ['fecha'] 
- IX_faltofacturar_kardex: ['kardex'] 
- IX_faltofacturar_usuario: ['usuario'] 
- IX_faltofacturar_vendedor: ['vendedor'] 

### Tabla: fase
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fase | INTEGER |  | ✓ |
| nfase | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| iteracion | INTEGER |  |  |
| duracion | DECIMAL(18, 2) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_fase_empresa: ['empresa'] 
- IX_fase_fase: ['fase'] 
- IX_fase_iteracion: ['iteracion'] 
- IX_fase_nfase: ['nfase'] 
- IX_fase_usuario: ['usuario'] 

### Tabla: fbodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nfbodega | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fbodega | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_fbodega_empresa: ['empresa'] 
- IX_fbodega_fbodega: ['fbodega'] 
- IX_fbodega_nfbodega: ['nfbodega'] 
- IX_fbodega_usuario: ['usuario'] 

### Tabla: feldata
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dte | SMALLINT | ✓ |  |
| ncatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| catalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| scatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| descripcion | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| zcatalogo | NVARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tabla | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| depto | TINYINT | ✓ |  |
| municip | TINYINT | ✓ |  |

### Tabla: ffgasto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| gastoacum | NUMERIC(16, 6) |  |  |
| gastoacumlocal | NUMERIC(16, 6) |  |  |
| gastoacumseg | NUMERIC(16, 6) |  |  |
| gastomes | NUMERIC(16, 6) |  |  |
| gastomeslocal | NUMERIC(16, 6) |  |  |
| gastomesseg | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| costolocal | NUMERIC(16, 6) |  |  |
| costoseg | NUMERIC(16, 6) |  |  |
| vrescate | NUMERIC(16, 6) |  |  |
| vrescatelocal | NUMERIC(16, 6) |  |  |
| vrescateseg | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| moneda | INTEGER |  |  |
| ffgasto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fecha | DATETIME |  |  |
| periodoaf | INTEGER |  |  |

#### Índices
- IX_ffgasto_empresa: ['empresa'] 
- IX_ffgasto_fecha: ['fecha'] 
- IX_ffgasto_ffgasto: ['ffgasto'] 
- IX_ffgasto_moneda: ['moneda'] 
- IX_ffgasto_periodoaf: ['periodoaf'] 
- IX_ffgasto_usuario: ['usuario'] 

### Tabla: fgasto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | INTEGER |  |  |
| ano | INTEGER |  |  |
| fecha | DATETIME |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| gastoacum | NUMERIC(16, 6) |  |  |
| gastoacumlocal | NUMERIC(16, 6) |  |  |
| gastoacumseg | NUMERIC(16, 6) |  |  |
| gastomes | NUMERIC(16, 6) |  |  |
| gastomeslocal | NUMERIC(16, 6) |  |  |
| gastomesseg | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| costolocal | NUMERIC(16, 6) |  |  |
| costoseg | NUMERIC(16, 6) |  |  |
| vrescate | NUMERIC(16, 6) |  |  |
| vrescatelocal | NUMERIC(16, 6) |  |  |
| vrescateseg | NUMERIC(16, 6) |  |  |
| depreciado | BIT |  |  |
| fproducto | INTEGER |  |  |
| ffgasto | INTEGER |  |  |
| fgasto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_fgasto_ano: ['ano'] 
- IX_fgasto_empresa: ['empresa'] 
- IX_fgasto_fecha: ['fecha'] 
- IX_fgasto_ffgasto: ['ffgasto'] 
- IX_fgasto_fgasto: ['fgasto'] 
- IX_fgasto_fproducto: ['fproducto'] 
- IX_fgasto_mes: ['mes'] 
- IX_fgasto_moneda: ['moneda'] 
- IX_fgasto_usuario: ['usuario'] 

### Tabla: fgrupo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nfgrupo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fgrupo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_fgrupo_empresa: ['empresa'] 
- IX_fgrupo_fgrupo: ['fgrupo'] 
- IX_fgrupo_nfgrupo: ['nfgrupo'] 
- IX_fgrupo_usuario: ['usuario'] 

### Tabla: fixed
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nproducto | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| otroname | CHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| controla | BIT |  |  |
| bonificado | BIT |  |  |
| vineta | BIT |  |  |
| enventa | BIT |  |  |
| incluir | BIT |  |  |
| fabricar | BIT |  |  |
| exento | BIT |  |  |
| desccontad | BIT |  |  |
| parte | BIT |  |  |
| servicios | BIT |  |  |
| costo | NUMERIC(15, 7) |  |  |
| cantidadre | NUMERIC(15, 6) |  |  |
| minimo | NUMERIC(15, 6) |  |  |
| cantidadco | NUMERIC(15, 6) |  |  |
| compramini | NUMERIC(15, 6) |  |  |
| compramaxi | NUMERIC(15, 6) |  |  |
| promedio | NUMERIC(15, 6) |  |  |
| promlicita | NUMERIC(15, 6) |  |  |
| promedioex | NUMERIC(15, 6) |  |  |
| promlicit2 | NUMERIC(15, 6) |  |  |
| codbarra | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- ci_azure_fixup_dbo_fixed: ['nproducto'] 

### Tabla: fmodelo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nfmodelo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fmodelo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_fmodelo_empresa: ['empresa'] 
- IX_fmodelo_fmodelo: ['fmodelo'] 
- IX_fmodelo_nfmodelo: ['nfmodelo'] 
- IX_fmodelo_usuario: ['usuario'] 

### Tabla: formapago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| efectivo | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| cheque | NUMERIC(16, 6) |  |  |
| tarjeta | NUMERIC(16, 6) |  |  |
| billete1 | NUMERIC(16, 6) |  |  |
| billete2 | NUMERIC(16, 6) |  |  |
| billete3 | NUMERIC(16, 6) |  |  |
| billete4 | NUMERIC(16, 6) |  |  |
| billete5 | NUMERIC(16, 6) |  |  |
| billete6 | NUMERIC(16, 6) |  |  |
| moneda1 | NUMERIC(16, 6) |  |  |
| reparacion | NUMERIC(16, 6) |  |  |
| gastos | NUMERIC(16, 6) |  |  |
| fondosajenos | NUMERIC(16, 6) |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| fecha | DATETIME |  |  |
| nocheque | NUMERIC(16, 6) |  |  |
| notarjeta | NUMERIC(16, 6) |  |  |
| factura | NUMERIC(16, 6) |  |  |
| contrato | NUMERIC(16, 6) |  |  |
| formapago | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_formapago_empresa: ['empresa'] 
- IX_formapago_fecha: ['fecha'] 
- IX_formapago_formapago: ['formapago'] 
- IX_formapago_usuario: ['usuario'] 

### Tabla: formpago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nformpago | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| frecuente | BIT |  |  |
| activo | BIT |  |  |
| formpago | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| HORATIEMPO | DATETIME |  |  |
| FIJO | BIT | ✓ |  |
| OBRA | BIT | ✓ |  |
| COMISION | BIT | ✓ |  |

#### Índices
- IX_formpago_empresa: ['empresa'] 
- IX_formpago_formpago: ['formpago'] 
- IX_formpago_nformpago: ['nformpago'] 
- IX_formpago_usuario: ['usuario'] 

### Tabla: formula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| porcprecio | NUMERIC(16, 6) |  |  |
| porccosto | NUMERIC(16, 6) |  |  |
| mformula | INTEGER |  |  |
| producto | INTEGER |  |  |
| formula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| descripcion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| concentracion | NUMERIC(18, 6) |  |  |
| factor | NUMERIC(18, 6) |  |  |
| umedida | INTEGER |  |  |
| presenta | INTEGER |  |  |

#### Índices
- IX_formula_empresa: ['empresa'] 
- IX_formula_formula: ['formula'] 
- IX_formula_mformula: ['mformula'] 
- IX_formula_presenta: ['presenta'] 
- IX_formula_producto: ['producto'] 
- IX_formula_usuario: ['usuario'] 

### Tabla: formulataller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nformulaTaller | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| categoriTaller | INTEGER |  |  |
| formulataller | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| kilometraje | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: foto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| idfoto | INTEGER |  |  |
| foto | BINARY(50) | ✓ |  |
| nombre | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: fpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nfpartida | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipopart | INTEGER |  |  |
| concepto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fpartida | INTEGER |  | ✓ |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_fpartida_concepto: ['concepto'] 
- IX_fpartida_empresa: ['empresa'] 
- IX_fpartida_fpartida: ['fpartida'] 
- IX_fpartida_nfpartida: ['nfpartida'] 
- IX_fpartida_tipopart: ['tipopart'] 
- IX_fpartida_usuario: ['usuario'] 

### Tabla: fproducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| icdbarra | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nfproducto | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fbodega | INTEGER |  |  |
| ftipoprod | INTEGER |  |  |
| proveedor | INTEGER |  |  |
| fgrupo | INTEGER |  |  |
| umedida | INTEGER |  |  |
| fmodelo | INTEGER |  |  |
| moneda | INTEGER |  |  |
| marca | INTEGER |  |  |
| mes | INTEGER |  |  |
| ano | INTEGER |  |  |
| activo | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| costolocal | NUMERIC(16, 6) |  |  |
| costoseg | NUMERIC(16, 6) |  |  |
| vidautil | NUMERIC(16, 6) |  |  |
| gasto | NUMERIC(16, 6) |  |  |
| gastolocal | NUMERIC(16, 6) |  |  |
| gastoseg | NUMERIC(16, 6) |  |  |
| vrescate | NUMERIC(16, 6) |  |  |
| vrescatelocal | NUMERIC(16, 6) |  |  |
| vrescateseg | NUMERIC(16, 6) |  |  |
| cuota | NUMERIC(16, 6) |  |  |
| cuotalocal | NUMERIC(16, 6) |  |  |
| cuotaseg | NUMERIC(16, 6) |  |  |
| depreciado | BIT |  |  |
| cantidad | INTEGER |  |  |
| noserie | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| chasis | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| documento | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| comentario | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fproducto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| periodoaf | INTEGER |  |  |

#### Índices
- IX_fproducto_ano: ['ano'] 
- IX_fproducto_cantidad: ['cantidad'] 
- IX_fproducto_chasis: ['chasis'] 
- IX_fproducto_comentario: ['comentario'] 
- IX_fproducto_documento: ['documento'] 
- IX_fproducto_empresa: ['empresa'] 
- IX_fproducto_fbodega: ['fbodega'] 
- IX_fproducto_fecha: ['fecha'] 
- IX_fproducto_fgrupo: ['fgrupo'] 
- IX_fproducto_fmodelo: ['fmodelo'] 
- IX_fproducto_fproducto: ['fproducto'] 
- IX_fproducto_ftipoprod: ['ftipoprod'] 
- IX_fproducto_icdbarra: ['icdbarra'] 
- IX_fproducto_marca: ['marca'] 
- IX_fproducto_mes: ['mes'] 
- IX_fproducto_moneda: ['moneda'] 
- IX_fproducto_nfproducto: ['nfproducto'] 
- IX_fproducto_noserie: ['noserie'] 
- IX_fproducto_proveedor: ['proveedor'] 
- IX_fproducto_umedida: ['umedida'] 
- IX_fproducto_usuario: ['usuario'] 

### Tabla: frecpago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nfrecpago | VARCHAR(50) COLLATE "Modern_Spanish_CI_AS" |  |  |
| primera | BIT |  |  |
| uno | NUMERIC(5, 2) | ✓ |  |
| segunda | BIT |  |  |
| dos | NUMERIC(5, 2) |  |  |
| todas | BIT |  |  |
| activo | BIT |  |  |
| frecpago | INTEGER |  |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_frecpago_empresa: ['empresa'] 
- IX_frecpago_frecpago: ['frecpago'] 
- IX_frecpago_nfrecpago: ['nfrecpago'] 
- IX_frecpago_usuario: ['usuario'] 

### Tabla: fruta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fruta | INTEGER |  | ✓ |
| nfruta | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_fruta_empresa: ['empresa'] 
- IX_fruta_fruta: ['fruta'] 
- IX_fruta_nfruta: ['nfruta'] 
- IX_fruta_usuario: ['usuario'] 

### Tabla: ftablapart
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dfpartida | INTEGER |  |  |
| tabla | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ncampo | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| campo | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| ctrocosto | INTEGER |  |  |
| ftablapart | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ftablapart_campo: ['campo'] 
- IX_ftablapart_ctrocosto: ['ctrocosto'] 
- IX_ftablapart_cuenta: ['cuenta'] 
- IX_ftablapart_dfpartida: ['dfpartida'] 
- IX_ftablapart_empresa: ['empresa'] 
- IX_ftablapart_ftablapart: ['ftablapart'] 
- IX_ftablapart_ncampo: ['ncampo'] 
- IX_ftablapart_tabla: ['tabla'] 
- IX_ftablapart_usuario: ['usuario'] 

### Tabla: ftipoprod
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nftipoprod | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| ftipoprod | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ftipoprod_empresa: ['empresa'] 
- IX_ftipoprod_ftipoprod: ['ftipoprod'] 
- IX_ftipoprod_nftipoprod: ['nftipoprod'] 
- IX_ftipoprod_usuario: ['usuario'] 

### Tabla: garantia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ngarantia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| vencimiento | INTEGER |  |  |
| meses | BIT |  |  |
| garantia | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_garantia_empresa: ['empresa'] 
- IX_garantia_garantia: ['garantia'] 
- IX_garantia_ngarantia: ['ngarantia'] 
- IX_garantia_usuario: ['usuario'] 
- IX_garantia_vencimiento: ['vencimiento'] 

### Tabla: getcompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| esRecinto | BIT |  |  |
| numedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| cnumedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cfecha | DATETIME | ✓ |  |
| ocompra | INTEGER |  |  |
| compra | INTEGER |  |  |
| caja | INTEGER |  |  |
| recintofiscal | INTEGER |  |  |
| bodega | INTEGER |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| getcompra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| encompra | INTEGER |  |  |

### Tabla: giro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ngiro | VARCHAR(80) COLLATE "Modern_Spanish_CI_AS" |  |  |
| activo | BIT |  |  |
| giro | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- giro_giro: ['giro', 'empresa'] 
- IX_giro_empresa: ['empresa'] 
- IX_giro_giro: ['giro'] 
- IX_giro_ngiro: ['ngiro'] 
- IX_giro_usuario: ['usuario'] 

### Tabla: grupo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ngrupo | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| grupo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: grupoempleado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| grupo | INTEGER |  |  |
| empleado | INTEGER |  |  |
| grupoempleado | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |

### Tabla: hinvkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | DATETIME | ✓ |  |
| kardex | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| cuarentena | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| costoprom | NUMERIC(18, 6) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| invini | NUMERIC(16, 6) |  |  |
| qinvini | NUMERIC(16, 6) |  |  |
| compra | NUMERIC(16, 6) |  |  |
| qcompra | NUMERIC(16, 6) |  |  |
| otrosing | NUMERIC(16, 6) |  |  |
| qotrosing | NUMERIC(16, 6) |  |  |
| INGRESO | NUMERIC(16, 6) |  |  |
| SALIDA | NUMERIC(16, 6) |  |  |
| BONIF | NUMERIC(16, 6) |  |  |
| DEVOL | NUMERIC(16, 6) |  |  |
| VENTA | NUMERIC(16, 6) |  |  |
| INVFIN | NUMERIC(16, 6) |  |  |
| QINGRESO | NUMERIC(16, 6) |  |  |
| QSALIDA | NUMERIC(16, 6) |  |  |
| QBONIF | NUMERIC(16, 6) |  |  |
| QDEVOL | NUMERIC(16, 6) |  |  |
| QVENTA | NUMERIC(16, 6) |  |  |
| QINVFIN | NUMERIC(16, 6) |  |  |
| final | NUMERIC(18, 6) |  |  |
| producto | INTEGER |  |  |
| invkardex | INTEGER |  |  |

### Tabla: historenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| historenta | INTEGER |  | ✓ |
| isss | NUMERIC(18, 6) |  |  |
| afp | NUMERIC(18, 6) |  |  |
| renta | NUMERIC(18, 6) |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empleado | INTEGER |  |  |
| concepto | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| monto | NUMERIC(18, 6) |  |  |

#### Índices
- IX_historenta_concepto: ['concepto'] 
- IX_historenta_empleado: ['empleado'] 
- IX_historenta_empresa: ['empresa'] 
- IX_historenta_historenta: ['historenta'] 
- IX_historenta_usuario: ['usuario'] 

### Tabla: horario
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| anio | INTEGER |  |  |
| mes | INTEGER |  |  |
| semana | INTEGER |  |  |
| seccion | INTEGER |  |  |
| jornada | INTEGER |  |  |
| horario | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| midia | INTEGER |  |  |
| grupo | INTEGER |  |  |
| mesint | INTEGER |  |  |

### Tabla: horasExtras
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| horasExtras | INTEGER |  |  |
| nHorasExtras | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Horas | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_horasExtras: ['horasExtras'] 

### Tabla: idcaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| idCaller | INTEGER |  |  |
| fecha | DATETIME | ✓ |  |
| uFechaAcceso | DATETIME | ✓ |  |
| Iprouter | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| IpLocal | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| IpRemota | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| LocalHostName | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| remoteHostName | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| equipo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| registro | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| valor | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_idcaller: ['idCaller'] 

### Tabla: idtimecaller
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| idtimeCaller | INTEGER |  |  |
| fecha | DATETIME | ✓ |  |
| registro | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_idtimecaller: ['idtimeCaller'] 

### Tabla: impresor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| impresor | INTEGER |  | ✓ |
| nimpresor | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factura | BIT |  |  |
| recibo | BIT |  |  |
| bodega | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_impresor_empresa: ['empresa'] 
- IX_impresor_impresor: ['impresor'] 
- IX_impresor_nimpresor: ['nimpresor'] 
- IX_impresor_usuario: ['usuario'] 

### Tabla: impuesto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nimpuesto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factor | NUMERIC(5, 2) | ✓ |  |
| impuesto | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |

### Tabla: impvineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rollonum | INTEGER |  |  |
| factura | INTEGER |  |  |
| dfactura | INTEGER |  |  |
| codigo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecvence | DATETIME | ✓ |  |
| fechaliquida | DATETIME | ✓ |  |
| pagada | BIT |  |  |
| reimpresa | BIT |  |  |
| vinetanum | INTEGER |  |  |
| vvineta | NUMERIC(18, 6) |  |  |
| precioa | NUMERIC(18, 6) |  |  |
| preciob | NUMERIC(18, 6) |  |  |
| dfactura1 | INTEGER |  |  |
| codigo1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto1 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nolote1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecvence1 | DATETIME | ✓ |  |
| fechaliquida1 | DATETIME | ✓ |  |
| pagada1 | BIT |  |  |
| reimpresa1 | BIT |  |  |
| vinetanum1 | INTEGER |  |  |
| vvineta1 | NUMERIC(18, 6) |  |  |
| precioa1 | NUMERIC(18, 6) |  |  |
| preciob1 | NUMERIC(18, 6) |  |  |
| dfactura2 | INTEGER |  |  |
| codigo2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto2 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nolote2 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecvence2 | DATETIME | ✓ |  |
| fechaliquida2 | DATETIME | ✓ |  |
| pagada2 | BIT |  |  |
| reimpresa2 | BIT |  |  |
| vinetanum2 | INTEGER |  |  |
| vvineta2 | NUMERIC(18, 6) |  |  |
| precioa2 | NUMERIC(18, 6) |  |  |
| preciob2 | NUMERIC(18, 6) |  |  |
| dfactura3 | INTEGER |  |  |
| codigo3 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra3 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto3 | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nolote3 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecvence3 | DATETIME | ✓ |  |
| fechaliquida3 | DATETIME | ✓ |  |
| pagada3 | BIT |  |  |
| reimpresa3 | BIT |  |  |
| vinetanum3 | INTEGER |  |  |
| vvineta3 | NUMERIC(18, 6) |  |  |
| precioa3 | NUMERIC(18, 6) |  |  |
| preciob3 | NUMERIC(18, 6) |  |  |
| impvineta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| precioc | NUMERIC(18, 6) |  |  |
| preciod | NUMERIC(18, 6) |  |  |
| precioc1 | NUMERIC(18, 6) |  |  |
| precioc2 | NUMERIC(18, 6) |  |  |
| precioc3 | NUMERIC(18, 6) |  |  |
| preciod1 | NUMERIC(18, 6) |  |  |
| preciod2 | NUMERIC(18, 6) |  |  |
| preciod3 | NUMERIC(18, 6) |  |  |
| dispensador | BIT |  |  |
| recvineta | INTEGER |  |  |

### Tabla: infobanco
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| infobanco | INTEGER |  | ✓ |
| contenido | VARCHAR(140) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| codbarra | VARCHAR(82) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| monto | NUMERIC(18, 2) |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_infobanco_codbarra: ['codbarra'] 
- IX_infobanco_contenido: ['contenido'] 
- IX_infobanco_empresa: ['empresa'] 
- IX_infobanco_fecha: ['fecha'] 
- IX_infobanco_infobanco: ['infobanco'] 
- IX_infobanco_usuario: ['usuario'] 
- IX_infobanco_vendedor: ['vendedor'] 

### Tabla: ingesp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ningesp | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| porcentaje | NUMERIC(8, 4) |  |  |
| hed | BIT | ✓ |  |
| hen | BIT | ✓ |  |
| nocturnida | BIT | ✓ |  |
| vacaciones | BIT | ✓ |  |
| aguinaldo | BIT | ✓ |  |
| indemnizac | BIT | ✓ |  |
| activo | BIT | ✓ |  |
| ingesp | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| tabla | BIT |  |  |
| hevacacion | NUMERIC(16, 6) |  |  |
| hev | BIT | ✓ |  |
| hedom | BIT | ✓ |  |
| factornocturna | NUMERIC(18, 6) | ✓ |  |
| hnormal | NUMERIC(18, 6) |  |  |
| hextra | NUMERIC(18, 6) |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| notrabajo | BIT |  |  |
| politaller | BIT |  |  |
| horario | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factorhnormal | NUMERIC(18, 6) | ✓ |  |
| fijo | NUMERIC(12, 2) | ✓ |  |

#### Índices
- IX_ingesp_empresa: ['empresa'] 
- IX_ingesp_ingesp: ['ingesp'] 
- IX_ingesp_ningesp: ['ningesp'] 
- IX_ingesp_usuario: ['usuario'] 

### Tabla: ingfijo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ingfijo | INTEGER |  | ✓ |
| empleado | INTEGER |  |  |
| polingpla | INTEGER |  |  |
| monto | NUMERIC(9, 3) |  |  |
| monto1 | NUMERIC(9, 3) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: ingreso
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ningreso | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT | ✓ |  |
| comision | BIT | ✓ |  |
| aguinaldo | BIT | ✓ |  |
| vacacion | BIT | ✓ |  |
| frecpago | INTEGER | ✓ |  |
| ingreso | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| VIATICOS | BIT | ✓ |  |
| PROPORCIONAL | BIT |  |  |
| gratificacion | BIT | ✓ |  |
| HEF | BIT | ✓ |  |
| Alimentacion | BIT | ✓ |  |

#### Índices
- IX_ingreso_empresa: ['empresa'] 
- IX_ingreso_frecpago: ['frecpago'] 
- IX_ingreso_ingreso: ['ingreso'] 
- IX_ingreso_ningreso: ['ningreso'] 
- IX_ingreso_usuario: ['usuario'] 

### Tabla: insertPartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| InsertPartida | INTEGER |  | ✓ |
| opartida | INTEGER | ✓ |  |
| dpartida | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: interes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ninteres | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| factor | NUMERIC(16, 6) |  |  |
| operador | VARCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainici | DATETIME | ✓ |  |
| fechafinal | DATETIME | ✓ |  |
| interessimple | BIT |  |  |
| interescompuesto | BIT |  |  |
| interesmoratorio | BIT |  |  |
| interes | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_interes_empresa: ['empresa'] 
- IX_interes_interes: ['interes'] 
- IX_interes_ninteres: ['ninteres'] 
- IX_interes_operador: ['operador'] 
- IX_interes_usuario: ['usuario'] 

### Tabla: invcliente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipomov | INTEGER |  |  |
| factura | INTEGER |  |  |
| condpago | INTEGER |  |  |
| numedocu | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacan | DATETIME | ✓ |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| hmontfact | NUMERIC(16, 6) |  |  |
| habono | NUMERIC(16, 6) |  |  |
| hcargo | NUMERIC(16, 6) |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| invcliente | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| incluir | BIT |  |  |
| vendedor | INTEGER |  |  |
| cheque | BIT |  |  |
| nocheque | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| montochq | NUMERIC(16, 6) |  |  |
| hexenta | NUMERIC(18, 6) |  |  |
| hviva | NUMERIC(18, 6) |  |  |
| enruta | BIT |  |  |
| escheque | BIT |  |  |
| bodega | INTEGER |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| DPAGOS | INTEGER |  |  |
| CAJA | INTEGER |  |  |
| apagar | BIT |  |  |
| ccontrato | INTEGER |  |  |
| cambodega | INTEGER |  |  |
| montoaplicar | NUMERIC(18, 6) |  |  |
| esprima | BIT |  |  |
| ofactura | INTEGER |  |  |
| pdesc | NUMERIC(18, 6) |  |  |
| quedan | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechaquedan | DATETIME | ✓ |  |
| fechapago | DATETIME | ✓ |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['factura'] → factura.['factura']
- ['tipomov'] → tipomov.['tipomov']
- ['vendedor'] → vendedor.['vendedor']

#### Índices
- CXC_INVCLIENTE_CLIENTES: ['clientes', 'fecha'] 
- CXC_INVCLIENTE_EMPRESA_CLIENTES: ['empresa', 'clientes', 'fecha'] 
- CXC_INVCLIENTE_FACTURA: ['factura'] 
- invcliente_factura_empresa_fecha: ['factura', 'empresa', 'fecha'] 
- invcliente_tipomov: ['tipomov'] 
- IX_invcliente_clientes: ['clientes'] 
- IX_invcliente_condpago: ['condpago'] 
- IX_invcliente_empresa: ['empresa'] 
- IX_invcliente_factura: ['factura'] 
- IX_invcliente_fecha: ['fecha'] 
- IX_invcliente_invcliente: ['invcliente'] 
- IX_invcliente_moneda: ['moneda'] 
- IX_invcliente_nocheque: ['nocheque'] 
- IX_invcliente_tipomov: ['tipomov'] 
- IX_invcliente_usuario: ['usuario'] 
- IX_invcliente_vendedor: ['vendedor'] 

### Tabla: invkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | DATETIME | ✓ |  |
| costoprom | NUMERIC(18, 6) |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| INVFIN | NUMERIC(16, 6) |  |  |
| QINVFIN | NUMERIC(16, 6) |  |  |
| kardex | INTEGER |  |  |
| producto | INTEGER | ✓ |  |

#### Índices
- IDX_InvKardex_Mes: ['mes', 'kardex'] 
- invkardex: ['kardex'] 
- invkardex_28122012_01: ['mes', 'empresa'] 
- invkardex_empresa: ['empresa'] 
- invkardex_kardex: ['kardex'] 
- invkardex_producto_mes: ['producto'] 
- invkardex_producto_mes_costo: ['producto'] 
- invKardex100: ['mes', 'kardex'] 
- invkardex102: ['mes', 'kardex'] 

### Tabla: invoct
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | DATETIME | ✓ |  |
| kardex | INTEGER |  |  |
| cantidad | DECIMAL(16, 6) |  |  |
| reservado | DECIMAL(16, 6) |  |  |
| cuarentena | DECIMAL(16, 6) |  |  |
| costo | DECIMAL(16, 6) |  |  |
| costoprom | DECIMAL(18, 6) |  |  |
| invkardex | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| invini | DECIMAL(16, 6) |  |  |
| qinvini | DECIMAL(16, 6) |  |  |
| compra | DECIMAL(16, 6) |  |  |
| qcompra | DECIMAL(16, 6) |  |  |
| otrosing | DECIMAL(16, 6) |  |  |
| qotrosing | DECIMAL(16, 6) |  |  |
| INGRESO | DECIMAL(16, 6) |  |  |
| SALIDA | DECIMAL(16, 6) |  |  |
| BONIF | DECIMAL(16, 6) |  |  |
| DEVOL | DECIMAL(16, 6) |  |  |
| VENTA | DECIMAL(16, 6) |  |  |
| INVFIN | DECIMAL(16, 6) |  |  |
| QINGRESO | DECIMAL(16, 6) |  |  |
| QSALIDA | DECIMAL(16, 6) |  |  |
| QBONIF | DECIMAL(16, 6) |  |  |
| QDEVOL | DECIMAL(16, 6) |  |  |
| QVENTA | DECIMAL(16, 6) |  |  |
| QINVFIN | DECIMAL(16, 6) |  |  |
| final | DECIMAL(18, 6) |  |  |
| producto | INTEGER | ✓ |  |

### Tabla: invpago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER |  |  |
| fecha | DATETIME |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| tarjeta | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cheque | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pcheque | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| acheque | NUMERIC(16, 6) |  |  |
| atarjeta | NUMERIC(16, 6) |  |  |
| aefectivo | NUMERIC(16, 6) |  |  |
| apcheque | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambi2 | NUMERIC(16, 6) |  |  |
| tasacambi3 | NUMERIC(16, 6) |  |  |
| invpago | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_invpago_cheque: ['cheque'] 
- IX_invpago_empresa: ['empresa'] 
- IX_invpago_factura: ['factura'] 
- IX_invpago_fecha: ['fecha'] 
- IX_invpago_invpago: ['invpago'] 
- IX_invpago_moneda: ['moneda'] 
- IX_invpago_pcheque: ['pcheque'] 
- IX_invpago_tarjeta: ['tarjeta'] 
- IX_invpago_usuario: ['usuario'] 

### Tabla: iva
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| niva | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| factor | NUMERIC(16, 6) |  |  |
| operador | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainicio | DATETIME | ✓ |  |
| fechafinal | DATETIME | ✓ |  |
| ivalocal | BIT |  |  |
| ivaexport | BIT |  |  |
| ivaimport | BIT |  |  |
| iva | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| tipovta | INTEGER |  |  |
| PERCEPCION | NUMERIC(18, 6) |  |  |
| pais | INTEGER |  |  |
| fseguridad | NUMERIC(2, 0) |  |  |

#### Índices
- IX_iva_empresa: ['empresa'] 
- IX_iva_iva: ['iva'] 
- IX_iva_niva: ['niva'] 
- IX_iva_operador: ['operador'] 
- IX_iva_tipovta: ['tipovta'] 
- IX_iva_usuario: ['usuario'] 

### Tabla: iva05
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| periodoiva | FLOAT | ✓ |  |
| fecha | DATETIME | ✓ |  |
| nocheque | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numedocu | FLOAT | ✓ |  |
| proveedor | FLOAT | ✓ |  |
| moneda | FLOAT | ✓ |  |
| afecta  | FLOAT | ✓ |  |
| importacion | FLOAT | ✓ |  |
| viva | FLOAT | ✓ |  |
| exenta | FLOAT | ✓ |  |
| retencion | FLOAT | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| usario | FLOAT | ✓ |  |
| otro | FLOAT | ✓ |  |
| fovial | FLOAT | ✓ |  |
| nproveedor | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nocuenta | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipobodega | FLOAT | ✓ |  |
| percepcion | FLOAT | ✓ |  |
| partida | FLOAT | ✓ |  |
| pagos | FLOAT | ✓ |  |
| compras | FLOAT | ✓ |  |

### Tabla: jornada
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| diurna | BIT |  |  |
| njornada | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horasjornada | NUMERIC(4, 2) |  |  |
| activo | BIT |  |  |
| jornada | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| MEDIA | BIT |  |  |
| INICIAHE | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tiempo | INTEGER | ✓ |  |
| codreloj | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| HELunes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSLunes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDLunes | INTEGER |  |  |
| HEMartes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSMartes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDMartes | INTEGER |  |  |
| HEMiercoles | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSMiercoles | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDMiercoles | INTEGER |  |  |
| HEJueves | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSJueves | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDJueves | INTEGER |  |  |
| HEViernes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSViernes | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDViernes | INTEGER |  |  |
| HESabado | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSSabado | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDSabado | INTEGER |  |  |
| HEDomingo | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| HSDomingo | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| TDDomigno | INTEGER |  |  |
| FactorHN | NUMERIC(18, 6) |  |  |
| FactorHE | NUMERIC(18, 6) |  |  |
| PeriodoGracia | NUMERIC(18, 6) |  |  |
| MinCalificaHE | NUMERIC(18, 6) |  |  |
| DuracionAlmuerzo | NUMERIC(18, 6) |  |  |
| ExcluirHoraAlmuerzo | BIT |  |  |
| TExtraAntesE | BIT |  |  |

#### Índices
- IX_jornada_empresa: ['empresa'] 
- IX_jornada_INICIAHE: ['INICIAHE'] 
- IX_jornada_jornada: ['jornada'] 
- IX_jornada_njornada: ['njornada'] 
- IX_jornada_usuario: ['usuario'] 

### Tabla: kardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| lote | INTEGER |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| reservado | NUMERIC(16, 6) |  |  |
| cuarentena | NUMERIC(16, 6) |  |  |
| fcantidad | NUMERIC(16, 6) |  |  |
| freservado | NUMERIC(16, 6) |  |  |
| fcuarentena | NUMERIC(16, 6) |  |  |
| ajuste | BIT |  |  |
| nota | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| kardex | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| preparaJornada | INTEGER |  |  |
| corridaA1 | INTEGER |  |  |
| corridaA2 | INTEGER |  |  |
| corridaA3 | INTEGER |  |  |
| corridaA4 | INTEGER |  |  |
| corridaA5 | INTEGER |  |  |
| corridaA6 | INTEGER |  |  |
| corridaA7 | INTEGER |  |  |
| corridaA8 | INTEGER |  |  |
| totalEscala | INTEGER |  |  |
| ocCantidad | NUMERIC(18, 6) |  |  |
| docompra | INTEGER |  |  |
| docompra1 | INTEGER |  |  |

#### Foreign Keys
- ['bodega'] → bodega.['bodega']
- ['lote'] → lote.['lote']
- ['producto'] → producto.['producto']

#### Índices
- IDX_2: ['empresa'] 
- IX_kardex_bodega: ['bodega'] 
- IX_kardex_empresa: ['empresa'] 
- IX_kardex_kardex: ['kardex'] 
- IX_kardex_lote: ['lote'] 
- IX_kardex_nota: ['nota'] 
- IX_kardex_producto: ['producto'] 
- IX_kardex_usuario: ['usuario'] 
- kardex_bodega: ['bodega'] 
- kardex_bodega_empresa: ['bodega', 'empresa'] 
- kardex_lote: ['lote'] 
- kardex1: ['cantidad'] 

### Tabla: kardex_caja
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| caja | INTEGER |  |  |
| kardex | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| kardex_caja | INTEGER |  | ✓ |

### Tabla: kclientes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| codigo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nclientes | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| email | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| propietario | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ncondpago | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nprodprec | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| contacto | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| direccion | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| razonsoc | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| registro | NVARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| giro | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nit | NVARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono1 | NVARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono2 | NVARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| limitecredito | FLOAT | ✓ |  |
| notas | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| retencion | BIT | ✓ |  |
| propio | INTEGER | ✓ |  |
| ExcluirCredito | INTEGER | ✓ |  |
| nvendedor | NVARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| condpago | INTEGER | ✓ |  |
| vendedor | INTEGER | ✓ |  |
| prodprec | INTEGER | ✓ |  |

### Tabla: kcodbarra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| codigo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codbarra | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: kcuenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nocuenta | INTEGER |  |  |
| nocheque | INTEGER | ✓ |  |
| miformato | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| banco | BIT |  |  |
| proveedor | BIT |  |  |
| provbol | BIT |  |  |
| iva | BIT |  |  |
| ret | TINYINT |  |  |
| Excl | TINYINT |  |  |
| Fovial | TINYINT |  |  |
| Renta | TINYINT |  |  |
| factor | FLOAT |  |  |
| debe | BIT |  |  |
| micheque | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| AplicaRete | TINYINT |  |  |
| REGISTRO | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| IMPORTACION | TINYINT |  |  |
| misformato | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cotrans | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| lineascheque | TINYINT |  |  |
| nit | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| giro | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| razonsoc | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| email | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| sitioweb | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| notas | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| direccion | NVARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PERCEPCION | BIT |  |  |
| CxCProveedor | TINYINT |  |  |
| cuentaCxC | TINYINT |  |  |
| deduccion1 | TINYINT |  |  |
| deduccion1_2 | TINYINT |  |  |
| deduccion2 | TINYINT |  |  |
| AplicaPercepcion | TINYINT |  |  |

### Tabla: kproducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tprecio | FLOAT |  |  |
| fprecio | FLOAT |  |  |
| precio | TINYINT |  |  |
| nprodprec | NVARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codigo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproducto | NVARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| prodprec | INTEGER | ✓ |  |
| producto | INTEGER | ✓ |  |

### Tabla: ldpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| cargo | NUMERIC(16, 6) |  |  |
| nula | BIT |  |  |
| abono | NUMERIC(16, 6) |  |  |
| hcargo | NUMERIC(16, 6) |  |  |
| habono | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| letras | INTEGER |  |  |
| pagos | INTEGER |  |  |
| dpagos | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| ldpagos | INTEGER |  | ✓ |

#### Índices
- IX_ldpagos_dpagos: ['dpagos'] 
- IX_ldpagos_empresa: ['empresa'] 
- IX_ldpagos_ldpagos: ['ldpagos'] 
- IX_ldpagos_letras: ['letras'] 
- IX_ldpagos_pagos: ['pagos'] 
- IX_ldpagos_usuario: ['usuario'] 

### Tabla: lecturabanco
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| datobanco | VARCHAR(140) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Lectura | VARCHAR(84) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FechaBanco | DATETIME | ✓ |  |
| fechaLectura | DATETIME | ✓ |  |
| MontoBanco | NUMERIC(18, 6) | ✓ |  |
| MontoLectura | NUMERIC(18, 6) | ✓ |  |
| Diferencia | NUMERIC(19, 6) | ✓ |  |
| carnet | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factura | INTEGER | ✓ |  |
| impresa | BIT | ✓ |  |
| pagos | INTEGER | ✓ |  |
| lecturabanco | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_lecturabanco_carnet: ['carnet'] 
- IX_lecturabanco_datobanco: ['datobanco'] 
- IX_lecturabanco_empresa: ['empresa'] 
- IX_lecturabanco_factura: ['factura'] 
- IX_lecturabanco_Lectura: ['Lectura'] 
- IX_lecturabanco_lecturabanco: ['lecturabanco'] 
- IX_lecturabanco_pagos: ['pagos'] 
- IX_lecturabanco_usuario: ['usuario'] 

### Tabla: lecturabodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| bodega | INTEGER |  |  |
| Producto | INTEGER |  |  |
| valor | NUMERIC(18, 6) |  |  |
| lecturavara | NUMERIC(18, 6) |  |  |
| galones | NUMERIC(18, 6) |  |  |
| LecturaBodega | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: lecturabomba
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| bomba | INTEGER |  |  |
| Producto | INTEGER |  |  |
| valor | NUMERIC(18, 6) |  |  |
| galones | NUMERIC(18, 6) |  |  |
| lecturaBomba | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: letras
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipomov | INTEGER |  |  |
| contrato | INTEGER |  |  |
| condpago | INTEGER |  |  |
| numedocu | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacanc | DATETIME | ✓ |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(18, 6) |  |  |
| viva | NUMERIC(18, 6) |  |  |
| hmontfact | NUMERIC(16, 6) |  |  |
| habono | NUMERIC(16, 6) |  |  |
| hcargo | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| cuotas | NUMERIC(16, 6) |  |  |
| moneda | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| vendedor | INTEGER |  |  |
| letras | INTEGER |  | ✓ |
| noletras | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| saldoanterior | NUMERIC(16, 6) |  |  |

#### Índices
- IX_letras_clientes: ['clientes'] 
- IX_letras_condpago: ['condpago'] 
- IX_letras_contrato: ['contrato'] 
- IX_letras_empresa: ['empresa'] 
- IX_letras_fecha: ['fecha'] 
- IX_letras_letras: ['letras'] 
- IX_letras_moneda: ['moneda'] 
- IX_letras_noletras: ['noletras'] 
- IX_letras_tipomov: ['tipomov'] 
- IX_letras_usuario: ['usuario'] 
- IX_letras_vendedor: ['vendedor'] 

### Tabla: lote
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fecvence | DATETIME | ✓ |  |
| fecingreso | DATETIME | ✓ |  |
| lote | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pureza | NUMERIC(18, 6) |  |  |
| TipoEscala | INTEGER |  |  |
| TotalEscala | INTEGER |  |  |
| resolucion | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| corridaA1 | INTEGER |  |  |
| corridaA2 | INTEGER |  |  |
| corridaA3 | INTEGER |  |  |
| corridaA4 | INTEGER |  |  |
| corridaA5 | INTEGER |  |  |
| corridaA6 | INTEGER |  |  |
| corridaA7 | INTEGER |  |  |
| corridaA8 | INTEGER |  |  |
| z1 | NUMERIC(5, 1) | ✓ |  |
| z2 | NUMERIC(5, 1) | ✓ |  |
| z3 | NUMERIC(5, 1) | ✓ |  |
| z4 | NUMERIC(5, 1) | ✓ |  |
| z5 | NUMERIC(5, 1) | ✓ |  |
| z6 | NUMERIC(5, 1) | ✓ |  |
| z7 | NUMERIC(5, 1) | ✓ |  |
| z8 | NUMERIC(5, 1) | ✓ |  |

#### Índices
- IX_lote_empresa: ['empresa'] 
- IX_lote_lote: ['lote'] 
- IX_lote_nolote: ['nolote'] 
- IX_lote_usuario: ['usuario'] 

### Tabla: lpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| impresa | BIT |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipomov | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| nula | BIT |  |  |
| iva | INTEGER |  |  |
| moneda | INTEGER |  |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| mora | NUMERIC(16, 6) |  |  |
| difcambio | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| pagos | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| lpagos | INTEGER |  | ✓ |
| condpago | INTEGER |  |  |

#### Índices
- IX_lpagos_clientes: ['clientes'] 
- IX_lpagos_condpago: ['condpago'] 
- IX_lpagos_empresa: ['empresa'] 
- IX_lpagos_fecha: ['fecha'] 
- IX_lpagos_iva: ['iva'] 
- IX_lpagos_lpagos: ['lpagos'] 
- IX_lpagos_moneda: ['moneda'] 
- IX_lpagos_notas: ['notas'] 
- IX_lpagos_pagos: ['pagos'] 
- IX_lpagos_referencia: ['referencia'] 
- IX_lpagos_tipomov: ['tipomov'] 
- IX_lpagos_usuario: ['usuario'] 
- IX_lpagos_vendedor: ['vendedor'] 

### Tabla: lpagosnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| lpagos | INTEGER |  |  |
| lpagosnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| impresa | BIT |  |  |

#### Índices
- IX_lpagosnula_empresa: ['empresa'] 
- IX_lpagosnula_fecha: ['fecha'] 
- IX_lpagosnula_lpagos: ['lpagos'] 
- IX_lpagosnula_lpagosnula: ['lpagosnula'] 
- IX_lpagosnula_motivo: ['motivo'] 
- IX_lpagosnula_usuario: ['usuario'] 

### Tabla: lpartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| concepto | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| nula | BIT |  |  |
| automatico | BIT |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| tipopart | INTEGER |  |  |
| partida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| debemont | NUMERIC(16, 6) |  |  |
| habermont | NUMERIC(16, 6) |  |  |
| fpartida | INTEGER |  |  |
| lpartida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_lpartida_concepto: ['concepto'] 
- IX_lpartida_empresa: ['empresa'] 
- IX_lpartida_fecha: ['fecha'] 
- IX_lpartida_fpartida: ['fpartida'] 
- IX_lpartida_lpartida: ['lpartida'] 
- IX_lpartida_moneda: ['moneda'] 
- IX_lpartida_partida: ['partida'] 
- IX_lpartida_tipopart: ['tipopart'] 
- IX_lpartida_usuario: ['usuario'] 

### Tabla: maestros
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tabla | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nombre | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ntabla | VARCHAR(210) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| acceso | INTEGER |  |  |
| crear | INTEGER |  |  |
| modificar | INTEGER |  |  |
| eliminar | INTEGER |  |  |
| imprimir | INTEGER |  |  |
| excel | INTEGER |  |  |
| reportes | INTEGER |  |  |
| modulo | INTEGER |  |  |
| maestros | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_maestros_acceso: ['acceso'] 
- IX_maestros_crear: ['crear'] 
- IX_maestros_eliminar: ['eliminar'] 
- IX_maestros_empresa: ['empresa'] 
- IX_maestros_excel: ['excel'] 
- IX_maestros_imprimir: ['imprimir'] 
- IX_maestros_maestros: ['maestros'] 
- IX_maestros_modificar: ['modificar'] 
- IX_maestros_modulo: ['modulo'] 
- IX_maestros_nombre: ['nombre'] 
- IX_maestros_ntabla: ['ntabla'] 
- IX_maestros_reportes: ['reportes'] 
- IX_maestros_tabla: ['tabla'] 
- IX_maestros_usuario: ['usuario'] 

### Tabla: marca
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmarca | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| marca | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_marca_empresa: ['empresa'] 
- IX_marca_marca: ['marca'] 
- IX_marca_nmarca: ['nmarca'] 
- IX_marca_usuario: ['usuario'] 

### Tabla: marcavehiculo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmarcavehiculo | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horatiempo | DATETIME |  |  |
| marcavehiculo | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

### Tabla: material
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmaterial | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| material | INTEGER |  | ✓ |
| producto | INTEGER | ✓ |  |
| cantidad | NUMERIC(16, 6) | ✓ |  |
| rupot | INTEGER | ✓ |  |
| precio1 | NUMERIC(18, 6) | ✓ |  |
| precio2 | NUMERIC(18, 6) | ✓ |  |
| precio3 | NUMERIC(18, 6) | ✓ |  |
| aprobado | INTEGER | ✓ |  |
| ocompra | INTEGER | ✓ |  |
| proveedor | INTEGER | ✓ |  |

### Tabla: mesCompleto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| meses | INTEGER |  |  |
| ano | INTEGER |  |  |
| D1 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D2 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D3 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D4 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D5 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D6 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D7 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D8 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D9 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D10 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D11 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D12 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D13 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D14 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D15 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D16 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D17 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D18 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D19 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D20 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D21 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D22 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D23 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D24 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D25 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D26 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D27 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D28 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D29 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D30 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| D31 | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| mescompleto | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: meses
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmes | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| meses | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_meses_empresa: ['empresa'] 
- IX_meses_meses: ['meses'] 
- IX_meses_nmes: ['nmes'] 
- IX_meses_usuario: ['usuario'] 

### Tabla: mform983
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| descripcion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| UnidadMedida | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| TotalUnidades | NUMERIC(18, 2) | ✓ |  |
| CostoNeto | NUMERIC(18, 6) | ✓ |  |
| CostoTotal | NUMERIC(18, 6) | ✓ |  |
| CategoriaBien | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ReferenciaLibros | VARCHAR(2) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| anio | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_mform983: ['descripcion'] 

### Tabla: mformprod
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| mformula | INTEGER |  |  |
| producto | INTEGER |  |  |
| mformprod | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| costo | BIT |  |  |
| tipogasto | BIT |  |  |

#### Índices
- IX_mformprod_empresa: ['empresa'] 
- IX_mformprod_mformprod: ['mformprod'] 
- IX_mformprod_mformula: ['mformula'] 
- IX_mformprod_producto: ['producto'] 
- IX_mformprod_usuario: ['usuario'] 

### Tabla: mformula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmformula | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cantidad | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| producto | INTEGER |  |  |
| pformula | INTEGER |  |  |
| mformula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_mformula_empresa: ['empresa'] 
- IX_mformula_mformula: ['mformula'] 
- IX_mformula_nmformula: ['nmformula'] 
- IX_mformula_pformula: ['pformula'] 
- IX_mformula_producto: ['producto'] 
- IX_mformula_usuario: ['usuario'] 

### Tabla: miAlmacenmov
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| idkardex | INTEGER | ✓ |  |
| dia | DATETIME | ✓ |  |
| TipoMovimiento | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Signo | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Documento | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Codigo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Producto | VARCHAR(160) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Bodega | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Lote | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cantidad | NUMERIC(18, 6) | ✓ |  |
| reservado | NUMERIC(18, 6) | ✓ |  |
| Revision | NUMERIC(18, 6) | ✓ |  |
| CostoPromedio | NUMERIC(18, 6) | ✓ |  |
| Fabricante | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Categoria | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| presentacion | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nTipoProd | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| factor | NUMERIC(18, 6) | ✓ |  |
| propio | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecvence | DATETIME | ✓ |  |
| empresa | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechadesde | DATETIME | ✓ |  |
| fechaHasta | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_miAlmacenmov: ['idkardex'] 

### Tabla: miCartera
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| VENDEDOR | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CODIGOCLIENTE | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CLIENTE | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FECHA | DATETIME | ✓ |  |
| DOCUMENTO | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| monto | NUMERIC(18, 6) | ✓ |  |
| saldonormal | NUMERIC(18, 6) | ✓ |  |
| saldo30 | NUMERIC(18, 6) | ✓ |  |
| saldo60 | NUMERIC(18, 6) | ✓ |  |
| saldo90 | NUMERIC(18, 6) | ✓ |  |
| saldo120 | NUMERIC(18, 6) | ✓ |  |
| saldom120 | NUMERIC(18, 6) | ✓ |  |
| saldo | NUMERIC(18, 6) | ✓ |  |
| Telefono | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Municip | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| LimiteCredito | NUMERIC(18, 6) | ✓ |  |
| vencida | INTEGER | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_miCartera: ['vencida'] 

### Tabla: mibaseflujo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| anio | INTEGER |  |  |
| mes | INTEGER |  |  |
| Mayorno | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| MayorNombre | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| concepto | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| monto | NUMERIC(18, 6) | ✓ |  |
| grupo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| gruponombre | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empresa_ | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| ejecutado | NUMERIC(18, 6) |  |  |
| proyectado | NUMERIC(18, 6) |  |  |

#### Índices
- IX_mibaseflujo: ['anio', 'mes', 'Mayorno'] 

### Tabla: micolor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| micolor | INTEGER |  | ✓ |
| nmicolor | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Descripcion | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| codigocolor | INTEGER |  |  |
| codigoRGB | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codR | VARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codG | VARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codB | VARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: midia
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| mes | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| semana | INTEGER |  |  |
| midia | INTEGER |  | ✓ |

### Tabla: midsemana
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Domingo | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Lunes | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Martes | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Miercoles | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Jueves | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Viernes | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Sabado | NCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| midsemana | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: miempleado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| codigo | INTEGER | ✓ |  |
| Nombres | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Apellidos | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Nombre según ISSS | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Dirección | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Tel casa/movil | NUMERIC(18, 0) | ✓ |  |
| Tel Movil | NUMERIC(18, 0) | ✓ |  |
| Tipo Sangre | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Sexo | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Nacionalidad | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Profesión | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Lugar Nac | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Email | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Fecha Ingreso | DATETIME | ✓ |  |
| Fecha Vcto | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Departamento | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Cargo | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Jornada | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Plaza | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Salario Mes | MONEY | ✓ |  |
| Fma Pago | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| No# ISSS | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| AFP | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| No AFP | NUMERIC(18, 0) | ✓ |  |
| DUI | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| NIT | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PASAPORTE | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_miempleado_codigo: ['codigo'] 

### Tabla: mifecha
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | SMALLDATETIME |  |  |
| mifecha | INTEGER |  | ✓ |

#### Índices
- IX_mifecha_fecha: ['fecha'] 
- IX_mifecha_mifecha: ['mifecha'] 

### Tabla: mikardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| kardex | INTEGER |  |  |
| nproducto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| producto | INTEGER |  |  |
| bodega | INTEGER |  |  |
| ini | NUMERIC(16, 6) |  |  |
| compra | NUMERIC(16, 6) |  |  |
| ing | NUMERIC(16, 6) |  |  |
| vent | NUMERIC(16, 6) |  |  |
| bonif | NUMERIC(16, 6) |  |  |
| out | NUMERIC(16, 6) |  |  |
| devo | NUMERIC(16, 6) |  |  |
| exist | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| vexi | NUMERIC(16, 6) |  |  |
| ncasa | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| npresenta | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ncategori | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nbodega | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ntipoprod | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| mikardex | INTEGER |  | ✓ |

#### Índices
- IX_mikardex_bodega: ['bodega'] 
- IX_mikardex_codbarra: ['codbarra'] 
- IX_mikardex_icdbarra: ['icdbarra'] 
- IX_mikardex_kardex: ['kardex'] 
- IX_mikardex_mikardex: ['mikardex'] 
- IX_mikardex_nbodega: ['nbodega'] 
- IX_mikardex_ncasa: ['ncasa'] 
- IX_mikardex_ncategori: ['ncategori'] 
- IX_mikardex_npresenta: ['npresenta'] 
- IX_mikardex_nproducto: ['nproducto'] 
- IX_mikardex_ntipoprod: ['ntipoprod'] 
- IX_mikardex_producto: ['producto'] 

### Tabla: miplan
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| miplan | INTEGER |  | ✓ |
| misfinanzas | INTEGER | ✓ |  |
| tipoPrograma | INTEGER | ✓ |  |
| dia | INTEGER | ✓ |  |
| mes | INTEGER | ✓ |  |
| vigente | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

#### Foreign Keys
- ['misfinanzas'] → misfinanzas.['misfinanzas']

### Tabla: miprecio
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dprodprec | INTEGER | ✓ |  |
| producto | INTEGER | ✓ |  |
| prodprec | INTEGER | ✓ |  |
| tprecio | NUMERIC(18, 6) | ✓ |  |
| fprecio | NUMERIC(18, 6) | ✓ |  |

### Tabla: misVentas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipoVenta | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dia | DATETIME | ✓ |  |
| codigoCliente | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| TipoCliente | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Cliente | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Pais | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Sucursal | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Departamento | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Provincia_Municipio | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipovendedor | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CodigoVendedor | INTEGER | ✓ |  |
| Vendedor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CodigoProducto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Producto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ProductoPropio | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| TipoProducto | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PresentacionProducto | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FactorPresentacionProducto | NUMERIC(18, 6) | ✓ |  |
| CategoriaProducto | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CasaProducto | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Bodega | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| loteProducto | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| diasCredito | NUMERIC(18, 6) | ✓ |  |
| condicionPago | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| FormaPago | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Unidadvendida | NUMERIC(18, 6) | ✓ |  |
| UnidadDevolucion | NUMERIC(18, 6) | ✓ |  |
| Unidadbonificada | NUMERIC(18, 6) | ✓ |  |
| UnidadDevolucionBonificada | NUMERIC(18, 6) | ✓ |  |
| ventaNeta | NUMERIC(18, 6) | ✓ |  |
| ventaNetaDevolucion | NUMERIC(18, 6) | ✓ |  |
| ImpuestoVenta | NUMERIC(18, 6) | ✓ |  |
| ImpuestoVentaDevolucion | NUMERIC(18, 6) | ✓ |  |
| NotaCreditoxPrecio | NUMERIC(18, 6) | ✓ |  |
| VentaNeta_NCPrecio | NUMERIC(18, 6) | ✓ |  |
| CostoUnitarioVenta | NUMERIC(18, 6) | ✓ |  |
| PrecioVenta | NUMERIC(18, 6) | ✓ |  |
| ListaPrecios | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| id | INTEGER | ✓ |  |
| NumeroDocumento | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| existencia | NUMERIC(18, 6) | ✓ |  |
| lotevence | DATETIME | ✓ |  |
| unidadGratificada | NUMERIC(18, 6) | ✓ |  |
| descuentoGratificado | NUMERIC(18, 6) | ✓ |  |
| descuento | NUMERIC(18, 6) | ✓ |  |
| unidadBonificadaProveedor | NUMERIC(18, 6) | ✓ |  |
| descuentoProveedor | NUMERIC(18, 6) | ✓ |  |
| fechadesde | DATETIME | ✓ |  |
| fechahasta | DATETIME | ✓ |  |
| VentaBruta | NUMERIC(18, 6) | ✓ |  |
| VentaBonficada | NUMERIC(18, 6) | ✓ |  |
| VentaGratificada | NUMERIC(18, 6) | ✓ |  |
| VentaBonificadaProveedor | NUMERIC(18, 6) | ✓ |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| razonsocial | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| propietario | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Conglomerado | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| costoventa | NUMERIC(18, 6) |  |  |
| Margenventa | NUMERIC(18, 6) |  |  |
| PrecioFinalventa | NUMERIC(18, 6) |  |  |
| kardex | INTEGER |  |  |
| exhibidor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- misventas: ['dia', 'codigoCliente'] 

### Tabla: miscompras
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| TipoCompra | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dia | DATETIME | ✓ |  |
| CodigoProveedor | INTEGER | ✓ |  |
| CodigoProducto | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Producto | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Propio | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Presentacion | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Factor | NUMERIC(18, 6) | ✓ |  |
| Bodega | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Lote | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CantidadCompra | NUMERIC(18, 6) | ✓ |  |
| DevolucionCompra | NUMERIC(18, 6) | ✓ |  |
| Bonificacion | NUMERIC(18, 6) | ✓ |  |
| DevolucionBonificacion | NUMERIC(18, 6) | ✓ |  |
| idKardex | INTEGER | ✓ |  |
| CompraNeta | NUMERIC(18, 6) | ✓ |  |
| CompraBruta | NUMERIC(18, 6) | ✓ |  |
| Factor1 | NUMERIC(18, 6) | ✓ |  |
| Factor2 | NUMERIC(18, 6) | ✓ |  |
| Factor3 | NUMERIC(18, 6) | ✓ |  |
| NCxPrecio | NUMERIC(18, 6) | ✓ |  |
| PrecioCompra | NUMERIC(18, 6) | ✓ |  |
| EncargadoCompra | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| TipoProveedor | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Registro | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Proveedor | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Plazo | INTEGER | ✓ |  |
| CompraContado | BIT | ✓ |  |
| Pais | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Departamento | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Municipio | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| TipoProducto | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CasaProducto | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| CategoriaProducto | VARCHAR(90) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| gastos | NUMERIC(18, 6) | ✓ |  |
| aranceles | NUMERIC(18, 6) | ✓ |  |
| OtrosValores | NUMERIC(18, 6) | ✓ |  |
| CostoCompra | NUMERIC(18, 6) | ✓ |  |
| costoPromedio | NUMERIC(18, 6) | ✓ |  |
| fecvence | DATETIME | ✓ |  |
| empresa | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechadesde | DATETIME | ✓ |  |
| fechaHasta | DATETIME | ✓ |  |
| CostoUnitarioCompra | NUMERIC(18, 6) |  |  |

#### Índices
- ci_azure_fixup_dbo_miscompras: ['CodigoProveedor'] 

### Tabla: misfinanzas
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| misfinanzas | INTEGER |  | ✓ |
| TipoCargo | INTEGER | ✓ |  |
| fecha | DATETIME |  |  |
| documento | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| monto | NUMERIC(9, 2) | ✓ |  |
| cargo | NUMERIC(9, 2) | ✓ |  |
| abono | NUMERIC(9, 2) | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| impresa | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| pagada | BIT | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

#### Foreign Keys
- ['TipoCargo'] → TipoCargo.['TipoCargo']

### Tabla: misnopagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| invcliente | INTEGER |  |  |
| factura_a | INTEGER |  |  |
| factura_b | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factfecha | DATETIME | ✓ |  |
| montfact | NUMERIC(15, 6) |  |  |
| abono | NUMERIC(15, 6) |  |  |
| cargo | NUMERIC(15, 6) |  |  |
| saldo | NUMERIC(17, 6) |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pagos | INTEGER |  |  |
| fecha | SMALLDATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipomov | INTEGER |  |  |
| ntipomov | CHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| misabonos | NUMERIC(15, 6) |  |  |
| miscargos | NUMERIC(15, 6) |  |  |
| dpagos | INTEGER |  |  |

#### Índices
- IX_misnopagos_clientes: ['clientes'] 
- IX_misnopagos_dpagos: ['dpagos'] 
- IX_misnopagos_factura_a: ['factura_a'] 
- IX_misnopagos_fecha: ['fecha'] 
- IX_misnopagos_invcliente: ['invcliente'] 
- IX_misnopagos_pagos: ['pagos'] 
- IX_misnopagos_tipomov: ['tipomov'] 

### Tabla: mispagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mispagos | INTEGER |  | ✓ |
| misFinanzas | INTEGER | ✓ |  |
| doctipo | INTEGER | ✓ |  |
| fechaPago | DATETIME | ✓ |  |
| fechaPlan | DATETIME |  |  |
| documento | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cargo | NUMERIC(9, 2) | ✓ |  |
| abono | NUMERIC(9, 2) | ✓ |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| impresa | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

#### Foreign Keys
- ['misFinanzas'] → misfinanzas.['misfinanzas']

### Tabla: modulo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmodulo | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| contabilidad | BIT |  |  |
| integracion | BIT |  |  |
| ventas | BIT |  |  |
| facturacion | BIT |  |  |
| planilla | BIT |  |  |
| produccion | BIT |  |  |
| ctascobrar | BIT |  |  |
| ctaspagar | BIT |  |  |
| compras | BIT |  |  |
| bancos | BIT |  |  |
| almacen | BIT |  |  |
| gerencia | BIT |  |  |
| manttogral | BIT |  |  |
| iva | BIT |  |  |
| enlace | BIT |  |  |
| controlproy | BIT |  |  |
| recons | BIT |  |  |
| cotiza | BIT |  |  |
| modulo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| formulacion | BIT |  |  |
| mismanttos | BIT |  |  |
| controlCarga | BIT |  |  |
| manttosadmin | BIT |  |  |
| controlvence | BIT |  |  |
| controlhacienda | BIT |  |  |
| CONTROLMEDIOS | BIT |  |  |
| gestiontaller | INTEGER |  |  |
| cocinabar | BIT |  |  |
| activofijo | BIT |  |  |

#### Índices
- IX_modulo_empresa: ['empresa'] 
- IX_modulo_modulo: ['modulo'] 
- IX_modulo_nmodulo: ['nmodulo'] 
- IX_modulo_usuario: ['usuario'] 

### Tabla: moneda
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmoneda | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| simmoneda | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| principal | BIT |  |  |
| segunda | BIT |  |  |
| tercera | BIT |  |  |
| activo | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| moneda | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_moneda_empresa: ['empresa'] 
- IX_moneda_moneda: ['moneda'] 
- IX_moneda_nmoneda: ['nmoneda'] 
- IX_moneda_simmoneda: ['simmoneda'] 
- IX_moneda_usuario: ['usuario'] 

### Tabla: motorista
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmotorista | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ordenNumero | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| motorista | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| telefono | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| licencia | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| carnet | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nacionalidad | INTEGER |  |  |
| empleado | INTEGER |  |  |
| codaduanero | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: movimiento
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| movimiento | INTEGER |  | ✓ |
| nmovimiento | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: movkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| kardex | INTEGER |  |  |
| producto | INTEGER |  |  |
| nproducto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sgn | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| ntipomov | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nbodega | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| lote | INTEGER |  |  |
| nolote | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| doc | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| aus | NUMERIC(16, 6) |  |  |
| avs | NUMERIC(16, 6) |  |  |
| ui | NUMERIC(16, 6) |  |  |
| uo | NUMERIC(16, 6) |  |  |
| us | NUMERIC(16, 6) |  |  |
| vi | NUMERIC(16, 6) |  |  |
| vo | NUMERIC(16, 6) |  |  |
| vs | NUMERIC(16, 6) |  |  |
| vc | NUMERIC(16, 6) |  |  |
| vcp | NUMERIC(16, 6) |  |  |
| cpra | BIT |  |  |
| cod | INTEGER |  |  |
| movkardex | INTEGER |  | ✓ |

#### Índices
- IX_movkardex_bodega: ['bodega'] 
- IX_movkardex_cod: ['cod'] 
- IX_movkardex_doc: ['doc'] 
- IX_movkardex_fecha: ['fecha'] 
- IX_movkardex_icdbarra: ['icdbarra'] 
- IX_movkardex_kardex: ['kardex'] 
- IX_movkardex_lote: ['lote'] 
- IX_movkardex_movkardex: ['movkardex'] 
- IX_movkardex_nbodega: ['nbodega'] 
- IX_movkardex_nolote: ['nolote'] 
- IX_movkardex_nproducto: ['nproducto'] 
- IX_movkardex_ntipomov: ['ntipomov'] 
- IX_movkardex_producto: ['producto'] 
- IX_movkardex_sgn: ['sgn'] 

### Tabla: municip
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmunicip | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| depto | INTEGER |  |  |
| municip | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| codigo | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Foreign Keys
- ['depto'] → depto.['depto']

#### Índices
- IX_municip_depto: ['depto'] 
- IX_municip_empresa: ['empresa'] 
- IX_municip_municip: ['municip'] 
- IX_municip_nmunicip: ['nmunicip'] 
- IX_municip_usuario: ['usuario'] 

### Tabla: nacional
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nnacional | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| nacional | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| codigoPais | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_nacional_empresa: ['empresa'] 
- IX_nacional_nacional: ['nacional'] 
- IX_nacional_nnacional: ['nnacional'] 
- IX_nacional_usuario: ['usuario'] 

### Tabla: ncpedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pedido | INTEGER |  |  |
| ncpedido | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: ncv
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pagos | INTEGER |  |  |
| dfactura | INTEGER |  |  |
| ncmonto | NUMERIC(16, 6) |  |  |
| ncafecta | NUMERIC(16, 6) |  |  |
| ncexenta | NUMERIC(16, 6) |  |  |
| ncviva | NUMERIC(16, 6) |  |  |
| ncv | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| qlinea | INTEGER |  |  |

#### Índices
- IX_ncv_dfactura: ['dfactura'] 
- IX_ncv_empresa: ['empresa'] 
- IX_ncv_ncv: ['ncv'] 
- IX_ncv_pagos: ['pagos'] 
- IX_ncv_usuario: ['usuario'] 

### Tabla: nivel
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nnivel | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipo | INTEGER |  |  |
| nota | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nivel | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_nivel_empresa: ['empresa'] 
- IX_nivel_nivel: ['nivel'] 
- IX_nivel_nnivel: ['nnivel'] 
- IX_nivel_nota: ['nota'] 
- IX_nivel_tipo: ['tipo'] 
- IX_nivel_usuario: ['usuario'] 

### Tabla: nmicontrol
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nmicontrol | INTEGER |  |  |
| clave | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| nconn | INTEGER |  |  |
| naut | INTEGER |  |  |
| ntiempo | DATETIME |  |  |

#### Índices
- ci_azure_fixup_dbo_nmicontrol: ['nmicontrol'] 
- IX_nmicontrol_clave: ['clave'] 
- IX_nmicontrol_empresa: ['empresa'] 
- IX_nmicontrol_naut: ['naut'] 
- IX_nmicontrol_nconn: ['nconn'] 
- IX_nmicontrol_nmicontrol: ['nmicontrol'] 
- IX_nmicontrol_usuario: ['usuario'] 

### Tabla: nochpedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pedido | INTEGER |  |  |
| nochpedido | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: nocpedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| concepto | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| pedido | INTEGER |  |  |
| nocpedido | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_nocpedido_concepto: ['concepto'] 
- IX_nocpedido_empresa: ['empresa'] 
- IX_nocpedido_nocpedido: ['nocpedido'] 
- IX_nocpedido_pedido: ['pedido'] 
- IX_nocpedido_usuario: ['usuario'] 

### Tabla: nominacliente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| cliencatego | INTEGER |  |  |
| nominacliente | INTEGER |  |  |
| invcliente | INTEGER |  |  |
| consumo | NUMERIC(18, 6) |  |  |
| cuotas | NUMERIC(18, 6) |  |  |
| pago | NUMERIC(18, 6) |  |  |
| liquidado | BIT |  |  |
| presentada | BIT |  |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| fechapago | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nopago | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nofactura | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pagos | INTEGER |  |  |

### Tabla: nopedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| pedido | INTEGER |  |  |
| nopedido | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| lotengo | BIT |  |  |
| caja | INTEGER |  |  |

#### Índices
- IX_nopedido_empresa: ['empresa'] 
- IX_nopedido_nopedido: ['nopedido'] 
- IX_nopedido_pedido: ['pedido'] 
- IX_nopedido_usuario: ['usuario'] 

### Tabla: ocompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| impresa | BIT |  |  |
| enfirme | BIT |  |  |
| contabilidad | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| tipovta | INTEGER |  |  |
| encompra | INTEGER |  |  |
| proveedor | INTEGER |  |  |
| proveedor2 | INTEGER |  |  |
| condpago | INTEGER |  |  |
| iva | INTEGER |  |  |
| cprodprec | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| tax | NUMERIC(16, 6) |  |  |
| descuentos | NUMERIC(16, 6) |  |  |
| descaplica | BIT |  |  |
| flete | NUMERIC(16, 6) |  |  |
| fob | NUMERIC(16, 6) |  |  |
| seguro | NUMERIC(16, 6) |  |  |
| monto | NUMERIC(16, 6) |  |  |
| montcomp | NUMERIC(16, 6) |  |  |
| montgasto | NUMERIC(16, 6) |  |  |
| montbonif | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| notas | VARCHAR(400) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ocompra | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| rfecha | DATETIME | ✓ |  |
| rnumedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| compra | INTEGER |  |  |
| rmontcomp | NUMERIC(16, 6) |  |  |
| pagada | BIT |  |  |
| pfecha | DATETIME | ✓ |  |
| proyecto | INTEGER |  |  |
| caja | INTEGER |  |  |
| bodega | INTEGER |  |  |
| fechaDespacho | DATETIME | ✓ |  |
| fechaRecepcion | DATETIME | ✓ |  |
| retencion | NUMERIC(18, 6) |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| contenedor | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vcartacredito | NUMERIC(18, 6) |  |  |
| vpagocredito | NUMERIC(18, 6) |  |  |
| vpagocontado | NUMERIC(18, 6) |  |  |
| vdeposito | NUMERIC(18, 6) |  |  |
| cartacredito | BIT |  |  |
| pagocredito | BIT |  |  |
| pagocontado | BIT |  |  |
| deposito | BIT |  |  |
| notasPago | VARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| transpte | INTEGER |  |  |
| embarque | INTEGER |  |  |
| cembarque | INTEGER |  |  |
| pdesc1 | NUMERIC(5, 2) |  |  |
| pdesc2 | NUMERIC(5, 2) |  |  |
| pdesc3 | NUMERIC(5, 2) |  |  |
| pdesc4 | NUMERIC(5, 2) |  |  |
| pdesc5 | NUMERIC(5, 2) |  |  |
| pdesc6 | NUMERIC(5, 2) |  |  |
| cuota1 | NUMERIC(18, 6) |  |  |
| cuota2 | NUMERIC(18, 6) |  |  |
| cuota3 | NUMERIC(18, 6) |  |  |
| carta | NUMERIC(18, 6) |  |  |
| cartaCred | NUMERIC(18, 6) |  |  |
| otra | NUMERIC(18, 6) |  |  |
| fdevolucion1 | DATETIME | ✓ |  |
| fdevolucion2 | DATETIME | ✓ |  |
| fdevolucion3 | DATETIME | ✓ |  |
| fdevolucion4 | DATETIME | ✓ |  |
| fdevolucion5 | DATETIME | ✓ |  |
| fentrega1 | DATETIME | ✓ |  |
| fentrega2 | DATETIME | ✓ |  |
| fentrega3 | DATETIME | ✓ |  |
| fentrega4 | DATETIME | ✓ |  |
| fentrega5 | DATETIME | ✓ |  |
| micaja1 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| micaja2 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| loadingcontainer | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| billloading | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| containerno | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| marchamo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| loadingPort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| DischargePort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| DeliveryPort | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hechoen | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| deliveryterms | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ctracking | INTEGER |  |  |
| doccompra | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechacompra | DATETIME | ✓ |  |
| recinto | BIT |  |  |
| metros3 | NUMERIC(18, 6) |  |  |
| metros3p | NUMERIC(18, 6) |  |  |
| fecharecinto | DATETIME | ✓ |  |
| impuesto | NUMERIC(18, 6) |  |  |
| impuestop | NUMERIC(18, 6) |  |  |
| arancel | NUMERIC(18, 6) |  |  |
| arancelp | NUMERIC(18, 6) |  |  |
| cif | NUMERIC(18, 6) |  |  |
| montoiva | NUMERIC(18, 6) |  |  |
| polisa | INTEGER |  |  |
| ndeposito | INTEGER |  |  |
| recintofiscal | INTEGER |  |  |
| poliza | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_ocompra_compra: ['compra'] 
- IX_ocompra_condpago: ['condpago'] 
- IX_ocompra_cprodprec: ['cprodprec'] 
- IX_ocompra_empresa: ['empresa'] 
- IX_ocompra_encompra: ['encompra'] 
- IX_ocompra_fecha: ['fecha'] 
- IX_ocompra_iva: ['iva'] 
- IX_ocompra_moneda: ['moneda'] 
- IX_ocompra_notas: ['notas'] 
- IX_ocompra_ocompra: ['ocompra'] 
- IX_ocompra_pedido: ['pedido'] 
- IX_ocompra_proveedor: ['proveedor'] 
- IX_ocompra_proveedor2: ['proveedor2'] 
- IX_ocompra_proyecto: ['proyecto'] 
- IX_ocompra_rnumedocu: ['rnumedocu'] 
- IX_ocompra_tipomov: ['tipomov'] 
- IX_ocompra_tipovta: ['tipovta'] 
- IX_ocompra_usuario: ['usuario'] 

### Tabla: ocomprafirme
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ocomprafirme | INTEGER |  | ✓ |
| docompra | INTEGER | ✓ |  |
| opagada | INTEGER | ✓ |  |
| cantidad | NUMERIC(12, 2) | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: ofactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| cancelada | BIT |  |  |
| impbod | BIT |  |  |
| impresa | BIT |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| comentario | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| expcomen | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacanc | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| iva | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipovta | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| factoriva | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| ofactura | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| pesoofactura | NUMERIC(16, 6) |  |  |
| pagos | INTEGER |  |  |
| basesiniva | BIT |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| efectivo | NUMERIC(16, 6) |  |  |
| cheque | NUMERIC(16, 6) |  |  |
| tarjeta | NUMERIC(16, 6) |  |  |
| nocheque | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notarjeta | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| caja | INTEGER |  |  |
| combustible | NUMERIC(18, 6) |  |  |
| encomienda | NUMERIC(18, 6) |  |  |
| ivaCombustible | NUMERIC(18, 6) |  |  |
| ivaencomienda | NUMERIC(18, 6) |  |  |
| Cotrans | NUMERIC(16, 8) |  |  |
| fechafin | DATETIME | ✓ |  |
| estado | INTEGER |  |  |
| prioridad | INTEGER |  |  |
| terminado | BIT |  |  |
| turno | INTEGER |  |  |
| rliquida | INTEGER |  |  |
| aprobado | BIT |  |  |
| impempaque | BIT |  |  |
| impvineta | BIT |  |  |
| vineta | INTEGER |  |  |
| enfirme | BIT |  |  |
| dgratif | NUMERIC(18, 6) |  |  |
| tipopago | INTEGER |  |  |
| bnotas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cobrador | INTEGER |  |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| concaja | BIT |  |  |
| clientes2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pais | INTEGER |  |  |
| pagencia | NUMERIC(5, 2) |  |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| ordenno | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nombreref | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| docref | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| camion | INTEGER |  |  |
| ofacturaReferencia | BIGINT |  |  |
| enruta | BIT |  |  |
| anulada | BIT |  |  |
| propina | NUMERIC(18, 6) |  |  |
| nopropina | BIT |  |  |
| mesa | BIT |  |  |
| nomesa | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nclientes | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Descautorizado | NUMERIC(18, 2) |  |  |
| fechaEntrega | DATETIME |  |  |
| entregas | INTEGER |  |  |
| showroom | BIT |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['iva'] → iva.['iva']
- ['tipomov'] → tipomov.['tipomov']
- ['vendedor'] → vendedor.['vendedor']

### Tabla: office
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| licencias | INTEGER | ✓ |  |
| noffice | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| horatiempo | DATETIME |  |  |
| office | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| email | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| col1 | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Col2 | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: oldprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| preciopublico | NUMERIC(16, 6) |  |  |
| nvoprecio | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| producto | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| oldprec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_oldprec_empresa: ['empresa'] 
- IX_oldprec_fecha: ['fecha'] 
- IX_oldprec_oldprec: ['oldprec'] 
- IX_oldprec_prodprec: ['prodprec'] 
- IX_oldprec_producto: ['producto'] 
- IX_oldprec_usuario: ['usuario'] 

### Tabla: ordenFormula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ordenFormula | INTEGER |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| porcprecio | NUMERIC(18, 6) |  |  |
| porccosto | NUMERIC(18, 6) |  |  |
| concentracion | NUMERIC(18, 6) |  |  |
| factor | NUMERIC(18, 6) |  |  |
| producto | INTEGER |  |  |
| ordentrabajo | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_ordenFormula: ['ordenFormula'] 

### Tabla: order
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| order_id | INTEGER |  | ✓ |
| user_id | INTEGER | ✓ |  |
| order_date | DATETIME | ✓ |  |
| ready_date | DATETIME | ✓ |  |
| status | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: order_detail
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| order_detial_id | INTEGER |  | ✓ |
| order_id | INTEGER | ✓ |  |
| product_id | INTEGER | ✓ |  |
| quantity | FLOAT | ✓ |  |
| unit_price | FLOAT | ✓ |  |
| empresa | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: oventa
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| impresa | BIT |  |  |
| enfirme | BIT |  |  |
| contabilidad | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| tipovta | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| proveedor | INTEGER |  |  |
| proveedor2 | INTEGER |  |  |
| condpago | INTEGER |  |  |
| iva | INTEGER |  |  |
| cprodprec | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| tax | NUMERIC(16, 6) |  |  |
| descuentos | NUMERIC(16, 6) |  |  |
| descaplica | BIT |  |  |
| flete | NUMERIC(16, 6) |  |  |
| fob | NUMERIC(16, 6) |  |  |
| seguro | NUMERIC(16, 6) |  |  |
| monto | NUMERIC(16, 6) |  |  |
| montcomp | NUMERIC(16, 6) |  |  |
| montgasto | NUMERIC(16, 6) |  |  |
| montbonif | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| notas | VARCHAR(400) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| oventa | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| rfecha | DATETIME | ✓ |  |
| rnumedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| venta | INTEGER |  |  |
| rmontcomp | NUMERIC(16, 6) |  |  |
| pagada | BIT |  |  |
| pfecha | DATETIME | ✓ |  |
| proyecto | INTEGER |  |  |
| caja | INTEGER |  |  |
| bodega | INTEGER |  |  |
| fechaDespacho | DATETIME | ✓ |  |
| fechaRecepcion | DATETIME | ✓ |  |
| retencion | NUMERIC(18, 6) |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nclientes | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipopedido | INTEGER |  |  |
| datoscliente | VARCHAR(450) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factura | INTEGER |  |  |
| basesinimpuesto | BIT |  |  |
| nosujeto | NUMERIC(12, 2) |  |  |
| dgratif | NUMERIC(12, 2) |  |  |

#### Índices
- IX_oventa_oventa: ['oventa'] 

### Tabla: pEntrega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pEntrega | INTEGER |  |  |
| fecha | DATETIME |  |  |
| concepto | INTEGER |  |  |
| Distrito | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_pEntrega: ['pEntrega'] 

### Tabla: pagocomision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| CodVendedor | INTEGER |  |  |
| vendedor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| VentaEfectivo | NUMERIC(18, 6) |  |  |
| VentaCredito | NUMERIC(18, 6) |  |  |
| recuperacion | NUMERIC(18, 6) |  |  |
| FactorComision | NUMERIC(6, 4) |  |  |
| Comision | NUMERIC(18, 6) |  |  |
| ajusteComision | NUMERIC(18, 6) |  |  |
| antiguedad | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| pagocomision | INTEGER |  | ✓ |
| tipomov | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numedocu | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechadoc | DATETIME | ✓ |  |
| clientes | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fechacan | DATETIME | ✓ |  |

### Tabla: pagocompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pagocompra | INTEGER |  | ✓ |
| npagocompra | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Fecha | DATETIME |  |  |
| monto | NUMERIC(18, 6) |  |  |
| factor | NUMERIC(18, 6) |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(18, 6) |  |  |
| ocompra | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: pagom3
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pagom3 | INTEGER |  | ✓ |
| ocompra | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| montom3 | NUMERIC(18, 6) | ✓ |  |
| monto | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: pagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| contabilidad | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| difcambio | NUMERIC(16, 6) |  |  |
| mora | NUMERIC(16, 6) |  |  |
| pagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| iva | INTEGER |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| caja | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipopago | INTEGER |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| rutacobro | INTEGER |  |  |
| ENFIRME | BIT |  |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| autopago | BIT |  |  |
| factura | INTEGER |  |  |
| referenciapagos | INTEGER |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['tipomov'] → tipomov.['tipomov']
- ['vendedor'] → vendedor.['vendedor']

#### Índices
- IX_pagos_caja: ['caja'] 
- IX_pagos_clientes: ['clientes'] 
- IX_pagos_condpago: ['condpago'] 
- IX_pagos_empresa: ['empresa'] 
- IX_pagos_fecha: ['fecha'] 
- IX_pagos_iva: ['iva'] 
- IX_pagos_moneda: ['moneda'] 
- IX_pagos_notas: ['notas'] 
- IX_pagos_pagos: ['pagos'] 
- IX_pagos_referencia: ['referencia'] 
- IX_pagos_tipomov: ['tipomov'] 
- IX_pagos_usuario: ['usuario'] 
- IX_pagos_vendedor: ['vendedor'] 
- pagos_empresa_autopago_fecha: ['empresa', 'autopago', 'fecha'] 

### Tabla: pagosnula
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| motivo | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| pagos | INTEGER |  |  |
| pagosnula | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['pagos'] → pagos.['pagos']

#### Índices
- IX_pagosnula_empresa: ['empresa'] 
- IX_pagosnula_fecha: ['fecha'] 
- IX_pagosnula_motivo: ['motivo'] 
- IX_pagosnula_pagos: ['pagos'] 
- IX_pagosnula_pagosnula: ['pagosnula'] 
- IX_pagosnula_usuario: ['usuario'] 

### Tabla: pais
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npais | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| preferido | BIT |  |  |
| pais | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| NACIONAL | INTEGER |  |  |
| ElSalvador | BIT |  |  |
| Guatemala | BIT |  |  |
| Honduras | BIT |  |  |
| Costarica | BIT |  |  |
| Panama | BIT |  |  |
| Nicaragua | BIT |  |  |
| EstadosUnidos | BIT |  |  |
| Mexico | BIT |  |  |
| Chile | BIT |  |  |
| Ecuador | BIT |  |  |
| Peru | BIT |  |  |
| bolivia | BIT |  |  |
| Venezuela | BIT |  |  |
| moneda | INTEGER |  |  |
| ImpresorFiscal | BIT |  |  |
| datosfactura | BIT |  |  |
| tipoCompra | INTEGER |  |  |
| dominicana | BIT |  |  |
| libroconsumidor | BIT |  |  |
| limitepago | NUMERIC(18, 6) |  |  |
| belice | BIT |  |  |

#### Índices
- IX_pais_empresa: ['empresa'] 
- IX_pais_npais: ['npais'] 
- IX_pais_pais: ['pais'] 
- IX_pais_usuario: ['usuario'] 

### Tabla: parentes
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nparentes | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| parentes | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_parentes_empresa: ['empresa'] 
- IX_parentes_nparentes: ['nparentes'] 
- IX_parentes_parentes: ['parentes'] 
- IX_parentes_usuario: ['usuario'] 

### Tabla: partida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nopartida | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nocheque | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nofacturas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| noquedan | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| concepto | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| nula | BIT |  |  |
| quedan | BIT |  |  |
| impresa | BIT |  |  |
| cheqimp | BIT |  |  |
| conciliado | BIT |  |  |
| contabilidad | BIT |  |  |
| automatico | BIT |  |  |
| fecha | DATETIME |  |  |
| fechapago | DATETIME | ✓ |  |
| reffecha | DATETIME | ✓ |  |
| tipopart | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| periodo | INTEGER |  |  |
| ccuenta | INTEGER |  |  |
| chpartida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| debe | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| partida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| abono | NUMERIC(16, 6) |  |  |
| CDEBE | NUMERIC(18, 6) |  |  |
| CHABER | NUMERIC(18, 6) |  |  |
| IMPRIMECHEQUE | BIT |  |  |
| CMONTO | NUMERIC(18, 6) |  |  |
| TASACAMBIOTRES | NUMERIC(18, 6) |  |  |
| pagado | BIT |  |  |
| OPERADORTRES | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| OPERADOR | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ctrocosto | INTEGER |  |  |
| sucursal | INTEGER |  |  |
| notaremision | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| impremision | BIT |  |  |
| cerrada | BIT |  |  |
| cprovision | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ProvisionImpresa | BIT |  |  |
| cargo | NUMERIC(18, 6) |  |  |
| liquidadora | BIT |  |  |
| cajachica | BIT |  |  |
| mifecha | DATETIME | ✓ |  |

#### Foreign Keys
- ['periodo'] → periodo.['periodo']
- ['tipopart'] → tipopart.['tipopart']

#### Índices
- IX_partida_ccuenta: ['ccuenta'] 
- IX_partida_chpartida: ['chpartida'] 
- IX_partida_concepto: ['concepto'] 
- IX_partida_cuenta: ['cuenta'] 
- IX_partida_empresa: ['empresa'] 
- IX_partida_fecha: ['fecha'] 
- IX_partida_moneda: ['moneda'] 
- IX_partida_nocheque: ['nocheque'] 
- IX_partida_nofacturas: ['nofacturas'] 
- IX_partida_nopartida: ['nopartida'] 
- IX_partida_noquedan: ['noquedan'] 
- IX_partida_partida: ['partida'] 
- IX_partida_periodo: ['periodo'] 
- IX_partida_referencia: ['referencia'] 
- IX_partida_tipopart: ['tipopart'] 
- IX_partida_usuario: ['usuario'] 
- miflujoefectivo_dpartida_nula_debe: ['nula', 'debe'] 
- partida_nula_empresa_debe: ['nula', 'empresa', 'debe'] 

### Tabla: partidavta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| partidavta | INTEGER |  | ✓ |
| factura | INTEGER | ✓ |  |
| partida | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: patrono
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npatrono | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numpatro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nacional | INTEGER | ✓ |  |
| direccion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefon2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nomtraba | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nit | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numiva | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| giro | INTEGER | ✓ |  |
| dirtraba | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| municip | INTEGER | ✓ |  |
| depto | INTEGER | ✓ |  |
| pais | INTEGER | ✓ |  |
| teltrab1 | NUMERIC(8, 0) | ✓ |  |
| teltrab2 | NUMERIC(8, 0) | ✓ |  |
| fax | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| patrono | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_patrono_depto: ['depto'] 
- IX_patrono_direccion: ['direccion'] 
- IX_patrono_dirtraba: ['dirtraba'] 
- IX_patrono_empresa: ['empresa'] 
- IX_patrono_fax: ['fax'] 
- IX_patrono_giro: ['giro'] 
- IX_patrono_municip: ['municip'] 
- IX_patrono_nacional: ['nacional'] 
- IX_patrono_nit: ['nit'] 
- IX_patrono_nomtraba: ['nomtraba'] 
- IX_patrono_npatrono: ['npatrono'] 
- IX_patrono_numiva: ['numiva'] 
- IX_patrono_numpatro: ['numpatro'] 
- IX_patrono_pais: ['pais'] 
- IX_patrono_patrono: ['patrono'] 
- IX_patrono_telefon1: ['telefon1'] 
- IX_patrono_telefon2: ['telefon2'] 
- IX_patrono_tipo: ['tipo'] 
- IX_patrono_usuario: ['usuario'] 

### Tabla: pedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| fecha | SMALLDATETIME |  |  |
| documento | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nentregas | NUMERIC(2, 0) |  |  |
| terminado | BIT |  |  |
| cancelado | BIT |  |  |
| fecharecib | DATETIME | ✓ |  |
| fechalimite | DATETIME | ✓ |  |
| fechadesp | DATETIME | ✓ |  |
| tipovta | INTEGER |  |  |
| impresa | BIT |  |  |
| nota | TEXT(2147483647) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pedido | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| timestamp | DATETIME | ✓ |  |

#### Índices
- IX_pedido_clientes: ['clientes'] 
- IX_pedido_fecha: ['fecha'] 
- IX_pedido_pedido: ['pedido'] 
- IX_pedido_tipovta: ['tipovta'] 
- IX_pedido_usuario: ['usuario'] 

### Tabla: pedidoalmacen
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| tipomov | INTEGER |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| pedidoalmacen | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| CAJA | INTEGER | ✓ |  |
| bodega | INTEGER |  |  |
| cambodegaReferencia | INTEGER |  |  |
| enviado | BIT |  |  |
| caja2 | INTEGER |  |  |
| cambodega | INTEGER |  |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']

### Tabla: pedidos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nclientes | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| condpago | INTEGER |  |  |
| ncondpago | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nvendedor | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendedor | INTEGER |  |  |
| direccion | CHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registro | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono1 | CHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| limitecred | MONEY |  |  |

#### Índices
- IX_pedidos_clientes: ['clientes'] 
- IX_pedidos_condpago: ['condpago'] 
- IX_pedidos_vendedor: ['vendedor'] 

### Tabla: periodo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fechaini | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| mesesmas | INTEGER |  |  |
| activo | BIT |  |  |
| liqgtoing | BIT |  |  |
| periodo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_periodo_empresa: ['empresa'] 
- IX_periodo_mesesmas: ['mesesmas'] 
- IX_periodo_periodo: ['periodo'] 
- IX_periodo_usuario: ['usuario'] 

### Tabla: periodoPago
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dia | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| periodoPago | INTEGER |  | ✓ |

### Tabla: periodoactivo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| fecha | DATETIME |  |  |
| periodoactivo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |

### Tabla: periodocomision
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| periodocomision | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: periodoiva
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| fecha | DATETIME |  |  |
| exportacion | NUMERIC(16, 6) |  |  |
| remanente | NUMERIC(16, 6) |  |  |
| rempagocta | NUMERIC(16, 6) |  |  |
| ventas | NUMERIC(16, 6) |  |  |
| compras | NUMERIC(16, 6) |  |  |
| debitos | NUMERIC(16, 6) |  |  |
| creditos | NUMERIC(16, 6) |  |  |
| sujetos | NUMERIC(16, 6) |  |  |
| retenciones | NUMERIC(16, 6) |  |  |
| pagoacuenta | NUMERIC(16, 6) |  |  |
| excluido | NUMERIC(16, 6) |  |  |
| periodoiva | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |

#### Índices
- IX_periodoiva_empresa: ['empresa'] 
- IX_periodoiva_fecha: ['fecha'] 
- IX_periodoiva_moneda: ['moneda'] 
- IX_periodoiva_periodoiva: ['periodoiva'] 
- IX_periodoiva_usuario: ['usuario'] 

### Tabla: permisos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| modulo | INTEGER |  |  |
| usuario | INTEGER |  |  |
| permisos | INTEGER |  | ✓ |
| acceso | INTEGER |  |  |
| crear | INTEGER |  |  |
| modificar | INTEGER |  |  |
| eliminar | INTEGER |  |  |
| imprimir | INTEGER |  |  |
| excel | INTEGER |  |  |
| reporte | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_permisos_acceso: ['acceso'] 
- IX_permisos_crear: ['crear'] 
- IX_permisos_eliminar: ['eliminar'] 
- IX_permisos_empresa: ['empresa'] 
- IX_permisos_excel: ['excel'] 
- IX_permisos_imprimir: ['imprimir'] 
- IX_permisos_modificar: ['modificar'] 
- IX_permisos_modulo: ['modulo'] 
- IX_permisos_permisos: ['permisos'] 
- IX_permisos_reporte: ['reporte'] 
- IX_permisos_usuario: ['usuario'] 

### Tabla: perpla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nperpla | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nopla | NUMERIC(6, 4) |  |  |
| activo | BIT |  |  |
| perpla | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_perpla_empresa: ['empresa'] 
- IX_perpla_nperpla: ['nperpla'] 
- IX_perpla_perpla: ['perpla'] 
- IX_perpla_usuario: ['usuario'] 

### Tabla: pfactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nula | BIT |  |  |
| cancelada | BIT |  |  |
| enfirme | BIT |  |  |
| impresa | BIT |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pedido | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| comentario | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| expcomen | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| fechacanc | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| iva | INTEGER |  |  |
| transpte | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipovta | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| factoriva | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| pdesc | NUMERIC(16, 6) |  |  |
| vdesc | NUMERIC(16, 6) |  |  |
| factura | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| fechafact | DATETIME | ✓ |  |
| fexenta | NUMERIC(16, 6) |  |  |
| fafecta | NUMERIC(16, 6) |  |  |
| fviva | NUMERIC(16, 6) |  |  |
| fmontfact | NUMERIC(16, 6) |  |  |
| fpdesc | NUMERIC(16, 6) |  |  |
| fvdesc | NUMERIC(16, 6) |  |  |
| pfactura | INTEGER |  | ✓ |
| fnumedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| validez | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tdeliver | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas1 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas2 | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| caja | INTEGER |  |  |
| basesiniva | INTEGER |  |  |
| SINIVA | INTEGER |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| clientes2 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha1 | DATETIME |  |  |
| fecha2 | DATETIME |  |  |
| pais | INTEGER |  |  |
| archivada | BIT |  |  |
| Faltandatos | BIT |  |  |
| AprobadoAutoriza | INTEGER |  |  |
| conNotas | BIT |  |  |
| sinExistencias | BIT |  |  |
| Facturado | BIT |  |  |
| FacturaParcial | BIT |  |  |
| Modificado | BIT |  |  |
| ModifAutoriza | INTEGER |  |  |
| conDescuento | BIT |  |  |
| descAutoriza | INTEGER |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- IX_pfactura_bodega: ['bodega'] 
- IX_pfactura_clientes: ['clientes'] 
- IX_pfactura_comentario: ['comentario'] 
- IX_pfactura_condpago: ['condpago'] 
- IX_pfactura_empresa: ['empresa'] 
- IX_pfactura_expcomen: ['expcomen'] 
- IX_pfactura_factura: ['factura'] 
- IX_pfactura_fecha: ['fecha'] 
- IX_pfactura_fnumedocu: ['fnumedocu'] 
- IX_pfactura_iva: ['iva'] 
- IX_pfactura_moneda: ['moneda'] 
- IX_pfactura_notas: ['notas'] 
- IX_pfactura_notas1: ['notas1'] 
- IX_pfactura_notas2: ['notas2'] 
- IX_pfactura_pedido: ['pedido'] 
- IX_pfactura_pfactura: ['pfactura'] 
- IX_pfactura_prodprec: ['prodprec'] 
- IX_pfactura_tdeliver: ['tdeliver'] 
- IX_pfactura_tipomov: ['tipomov'] 
- IX_pfactura_tipovta: ['tipovta'] 
- IX_pfactura_transpte: ['transpte'] 
- IX_pfactura_usuario: ['usuario'] 
- IX_pfactura_validez: ['validez'] 
- IX_pfactura_vendedor: ['vendedor'] 

### Tabla: pieza
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npieza | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pieza | INTEGER |  | ✓ |

### Tabla: planPrestamo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| planPrestamo | INTEGER |  | ✓ |
| plaperio | INTEGER | ✓ |  |
| prestemp | INTEGER | ✓ |  |
| monto | MONEY | ✓ |  |
| montopatrono | MONEY | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| tipopla | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| planilla | INTEGER | ✓ |  |
| numero | INTEGER | ✓ |  |
| dplanilla | INTEGER | ✓ |  |

#### Índices
- IX_planPrestamo_dplanilla: ['dplanilla'] 
- IX_planPrestamo_empleado: ['empleado'] 
- IX_planPrestamo_empresa: ['empresa'] 
- IX_planPrestamo_numero: ['numero'] 
- IX_planPrestamo_planilla: ['planilla'] 
- IX_planPrestamo_planPrestamo: ['planPrestamo'] 
- IX_planPrestamo_plaperio: ['plaperio'] 
- IX_planPrestamo_prestemp: ['prestemp'] 
- IX_planPrestamo_tipopla: ['tipopla'] 
- IX_planPrestamo_usuario: ['usuario'] 

### Tabla: plandescuento
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| plandescuento | INTEGER |  | ✓ |
| plaperio | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| poldesc | INTEGER | ✓ |  |
| monto | MONEY | ✓ |  |
| montopatrono | MONEY | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| tipopla | INTEGER | ✓ |  |
| planilla | INTEGER | ✓ |  |
| dplanilla | INTEGER | ✓ |  |

#### Índices
- IX_plandescuento_dplanilla: ['dplanilla'] 
- IX_plandescuento_empleado: ['empleado'] 
- IX_plandescuento_empresa: ['empresa'] 
- IX_plandescuento_plandescuento: ['plandescuento'] 
- IX_plandescuento_planilla: ['planilla'] 
- IX_plandescuento_plaperio: ['plaperio'] 
- IX_plandescuento_poldesc: ['poldesc'] 
- IX_plandescuento_tipopla: ['tipopla'] 
- IX_plandescuento_usuario: ['usuario'] 

### Tabla: planempty
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| hora | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| jornada | BIT | ✓ |  |
| content1 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content2 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content3 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content4 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content5 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content6 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| content7 | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| planempty | INTEGER |  | ✓ |

### Tabla: planilla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nplanilla | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| plaperio | INTEGER | ✓ |  |
| plano | NUMERIC(1, 0) | ✓ |  |
| nopla | NUMERIC(1, 0) | ✓ |  |
| pais | INTEGER | ✓ |  |
| fechaemi | DATETIME | ✓ |  |
| moneda | INTEGER | ✓ |  |
| totaldev | NUMERIC(18, 6) | ✓ |  |
| totalded | NUMERIC(18, 6) | ✓ |  |
| dias | BIT | ✓ |  |
| tipopla | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| comentario | CHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| contabilidad | BIT | ✓ |  |
| patrono | INTEGER | ✓ |  |
| planilla | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| noplanilla | CHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| totaldevseg | NUMERIC(18, 6) | ✓ |  |
| totaldedseg | NUMERIC(18, 6) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| impresa | BIT | ✓ |  |
| nula | BIT | ✓ |  |
| FINICIO | DATETIME | ✓ |  |
| FFIN | DATETIME | ✓ |  |
| ndias | INTEGER | ✓ |  |
| montoapagar | NUMERIC(16, 8) | ✓ |  |
| nopersonas | INTEGER | ✓ |  |
| sueldo | NUMERIC(16, 9) | ✓ |  |
| fpago | DATETIME | ✓ |  |
| identificapla | INTEGER |  |  |
| IdPlanillaNormal | INTEGER |  |  |
| recalculo | BIT |  |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| midia | INTEGER | ✓ |  |

#### Foreign Keys
- ['plaperio'] → plaperio.['plaperio']

#### Índices
- IX_planilla_empresa: ['empresa'] 
- IX_planilla_identificapla: ['identificapla'] 
- IX_planilla_moneda: ['moneda'] 
- IX_planilla_ndias: ['ndias'] 
- IX_planilla_nopersonas: ['nopersonas'] 
- IX_planilla_nplanilla: ['nplanilla'] 
- IX_planilla_pais: ['pais'] 
- IX_planilla_patrono: ['patrono'] 
- IX_planilla_planilla: ['planilla'] 
- IX_planilla_plaperio: ['plaperio'] 
- IX_planilla_tipopla: ['tipopla'] 
- IX_planilla_usuario: ['usuario'] 

### Tabla: planillareloj
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| empleado | INTEGER |  |  |
| codreloj | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| tipodia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horario | INTEGER |  |  |
| horaentrada | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| horasalida | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| horasnormal | NUMERIC(18, 6) | ✓ |  |
| horasxtras | NUMERIC(18, 6) | ✓ |  |
| montohnormal | NUMERIC(18, 6) | ✓ |  |
| montohxtras | NUMERIC(18, 6) | ✓ |  |
| denegado | BIT |  |  |
| enfirme | BIT |  |  |
| planillareloj | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| usuarioautoriza | INTEGER | ✓ |  |
| fechaautoriza | DATETIME | ✓ |  |
| heantesentrada | NUMERIC(18, 6) |  |  |
| hedespuessalida | NUMERIC(18, 6) |  |  |
| cambienhn | BIT |  |  |
| cambienhe | BIT |  |  |
| jornada | INTEGER |  |  |
| reloj | INTEGER | ✓ |  |

### Tabla: planingreso
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| planingreso | INTEGER |  | ✓ |
| plaperio | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| ingreso | INTEGER | ✓ |  |
| monto | MONEY | ✓ |  |
| montopatrono | MONEY | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| tipopla | INTEGER | ✓ |  |
| planilla | INTEGER | ✓ |  |
| dplanilla | INTEGER | ✓ |  |

#### Índices
- IX_planingreso_dplanilla: ['dplanilla'] 
- IX_planingreso_empleado: ['empleado'] 
- IX_planingreso_empresa: ['empresa'] 
- IX_planingreso_ingreso: ['ingreso'] 
- IX_planingreso_planilla: ['planilla'] 
- IX_planingreso_planingreso: ['planingreso'] 
- IX_planingreso_plaperio: ['plaperio'] 
- IX_planingreso_tipopla: ['tipopla'] 
- IX_planingreso_usuario: ['usuario'] 

### Tabla: planwork
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dia | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| equipo | INTEGER | ✓ |  |
| rupfase | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| planwork | INTEGER |  | ✓ |

### Tabla: plaperio
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nplaperio | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| meses | INTEGER | ✓ |  |
| año | INTEGER | ✓ |  |
| aguinaldo | BIT | ✓ |  |
| vacacion | BIT | ✓ |  |
| activo | BIT | ✓ |  |
| plaperio | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| FINICIO | DATETIME | ✓ |  |
| FFIN | DATETIME | ✓ |  |
| f1 | DATETIME | ✓ |  |
| f2 | DATETIME | ✓ |  |
| f3 | DATETIME | ✓ |  |
| f4 | DATETIME | ✓ |  |
| ndias | INTEGER |  |  |

#### Índices
- IX_plaperio_año: ['año'] 
- IX_plaperio_empresa: ['empresa'] 
- IX_plaperio_meses: ['meses'] 
- IX_plaperio_nplaperio: ['nplaperio'] 
- IX_plaperio_plaperio: ['plaperio'] 
- IX_plaperio_usuario: ['usuario'] 

### Tabla: pncv
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ppagos | INTEGER |  |  |
| dcompra | INTEGER |  |  |
| ncmonto | NUMERIC(16, 6) |  |  |
| ncafecta | NUMERIC(16, 6) |  |  |
| ncexenta | NUMERIC(16, 6) |  |  |
| ncviva | NUMERIC(16, 6) |  |  |
| pncv | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dppagos | INTEGER | ✓ |  |

#### Índices
- IX_pncv_dcompra: ['dcompra'] 
- IX_pncv_empresa: ['empresa'] 
- IX_pncv_pncv: ['pncv'] 
- IX_pncv_ppagos: ['ppagos'] 
- IX_pncv_usuario: ['usuario'] 

### Tabla: pnopedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| pedido | INTEGER |  |  |
| nopedido | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pnopedido | INTEGER |  | ✓ |

#### Índices
- IX_pnopedido_empresa: ['empresa'] 
- IX_pnopedido_nopedido: ['nopedido'] 
- IX_pnopedido_pedido: ['pedido'] 
- IX_pnopedido_pnopedido: ['pnopedido'] 
- IX_pnopedido_usuario: ['usuario'] 

### Tabla: poldesc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npoldesc | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pais | INTEGER | ✓ |  |
| aplpat | BIT |  |  |
| procura | BIT |  |  |
| segsoc | BIT |  |  |
| renta | BIT |  |  |
| educa | BIT |  |  |
| otros | BIT |  |  |
| con1 | BIT |  |  |
| con2 | BIT |  |  |
| con3 | BIT |  |  |
| con4 | BIT |  |  |
| con5 | BIT |  |  |
| activo | BIT |  |  |
| perpla | INTEGER | ✓ |  |
| poldesc | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| despensa | BIT |  |  |
| facturacion | BIT |  |  |
| personal | BIT |  |  |
| transporte | BIT |  |  |
| optica | BIT |  |  |
| empresa | INTEGER |  |  |
| tipdeduccion | INTEGER |  |  |
| segurov | BIT | ✓ |  |
| deley | BIT | ✓ |  |
| manual | BIT | ✓ |  |
| segurovida | BIT |  |  |
| banco | BIT |  |  |
| cooperativa | BIT |  |  |
| ORDEN | INTEGER |  |  |
| Aguinaldo | BIT | ✓ |  |
| Indemnizacion | BIT | ✓ |  |
| Vacacion | BIT | ✓ |  |
| Anticipo | BIT |  |  |
| recalculojunio | BIT |  |  |
| recalculodiciembre | BIT |  |  |
| topemax | NUMERIC(8, 2) | ✓ |  |

#### Índices
- IX_poldesc_empresa: ['empresa'] 
- IX_poldesc_npoldesc: ['npoldesc'] 
- IX_poldesc_pais: ['pais'] 
- IX_poldesc_perpla: ['perpla'] 
- IX_poldesc_poldesc: ['poldesc'] 
- IX_poldesc_tipdeduccion: ['tipdeduccion'] 
- IX_poldesc_usuario: ['usuario'] 

### Tabla: polingpla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npolingpla | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| pais | INTEGER | ✓ |  |
| aplpat | BIT |  |  |
| aguinaldo | BIT |  |  |
| vacacion | BIT |  |  |
| indemnizacion | BIT |  |  |
| otros | BIT |  |  |
| con1 | BIT |  |  |
| con2 | BIT |  |  |
| con3 | BIT |  |  |
| con4 | BIT |  |  |
| con5 | BIT |  |  |
| activo | BIT |  |  |
| polingpla | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| tipingpla | INTEGER |  |  |
| salMinimo | NUMERIC(18, 6) | ✓ |  |
| SalMaximo | NUMERIC(18, 6) | ✓ |  |
| devengado | BIT | ✓ |  |
| manual | BIT | ✓ |  |
| isss | BIT |  |  |
| afp | BIT |  |  |
| renta | BIT |  |  |
| gratificacion | BIT |  |  |
| viaticos | BIT |  |  |
| agricola | BIT |  |  |
| depreciacion | BIT |  |  |
| comision | BIT |  |  |
| ORDEN | INTEGER |  |  |
| ingresofijo | BIT |  |  |
| automatico | BIT | ✓ |  |
| bonodia | BIT |  |  |

#### Índices
- IX_polingpla_empresa: ['empresa'] 
- IX_polingpla_npolingpla: ['npolingpla'] 
- IX_polingpla_pais: ['pais'] 
- IX_polingpla_polingpla: ['polingpla'] 
- IX_polingpla_tipingpla: ['tipingpla'] 
- IX_polingpla_usuario: ['usuario'] 

### Tabla: politing
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipopla | INTEGER | ✓ |  |
| ingreso | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| poliing | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| emptipla | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| monto | MONEY | ✓ |  |
| manual | BIT | ✓ |  |
| devengado | BIT | ✓ |  |

#### Índices
- IX_politing_empleado: ['empleado'] 
- IX_politing_empresa: ['empresa'] 
- IX_politing_emptipla: ['emptipla'] 
- IX_politing_ingreso: ['ingreso'] 
- IX_politing_poliing: ['poliing'] 
- IX_politing_tipopla: ['tipopla'] 
- IX_politing_tipopla_ingreso: ['tipopla', 'ingreso'] (UNIQUE)
- IX_politing_usuario: ['usuario'] 

### Tabla: politpla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| poldesc | INTEGER | ✓ |  |
| tipopla | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| politpla | INTEGER |  | ✓ |
| empresa | INTEGER | ✓ |  |
| emptipla | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| MONTO | MONEY | ✓ |  |

#### Índices
- IX_politpla_empleado: ['empleado'] 
- IX_politpla_empresa: ['empresa'] 
- IX_politpla_emptipla: ['emptipla'] 
- IX_politpla_poldesc: ['poldesc'] 
- IX_politpla_politpla: ['politpla'] 
- IX_politpla_tipopla: ['tipopla'] 
- IX_politpla_usuario: ['usuario'] 

### Tabla: polpladeduc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npolpladeduc | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| polpladeduc | INTEGER |  | ✓ |
| deley | BIT |  |  |
| aguinaldo | BIT |  |  |
| indemnizacion | BIT |  |  |
| vacacion | BIT |  |  |
| empresa | INTEGER |  |  |

### Tabla: ppagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| encompra | INTEGER |  |  |
| proveedor | INTEGER |  |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| contabilidad | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| difcambio | NUMERIC(16, 6) |  |  |
| mora | NUMERIC(16, 6) |  |  |
| ppagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| iva | INTEGER |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| condpago | INTEGER |  |  |
| fovial | NUMERIC(18, 6) |  |  |
| importacion | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| tipobodega | INTEGER |  |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- IX_ppagos_condpago: ['condpago'] 
- IX_ppagos_empresa: ['empresa'] 
- IX_ppagos_encompra: ['encompra'] 
- IX_ppagos_fecha: ['fecha'] 
- IX_ppagos_iva: ['iva'] 
- IX_ppagos_moneda: ['moneda'] 
- IX_ppagos_notas: ['notas'] 
- IX_ppagos_ppagos: ['ppagos'] 
- IX_ppagos_proveedor: ['proveedor'] 
- IX_ppagos_referencia: ['referencia'] 
- IX_ppagos_tipomov: ['tipomov'] 
- IX_ppagos_usuario: ['usuario'] 

### Tabla: ppartida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nopartida | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nocheque | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nofacturas | VARCHAR(254) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| noquedan | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| concepto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| nula | BIT |  |  |
| quedan | BIT |  |  |
| impresa | BIT |  |  |
| cheqimp | BIT |  |  |
| conciliado | BIT |  |  |
| contabilid | BIT |  |  |
| automatico | BIT |  |  |
| fecha | DATETIME |  |  |
| fechapago | DATETIME | ✓ |  |
| reffecha | DATETIME | ✓ |  |
| tipopart | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| periodo | INTEGER |  |  |
| ccuenta | INTEGER |  |  |
| chpartida | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| debe | NUMERIC(16, 6) |  |  |
| haber | NUMERIC(16, 6) |  |  |
| pdebe | NUMERIC(16, 6) |  |  |
| phaber | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| ppartida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| CDEBE | NUMERIC(18, 6) |  |  |
| CHABER | NUMERIC(18, 6) |  |  |
| CMONTO | NUMERIC(18, 6) |  |  |

#### Foreign Keys
- ['periodo'] → periodo.['periodo']

#### Índices
- IX_ppartida_ccuenta: ['ccuenta'] 
- IX_ppartida_chpartida: ['chpartida'] 
- IX_ppartida_concepto: ['concepto'] 
- IX_ppartida_cuenta: ['cuenta'] 
- IX_ppartida_empresa: ['empresa'] 
- IX_ppartida_fecha: ['fecha'] 
- IX_ppartida_moneda: ['moneda'] 
- IX_ppartida_nocheque: ['nocheque'] 
- IX_ppartida_nofacturas: ['nofacturas'] 
- IX_ppartida_nopartida: ['nopartida'] 
- IX_ppartida_noquedan: ['noquedan'] 
- IX_ppartida_periodo: ['periodo'] 
- IX_ppartida_ppartida: ['ppartida'] 
- IX_ppartida_referencia: ['referencia'] 
- IX_ppartida_tipopart: ['tipopart'] 
- IX_ppartida_usuario: ['usuario'] 

### Tabla: prePed
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| numedocu | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME | ✓ |  |
| Notas | VARCHAR(125) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| au1 | INTEGER | ✓ |  |
| au2 | INTEGER | ✓ |  |
| au3 | INTEGER | ✓ |  |
| au4 | INTEGER | ✓ |  |
| b1 | INTEGER | ✓ |  |
| b2 | INTEGER | ✓ |  |
| caja1 | INTEGER | ✓ |  |
| caja2 | INTEGER | ✓ |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| prePed | INTEGER |  | ✓ |

### Tabla: preciovineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npreciovineta | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| preciovineta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: presenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| npresenta | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| factor | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| umedida | INTEGER |  |  |
| presenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_presenta_empresa: ['empresa'] 
- IX_presenta_npresenta: ['npresenta'] 
- IX_presenta_presenta: ['presenta'] 
- IX_presenta_umedida: ['umedida'] 
- IX_presenta_usuario: ['usuario'] 

### Tabla: presociales
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| empleado | INTEGER |  |  |
| anios | INTEGER |  |  |
| meses | INTEGER |  |  |
| dias | INTEGER |  |  |
| suelmen | NUMERIC(18, 6) |  |  |
| sueldiario | NUMERIC(18, 6) |  |  |
| suelmenprom | NUMERIC(18, 6) |  |  |
| sueldiarioprom | NUMERIC(18, 6) |  |  |
| diaspreaviso | INTEGER |  |  |
| preaviso | NUMERIC(18, 6) |  |  |
| diascesantia | INTEGER |  |  |
| cesantia | NUMERIC(18, 6) |  |  |
| diaspreavisoprop | INTEGER |  |  |
| preavisoprop | NUMERIC(18, 6) |  |  |
| diascesantiaprop | INTEGER |  |  |
| cesantiaprop | NUMERIC(18, 6) |  |  |
| diasvacacion | INTEGER |  |  |
| vacacion | NUMERIC(18, 6) |  |  |
| diasdecimo3 | INTEGER |  |  |
| decimo3 | NUMERIC(18, 6) |  |  |
| diasdecimo4 | INTEGER |  |  |
| decimo4 | NUMERIC(18, 6) |  |  |
| diasbonovacacion | INTEGER |  |  |
| bonovacacion | NUMERIC(18, 6) |  |  |
| diastrabajados | INTEGER |  |  |
| trabajados | NUMERIC(18, 6) |  |  |
| diasbonoedu | INTEGER |  |  |
| bonoedu | NUMERIC(18, 6) |  |  |
| total | NUMERIC(18, 6) |  |  |
| diasleyvacaciones | INTEGER |  |  |
| techobonoedu | NUMERIC(18, 6) |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| presociales | INTEGER |  | ✓ |

### Tabla: prestemp
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nprestemp | VARCHAR(80) COLLATE "Modern_Spanish_CI_AS" |  |  |
| tipoprest | INTEGER | ✓ |  |
| banco | INTEGER | ✓ |  |
| montoprest | NUMERIC(18, 6) |  |  |
| fecprestam | DATETIME | ✓ |  |
| fecucuota | DATETIME | ✓ |  |
| numcuotas | INTEGER |  |  |
| numpcuota | INTEGER |  |  |
| ultimacuota | INTEGER |  |  |
| montocuota | NUMERIC(18, 6) |  |  |
| cuotanum | INTEGER |  |  |
| saldo | NUMERIC(18, 6) |  |  |
| nota | VARCHAR(100) COLLATE "Modern_Spanish_CI_AS" |  |  |
| frecpago | INTEGER | ✓ |  |
| activo | BIT |  |  |
| empleado | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| prestemp | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| montoprestseg | NUMERIC(18, 6) |  |  |
| montocuotaseg | NUMERIC(18, 6) |  |  |
| saldoseg | NUMERIC(18, 6) |  |  |
| empresa | INTEGER | ✓ |  |
| cancelado | BIT | ✓ |  |
| noprestamo | CHAR(50) COLLATE "Modern_Spanish_CI_AS" | ✓ |  |
| fechavence | DATETIME | ✓ |  |
| suspendido | BIT | ✓ |  |
| montocuota2 | NUMERIC(18, 6) |  |  |

#### Índices
- IX_prestemp_banco: ['banco'] 
- IX_prestemp_cuotanum: ['cuotanum'] 
- IX_prestemp_empleado: ['empleado'] 
- IX_prestemp_empresa: ['empresa'] 
- IX_prestemp_frecpago: ['frecpago'] 
- IX_prestemp_nota: ['nota'] 
- IX_prestemp_nprestemp: ['nprestemp'] 
- IX_prestemp_numcuotas: ['numcuotas'] 
- IX_prestemp_numpcuota: ['numpcuota'] 
- IX_prestemp_prestemp: ['prestemp'] 
- IX_prestemp_tipoprest: ['tipoprest'] 
- IX_prestemp_ultimacuota: ['ultimacuota'] 
- IX_prestemp_usuario: ['usuario'] 
- prestemp: ['prestemp'] 

### Tabla: proceso
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| descrip | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nproceso | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| proceso | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| SISTEMA | BIT |  |  |
| micolor | INTEGER |  |  |
| diasDeGracia | INTEGER |  |  |
| esProceso | BIT |  |  |
| validado | BIT |  |  |

#### Índices
- IX_proceso_descrip: ['descrip'] 
- IX_proceso_empresa: ['empresa'] 
- IX_proceso_nproceso: ['nproceso'] 
- IX_proceso_nproceso_uniq: ['nproceso'] (UNIQUE)
- IX_proceso_proceso: ['proceso'] 
- IX_proceso_usuario: ['usuario'] 

### Tabla: prodentregado
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| prodentregado | INTEGER |  | ✓ |
| factura | INTEGER |  |  |
| registroproducto | INTEGER |  |  |
| cantidad | NUMERIC(18, 6) |  |  |
| garantia | DATETIME | ✓ |  |
| garantiaprov | DATETIME | ✓ |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| dFactura | INTEGER |  |  |
| entregado | BIT |  |  |
| registrogarantia | INTEGER |  |  |

#### Índices
- IX_prodentregado_dFactura: ['dFactura'] 
- IX_prodentregado_factura: ['factura'] 
- IX_prodentregado_prodentregado: ['prodentregado'] 
- IX_prodentregado_registrogarantia: ['registrogarantia'] 
- IX_prodentregado_registroproducto: ['registroproducto'] 
- IX_prodentregado_usuario: ['usuario'] 

### Tabla: prodform
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nprodform | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ncprodform | VARCHAR(55) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| especific | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registrosani | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecini1 | DATETIME | ✓ |  |
| vence1 | DATETIME | ✓ |  |
| estado1 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| responsable1 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion1 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono1 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| registromarca | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecini2 | DATETIME | ✓ |  |
| vence2 | DATETIME | ✓ |  |
| estado2 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| responsable2 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion2 | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| telefono | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| formato | INTEGER |  |  |
| producto | INTEGER |  |  |
| prodform | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['producto'] → producto.['producto']

#### Índices
- IX_prodform_direccion1: ['direccion1'] 
- IX_prodform_direccion2: ['direccion2'] 
- IX_prodform_empresa: ['empresa'] 
- IX_prodform_especific: ['especific'] 
- IX_prodform_estado1: ['estado1'] 
- IX_prodform_estado2: ['estado2'] 
- IX_prodform_formato: ['formato'] 
- IX_prodform_ncprodform: ['ncprodform'] 
- IX_prodform_nprodform: ['nprodform'] 
- IX_prodform_prodform: ['prodform'] 
- IX_prodform_producto: ['producto'] 
- IX_prodform_registromarca: ['registromarca'] 
- IX_prodform_registrosani: ['registrosani'] 
- IX_prodform_responsable1: ['responsable1'] 
- IX_prodform_responsable2: ['responsable2'] 
- IX_prodform_telefono: ['telefono'] 
- IX_prodform_telefono1: ['telefono1'] 
- IX_prodform_usuario: ['usuario'] 

### Tabla: prodorden
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER | ✓ |  |
| almacen | INTEGER | ✓ |  |
| fecha | DATETIME | ✓ |  |
| fechainicio | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| estatus | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| prodorden | INTEGER |  | ✓ |

### Tabla: prodplanta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME | ✓ |  |
| bodega | INTEGER | ✓ |  |
| empleado | INTEGER | ✓ |  |
| producto | INTEGER | ✓ |  |
| precio | NUMERIC(12, 6) | ✓ |  |
| pextra | NUMERIC(12, 6) | ✓ |  |
| pagado | BIT |  |  |
| cantidad | NUMERIC(12, 2) | ✓ |  |
| extra | NUMERIC(12, 2) | ✓ |  |
| empresa | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| prodplanta | INTEGER |  | ✓ |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dplanilla | INTEGER | ✓ |  |
| bextra | BIT | ✓ |  |
| almacen | INTEGER | ✓ |  |

### Tabla: prodprec
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nprodprec | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainicial | DATETIME | ✓ |  |
| fechafinal | DATETIME | ✓ |  |
| moneda | INTEGER |  |  |
| prodprec | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| condicion1 | BIT |  |  |
| Margen | NUMERIC(18, 6) | ✓ |  |
| MargenMinimo | NUMERIC(18, 6) | ✓ |  |
| Preferido | BIT | ✓ |  |
| ruta | BIT |  |  |
| taller | BIT |  |  |
| PorcDescuento | NUMERIC(18, 6) |  |  |
| porcentaje | BIT |  |  |

#### Índices
- IX_prodprec_empresa: ['empresa'] 
- IX_prodprec_moneda: ['moneda'] 
- IX_prodprec_nprodprec: ['nprodprec'] 
- IX_prodprec_prodprec: ['prodprec'] 
- IX_prodprec_usuario: ['usuario'] 

### Tabla: prodprectipcli
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| prodprec | INTEGER |  |  |
| tipcli | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| prodprectipcli | INTEGER |  | ✓ |

#### Foreign Keys
- ['prodprec'] → prodprec.['prodprec']
- ['tipcli'] → tipcli.['tipcli']

#### Índices
- IX_prodprectipcli_empresa: ['empresa'] 
- IX_prodprectipcli_prodprec: ['prodprec'] 
- IX_prodprectipcli_prodprectipcli: ['prodprectipcli'] 
- IX_prodprectipcli_tipcli: ['tipcli'] 

### Tabla: producto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nproducto | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| otroname | VARCHAR(1000) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| controla | BIT |  |  |
| bonificado | BIT |  |  |
| vineta | BIT |  |  |
| enventa | BIT |  |  |
| incluir | BIT |  |  |
| fabricar | BIT |  |  |
| exento | BIT |  |  |
| desccontado | BIT |  |  |
| parte | BIT |  |  |
| servicios | BIT |  |  |
| tipoprod | INTEGER |  |  |
| categori | INTEGER |  |  |
| umedida | INTEGER |  |  |
| presenta | INTEGER |  |  |
| casaprod | INTEGER |  |  |
| costo | NUMERIC(16, 6) |  |  |
| cantidadreor | NUMERIC(16, 6) |  |  |
| minimo | NUMERIC(16, 6) |  |  |
| cantidadcompra | NUMERIC(16, 6) |  |  |
| compraminima | NUMERIC(16, 6) |  |  |
| compramaxima | NUMERIC(16, 6) |  |  |
| promedio | NUMERIC(16, 6) |  |  |
| promlicitacionexport | NUMERIC(16, 6) |  |  |
| promedioexportacion | NUMERIC(16, 6) |  |  |
| promlicitacion | NUMERIC(16, 6) |  |  |
| codbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| icdbarra | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| producto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| peso | NUMERIC(16, 6) |  |  |
| condicion1 | BIT |  |  |
| recargo | BIT |  |  |
| cicloanterior | BIT |  |  |
| vvineta | NUMERIC(16, 6) |  |  |
| mformula | INTEGER |  |  |
| sretencion | BIT | ✓ |  |
| condicion2 | BIT |  |  |
| indicador | INTEGER |  |  |
| estatus | INTEGER |  |  |
| dispensador | BIT |  |  |
| codblister | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| noblister | INTEGER |  |  |
| nosujeto | BIT |  |  |
| cuenta | INTEGER |  |  |
| BODEGA | INTEGER |  |  |
| PRODPREC | INTEGER |  |  |
| TPRECIO | NUMERIC(18, 6) |  |  |
| FPRECIO | NUMERIC(18, 6) |  |  |
| Cargofull | BIT |  |  |
| marchamo | BIT |  |  |
| viajecompleto | BIT |  |  |
| combustible | BIT |  |  |
| repuesto | BIT |  |  |
| produccion | BIT |  |  |
| ActivoFijo | BIT |  |  |
| CostoTipo | INTEGER |  |  |
| CategoriaBien | INTEGER |  |  |
| batch | NUMERIC(18, 6) |  |  |
| factor1 | NUMERIC(18, 6) |  |  |
| umedida1 | INTEGER |  |  |
| taller | BIT |  |  |
| miImagen | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| volumen | NUMERIC(18, 6) |  |  |
| TipoEscala | INTEGER |  |  |
| miColor | INTEGER |  |  |
| controlado | BIT |  |  |
| sexo | INTEGER |  |  |
| estilo | INTEGER |  |  |
| maximo | NUMERIC(18, 6) |  |  |
| clase | INTEGER |  |  |
| temporada | INTEGER |  |  |
| fabricacion | INTEGER |  |  |
| envio | INTEGER |  |  |
| deTemporada | BIT |  |  |
| feature01 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| feature02 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| feature03 | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| orden | VARCHAR(3) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pingreso | BIT |  |  |
| fila | INTEGER |  |  |
| columna | INTEGER |  |  |
| hproduccion | NUMERIC(18, 6) |  |  |
| diasvence | INTEGER |  |  |
| showroom | BIT |  |  |
| talla | NUMERIC(5, 2) |  |  |
| tallau | NUMERIC(5, 2) |  |  |
| tallak | NUMERIC(5, 2) |  |  |
| parte1 | BIT |  |  |
| cocina | BIT |  |  |
| mibar | BIT |  |  |
| apdesc | BIT |  |  |

#### Foreign Keys
- ['casaprod'] → casaprod.['casaprod']
- ['categori'] → categori.['categori']
- ['presenta'] → presenta.['presenta']
- ['tipoprod'] → tipoprod.['tipoprod']
- ['umedida'] → umedida.['umedida']

#### Índices
- IX_producto_casaprod: ['casaprod'] 
- IX_producto_categori: ['categori'] 
- IX_producto_codbarra: ['codbarra'] 
- IX_producto_COLUMNA: ['columna'] 
- IX_producto_empresa: ['empresa'] 
- IX_producto_FILA: ['fila'] 
- IX_producto_icdbarra: ['icdbarra'] 
- IX_producto_mformula: ['mformula'] 
- IX_producto_nproducto: ['nproducto'] 
- IX_producto_orden: ['orden'] 
- IX_producto_otroname: ['otroname'] 
- IX_producto_presenta: ['presenta'] 
- IX_producto_producto: ['producto'] 
- IX_producto_tipoprod: ['tipoprod'] 
- IX_producto_umedida: ['umedida'] 
- IX_producto_usuario: ['usuario'] 
- producto_icdbarra: ['icdbarra'] 
- ProductoServicios: ['servicios'] 
- ProductoServicos02: ['servicios', 'repuesto', 'produccion', 'ActivoFijo'] 

### Tabla: profesion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nprofesion | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| profesion | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_profesion_empresa: ['empresa'] 
- IX_profesion_nprofesion: ['nprofesion'] 
- IX_profesion_profesion: ['profesion'] 
- IX_profesion_usuario: ['usuario'] 

### Tabla: proveedor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nproveedor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| municip | INTEGER |  |  |
| moneda | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| condpago | INTEGER |  |  |
| tipoprov | INTEGER |  |  |
| contado | BIT |  |  |
| exento | BIT |  |  |
| nit | VARCHAR(21) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| registro | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| giro | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| contacto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| razonsoc | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| sitioweb | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| email | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| direccion | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descuento | INTEGER |  |  |
| promcomp | NUMERIC(16, 6) |  |  |
| prompago | NUMERIC(16, 6) |  |  |
| fechalim | DATETIME | ✓ |  |
| recomendado | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| telefono1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefono2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fax | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| limitecredito | NUMERIC(16, 6) |  |  |
| hora | DATETIME | ✓ |  |
| proveedor | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | BIT |  |  |
| ivacero | BIT | ✓ |  |
| percepcion | BIT |  |  |
| cuenta | INTEGER |  |  |
| comisionmedios | NUMERIC(18, 6) |  |  |
| pais | INTEGER |  |  |
| otroDocumento | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| otroDoc | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| diasEntrega | INTEGER |  |  |
| infopago | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| puertoEmbarque | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cuenta1 | INTEGER | ✓ |  |
| diasDespacho | INTEGER |  |  |
| tipo | INTEGER |  |  |
| clasificacion | INTEGER |  |  |
| sector | INTEGER |  |  |
| costo | INTEGER |  |  |

#### Foreign Keys
- ['municip'] → municip.['municip']

#### Índices
- IX_proveedor_condpago: ['condpago'] 
- IX_proveedor_contacto: ['contacto'] 
- IX_proveedor_descuento: ['descuento'] 
- IX_proveedor_direccion: ['direccion'] 
- IX_proveedor_email: ['email'] 
- IX_proveedor_empresa: ['empresa'] 
- IX_proveedor_fax: ['fax'] 
- IX_proveedor_giro: ['giro'] 
- IX_proveedor_moneda: ['moneda'] 
- IX_proveedor_municip: ['municip'] 
- IX_proveedor_notas: ['notas'] 
- IX_proveedor_nproveedor: ['nproveedor'] 
- IX_proveedor_prodprec: ['prodprec'] 
- IX_proveedor_proveedor: ['proveedor'] 
- IX_proveedor_razonsoc: ['razonsoc'] 
- IX_proveedor_recomendado: ['recomendado'] 
- IX_proveedor_registro: ['registro'] 
- IX_proveedor_sitioweb: ['sitioweb'] 
- IX_proveedor_telefono1: ['telefono1'] 
- IX_proveedor_telefono2: ['telefono2'] 
- IX_proveedor_tipoprov: ['tipoprov'] 
- IX_proveedor_usuario: ['usuario'] 

### Tabla: proyecto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nproyecto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainicion | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| activo | BIT |  |  |
| encargado | INTEGER |  |  |
| proyecto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| NULA | BIT |  |  |
| PROCESADA | BIT |  |  |
| PRESUPUESTO | BIT |  |  |

#### Índices
- IX_proyecto_descripcion: ['descripcion'] 
- IX_proyecto_empresa: ['empresa'] 
- IX_proyecto_encargado: ['encargado'] 
- IX_proyecto_nproyecto: ['nproyecto'] 
- IX_proyecto_proyecto: ['proyecto'] 
- IX_proyecto_usuario: ['usuario'] 

### Tabla: ptovta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| nptovta | CHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nota | CHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| ptovta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_ptovta_empresa: ['empresa'] 
- IX_ptovta_ptovta: ['ptovta'] 
- IX_ptovta_usuario: ['usuario'] 

### Tabla: quienprepara
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| factura | INTEGER | ✓ |  |
| cambodega | INTEGER | ✓ |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| fecha3 | DATETIME | ✓ |  |
| bodeguero1 | INTEGER | ✓ |  |
| bodeguero2 | INTEGER | ✓ |  |
| quienprepara | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| bultos | INTEGER | ✓ |  |

### Tabla: rangospagados
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rangospagados | INTEGER |  | ✓ |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| impresa | BIT |  |  |
| pcomision | NUMERIC(18, 6) |  |  |

#### Índices
- IX_rangospagados_rangospagados: ['rangospagados'] 

### Tabla: razoncuenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activocirculante | BIT |  |  |
| pasivocirculante | BIT |  |  |
| inventario | BIT |  |  |
| costoventa | BIT |  |  |
| cuentasxcobrar | BIT |  |  |
| cuentasxpagar | BIT |  |  |
| ventas | BIT |  |  |
| devventas | BIT |  |  |
| activostotales | BIT |  |  |
| pasivostotales | BIT |  |  |
| pasivolargoplazo | BIT |  |  |
| capitalsocial | BIT |  |  |
| ingresofinanciero | BIT |  |  |
| oingresosnograv | BIT |  |  |
| ogastosnodeduc | BIT |  |  |
| gastosoperacion | BIT |  |  |
| gastosventa | BIT |  |  |
| gastosadmon | BIT |  |  |
| gastosfinan | BIT |  |  |
| otrosingresos | BIT |  |  |
| otrosgastos | BIT |  |  |
| utilidad | BIT |  |  |
| reservacapital | BIT |  |  |
| horatiempo | DATETIME |  |  |
| razoncuenta | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| cuenta | INTEGER |  |  |
| interes | BIT |  |  |
| efectivo | BIT | ✓ |  |

### Tabla: rcontrol
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| variable | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| valor | BIT |  |  |
| ncondicion | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| rcontrol | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| dia | INTEGER | ✓ |  |
| caja | INTEGER | ✓ |  |

#### Índices
- IX_rcontrol_empresa: ['empresa'] 
- IX_rcontrol_ncondicion: ['ncondicion'] 
- IX_rcontrol_rcontrol: ['rcontrol'] 
- IX_rcontrol_usuario: ['usuario'] 
- IX_rcontrol_variable: ['variable'] 

### Tabla: rdte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dte | INTEGER |  | ✓ |
| dtabla | INTEGER |  | ✓ |
| empresa | INTEGER |  | ✓ |

### Tabla: recordar
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nrecordar | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| hrecordar | NUMERIC(18, 6) | ✓ |  |
| recordar | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: recvineta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| recvineta | INTEGER |  | ✓ |
| vendedor | INTEGER |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| pagada | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: reffecha
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fechaini | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| reffecha | INTEGER |  | ✓ |

#### Índices
- IX_reffecha_reffecha: ['reffecha'] 
- reffecha100: ['fechaini'] 

### Tabla: regciclo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| regciclo | INTEGER |  | ✓ |
| ciclo | CHAR(7) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| fechaini | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| nocuotas | INTEGER |  |  |
| prodprec | INTEGER |  |  |
| impresa | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_regciclo_empresa: ['empresa'] 
- IX_regciclo_nocuotas: ['nocuotas'] 
- IX_regciclo_prodprec: ['prodprec'] 
- IX_regciclo_regciclo: ['regciclo'] 
- IX_regciclo_usuario: ['usuario'] 

### Tabla: registroControl
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| RegistroControl | INTEGER |  | ✓ |
| idUsuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| modulo | INTEGER |  |  |
| FinSesion | DATETIME | ✓ |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| equipo | INTEGER |  |  |

#### Índices
- IX_registroControl_empresa: ['empresa'] 
- IX_registroControl_equipo: ['equipo'] 
- IX_registroControl_idUsuario: ['idUsuario'] 
- IX_registroControl_modulo: ['modulo'] 
- IX_registroControl_RegistroControl: ['RegistroControl'] 
- IX_registroControl_usuario: ['usuario'] 

### Tabla: regpagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipomov | INTEGER |  |  |
| moneda | INTEGER |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| referencia | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| contabilidad | BIT |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| difcambio | NUMERIC(16, 6) |  |  |
| mora | NUMERIC(16, 6) |  |  |
| regpagos | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cargo | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| iva | INTEGER |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| caja | INTEGER |  |  |
| condpago | INTEGER |  |  |

#### Índices
- IX_regpagos_caja: ['caja'] 
- IX_regpagos_clientes: ['clientes'] 
- IX_regpagos_condpago: ['condpago'] 
- IX_regpagos_empresa: ['empresa'] 
- IX_regpagos_fecha: ['fecha'] 
- IX_regpagos_iva: ['iva'] 
- IX_regpagos_moneda: ['moneda'] 
- IX_regpagos_notas: ['notas'] 
- IX_regpagos_referencia: ['referencia'] 
- IX_regpagos_regpagos: ['regpagos'] 
- IX_regpagos_tipomov: ['tipomov'] 
- IX_regpagos_usuario: ['usuario'] 
- IX_regpagos_vendedor: ['vendedor'] 

### Tabla: reloj
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| reloj | INTEGER |  | ✓ |
| nreloj | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| codreloj | INTEGER |  |  |
| hecomoingreso | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: repo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nrepo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nprinter | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fuente | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cabeza | BIT | ✓ |  |
| pie | BIT | ✓ |  |
| alto | BIT | ✓ |  |
| campo | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| vpos | NUMERIC(9, 5) | ✓ |  |
| hpos | NUMERIC(9, 5) | ✓ |  |
| ancho | NUMERIC(9, 5) | ✓ |  |
| mascara | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| repoid | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| repo | INTEGER |  | ✓ |
| otipo | INTEGER |  |  |

### Tabla: report
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nReport | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| Activo | BIT |  |  |
| Report | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| sucursal | INTEGER |  |  |
| manual | BIT |  |  |
| nprinter | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_report_empresa: ['empresa'] 
- IX_report_nReport: ['nReport'] 
- IX_report_Report: ['Report'] 
- IX_report_usuario: ['usuario'] 

### Tabla: reportHeader
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| header1 | NCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header2 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header3 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header4 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header5 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header6 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header7 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header8 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header9 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header10 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header11 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header12 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header13 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header14 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header15 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header16 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header17 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header18 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header19 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header20 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header21 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header22 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header23 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header24 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header25 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header26 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header27 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header28 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header29 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header30 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| header31 | NCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: reportcolumna
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| columna1 | NCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| columna2 | NCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| columna3 | NUMERIC(18, 6) | ✓ |  |
| columna4 | NUMERIC(18, 6) | ✓ |  |
| columna5 | NUMERIC(18, 6) | ✓ |  |
| columna6 | NUMERIC(18, 6) | ✓ |  |
| columna7 | NUMERIC(18, 6) | ✓ |  |
| columna8 | NUMERIC(18, 6) | ✓ |  |
| columna9 | NUMERIC(18, 6) | ✓ |  |
| columna10 | NUMERIC(18, 6) | ✓ |  |
| columna11 | NUMERIC(18, 6) | ✓ |  |
| columna12 | NUMERIC(18, 6) | ✓ |  |
| columna13 | NUMERIC(18, 6) | ✓ |  |
| columna14 | NUMERIC(18, 6) | ✓ |  |
| columna15 | NUMERIC(18, 6) | ✓ |  |
| columna16 | NUMERIC(18, 6) | ✓ |  |
| columna17 | NUMERIC(18, 6) | ✓ |  |
| columna18 | NUMERIC(18, 6) | ✓ |  |
| columna19 | NUMERIC(18, 6) | ✓ |  |
| columna20 | NUMERIC(18, 6) | ✓ |  |
| columna21 | NUMERIC(18, 6) | ✓ |  |
| columna22 | NUMERIC(18, 6) | ✓ |  |
| columna23 | NUMERIC(18, 6) | ✓ |  |
| columna24 | NUMERIC(18, 6) | ✓ |  |
| columna25 | NUMERIC(18, 6) | ✓ |  |
| columna26 | NUMERIC(18, 6) | ✓ |  |
| columna27 | NUMERIC(18, 6) | ✓ |  |
| columna28 | NUMERIC(18, 6) | ✓ |  |
| columna29 | NUMERIC(18, 6) | ✓ |  |
| columna30 | NUMERIC(18, 6) | ✓ |  |
| columna31 | NCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: reporte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nreporte | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encab1 | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encab2 | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encab3 | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| columna | NUMERIC(16, 6) |  |  |
| encolum1 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encolum2 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encolum3 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encolum4 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encolum5 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| encolum6 | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tot1 | BIT |  |  |
| tot2 | BIT |  |  |
| tot3 | BIT |  |  |
| tot4 | BIT |  |  |
| tot5 | BIT |  |  |
| repftot | NUMERIC(16, 6) |  |  |
| firma1 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| firma2 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| firma3 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| titulo1 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| titulo2 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| titulo3 | VARCHAR(32) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| reporte | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| auto | INTEGER |  |  |
| cTotal1 | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cTotal2 | VARCHAR(70) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_reporte_empresa: ['empresa'] 
- IX_reporte_encab1: ['encab1'] 
- IX_reporte_encab2: ['encab2'] 
- IX_reporte_encab3: ['encab3'] 
- IX_reporte_encolum1: ['encolum1'] 
- IX_reporte_encolum2: ['encolum2'] 
- IX_reporte_encolum3: ['encolum3'] 
- IX_reporte_encolum4: ['encolum4'] 
- IX_reporte_encolum5: ['encolum5'] 
- IX_reporte_encolum6: ['encolum6'] 
- IX_reporte_firma1: ['firma1'] 
- IX_reporte_firma2: ['firma2'] 
- IX_reporte_firma3: ['firma3'] 
- IX_reporte_nreporte: ['nreporte'] 
- IX_reporte_reporte: ['reporte'] 
- IX_reporte_titulo1: ['titulo1'] 
- IX_reporte_titulo2: ['titulo2'] 
- IX_reporte_titulo3: ['titulo3'] 
- IX_reporte_usuario: ['usuario'] 

### Tabla: retencion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| proveedor | INTEGER |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numedocux | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| compra | INTEGER |  |  |
| fecha | DATETIME |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| retencion | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| percepcion | NUMERIC(18, 6) |  |  |

#### Índices
- IX_retencion_compra: ['compra'] 
- IX_retencion_empresa: ['empresa'] 
- IX_retencion_fecha: ['fecha'] 
- IX_retencion_moneda: ['moneda'] 
- IX_retencion_notas: ['notas'] 
- IX_retencion_numedocux: ['numedocux'] 
- IX_retencion_proveedor: ['proveedor'] 
- IX_retencion_retencion: ['retencion'] 
- IX_retencion_usuario: ['usuario'] 

### Tabla: rliquida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rliquida | INTEGER |  | ✓ |
| impresa | BIT |  |  |
| enfirme | BIT |  |  |
| vendedor | INTEGER |  |  |
| fecha | DATETIME |  |  |
| prodprec | INTEGER |  |  |
| montliquida | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| vdevolucion | NUMERIC(16, 6) |  |  |
| vtventa | NUMERIC(16, 6) |  |  |
| efectivo | NUMERIC(18, 6) |  |  |
| cheque | NUMERIC(18, 6) |  |  |
| remesa | NUMERIC(18, 6) |  |  |
| tarjeta | NUMERIC(18, 6) |  |  |
| ventacredito | NUMERIC(18, 6) |  |  |
| ventaefectivo | NUMERIC(18, 6) |  |  |
| horasJornada | INTEGER |  |  |
| horaSalida | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| motorista | INTEGER |  |  |
| camion | INTEGER |  |  |
| horasExtras | INTEGER |  |  |
| motorista1 | INTEGER |  |  |
| horaSalida1 | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horasJornada1 | INTEGER |  |  |
| horasExtras1 | INTEGER |  |  |
| camion1 | INTEGER |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horas | INTEGER |  |  |
| horas1 | INTEGER |  |  |
| cienll | INTEGER |  |  |
| cincuentadoll | INTEGER |  |  |
| veintell | INTEGER |  |  |
| diezll | INTEGER |  |  |
| cincoll | INTEGER |  |  |
| unoll | INTEGER |  |  |
| cincuentavos | INTEGER |  |  |
| veintecincovos | INTEGER |  |  |
| diezvos | INTEGER |  |  |
| cincovos | INTEGER |  |  |
| unvos | INTEGER |  |  |

#### Índices
- IX_rliquida_empresa: ['empresa'] 
- IX_rliquida_fecha: ['fecha'] 
- IX_rliquida_prodprec: ['prodprec'] 
- IX_rliquida_rliquida: ['rliquida'] 
- IX_rliquida_usuario: ['usuario'] 
- IX_rliquida_vendedor: ['vendedor'] 

### Tabla: roles
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| roles | INTEGER |  | ✓ |
| nroles | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_roles_empresa: ['empresa'] 
- IX_roles_nroles: ['nroles'] 
- IX_roles_roles: ['roles'] 
- IX_roles_usuario: ['usuario'] 

### Tabla: rollonum
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| novinetas | INTEGER |  |  |
| Noimpresas | INTEGER |  |  |
| perdidas | INTEGER |  |  |
| minimo | INTEGER |  |  |
| maximo | INTEGER |  |  |
| correlativo | INTEGER |  |  |
| rollonum | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: room
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nroom | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| room | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_room_empresa: ['empresa'] 
- IX_room_nroom: ['nroom'] 
- IX_room_room: ['room'] 
- IX_room_usuario: ['usuario'] 

### Tabla: rpImpuesto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rpImpuesto | INTEGER |  | ✓ |
| numedocu | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Impreso | BIT | ✓ |  |
| descrip | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | SMALLDATETIME | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| monto | NUMERIC(18, 6) | ✓ |  |

#### Índices
- IX_rpImpuesto_descrip: ['descrip'] 
- IX_rpImpuesto_empresa: ['empresa'] 
- IX_rpImpuesto_fecha: ['fecha'] 
- IX_rpImpuesto_numedocu: ['numedocu'] 
- IX_rpImpuesto_rpImpuesto: ['rpImpuesto'] 
- IX_rpImpuesto_usuario: ['usuario'] 

### Tabla: rpdImpuesto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rpdImpuesto | INTEGER |  | ✓ |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| monto | NUMERIC(18, 2) | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| rpImpuesto | INTEGER | ✓ |  |

#### Índices
- IX_rpdImpuesto_clientes: ['clientes'] 
- IX_rpdImpuesto_empresa: ['empresa'] 
- IX_rpdImpuesto_rpdImpuesto: ['rpdImpuesto'] 
- IX_rpdImpuesto_rpImpuesto: ['rpImpuesto'] 
- IX_rpdImpuesto_usuario: ['usuario'] 

### Tabla: rubro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nrubro | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| operador | NUMERIC(16, 6) |  |  |
| activo | BIT |  |  |
| rubro | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| bienes | BIT |  |  |
| pasivo | BIT |  |  |
| capital | BIT |  |  |
| gastos | BIT |  |  |
| ingresos | BIT |  |  |
| liquidadora | BIT |  |  |
| NORUBRO | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_rubro_empresa: ['empresa'] 
- IX_rubro_noRUBRO: ['NORUBRO'] 
- IX_rubro_nrubro: ['nrubro'] 
- IX_rubro_rubro: ['rubro'] 
- IX_rubro_usuario: ['usuario'] 

### Tabla: rupotkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rupot | INTEGER |  | ✓ |
| kardex | INTEGER |  | ✓ |
| cantidad | NUMERIC(14, 6) | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: ruta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| unidad | BINARY(100) |  |  |
| ruta | INTEGER |  | ✓ |

#### Índices
- IX_ruta_ruta: ['ruta'] 

### Tabla: rutacobro
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| vendedor | INTEGER |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| liquidada | BIT |  |  |
| notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| rutacobro | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |
| saldo | NUMERIC(18, 6) |  |  |
| numedocu | INTEGER |  |  |
| entregada | BIT |  |  |

### Tabla: rutapagos
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| rutapagos | INTEGER |  | ✓ |
| rutacobro | INTEGER | ✓ |  |
| pagos | INTEGER | ✓ |  |
| dpagos | INTEGER | ✓ |  |
| cambodega | INTEGER | ✓ |  |
| factura | INTEGER | ✓ |  |
| invcliente | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: sacceso
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| voriginal | NUMERIC(18, 6) |  |  |
| vnuevo | NUMERIC(18, 6) |  |  |
| idtabla | INTEGER |  |  |
| estatus | INTEGER |  |  |
| caccesos | INTEGER |  |  |
| fecha | DATETIME |  |  |
| encargado | INTEGER |  |  |
| tabla | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| notas | VARCHAR(300) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| sacceso | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| numedocu | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| archivo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| documento | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hoy | DATETIME |  |  |
| equipo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nivel | INTEGER |  |  |
| tpermiso | BIT |  |  |
| porcentaje | NUMERIC(18, 6) |  |  |
| suPorcent | NUMERIC(18, 6) |  |  |
| dNotas | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| didTabla | INTEGER |  |  |
| ausuario | INTEGER |  |  |
| ahora | DATETIME | ✓ |  |
| anulada | BIT |  |  |

#### Índices
- IX_sacceso_sacceso: ['sacceso'] 

### Tabla: saldocliente
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| mes | DATETIME | ✓ |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cargo | NUMERIC(16, 6) |  |  |
| abono | NUMERIC(16, 6) |  |  |
| saldocliente | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_saldocliente_clientes: ['clientes'] 
- IX_saldocliente_empresa: ['empresa'] 
- IX_saldocliente_saldocliente: ['saldocliente'] 
- IX_saldocliente_usuario: ['usuario'] 

### Tabla: seccion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nseccion | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| produccion | BIT |  |  |
| administracion | BIT |  |  |
| gerencia | BIT |  |  |
| otros | BIT |  |  |
| activo | BIT |  |  |
| seccion | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |
| correlisss | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| taller | BIT |  |  |
| reloj | BIT |  |  |
| sabsinhorario | BIT |  |  |
| nhorassab | NUMERIC(18, 6) |  |  |

#### Índices
- IX_seccion_empresa: ['empresa'] 
- IX_seccion_nseccion: ['nseccion'] 
- IX_seccion_seccion: ['seccion'] 
- IX_seccion_usuario: ['usuario'] 

### Tabla: sectorlaboral
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nsectorlaboral | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| simbolo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| sectorlaboral | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |

### Tabla: sexo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nsexo | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| sexo | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_sexo_empresa: ['empresa'] 
- IX_sexo_nsexo: ['nsexo'] 
- IX_sexo_sexo: ['sexo'] 
- IX_sexo_usuario: ['usuario'] 

### Tabla: sgzrdy
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| archivo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| hoy | DATETIME | ✓ |  |
| caccesos | INTEGER | ✓ |  |
| equipo | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME | ✓ |  |
| idTabla | INTEGER | ✓ |  |
| didTabla | INTEGER | ✓ |  |
| tabla | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nivel | INTEGER | ✓ |  |
| voriginal | NUMERIC(18, 6) | ✓ |  |
| vNuevo | NUMERIC(18, 6) | ✓ |  |
| usuario | INTEGER | ✓ |  |
| Notas | VARCHAR(350) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| dNotas | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tpermiso | BIT | ✓ |  |
| Empresa | INTEGER | ✓ |  |
| porcentaje | NUMERIC(18, 6) | ✓ |  |
| suporcent | NUMERIC(18, 6) | ✓ |  |
| sgzrdy | INTEGER |  |  |

#### Índices
- sgzrdy_28122012_01: ['equipo', 'tabla', 'idTabla'] 
- sgzrdy_28122012_02: ['equipo', 'idTabla', 'tabla'] 

### Tabla: sheetwork
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dia | DATETIME |  |  |
| activo | BIT |  |  |
| empleado | INTEGER |  |  |
| ingesp | INTEGER |  |  |
| hingesp | INTEGER |  |  |
| hnormal | NUMERIC(18, 6) |  |  |
| hextra | NUMERIC(18, 6) |  |  |
| presentada | BIT |  |  |
| liquidada | BIT |  |  |
| sheetwork | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| camion | INTEGER |  |  |
| rutacamion | INTEGER |  |  |
| jornada | INTEGER |  |  |
| HED | INTEGER |  |  |
| HEN | INTEGER |  |  |
| estaller | BIT |  |  |

#### Foreign Keys
- ['ingesp'] → ingesp.['ingesp']

#### Índices
- IX_sheetwork_empleado: ['dia', 'empleado'] (UNIQUE)

### Tabla: solicitaAutoriza
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| SolicitaAutoriza | INTEGER |  | ✓ |
| accesos | INTEGER |  |  |
| quienautoriza | INTEGER |  |  |
| fechasolicitud | DATETIME |  |  |
| fechaautoriza | DATETIME | ✓ |  |
| concedepermiso | BIT |  |  |
| niegapermiso | BIT |  |  |
| Notas | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: subproyecto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| proyecto | INTEGER |  |  |
| nsubproyecto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fechainicion | DATETIME | ✓ |  |
| fechafin | DATETIME | ✓ |  |
| activo | BIT |  |  |
| encargado | INTEGER |  |  |
| subproyecto | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_subproyecto_descripcion: ['descripcion'] 
- IX_subproyecto_empresa: ['empresa'] 
- IX_subproyecto_encargado: ['encargado'] 
- IX_subproyecto_nsubproyecto: ['nsubproyecto'] 
- IX_subproyecto_proyecto: ['proyecto'] 
- IX_subproyecto_subproyecto: ['subproyecto'] 
- IX_subproyecto_usuario: ['usuario'] 

### Tabla: sucursal
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoBodega | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT | ✓ |  |
| tipoBodega | INTEGER |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| principal | BIT |  |  |
| tercero | BIT |  |  |
| quedan | INTEGER |  |  |
| calculosiniva | BIT |  |  |
| direccion | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prefijo | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prefijo1 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prefijo2 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prefijo3 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| prefijo4 | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| cod_postal | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| correo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nit | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| razon_soc | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nomb_comercial | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| nombre_complemento | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| serie_ini | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| serie_fin | VARCHAR(60) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| _correo | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| _clave | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nosucursal | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| otrodato | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| puerto | VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Establecimiento | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PuntoVenta | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_sucursal_empresa: ['empresa'] 
- IX_sucursal_ntipoBodega: ['ntipoBodega'] 
- IX_sucursal_tipoBodega: ['tipoBodega'] 
- IX_sucursal_usuario: ['usuario'] 

### Tabla: tablacomisiones
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipovendedor | INTEGER |  |  |
| condpago | INTEGER |  |  |
| porcentaje | NUMERIC(18, 6) |  |  |
| horatiempo | DATETIME |  |  |
| tablacomisiones | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

### Tabla: tarea
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tarea | INTEGER |  | ✓ |
| ntarea | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| controles | INTEGER |  |  |
| duracion | DECIMAL(18, 2) | ✓ |  |

#### Índices
- IX_tarea_controles: ['controles'] 
- IX_tarea_ntarea: ['ntarea'] 
- IX_tarea_tarea: ['tarea'] 

### Tabla: tdespacho
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| numedocu | CHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| transpte | INTEGER |  |  |
| motorista | VARCHAR(45) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| placa | VARCHAR(12) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tdespacho | INTEGER |  | ✓ |
| valorfleteton | NUMERIC(16, 6) |  |  |
| valorfleteviaje | NUMERIC(16, 6) |  |  |
| bultos | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| kmsalida | NUMERIC(16, 6) |  |  |
| kmretorno | NUMERIC(16, 6) |  |  |
| kmrecorrido | NUMERIC(16, 6) |  |  |
| descripcion | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| capacidadcont | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| deposito | NUMERIC(16, 6) |  |  |
| peso | NUMERIC(16, 6) |  |  |
| destino | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| activo | BIT |  |  |
| notas | VARCHAR(120) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| cerrado | BIT |  |  |
| caja | INTEGER |  |  |

#### Índices
- IX_tdespacho_bultos: ['bultos'] 
- IX_tdespacho_capacidadcont: ['capacidadcont'] 
- IX_tdespacho_descripcion: ['descripcion'] 
- IX_tdespacho_destino: ['destino'] 
- IX_tdespacho_empresa: ['empresa'] 
- IX_tdespacho_fecha: ['fecha'] 
- IX_tdespacho_motorista: ['motorista'] 
- IX_tdespacho_notas: ['notas'] 
- IX_tdespacho_placa: ['placa'] 
- IX_tdespacho_tdespacho: ['tdespacho'] 
- IX_tdespacho_transpte: ['transpte'] 
- IX_tdespacho_usuario: ['usuario'] 

### Tabla: tiempococina
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| tiempoInicio | DATETIME |  |  |
| dfactura | INTEGER |  |  |
| tiempococina | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: tipcli
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipcli | VARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tipcli | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clave | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cliencatego | INTEGER | ✓ |  |
| agrupar | BIT |  |  |
| agencia | BIT |  |  |
| gobierno | BIT |  |  |
| pdesc | INTEGER |  |  |
| desc1 | INTEGER |  |  |
| desc2 | INTEGER |  |  |
| desc3 | INTEGER |  |  |
| desc4 | INTEGER |  |  |
| desc5 | INTEGER |  |  |
| tipomiembro | INTEGER |  |  |
| aplicadescuento | BIT |  |  |
| tipopago | INTEGER |  |  |
| d1 | BIT |  |  |
| d2 | BIT |  |  |
| d3 | BIT |  |  |
| d4 | BIT |  |  |
| d5 | BIT |  |  |
| d6 | BIT |  |  |
| d7 | BIT |  |  |
| tproddesc | INTEGER |  |  |
| restricciones | INTEGER |  |  |
| miembrofamiliar | BIT |  |  |
| titularcuenta | BIT |  |  |
| miembrohonorario | BIT |  |  |
| agregadomilitar | BIT |  |  |
| cortesia | BIT |  |  |
| visitante | BIT |  |  |
| empleado | BIT |  |  |
| efectivo | NUMERIC(18, 6) |  |  |
| tarjeta | NUMERIC(18, 6) |  |  |
| credito | NUMERIC(18, 6) |  |  |
| mesa | BIT |  |  |
| esmilitar | BIT |  |  |
| pdesc1 | NUMERIC(5, 2) |  |  |
| pdesc2 | NUMERIC(5, 2) |  |  |
| pdesc3 | NUMERIC(5, 2) |  |  |
| pdesc4 | NUMERIC(5, 2) |  |  |
| pdesc5 | NUMERIC(5, 2) |  |  |
| aPlicadesc | BIT |  |  |
| cuota | FLOAT |  |  |
| siPariente | BIT |  |  |
| siPluma | BIT |  |  |
| tienecredito | BIT |  |  |

#### Índices
- IX_tipcli_clave: ['clave'] 
- IX_tipcli_cliencatego: ['cliencatego'] 
- IX_tipcli_empresa: ['empresa'] 
- IX_tipcli_ntipcli: ['ntipcli'] 
- IX_tipcli_tipcli: ['tipcli'] 
- IX_tipcli_usuario: ['usuario'] 

### Tabla: tipcuenta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipcuenta | CHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tipcuenta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_tipcuenta_empresa: ['empresa'] 
- IX_tipcuenta_tipcuenta: ['tipcuenta'] 
- IX_tipcuenta_usuario: ['usuario'] 

### Tabla: tipoBodega
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoBodega | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT | ✓ |  |
| tipoBodega | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_tipoBodega_empresa: ['empresa'] 
- IX_tipoBodega_ntipoBodega: ['ntipoBodega'] 
- IX_tipoBodega_tipoBodega: ['tipoBodega'] 
- IX_tipoBodega_usuario: ['usuario'] 

### Tabla: tipoVehiculo
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nTipoVehiculo | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| TipoVehiculo | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: tipobudget
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipobudget | INTEGER |  | ✓ |
| producto | BIT |  |  |
| vendedor | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| depto | BIT |  |  |
| municip | BIT |  |  |
| ntipobudget | VARCHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| horatiempo | DATETIME |  |  |
| Activo | BIT |  |  |
| Empresa | INTEGER |  |  |
| Usuario | INTEGER |  |  |

#### Índices
- IX_tipobudget_clientes: ['clientes'] 
- IX_tipobudget_Empresa: ['Empresa'] 
- IX_tipobudget_ntipobudget: ['ntipobudget'] 
- IX_tipobudget_tipobudget: ['tipobudget'] 
- IX_tipobudget_Usuario: ['Usuario'] 

### Tabla: tipocta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipocta | CHAR(20) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| cheque | BIT |  |  |
| tipocta | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER | ✓ |  |
| simb | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_tipocta_empresa: ['empresa'] 
- IX_tipocta_simb: ['simb'] 
- IX_tipocta_tipocta: ['tipocta'] 
- IX_tipocta_usuario: ['usuario'] 

### Tabla: tipodato
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| equipo | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| dia | INTEGER |  |  |
| mes | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tipodato | INTEGER |  | ✓ |
| anio | INTEGER |  |  |
| miIp | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| milp | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

### Tabla: tipodatoread
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipodatotxt | INTEGER |  |  |
| tipodato | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tipodatoread | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

### Tabla: tipodatotxt
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dia | DATETIME |  |  |
| txt | VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| tipodatotxt | INTEGER |  | ✓ |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

### Tabla: tipogasto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipogasto | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipogasto | INTEGER |  | ✓ |
| activo | BIT |  |  |
| horatiempo | DATETIME |  |  |
| usuario | INTEGER |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_tipogasto_empresa: ['empresa'] 
- IX_tipogasto_ntipogasto: ['ntipogasto'] 
- IX_tipogasto_tipogasto: ['tipogasto'] 
- IX_tipogasto_usuario: ['usuario'] 

### Tabla: tipoincapacidad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| tipoincapacidad | INTEGER |  | ✓ |
| ntipoincapacidad | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| vacacion | BIT |  |  |
| incapacidad | BIT |  |  |
| nolaborado | BIT |  |  |
| activo | BIT |  |  |
| factor | NUMERIC(5, 2) |  |  |
| factor1 | NUMERIC(5, 2) |  |  |
| dias | INTEGER |  |  |
| cobisss | INTEGER |  |  |

#### Índices
- IX_tipoincapacidad_dias: ['dias'] 
- IX_tipoincapacidad_empresa: ['empresa'] 
- IX_tipoincapacidad_ntipoincapacidad: ['ntipoincapacidad'] 
- IX_tipoincapacidad_tipoincapacidad: ['tipoincapacidad'] 
- IX_tipoincapacidad_usuario: ['usuario'] 

### Tabla: tipomov
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipomov | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| preferido | BIT |  |  |
| factura | BIT |  |  |
| coniva | BIT |  |  |
| iva | BIT |  |  |
| cancelacion | BIT |  |  |
| anulacion | BIT |  |  |
| notacargo | BIT |  |  |
| notadebito | BIT |  |  |
| notacred | BIT |  |  |
| produccion | BIT |  |  |
| cambodega | BIT |  |  |
| devolucion | BIT |  |  |
| efectivo | BIT |  |  |
| cheque | BIT |  |  |
| ajuste | BIT |  |  |
| impuesto | BIT |  |  |
| costo | BIT |  |  |
| bonificacion | BIT |  |  |
| bonifextra | BIT |  |  |
| inventario | BIT |  |  |
| pedido | BIT |  |  |
| invinicial | BIT |  |  |
| nlineasmax | INTEGER |  |  |
| cargo | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| correl | INTEGER |  |  |
| modulo | INTEGER |  |  |
| tipomov | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| compra | BIT |  |  |
| contrato | BIT |  |  |
| ocompra | BIT |  |  |
| informe | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tiquet | BIT |  |  |
| retencion | BIT |  |  |
| bodega | INTEGER |  |  |
| PTOVTA | INTEGER |  |  |
| Movauto | BIT |  |  |
| cd | BIT |  |  |
| cp | BIT |  |  |
| impresor | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| noaplicariva | BIT |  |  |
| docunico | INTEGER |  |  |
| controlcorrel | INTEGER |  |  |
| correlpropio | BIT |  |  |
| qmin | INTEGER |  |  |
| qmax | INTEGER |  |  |
| chequerechazado | BIT |  |  |
| antifactura | BIT |  |  |
| warningcorrel | INTEGER |  |  |
| fwarning | DATETIME | ✓ |  |
| ANTICIPO | BIT |  |  |
| controlcarga | BIT |  |  |
| remision | BIT |  |  |
| ruta | BIT |  |  |
| nccompra | BIT |  |  |
| exportacion | BIT |  |  |
| empaque | BIT |  |  |
| Taller | BIT |  |  |
| notaenvio | BIT |  |  |
| diasparaAnular | INTEGER |  |  |
| oventa | BIT |  |  |
| ncaja | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| caja | INTEGER |  |  |
| ofactura | BIT | ✓ |  |
| IngxDevolucion | BIT |  |  |
| tipoventa | INTEGER |  |  |
| cortesia | BIT |  |  |
| norestariva | BIT |  |  |
| cuenta1 | INTEGER | ✓ |  |
| cuenta | INTEGER | ✓ |  |
| cuenta2 | INTEGER | ✓ |  |
| prodprec | INTEGER |  |  |
| condpago | INTEGER |  |  |
| compuesto | BIT |  |  |

#### Índices
- IX_tipomov_bodega: ['bodega'] 
- IX_tipomov_caja: ['caja'] 
- IX_tipomov_cargo: ['cargo'] 
- IX_tipomov_correl: ['correl'] 
- IX_tipomov_empresa: ['empresa'] 
- IX_tipomov_impresor: ['impresor'] 
- IX_tipomov_informe: ['informe'] 
- IX_tipomov_modulo: ['modulo'] 
- IX_tipomov_ncaja: ['ncaja'] 
- IX_tipomov_nlineasmax: ['nlineasmax'] 
- IX_tipomov_ntipomov: ['ntipomov'] 
- IX_tipomov_PTOVTA: ['PTOVTA'] 
- IX_tipomov_tipomov: ['tipomov'] 
- IX_tipomov_usuario: ['usuario'] 

### Tabla: tipopart
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipopart | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| diario | BIT |  |  |
| banco | BIT |  |  |
| remesa | BIT |  |  |
| tipopart | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| provision | BIT |  |  |
| ingreso | BIT |  |  |
| QUEDAM | BIT |  |  |
| CORRELATIVO | INTEGER |  |  |
| NotaCred | BIT |  |  |
| NotaDebito | BIT |  |  |
| notaremision | INTEGER |  |  |

#### Índices
- IX_tipopart_CORRELATIVO: ['CORRELATIVO'] 
- IX_tipopart_empresa: ['empresa'] 
- IX_tipopart_ntipopart: ['ntipopart'] 
- IX_tipopart_tipopart: ['tipopart'] 
- IX_tipopart_usuario: ['usuario'] 

### Tabla: tipopedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipopedido | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| sinExistencias | BIT |  |  |
| tipoPedido | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: tipopla
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipopla | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| activo | BIT |  |  |
| afp | BIT |  |  |
| prestamos | BIT | ✓ |  |
| patrono | INTEGER | ✓ |  |
| pais | INTEGER | ✓ |  |
| tipopla | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| pla1 | BIT | ✓ |  |
| pla4 | BIT | ✓ |  |
| pla3 | BIT | ✓ |  |
| pla2 | BIT | ✓ |  |
| enproceso | BIT | ✓ |  |
| ndias | INTEGER | ✓ |  |
| vacacion | BIT | ✓ |  |
| INDEMNIZACION | BIT | ✓ |  |
| granja | BIT | ✓ |  |
| aguinaldo | BIT | ✓ |  |
| Noplanilla | INTEGER |  |  |
| reporte | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| SALMAX | NUMERIC(18, 6) |  |  |
| diasminimos | INTEGER |  |  |
| diasaplicados | INTEGER |  |  |
| porcentaje | INTEGER |  |  |
| plazomeses | INTEGER |  |  |
| maxaguinaldo | NUMERIC(18, 6) |  |  |
| reloj | INTEGER |  |  |
| noplaisss | BIT |  |  |
| noplaafp | BIT |  |  |
| hfijo | BIT |  |  |

#### Índices
- IX_tipopla_empresa: ['empresa'] 
- IX_tipopla_ndias: ['ndias'] 
- IX_tipopla_Noplanilla: ['Noplanilla'] 
- IX_tipopla_ntipopla: ['ntipopla'] 
- IX_tipopla_pais: ['pais'] 
- IX_tipopla_patrono: ['patrono'] 
- IX_tipopla_reporte: ['reporte'] 
- IX_tipopla_tipopla: ['tipopla'] 
- IX_tipopla_usuario: ['usuario'] 

### Tabla: tipoprest
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoprest | VARCHAR(80) COLLATE "Modern_Spanish_CI_AS" |  |  |
| bancos | BIT |  |  |
| activo | BIT |  |  |
| procuraduria | BIT |  |  |
| prestamo | BIT |  |  |
| tipoprest | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fsv | BIT |  |  |
| empresa | INTEGER |  |  |
| factor | NUMERIC(8, 2) | ✓ |  |

#### Índices
- IX_tipoprest_empresa: ['empresa'] 
- IX_tipoprest_ntipoprest: ['ntipoprest'] 
- IX_tipoprest_tipoprest: ['tipoprest'] 
- IX_tipoprest_tipoprest1: ['tipoprest'] 
- IX_tipoprest_usuario: ['usuario'] 

### Tabla: tipoprod
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoprod | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| tipoprod | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| margenminimo | NUMERIC(16, 6) |  |  |
| margen | NUMERIC(16, 6) |  |  |
| Llanta | BIT |  |  |
| Bateria | BIT |  |  |
| gasolina | BIT |  |  |
| diesel | BIT |  |  |
| implante | BIT |  |  |
| bebidas | BIT |  |  |
| postres | BIT |  |  |
| ensaladas | BIT |  |  |
| principal | BIT |  |  |
| orden | VARCHAR(6) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| incluir | BIT |  |  |
| adescp | BIT |  |  |
| promosion | BIT |  |  |
| cocina | BIT |  |  |
| mibar | BIT |  |  |
| venta | BIT |  |  |
| otroiva | BIT |  |  |
| desc1 | INTEGER | ✓ |  |
| desc2 | INTEGER | ✓ |  |
| desc3 | INTEGER | ✓ |  |
| desc4 | INTEGER | ✓ |  |
| desc5 | INTEGER | ✓ |  |
| parancel | NUMERIC(18, 6) |  |  |
| Margen2 | NUMERIC(6, 2) |  |  |
| Margen3 | NUMERIC(6, 2) |  |  |
| Margen4 | NUMERIC(6, 2) |  |  |
| Margen5 | NUMERIC(6, 2) |  |  |
| miimagen | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| puno | INTEGER |  |  |
| pdos | INTEGER |  |  |
| ptres | INTEGER |  |  |
| pcuatro | INTEGER |  |  |
| pcinco | INTEGER |  |  |
| vol1 | INTEGER |  |  |
| vol2 | INTEGER |  |  |
| vol3 | INTEGER |  |  |
| vol4 | INTEGER |  |  |
| vol5 | INTEGER |  |  |
| fecha1 | DATETIME | ✓ |  |
| fecha2 | DATETIME | ✓ |  |
| factor1 | INTEGER |  |  |
| factor2 | INTEGER |  |  |
| factor3 | INTEGER |  |  |
| factor4 | INTEGER |  |  |
| factor5 | INTEGER |  |  |
| image | NVARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_tipoprod_empresa: ['empresa'] 
- IX_tipoprod_ntipoprod: ['ntipoprod'] 
- IX_tipoprod_tipoprod: ['tipoprod'] 
- IX_tipoprod_usuario: ['usuario'] 

### Tabla: tipoprov
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoprov | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tipoprov | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| preferido | BIT |  |  |

#### Índices
- IX_tipoprov_empresa: ['empresa'] 
- IX_tipoprov_ntipoprov: ['ntipoprov'] 
- IX_tipoprov_tipoprov: ['tipoprov'] 
- IX_tipoprov_usuario: ['usuario'] 

### Tabla: tiposan
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntiposan | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tiposan | INTEGER |  | ✓ |
| usuario | INTEGER | ✓ |  |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |

#### Índices
- IX_tiposan_empresa: ['empresa'] 
- IX_tiposan_ntiposan: ['ntiposan'] 
- IX_tiposan_tiposan: ['tiposan'] 
- IX_tiposan_usuario: ['usuario'] 

### Tabla: tiposeg
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntiposeg | VARCHAR(80) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tiposeg | INTEGER |  | ✓ |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| empresa | INTEGER |  |  |

#### Índices
- IX_tiposeg_empresa: ['empresa'] 
- IX_tiposeg_ntiposeg: ['ntiposeg'] 
- IX_tiposeg_tiposeg: ['tiposeg'] 
- IX_tiposeg_usuario: ['usuario'] 

### Tabla: tipoviaje
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipoviaje | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipoviaje | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

### Tabla: tipovta
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipovta | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| otra | BIT |  |  |
| normal | BIT |  |  |
| exportacion | BIT |  |  |
| licitacion | BIT |  |  |
| informe | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipovta | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| hora1 | VARCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| hora2 | VARCHAR(8) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

#### Índices
- IX_tipovta_empresa: ['empresa'] 
- IX_tipovta_hora1: ['hora1'] 
- IX_tipovta_hora2: ['hora2'] 
- IX_tipovta_informe: ['informe'] 
- IX_tipovta_ntipovta: ['ntipovta'] 
- IX_tipovta_tipovta: ['tipovta'] 
- IX_tipovta_usuario: ['usuario'] 
- ntipovta_index: ['ntipovta'] (UNIQUE)

### Tabla: tipvende
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ntipvende | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| tipvende | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_tipvende_empresa: ['empresa'] 
- IX_tipvende_ntipvende: ['ntipvende'] 
- IX_tipvende_tipvende: ['tipvende'] 
- IX_tipvende_usuario: ['usuario'] 

### Tabla: tmovkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| id | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecha | DATETIME |  |  |
| ntipomov | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| lote | NUMERIC(16, 6) |  |  |
| bodega | NUMERIC(16, 6) |  |  |
| entrada | NUMERIC(16, 6) |  |  |
| salida | NUMERIC(16, 6) |  |  |
| saldo | NUMERIC(16, 6) |  |  |
| valor | NUMERIC(16, 6) |  |  |
| costouni | NUMERIC(16, 6) |  |  |
| costo | NUMERIC(16, 6) |  |  |
| costoseg | NUMERIC(16, 6) |  |  |
| ordenador | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tmovkardex | INTEGER |  | ✓ |

#### Índices
- IX_tmovkardex_fecha: ['fecha'] 
- IX_tmovkardex_id: ['id'] 
- IX_tmovkardex_ntipomov: ['ntipomov'] 
- IX_tmovkardex_ordenador: ['ordenador'] 
- IX_tmovkardex_tmovkardex: ['tmovkardex'] 

### Tabla: tmpMiKardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| qinvfin | NUMERIC(18, 6) |  |  |
| invfin | NUMERIC(18, 6) |  |  |
| costoprom | NUMERIC(18, 6) |  |  |
| qcompra | NUMERIC(18, 6) |  |  |
| qotrosing | NUMERIC(18, 6) |  |  |
| qingreso | NUMERIC(18, 6) |  |  |
| qsalida | NUMERIC(18, 6) |  |  |
| qventa | NUMERIC(18, 6) |  |  |
| qdevol | NUMERIC(18, 6) |  |  |
| qbonif | NUMERIC(18, 6) |  |  |
| compra | NUMERIC(18, 6) |  |  |
| otrosing | NUMERIC(18, 6) |  |  |
| ingreso | NUMERIC(18, 6) |  |  |
| salida | NUMERIC(18, 6) |  |  |
| venta | NUMERIC(18, 6) |  |  |
| devol | NUMERIC(18, 6) |  |  |
| bonif | NUMERIC(18, 6) |  |  |
| invini | NUMERIC(18, 6) |  |  |
| qinvini | NUMERIC(18, 6) |  |  |
| PRODUCTO | INTEGER |  |  |
| mes | DATETIME | ✓ |  |
| KARDEX | INTEGER | ✓ |  |

### Tabla: tmpProducto
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| producto | INTEGER | ✓ |  |
| qinvfin | NUMERIC(18, 6) |  |  |
| invfin | NUMERIC(18, 6) |  |  |
| costoprom | NUMERIC(18, 6) |  |  |
| qcompra | NUMERIC(18, 6) |  |  |
| qotrosing | NUMERIC(18, 6) |  |  |
| qingreso | NUMERIC(18, 6) |  |  |
| qsalida | NUMERIC(18, 6) |  |  |
| qventa | NUMERIC(18, 6) |  |  |
| qdevol | NUMERIC(18, 6) |  |  |
| qbonif | NUMERIC(18, 6) |  |  |
| compra | NUMERIC(18, 6) |  |  |
| otrosing | NUMERIC(18, 6) |  |  |
| ingreso | NUMERIC(18, 6) |  |  |
| salida | NUMERIC(18, 6) |  |  |
| venta | NUMERIC(18, 6) |  |  |
| devol | NUMERIC(18, 6) |  |  |
| bonif | NUMERIC(18, 6) |  |  |
| invini | NUMERIC(18, 6) |  |  |
| qinvini | NUMERIC(18, 6) |  |  |

### Tabla: tmpkardex
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| qinvfin | NUMERIC(18, 6) |  |  |
| invfin | NUMERIC(18, 6) |  |  |
| costoprom | NUMERIC(18, 6) |  |  |
| qcompra | NUMERIC(18, 6) |  |  |
| qotrosing | NUMERIC(18, 6) |  |  |
| qingreso | NUMERIC(18, 6) |  |  |
| qsalida | NUMERIC(18, 6) |  |  |
| qventa | NUMERIC(18, 6) |  |  |
| qdevol | NUMERIC(18, 6) |  |  |
| qbonif | NUMERIC(18, 6) |  |  |
| compra | NUMERIC(18, 6) |  |  |
| otrosing | NUMERIC(18, 6) |  |  |
| ingreso | NUMERIC(18, 6) |  |  |
| salida | NUMERIC(18, 6) |  |  |
| venta | NUMERIC(18, 6) |  |  |
| devol | NUMERIC(18, 6) |  |  |
| bonif | NUMERIC(18, 6) |  |  |
| invini | NUMERIC(18, 6) |  |  |
| qinvini | NUMERIC(18, 6) |  |  |
| PRODUCTO | INTEGER |  |  |
| mes | DATETIME | ✓ |  |
| KARDEX | INTEGER | ✓ |  |

### Tabla: tocompra
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| ocompra | INTEGER |  |  |
| compra | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tocompra | INTEGER |  | ✓ |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |

#### Índices
- IX_tocompra_compra: ['compra'] 
- IX_tocompra_empresa: ['empresa'] 
- IX_tocompra_ocompra: ['ocompra'] 
- IX_tocompra_tocompra: ['tocompra'] 
- IX_tocompra_usuario: ['usuario'] 

### Tabla: tomafisica
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| tipomov | INTEGER |  |  |
| fecha | DATETIME |  |  |
| impresa | BIT |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| tomafisica | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Foreign Keys
- ['tipomov'] → tipomov.['tipomov']

#### Índices
- IX_tomafisica_empresa: ['empresa'] 
- IX_tomafisica_fecha: ['fecha'] 
- IX_tomafisica_moneda: ['moneda'] 
- IX_tomafisica_notas: ['notas'] 
- IX_tomafisica_tipomov: ['tipomov'] 
- IX_tomafisica_tomafisica: ['tomafisica'] 
- IX_tomafisica_usuario: ['usuario'] 

### Tabla: tpfactura
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| pfactura | INTEGER |  |  |
| factura | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| tpfactura | INTEGER |  | ✓ |

#### Índices
- IX_tpfactura_factura: ['factura'] 
- IX_tpfactura_pfactura: ['pfactura'] 
- IX_tpfactura_tpfactura: ['tpfactura'] 

### Tabla: transnopedido
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| pedido | INTEGER |  |  |
| nopedido | INTEGER |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| transnopedido | INTEGER |  | ✓ |

#### Índices
- IX_transnopedido_empresa: ['empresa'] 
- IX_transnopedido_nopedido: ['nopedido'] 
- IX_transnopedido_pedido: ['pedido'] 
- IX_transnopedido_transnopedido: ['transnopedido'] 
- IX_transnopedido_usuario: ['usuario'] 

### Tabla: transpte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| ntranspte | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| motorista | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| placas | VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| valorfleteton | NUMERIC(16, 6) |  |  |
| valorfleteviaje | NUMERIC(16, 6) |  |  |
| transpte | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| controlcorrel | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| propio | BIT |  |  |
| toneladas | NUMERIC(18, 6) |  |  |
| m3 | NUMERIC(18, 6) |  |  |
| correl | INTEGER |  |  |

#### Índices
- IX_transpte_descripcion: ['descripcion'] 
- IX_transpte_empresa: ['empresa'] 
- IX_transpte_motorista: ['motorista'] 
- IX_transpte_ntranspte: ['ntranspte'] 
- IX_transpte_placas: ['placas'] 
- IX_transpte_transpte: ['transpte'] 
- IX_transpte_usuario: ['usuario'] 

### Tabla: turno
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nturno | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| turno | INTEGER |  | ✓ |
| horatiempo | DATETIME | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuario | INTEGER | ✓ |  |
| activo | BIT | ✓ |  |

#### Índices
- IX_turno_empresa: ['empresa'] 
- IX_turno_nturno: ['nturno'] 
- IX_turno_turno: ['turno'] 
- IX_turno_usuario: ['usuario'] 

### Tabla: ubicaProd
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| uProd | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| producto | INTEGER | ✓ |  |
| caja | INTEGER | ✓ |  |
| empresa | INTEGER |  |  |
| activo | BIT |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| ubicaProd | INTEGER |  | ✓ |

### Tabla: umedida
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| numedida | VARCHAR(40) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| simumedida | VARCHAR(4) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| preferido | BIT |  |  |
| activo | BIT |  |  |
| umedida | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| i | INTEGER |  |  |
| unidad | BIT |  |  |
| factor | NUMERIC(18, 6) |  |  |
| factorut | NUMERIC(18, 6) |  |  |
| ancho | NUMERIC(18, 6) |  |  |
| largo | NUMERIC(18, 6) |  |  |
| alto | NUMERIC(18, 6) |  |  |
| factorm3 | NUMERIC(18, 6) |  |  |
| peso | NUMERIC(18, 6) |  |  |
| peso2 | NUMERIC(18, 6) |  |  |
| esfactor | BIT |  |  |
| ubase | INTEGER |  |  |
| fbase | NUMERIC(12, 2) |  |  |

#### Índices
- IX_umedida_empresa: ['empresa'] 
- IX_umedida_i: ['i'] 
- IX_umedida_numedida: ['numedida'] 
- IX_umedida_simumedida: ['simumedida'] 
- IX_umedida_umedida: ['umedida'] 
- IX_umedida_usuario: ['usuario'] 

### Tabla: unidad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nunidad | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | VARCHAR(75) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| unidad | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_unidad_descripcion: ['descripcion'] 
- IX_unidad_empresa: ['empresa'] 
- IX_unidad_nunidad: ['nunidad'] 
- IX_unidad_unidad: ['unidad'] 
- IX_unidad_usuario: ['usuario'] 

### Tabla: userIdentities
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| Id | NVARCHAR(450) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  | ✓ |
| UserName | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| NormalizedUserName | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Email | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| NormalizedEmail | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| EmailConfirmed | BIT |  |  |
| PasswordHash | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| SecurityStamp | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| ConcurrencyStamp | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PhoneNumber | NVARCHAR COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| PhoneNumberConfirmed | BIT |  |  |
| TwoFactorEnabled | BIT |  |  |
| LockoutEnd | DATETIMEOFFSET | ✓ |  |
| LockoutEnabled | BIT |  |  |
| AccessFailedCount | INTEGER |  |  |
| caja | INTEGER | ✓ |  |

### Tabla: usuario
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nusuario | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| administrador | BIT |  |  |
| acceso | INTEGER |  |  |
| crear | INTEGER |  |  |
| modificar | INTEGER |  |  |
| eliminar | INTEGER |  |  |
| imprimir | INTEGER |  |  |
| excel | INTEGER |  |  |
| reporte | INTEGER |  |  |
| clave | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nota | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| foto | IMAGE | ✓ |  |
| usuario | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| costohora | NUMERIC(18, 6) |  |  |
| roles | INTEGER |  |  |
| lectura | BIT |  |  |
| escritura | BIT |  |  |
| REGISTRADO | BIT |  |  |
| estadocta | BIT |  |  |
| cierremes | BIT |  |  |
| gerencial | BIT |  |  |
| Autoriza | BIT |  |  |
| Supervisa | BIT |  |  |
| Produccion | BIT |  |  |
| administracion | BIT |  |  |
| ventas | BIT |  |  |
| bodega | BIT |  |  |
| puedecorte | BIT |  |  |
| invkardexbloqueado | BIT |  |  |
| supervisor | BIT |  |  |
| vecostos | BIT |  |  |
| puedeBackup | BIT |  |  |
| puedePrecio | BIT |  |  |
| vecompras | BIT |  |  |
| PerfilUsuario | INTEGER |  |  |
| cambiaprecio | BIT |  |  |
| uno | BIT |  |  |
| dos | BIT |  |  |
| tres | BIT |  |  |
| cuatro | BIT |  |  |
| cinco | BIT |  |  |
| seis | BIT |  |  |
| siete | BIT |  |  |
| ocho | BIT |  |  |
| nueve | BIT |  |  |
| diez | BIT |  |  |
| correo | VARCHAR(250) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| conta1 | BIT |  |  |
| conta2 | BIT |  |  |
| conta3 | BIT |  |  |
| conta4 | BIT |  |  |
| conta5 | BIT |  |  |
| conta6 | BIT |  |  |
| vendedor | INTEGER |  |  |
| puedeSupervisor | BIT |  |  |
| otrospermisos | BIT |  |  |
| actualizaprecio | BIT |  |  |
| conta7 | BIT |  |  |
| fechacambio | DATETIME | ✓ |  |
| cambiolaClave | BIT | ✓ |  |
| vecortecaja | BIT |  |  |
| llave | TEXT(2147483647) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| email | VARCHAR(30) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| hash | TEXT(2147483647) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_usuario_acceso: ['acceso'] 
- IX_usuario_clave: ['clave'] 
- IX_usuario_crear: ['crear'] 
- IX_usuario_eliminar: ['eliminar'] 
- IX_usuario_empresa: ['empresa'] 
- IX_usuario_excel: ['excel'] 
- IX_usuario_imprimir: ['imprimir'] 
- IX_usuario_modificar: ['modificar'] 
- IX_usuario_nota: ['nota'] 
- IX_usuario_nusuario: ['nusuario'] 
- IX_usuario_reporte: ['reporte'] 
- IX_usuario_roles: ['roles'] 
- IX_usuario_usuario: ['usuario'] 

### Tabla: usuarioEmpresa
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| usuario | INTEGER | ✓ |  |
| empresa | INTEGER | ✓ |  |
| usuarioEmpresa | INTEGER |  | ✓ |
| activo | BIT |  |  |
| rempresa | INTEGER |  |  |
| rusuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: usuarioseccion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| usuario | INTEGER |  |  |
| seccion | INTEGER | ✓ |  |
| usuarioseccion | INTEGER |  | ✓ |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

### Tabla: vcontabilidad
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| idalumno | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| apellido1 | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| apellido2 | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nombres | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| idcategori | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| DescripC | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| email | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| idcarrera | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| Carrera | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| calleaven | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| numeroc | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| colonibarr | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| pasaje | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| telefijo | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nombred | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| nombremun | NVARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- ci_azure_fixup_dbo_vcontabilidad: ['idalumno'] 

### Tabla: vendclien
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| preferido | BIT |  |  |
| vendedor | INTEGER |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| vendclien | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| pdesc | NUMERIC(5, 2) |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['vendedor'] → vendedor.['vendedor']

#### Índices
- IX_vendclien_clientes: ['clientes'] 
- IX_vendclien_empresa: ['empresa'] 
- IX_vendclien_usuario: ['usuario'] 
- IX_vendclien_vendclien: ['vendclien'] 
- IX_vendclien_vendedor: ['vendedor'] 

### Tabla: vendedor
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| nvendedor | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| fecingreso | DATETIME | ✓ |  |
| fecretiro | DATETIME | ✓ |  |
| lvendedor | BIT |  |  |
| lcobrador | BIT |  |  |
| activo | BIT |  |  |
| tipvende | INTEGER |  |  |
| vendedor | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| bodega | INTEGER |  |  |
| noCAJERO | BIT |  |  |
| prodprec | INTEGER |  |  |
| fqmin | INTEGER |  |  |
| fqmax | INTEGER |  |  |
| cqmin | INTEGER |  |  |
| cqmax | INTEGER |  |  |
| fcorrel | INTEGER |  |  |
| ccorrel | INTEGER |  |  |
| tipomov | INTEGER |  |  |
| pqmin | INTEGER |  |  |
| pqmax | INTEGER |  |  |
| pcorrel | INTEGER |  |  |
| rqmin | INTEGER |  |  |
| rqmax | INTEGER |  |  |
| rcorrel | INTEGER |  |  |
| controlcorrel | INTEGER |  |  |
| zonavendedor | INTEGER |  |  |
| fact1 | INTEGER |  |  |
| fact2 | INTEGER |  |  |
| ccf1 | INTEGER |  |  |
| ccf2 | INTEGER |  |  |
| FACT | INTEGER |  |  |
| ccf | INTEGER |  |  |
| Pagos1 | INTEGER |  |  |
| Pagos2 | INTEGER |  |  |
| Pagos | INTEGER |  |  |
| recibo1 | INTEGER |  |  |
| recibo2 | INTEGER |  |  |
| recibo | INTEGER |  |  |
| vcorreo | VARCHAR(100) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cajero | BIT |  |  |
| cuota | NUMERIC(18, 6) |  |  |
| VENDEDOR1 | INTEGER |  |  |
| Mesero | BIT |  |  |
| pedidomin | INTEGER |  |  |
| pedidocorr | INTEGER |  |  |
| pedidomax | INTEGER |  |  |
| clave | INTEGER |  |  |
| tipovendedor | INTEGER |  |  |
| descrip | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| idvend | VARCHAR(15) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |

#### Índices
- IX_vendedor_bodega: ['bodega'] 
- IX_vendedor_ccf: ['ccorrel'] 
- IX_vendedor_ccf1: ['cqmin'] 
- IX_vendedor_ccf2: ['cqmax'] 
- IX_vendedor_clientes: ['clientes'] 
- IX_vendedor_empresa: ['empresa'] 
- IX_vendedor_FACT: ['fcorrel'] 
- IX_vendedor_fact1: ['fqmin'] 
- IX_vendedor_fact2: ['fqmax'] 
- IX_vendedor_nvendedor: ['nvendedor'] 
- IX_vendedor_prodprec: ['prodprec'] 
- IX_vendedor_tipomov: ['tipomov'] 
- IX_vendedor_tipvende: ['tipvende'] 
- IX_vendedor_usuario: ['usuario'] 
- IX_vendedor_vendedor: ['vendedor'] 

### Tabla: ventascc
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| numedocu | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| fecha | DATETIME |  |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| exportacion | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| serie | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| iva | INTEGER |  |  |
| periodoiva | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| ventascc | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| retencion | NUMERIC(16, 6) |  |  |
| factor | NUMERIC(16, 6) |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| tipomov | INTEGER |  |  |
| otro | NUMERIC(16, 6) |  |  |
| PEDIDO | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| cotrans | NUMERIC(18, 6) |  |  |
| tipobodega | INTEGER |  |  |
| CCREF | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| docunico | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| factura | INTEGER |  |  |
| pagos | INTEGER |  |  |
| importado | BIT |  |  |
| cuenta | INTEGER | ✓ |  |
| partida | INTEGER | ✓ |  |
| tarjeta | NUMERIC(9, 2) | ✓ |  |
| CESC | NUMERIC(9, 2) |  |  |

#### Foreign Keys
- ['clientes', 'empresa'] → clientes.['clientes', 'empresa']
- ['periodoiva'] → periodoiva.['periodoiva']

#### Índices
- IX_ventascc_CCREF: ['CCREF'] 
- IX_ventascc_clientes: ['clientes'] 
- IX_ventascc_empresa: ['empresa'] 
- IX_ventascc_fecha: ['fecha'] 
- IX_ventascc_iva: ['iva'] 
- IX_ventascc_moneda: ['moneda'] 
- IX_ventascc_PEDIDO: ['PEDIDO'] 
- IX_ventascc_periodoiva: ['periodoiva'] 
- IX_ventascc_serie: ['serie'] 
- IX_ventascc_tipobodega: ['tipobodega'] 
- IX_ventascc_tipomov: ['tipomov'] 
- IX_ventascc_usuario: ['usuario'] 
- IX_ventascc_ventascc: ['ventascc'] 

### Tabla: ventascon
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| fecha | DATETIME |  |  |
| docini | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| docfin | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" | ✓ |  |
| afecta | NUMERIC(16, 6) |  |  |
| exenta | NUMERIC(16, 6) |  |  |
| exportacion | NUMERIC(16, 6) |  |  |
| viva | NUMERIC(16, 6) |  |  |
| serie | VARCHAR(1) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| iva | INTEGER |  |  |
| periodoiva | INTEGER |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| ventascon | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |
| fovial | NUMERIC(16, 6) |  |  |
| ncaja | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| tipomov | INTEGER |  |  |
| nueva | BIT |  |  |
| cotrans | NUMERIC(18, 6) |  |  |
| tipobodega | INTEGER |  |  |
| ccref | VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| percepcion | NUMERIC(18, 6) |  |  |
| nosujeto | NUMERIC(18, 6) |  |  |
| factura | INTEGER |  |  |
| importado | BIT |  |  |
| total | NUMERIC(18, 6) |  |  |
| retencion | NUMERIC(18, 6) |  |  |
| cuenta | INTEGER | ✓ |  |
| partida | INTEGER | ✓ |  |
| tarjeta | INTEGER | ✓ |  |
| CESC | NUMERIC(9, 2) |  |  |

#### Foreign Keys
- ['periodoiva'] → periodoiva.['periodoiva']

#### Índices
- IX_ventascon_empresa: ['empresa'] 
- IX_ventascon_fecha: ['fecha'] 
- IX_ventascon_iva: ['iva'] 
- IX_ventascon_moneda: ['moneda'] 
- IX_ventascon_ncaja: ['ncaja'] 
- IX_ventascon_periodoiva: ['periodoiva'] 
- IX_ventascon_serie: ['serie'] 
- IX_ventascon_tipobodega: ['tipobodega'] 
- IX_ventascon_tipomov: ['tipomov'] 
- IX_ventascon_usuario: ['usuario'] 
- IX_ventascon_ventascon: ['ventascon'] 

### Tabla: vretencion
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| activo | BIT |  |  |
| clientes | VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numedocu | CHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| numedocux | VARCHAR(9) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| factura | INTEGER |  |  |
| fecha | DATETIME |  |  |
| nula | BIT |  |  |
| notas | VARCHAR(150) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| moneda | INTEGER |  |  |
| tasacambio | NUMERIC(16, 6) |  |  |
| tasacambioseg | NUMERIC(16, 6) |  |  |
| tasacambiotres | NUMERIC(16, 6) |  |  |
| montfact | NUMERIC(16, 6) |  |  |
| vretencion | INTEGER |  | ✓ |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_vretencion_clientes: ['clientes'] 
- IX_vretencion_empresa: ['empresa'] 
- IX_vretencion_factura: ['factura'] 
- IX_vretencion_fecha: ['fecha'] 
- IX_vretencion_moneda: ['moneda'] 
- IX_vretencion_notas: ['notas'] 
- IX_vretencion_numedocux: ['numedocux'] 
- IX_vretencion_usuario: ['usuario'] 
- IX_vretencion_vretencion: ['vretencion'] 

### Tabla: xdte
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| dte | SMALLINT |  |  |
| ncatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| catalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| scatalogo | NVARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| descripcion | NVARCHAR(200) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |

### Tabla: zona
#### Columnas
| Nombre | Tipo | Nullable | Primary Key |
|--------|------|----------|-------------|
| zona | INTEGER |  | ✓ |
| nzona | VARCHAR(35) COLLATE "SQL_Latin1_General_CP1_CI_AS" |  |  |
| activo | BIT |  |  |
| empresa | INTEGER |  |  |
| usuario | INTEGER |  |  |
| horatiempo | DATETIME |  |  |

#### Índices
- IX_zona_empresa: ['empresa'] 
- IX_zona_nzona: ['nzona'] 
- IX_zona_usuario: ['usuario'] 
- IX_zona_zona: ['zona'] 

