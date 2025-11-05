# Guia para subir a aplicação

Execute o comando abaixo para instalar as dependências do projeto:

```bash
pip install click==8.1.7
pip install Flask==0.12.2
pip install itsdangerous==2.2.0
pip install Jinja2==3.1.4
pip install MarkupSafe==2.1.5
pip install Werkzeug==3.0.4
```

Agora é necessário criar a base de dados, antes de subir o server, para isso execute o comando abaixo:

```bash
import sqlite3

db = sqlite3.connect("quiz.db")
print("Opened database successfully")

cursor = db.cursor()

startup_file = open("quiz.sql", "r")
startup_script = startup_file.read()
startup_file

cursor.executescript(startup_script)
```

Verifique que foi criado um arquivo chamado `quiz.db` dentro da pasta que você rodou o comando.

Agora, criei um aquivo chamado `users.csv`, com as colunas iguais a do script sql, ou seja, `user` e `pass`. Dentro deste arquivo, insira os usuários que deseja criar, como por exemplo, `admin,admin`.


Agora, rode o comando abaixo de fato adicionar os usuarios a base:

```bash
python3 adduser.py
```

Pronto, agora você esta apto a executar o server novament:

```bash
python3 softdes.py
```

Terminou, parabéns! Agora você pode acessar o site !!!

