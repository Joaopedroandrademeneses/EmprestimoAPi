from fastapi import APIRouter, HTTPException
from schemas.emprestimo import EmprestimoCreate, EmprestimoOut
from services.emprestimo_API import (
    criar_emprestimo,
    buscar_emprestimo,
    buscar_emprestimos_crianca_id,
    listar_emprestimos,
    alterar_emprestimos_id)

router = APIRouter(prefix="/emprestimos", tags=["Emprestimos"])

@router.post("", response_model=EmprestimoOut)
def post_emprestimo(data: EmprestimoCreate):
    return criar_emprestimo(data.id, data.brinquedo_id, data.datas, 0.0, data.crianca_id, data.status)

@router.get("", response_model=list[EmprestimoOut])
def get_emprestimos():
    return listar_emprestimos()

@router.get("/{id}", response_model=EmprestimoOut)
def get_emprestimo_por_id(id: int):
    emprestimo = buscar_emprestimo(id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Emprestimo nao encontrado")
    return emprestimo

@router.get("/crianca/{crianca_id}", response_model=EmprestimoOut)
def get_emprestimo_crianca(crianca_id: int):
    try:
        emprestimo = buscar_emprestimos_crianca_id(crianca_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Crianca emprestimo não encontrado")
    return emprestimo

@router.put("/{id}/emprestimo", response_model=EmprestimoOut)
def put_emprestimo(id: int, crianca_id: int):
    emprestimo = alterar_emprestimos_id(id, crianca_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Emprestimo não existe")
    return emprestimo