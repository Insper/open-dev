# Dependências e serviços usados

## Quais tecnologias são usadas no código? Além da linguagem de programação, liste também as bibliotecas/módulos externos usados.

- Linguagens: Python, SQL, HTML, JS, CSS, SCSS
- Tecnologias: sqlite, hashlib, flask, bootstrap

## A aplicação utiliza um banco de dados. Qual gerenciador? Onde a aplicação busca a base de dados? Quais são as tabelas usadas? Como elas são criadas?

Utiliza sim, o SQLite.

- No arquivo softdes.py existem algumas consultas SQL para:
  Pegar todos os Quizes,
  Pegar um USERQUIZ,
  Inserir na tabela USERQUIZ,
  Pegar um Quiz,
  Setar o password do usuário,

- No arquivo adduser.py existe uma consulta SQL para:
  Adicionar um novo usuário

- As tabelas utilizadas são 3: USER, USERQUIZ, QUIZ. Elas são criadas no arquivo quiz.sql

# Deploy inicial

## A aplicação usa autenticação? Se sim, qual tipo? Como usuários são criados? Existe algum usuário administrador? Como é feita a segurança das senhas? Qual a senha padrão?

A aplicação utiliza autenticação, feita através do HTTPBasicAuth do flask. Os usuários são criados a partir do script adduser.py, que lê um arquivo csv e cria usuários no banco de dados. O nome do usuário é encriptado para um hash utilizando a hashlib. Pelo código que existe em softdes.py, sabemos que existe um usuário chamado admin e outro chamado fabioja. Dessa forma a senha dos dois será o hash dessas palavras.

## Quais comandos você usou para rodar a aplicação? Escreva todos desde a criação do banco de dados e dos usuários até o funcionamento completo do projeto.

Para criar o banco de dados:

- Criei um arquivo quiz.db
- Utilizando a CLI do sqlite3 criei as tabelas do banco de dados

```bash
sqlite3 quiz.db
.read user.sql
```

- Criei um arquivo users.csv com os usuários admin e fabioja
- Rodei o arquivo adduser.py

- Criei um python virtual environment
- Fui tentando rodar o arquivo softdes.py e baixando as dependências necessárias: flask e flask_httpauth
- Troquei a porta 80, dado que não havia permissão necessária para rodar a aplicação nessa porta com usuário padrão do linux
- Aplicação rodando

## Agora que você consegue rodar a aplicação, explore-a um pouco e descreva em poucas frases para quê ela serve.

Parece um site da matéria de SoftDes, existe um botão para logout, outro para trocar senha e os desafios/quizes.

# Documentação do projeto

## Se você fosse criar um guia de usuário (aluno) para esta aplicação, quais tarefas descreveria?

## Se você fosse criar um guia de usuário (professor) para esta aplicação, quais tarefas descreveria?

## O quê você descreveria em um guia de desenvolvedor para esta aplicação?

- Como baixar as dependências
- Como criar o banco de dados
- O que cada arquivo está fazendo
- O que cada rota está fazendo
- O que as funções estão fazendo
- ...
