from fastapi import FastAPI
from pydantic import BaseModel  # Importa a classe BaseModel para definir a estrutura do modelo
from typing import Dict

# Define a classe modelo para representar os dados do chuveiro
class Chuveiro(BaseModel):
    id: int
    item: str
    status: str
    quantidade_tempo: int

# Cria uma instancia de FastAPI
app = FastAPI()

# Armazenamento de dados na memória para chuveiros
chuveiro_db: Dict[int, Chuveiro] = {}

# ID inicial para os chuveiros
chuveiro_id_counter = 1

@app.get("/")
def ler_raiz():
    return {"Mensagem": "Bem vindo a API de Chuveiros"}

@app.post("/chuveiros/")
def criar_chuveiro(chuveiro: Chuveiro):
    global chuveiro_id_counter
    chuveiro.id = chuveiro_id_counter
    chuveiro_db[chuveiro.id] = chuveiro
    chuveiro_id_counter += 1
    return {"Mensagem": "Chuveiro adicionado com sucesso!!"}

@app.get("/chuveiros")
def todos_chuveiros():
    return {"Chuveiros": list(chuveiro_db.values())}

@app.get("/chuveiros/{chuveiro_id}")
def mostrar_chuveiro_id(chuveiro_id: int):
    if chuveiro_id in chuveiro_db:
        return chuveiro_db[chuveiro_id]
    return {"Mensagem": "Chuveiro não encontrado"}

@app.put("/chuveiros/{chuveiro_id}")
def atualizar_chuveiro(chuveiro_id: int, chuveiro_atualizado: Chuveiro):
    if chuveiro_id in chuveiro_db:
        chuveiro_atualizado.id = chuveiro_id
        chuveiro_db[chuveiro_id] = chuveiro_atualizado
        return {"Mensagem": f"Chuveiro atualizado com ID: {chuveiro_id}"}
    return {"Mensagem": "Chuveiro não encontrado"}

@app.delete("/chuveiros/{chuveiro_id}")
def eliminar_chuveiro(chuveiro_id: int):
    if chuveiro_id in chuveiro_db:
        del chuveiro_db[chuveiro_id]
        return {"mensagem": f"Chuveiro eliminado com ID: {chuveiro_id}"}
    return {"mensagem": "Chuveiro não encontrado"}