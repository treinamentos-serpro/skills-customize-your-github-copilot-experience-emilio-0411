# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Nesta atividade você vai construir sua primeira API REST usando o framework **FastAPI**! Você criará uma API de gerenciamento de tarefas escolares, aprendendo passo a passo a criar endpoints para listar, buscar, criar, atualizar e remover dados. Ao final, você terá uma API completa com validação automática de dados e documentação interativa — habilidades essenciais para o desenvolvimento web moderno. 🚀

> 💡 **Dica**: use o arquivo `starter-code.py` como ponto de partida. Para rodar sua API, execute `uvicorn starter-code:app --reload` e acesse `http://127.0.0.1:8000/docs` para ver a documentação interativa gerada automaticamente!

## 📝 Tarefas

### 🛠️	Hello API

#### Descrição
Todo grande projeto começa com um primeiro passo! Crie um endpoint `GET /` que dá as boas-vindas aos usuários da sua API. Essa tarefa vai ajudar você a entender como o FastAPI transforma uma função Python em um endpoint web.

#### Requisitos
O programa concluído deve:

- Definir um endpoint `GET /` usando o decorator `@app.get("/")`
- Retornar um dicionário com uma mensagem de boas-vindas, por exemplo: `{"message": "Bem-vindo à API de Tarefas!"}`
- Rodar sem erros e responder corretamente ao acessar `http://127.0.0.1:8000/`


### 🛠️	Listar e Buscar Tarefas

#### Descrição
Agora vamos trabalhar com dados de verdade! Sua API armazena uma lista de tarefas em memória. Crie endpoints para listar todas as tarefas e para buscar uma tarefa específica pelo seu `id`, usando *path parameters*.

#### Requisitos
O programa concluído deve:

- Definir um endpoint `GET /tasks` que retorna a lista completa de tarefas
- Definir um endpoint `GET /tasks/{task_id}` que retorna apenas a tarefa com o `id` informado
- Retornar um erro `404` com uma mensagem clara (usando `HTTPException`) quando o `id` não existir


### 🛠️	Criar e Atualizar Tarefas

#### Descrição
Uma API de verdade precisa aceitar dados novos! Usando o modelo Pydantic `Task` do starter code, crie endpoints para adicionar novas tarefas e atualizar tarefas existentes. O FastAPI validará os dados recebidos automaticamente — experimente enviar dados inválidos e veja o que acontece!

#### Requisitos
O programa concluído deve:

- Definir um endpoint `POST /tasks` que recebe uma tarefa no corpo da requisição e a adiciona à lista
- Gerar automaticamente o `id` da nova tarefa (não confie no `id` enviado pelo cliente)
- Definir um endpoint `PUT /tasks/{task_id}` que atualiza os dados de uma tarefa existente
- Retornar erro `404` ao tentar atualizar uma tarefa que não existe


### 🛠️	Desafio: Filtros e Remoção

#### Descrição
Hora de ir além! 💪 Adicione suporte a *query parameters* para filtrar tarefas e crie um endpoint para remover tarefas. Esse é o toque final para sua API ter todas as operações CRUD (Create, Read, Update, Delete)!

#### Requisitos
O programa concluído deve:

- Permitir filtrar tarefas concluídas ou pendentes com um query parameter, por exemplo: `GET /tasks?completed=true`
- Manter o comportamento atual de `GET /tasks` quando nenhum filtro for informado
- Definir um endpoint `DELETE /tasks/{task_id}` que remove a tarefa da lista
- Retornar erro `404` ao tentar remover uma tarefa que não existe
