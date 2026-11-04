# 📘 Tarefa: Jogos em Python

## 🎯 Objetivo

Construa o clássico Jogo da Forca em Python! Nesta atividade, você vai praticar manipulação de strings, loops, condicionais e seleção aleatória, criando um jogo em que o jogador adivinha letras para revelar uma palavra oculta antes que as tentativas acabem.

## 📝 Tarefas

### 🛠️ Preparar o Jogo

#### Descrição
Configure o estado inicial do jogo: selecione a palavra secreta e inicialize as variáveis que controlarão o progresso do jogador.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida usando o módulo `random`.
- Inicializar uma estrutura para armazenar as letras já adivinhadas.
- Definir um contador de tentativas incorretas e um limite máximo de erros.

### 🛠️ Implementar o Loop Principal do Jogo

#### Descrição
Crie o loop que mantém o jogo em andamento, exibindo o progresso, recebendo palpites do jogador e atualizando o estado do jogo a cada rodada.

#### Requisitos
O programa concluído deve:

- Exibir o progresso atual da palavra, mostrando `_` para letras não descobertas (formato `_ _ _`).
- Aceitar palpites de letras do usuário por meio de `input()`.
- Verificar se a letra está na palavra secreta e atualizar as letras adivinhadas ou o contador de erros.
- Mostrar quantas tentativas incorretas ainda restam.

### 🛠️ Encerrar o Jogo

#### Descrição
Finalize a partida detectando as condições de vitória ou derrota e exibindo uma mensagem adequada ao jogador.

#### Requisitos
O programa concluído deve:

- Encerrar o loop quando a palavra for completamente adivinhada ou quando as tentativas se esgotarem.
- Exibir uma mensagem de vitória revelando a palavra quando o jogador vencer.
- Exibir uma mensagem de derrota informando a palavra secreta quando as tentativas acabarem.
