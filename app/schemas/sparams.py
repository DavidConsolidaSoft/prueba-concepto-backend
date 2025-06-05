from pydantic import BaseModel, ConfigDict

class ParamsBase(BaseModel):
    nombre: str
    nusuario: str
    cc: str
    empresa: int
    caja: int
    bodega: int
    vendedor: int
    prodprec: int

class ParamsCreate(ParamsBase):
    pass

class ParamsResponse(ParamsBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)