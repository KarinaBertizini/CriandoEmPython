from fastapi.testclient import TestClient
from fastapi import applications, status
from gerenciador_tarefa.gerenciador import app, TAREFA


def test_lista_tarefa_retorno_200():
    client = TestClient(app)
    response = client.get("/tarefa")
    assert response.status_code == status.HTTP_200_OK


def test_lista_tarefas_formato_json():
    client = TestClient(app)
    response = client.get("/tarefa")
    assert response.headers['Content-Type'] == "application/json"
    

def test_lista_tarefas_formato_lista():
    client = TestClient(app)
    response = client.get("/tarefa")
    assert isinstance(response.json(), list)


def test_listar_tarefa_retorno_id():
    TAREFA.append({"id": 1})
    client = TestClient(app)
    response = client.get("/tarefa")
    assert "id" in response.json().pop()
    TAREFA.clear()


def test_listar_tarefa_retorno_titulo():
    TAREFA.append({"titulo": "Boku no Hero"})
    client = TestClient(app)
    response = client.get("/tarefa")
    assert "titulo" in response.json().pop()
    TAREFA.clear()


def test_listar_tarefa_retorno_descricao():
    TAREFA.append({"descricao": "anime"})
    client = TestClient(app)
    response = client.get("/tarefa")
    assert "descricao" in response.json().pop()
    TAREFA.clear()


def test_listar_tarefa_retorno_estado():
    TAREFA.append({"estado": "lancando"})
    client = TestClient(app)
    response = client.get("/tarefa")
    assert "estado" in response.json().pop()
    TAREFA.clear()
