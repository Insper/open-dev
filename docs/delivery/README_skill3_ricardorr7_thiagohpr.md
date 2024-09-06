# Quiz Server - SoftDes INSPER


## Used technologies 
- Python
    - Flask
- Bootstrap
- HTML, CSS & JavaScript
- SQLite DB

## Database
The appplication uses the SQLite db, the application uses this db to store quizes, and users for the quizes. The db is created using the `quiz.sql` file, the tables created are:
- USER
- QUIZ
- USERQUIZ


## How to setup the application:

1. Install the dependencies:
```sh
pip install flask Flask-HTTPAuth
```

2. Create the db using the following script:
```python
import sqlite3

DB_PATH = "quiz.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open('quiz.sql') as file:
        cursor.executescript(file.read())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
```
3. Create the `users.csv` file:
```csv
your_user, user_type
```

4. Create the users using the `adduser.py` script:
```sh
python adduser.py
```

5. Run the application, use the set username as password:
```sh
python softdes.py
```

## About the aplication
Flask based Code Exercises server that interacts with SQLite, in each the main api call fetches all the quizzes and evaluates the user answers. 
The code itself is not safe, mainly because you can create an user with admin permissions by calling it "fabioja". This allows the user to see every quiz from the server, even those who aren't released yet. Also, if the user creates the the login credentials with the script `adduser.py`, the password will be the same as the user name. 