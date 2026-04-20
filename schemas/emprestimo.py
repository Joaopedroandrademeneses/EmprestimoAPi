from pydantic import BaseModel

class EmprestimoCreate(BaseModel):
    id:int
    brinquedo_id:int
    datas: str
    status:bool=True
    crianca_id=int
    

class EmprestimoOut(BaseModel):
    multa: float
    crianca_id:int =[]
    status:bool
    id:int
    brinquedo_id:int
    datas: str
    