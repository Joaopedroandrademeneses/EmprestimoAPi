from fastapi import APIRouter
from schemas.brinquedo import BrinquedoOut,BriquedoCreate
from services.emprestimo_API import criar_briquedo, lista_brinquedo

router=APIRouter(prefix="/brinquedo", tags=["Brinquedo"])

@router.post("",response_model=BrinquedoOut)
def post_brinquedo(brinquedo:BriquedoCreate):
    return criar_briquedo(brinquedo)

@router.get("",response_model=list[BrinquedoOut])
def get_brinquedo():
    return lista_brinquedo()