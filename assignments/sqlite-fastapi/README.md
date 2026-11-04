# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Adapte a API de tarefas criada com FastAPI para armazenar os dados em um banco SQLite. Você vai praticar consultas SQL parametrizadas e perceber como a persistência mantém os dados mesmo depois que o servidor é reiniciado.

## 📝 Tarefas

### 🛠️ Consultar Tarefas no Banco de Dados

#### Descrição
Substitua as consultas à lista em memória por consultas ao banco SQLite. Use o modelo `Task` e as funções auxiliares do starter code para transformar os registros do banco em respostas da API.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para listar as tarefas armazenadas
- Implementar `GET /tasks/{task_id}` para buscar uma tarefa pelo ID
- Retornar erro `404` quando o ID solicitado não existir
- Usar consultas SQL parametrizadas, sem montar comandos SQL concatenando valores recebidos

### 🛠️ Criar e Atualizar Tarefas

#### Descrição
Faça os endpoints de escrita salvarem as alterações no SQLite. O banco deve gerar o ID de cada nova tarefa, e a API deve continuar validando os dados recebidos com o modelo Pydantic `Task`.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para inserir uma tarefa no banco e retornar seu ID gerado
- Ignorar qualquer ID enviado pelo cliente ao criar uma tarefa
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente
- Retornar erro `404` ao tentar atualizar uma tarefa inexistente

### 🛠️ Remover, Filtrar e Verificar Persistência

#### Descrição
Complete as operações da API e confira que o SQLite preserva as mudanças entre execuções. Teste os endpoints pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /tasks/{task_id}` e retornar erro `404` se a tarefa não existir
- Permitir filtrar tarefas concluídas ou pendentes em `GET /tasks?completed=true` ou `GET /tasks?completed=false`
- Manter `GET /tasks` sem filtro para listar todas as tarefas
- Criar uma tarefa, reiniciar o servidor e confirmar que ela continua disponível
- Confirmar que as operações de atualizar e remover também persistem após reiniciar o servidor