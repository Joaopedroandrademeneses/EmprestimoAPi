from pydantic import BaseModel

class BriquedoCreate(BaseModel):
    id:int
    nome:str
    categoria:str
    faixa_etaria_minima:int
    disponivel:bool= True
class BrinquedoOut(BaseModel):
    id:int
    nome:str
    categoria:str
    faixa_etaria_minima:int
    disponivel:bool