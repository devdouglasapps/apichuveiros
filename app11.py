from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    item: str
    status: str
    quantidade_tempo: int

chuveiros = {
    1: {
        "item": "chuveiro 1",
        "status": "ligado",
        "quantidade_tempo": 5
    },
    2: {"item": "chuveiro 2", "status": "ligado", "quantidade_tempo": 8},
    3: {"item": "chuveiro 3", "status": "desligado", "quantidade_tempo": 5},
    4: {"item": "chuveiro 4", "status": "ligado", "quantidade_tempo": 12},
}


@app.get("/")
def todos_chuveiros():
    return {"Chuveiros": (chuveiros)}


@app.get("/chuveiros/{id_chuveiro}")
def pegar_chuveiro(id_chuveiro: int):
    if id_chuveiro in chuveiros:
        return chuveiros[id_chuveiro]
    else:
        return {"Erro": "ID Chuveiro não encontrado"}
    
@app.put("/chuveiros/{item_id}")
def update_item(id_chuveiro: int, chuveiro: Item):
    return {"item": chuveiro.item, "status": chuveiro.status, "quantidade_tempo": chuveiro.quantidade_tempo}
