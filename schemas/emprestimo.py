from pydantic import BaseModel
from typing import List

class EmprestimoCreate(BaseModel):
    id: int
    brinquedo_id: int
    datas: str
    status: bool = True
    crianca_id: List[int] = []

class EmprestimoOut(BaseModel):
    multa: float
    crianca_id: List[int] = []
    status: bool
    id: int
    brinquedo_id: int
    datas: str
    