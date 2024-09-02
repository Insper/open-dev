## Group: André Melo (andrebbm)
### Manual para Subir a Plataforma de Quiz SoftDes 2018.2

Passo a passo para corrigir e executar a plataforma de quiz SoftDes 2018.2 a partir do código fonte fornecido.

#### 1. **Pré-requisitos**

- **Python 3** 
- **pip**

#### 2. **Bibliotecas Necessárias**

Instale as seguintes bibliotecas Python necessárias para executar a plataforma de quiz, como no modelo abaixo:

```bash
pip install flask
```

- **Flask**
- **flask_httpauth**
- **datetime**
- **sqlite3**
- **hashlib**

#### 3. **Criação do Arquivo de Usuários**

Crie um arquivo `users.csv` na raiz do projeto para definir os usuários iniciais e adicioná-los ao banco de dados. O conteúdo do arquivo `users.csv` deve ter o seguinte formato:

```csv
admin,admin
```

#### 4. **Configuração do Banco de Dados**

No arquivo adduser.py, inclua na função addUser() o seguinte bloco de código entre conn.cursor() e conn.execute():

```python
cursor.execute("DROP TABLE IF EXISTS USER;")
cursor.execute("""
    CREATE TABLE USER(
    user TEXT NOT NULL PRIMARY KEY,
    pass TEXT NOT NULL,
    type TEXT NOT NULL);""")
```
a seguir, adicione a seguinte função:

```python
def addQuiz(id, release, expire, problem, tests, results, diagnosis, numb):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS QUIZ;")
    cursor.execute("""
        CREATE TABLE QUIZ(
        id INTEGER NOT NULL PRIMARY KEY,
        release TEXT NOT NULL,
        expire TEXT NOT NULL,
        problem TEXT NOT NULL,
        tests TEXT NOT NULL,
        results TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        numb INTEGER NOT NULL);""")
    cursor.execute('Insert into QUIZ(id,release,expire,problem,tests,results,diagnosis,numb) values({0},"{1}","{2}","{3}","{4}","{5}","{6}",{7});'.format(id, release, expire, problem, tests, results, diagnosis, numb))
    
    cursor.execute("DROP TABLE IF EXISTS USERQUIZ;")
    cursor.execute("""
        CREATE TABLE USERQUIZ(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        quizid INTEGER NOT NULL,
        sent TEXT NOT NULL,
        answer TEXT NOT NULL,
        result TEXT NOT NULL);""")
    conn.commit()
    conn.close()
```

Por fim, adicione a seguinte chamada de função no final do script:

```python
  addQuiz(1, '2018-01-01 00:00:00', '2018-01-01 00:00:00', 'problem', 'tests', 'results', 'diagnosis', 1)
```

#### 5. **Adição de Usuários ao Banco de Dados**

Execute o script `adduser.py` para criar a base e adicionar os usuários do arquivo `users.csv` ao banco de dados.

#### 6. **Executando a Aplicação**

Execute o script `quiz.py` para iniciar a aplicação Flask. A aplicação estará disponível em `http://192.168.1.144/`.

```bash
python3 quiz.py
```

#### 7. **Acessando a Plataforma**

Abra um navegador web e acesse `http://192.168.1.144/` para visualizar a plataforma de quiz.

A plataforma vai pedir um login e senha, que são os mesmos do arquivo `users.csv`: admin, admin.