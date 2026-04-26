from domain.brinquedo import Brinquedo
from domain.crianca import Crianca
from domain.emprestimo import Emprestimo
from repository.memory import db


def criar_crianca(data):
    crianca=Crianca(data.id,data.nome,data.idade,data.responsavel)
    db.criancas[crianca.id]=crianca
    return crianca

def lista_crianca():
    return list(db.criancas.values())

#----------------------------------------------------------
def criar_briquedo(data):
    brinquedo=Brinquedo(data.id,data.nome,data.categoria,data.faixa_etaria_minima,True)
    db.briquedos[brinquedo.id]=brinquedo
    return brinquedo

def lista_brinquedo():
    return list(db.briquedos.values())

#----------------------------------------------------------
def criar_emprestimo(id: int, brinquedo_id: int, datas: str, multa: float, crianca_id: list = [], status: bool = True):
    emprestimo = Emprestimo(
        id=id,
        brinquedo_id=brinquedo_id,
        datas=datas,
        multa=multa,
        crianca_id=crianca_id
    )
    db.emprestimos[emprestimo.id] = emprestimo
    return emprestimo

def listar_emprestimos():
    return list(db.emprestimos.values())

def buscar_emprestimo(id):
    return db.emprestimos.get(id)

def alterar_emprestimos_id(id,crianca_id):
    emprestimo=db.emprestimos.get(id)
    if not emprestimo:
        return None 
    
    if crianca_id<0:
        raise ValueError("Id criança não pode ser negativo") 
    
    if len(emprestimo.crianca_id)==2:
        emprestimo.status=True

    emprestimo.crianca_id.remove(crianca_id)
    return emprestimo

def buscar_emprestimos_crianca_id(crianca_id):
    for emprestimo in db.emprestimos.values():
        if crianca_id in emprestimo.crianca_id:
            return emprestimo
    raise ValueError("Crianca não encontrada")
    