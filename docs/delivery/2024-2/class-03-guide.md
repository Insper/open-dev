## Group: Antonio Martins, Enrrico Gemha e Felipe Catapano
### Guia para Rodar a Plataforma de Quiz

Este guia fornece um passo a passo para configurar e executar a aplicação de quiz localmente. Siga as instruções abaixo para garantir que todos os componentes necessários estejam instalados e configurados corretamente.

#### 1. **Pré-requisitos**

- **Python 3:** Certifique-se de que o Python 3 está instalado em sua máquina.
- **pip:** O gerenciador de pacotes `pip` deve estar instalado.

#### 2. **Instalação de Dependências**

Navegue até a pasta `/src` do projeto e instale as dependências necessárias executando o seguinte comando no terminal:

```bash
pip install flask flask_httpauth
```

Este comando instala o Flask, um framework web leve para Python, e o `flask_httpauth`, uma extensão para autenticação HTTP básica.

#### 3. **Criação do Arquivo de Usuários**

Crie um arquivo `users.csv` para definir os usuários iniciais:

```bash
echo "enriccog,aluno" > users.csv
```

Este comando cria um arquivo `users.csv` com um usuário chamado `enriccog` e define seu tipo como `aluno`.

#### 4. **Configuração do Banco de Dados**

Inicialize o banco de dados SQLite com o seguinte comando:

```bash
sqlite3 quiz.db < quiz.sql
```

Este comando cria o banco de dados `quiz.db` usando o script SQL `quiz.sql`, que deve conter as instruções para criar as tabelas necessárias.

#### 5. **Adição de Usuários ao Banco de Dados**

Execute o script `adduser.py` para adicionar os usuários do arquivo `users.csv` ao banco de dados:

```bash
python3 adduser.py
```

Este script lê o arquivo `users.csv` e insere os usuários especificados no banco de dados `quiz.db`.

#### 6. **Executando a Aplicação**

Defina a variável de ambiente `FLASK_APP` e inicie o servidor Flask com os comandos:

```bash
export FLASK_APP=softdes.py && flask run
```

Este comando configura o arquivo `softdes.py` como a aplicação Flask a ser executada e inicia o servidor. Por padrão, o servidor Flask estará acessível em `http://localhost:5000`.

#### 7. **Acessando a Plataforma**

Abra um navegador web e acesse `http://localhost:5000` para visualizar a plataforma de quiz.

Você agora deve estar pronto para usar a plataforma! Se houver quaisquer problemas ou erros durante o processo de configuração, verifique se todas as dependências estão instaladas corretamente e se os arquivos necessários estão no diretório correto.