"""Atividade: Persistência de Dados com SQLite e FastAPI
=======================================================

Como rodar a API:
    1. Instale as dependências:  pip install fastapi uvicorn
    2. Inicie o servidor:        uvicorn starter-code:app --reload
    3. Acesse a documentação:    http://127.0.0.1:8000/docs

Complete os TODOs seguindo as tarefas do README.md.
"""

import sqlite3
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Tarefas com SQLite - Mergington High School")
DATABASE_PATH = Path(__file__).with_name("tasks.db")


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str = ""
    completed: bool = False


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        completed=bool(row["completed"]),
    )


initialize_database()


# TODO: Implemente GET /tasks para consultar e retornar as tarefas do banco.
# Aceite um query parameter opcional "completed" para filtrar os resultados.


# TODO: Implemente GET /tasks/{task_id} para buscar uma tarefa pelo ID.
# Retorne HTTP 404 quando o banco não contiver esse ID.


# TODO: Implemente POST /tasks para inserir uma tarefa no banco.
# Use o ID gerado pelo SQLite na resposta e não confie no ID enviado pelo cliente.


# TODO: Implemente PUT /tasks/{task_id} para atualizar título, descrição e status.
# Retorne HTTP 404 quando a tarefa não existir.


# TODO: Implemente DELETE /tasks/{task_id} para remover uma tarefa.
# Retorne HTTP 404 quando a tarefa não existir.