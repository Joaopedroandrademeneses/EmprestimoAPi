from fastapi import APIRouter
from schemas.crianca import CriancaCreate,CriancaOut
from services.emprestimo_API import criar_crianca, lista_crianca

router=APIRouter(prefix="/crianca", tags=["Crianca"])

@router.post("",response_model=CriancaOut)
def post_crianca(crianca:CriancaCreate):
    return criar_crianca(crianca)


router.get("",response_model=list[CriancaOut])
def get_crianca():
    return lista_crianca()