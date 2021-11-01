from fastapi import FastAPI

app = FastAPI()
TAREFA = []

@app.get("/tarefa")
def listar():
    return TAREFA