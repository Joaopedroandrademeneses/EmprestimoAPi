from fastapi import FastAPI
from api.router.crianças import router as crianca_router
from api.router.brinquedos import router as brinquedo_router
from api.router.emprestimos import router as emprestimo_router


app=FastAPI(title="Api funcionando")


@app.get("/")
def home():
    return{"msg":"Emprestimo api funcionando"}
app.include_router(brinquedo_router)
app.include_router(crianca_router)
app.include_router(emprestimo_router)