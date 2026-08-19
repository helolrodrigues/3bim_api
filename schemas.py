from pydantic import BaseModel
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass
class ProdutoResponse(ProdutoBase):
    id: int
    
class Config:
    from_attributes = True



class EventoBase(BaseModel):
    nome: str
    local: str
    preco: float
    data_evento: float
    quantidade: int

class EventoCreate(EventoBase):
    pass
class EventoResponse(EventoBase):
    id: int
    
class Config:
    from_attributes = True
