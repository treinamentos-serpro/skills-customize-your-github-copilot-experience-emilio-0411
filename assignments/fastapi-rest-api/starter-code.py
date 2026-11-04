"""
Atividade: Building REST APIs com FastAPI
=========================================

Como rodar a API:
    1. Instale as dependências:  pip install fastapi uvicorn
    2. Inicie o servidor:        uvicorn starter-code:app --reload
    3. Acesse a documentação:    http://127.0.0.1:8000/docs

Complete os TODOs abaixo seguindo as tarefas do README.md. Boa sorte! 🚀
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas - Mergington High School")


# Modelo de dados: o FastAPI usa esta classe para validar
# automaticamente os dados recebidos nas requisições.
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str = ""
    completed: bool = False


# "Banco de dados" em memória com algumas tarefas de exemplo
tasks: list[Task] = [
    Task(id=1, title="Estudar FastAPI", description="Ler a documentação oficial", completed=False),
    Task(id=2, title="Fazer lição de matemática", description="Exercícios do capítulo 5", completed=True),
    Task(id=3, title="Projeto de ciências", description="Preparar apresentação", completed=False),
]


# ---------------------------------------------------------------
# Tarefa 1: Hello API
# ---------------------------------------------------------------
# TODO: Crie um endpoint GET / que retorna uma mensagem de boas-vindas.
# Dica: use o decorator @app.get("/") em uma função que retorna um dicionário.


# ---------------------------------------------------------------
# Tarefa 2: Listar e Buscar Tarefas
# ---------------------------------------------------------------
# TODO: Crie um endpoint GET /tasks que retorna a lista de tarefas.


# TODO: Crie um endpoint GET /tasks/{task_id} que retorna a tarefa com o id informado.
# Dica: se nenhuma tarefa tiver esse id, lance:
#     raise HTTPException(status_code=404, detail="Tarefa não encontrada")


# ---------------------------------------------------------------
# Tarefa 3: Criar e Atualizar Tarefas
# ---------------------------------------------------------------
# TODO: Crie um endpoint POST /tasks que recebe uma Task no corpo da
# requisição, gera um novo id e adiciona a tarefa à lista.
# Assinatura sugerida:
#     def create_task(task: Task) -> Task:


# TODO: Crie um endpoint PUT /tasks/{task_id} que atualiza uma tarefa existente.
# Lembre-se de retornar 404 se a tarefa não existir.


# ---------------------------------------------------------------
# Tarefa 4 (Desafio): Filtros e Remoção
# ---------------------------------------------------------------
# TODO: Modifique o endpoint GET /tasks para aceitar um query parameter
# opcional "completed" e filtrar as tarefas.
# Assinatura sugerida:
#     def list_tasks(completed: Optional[bool] = None) -> list[Task]:


# TODO: Crie um endpoint DELETE /tasks/{task_id} que remove a tarefa da lista.
# Lembre-se de retornar 404 se a tarefa não existir.
