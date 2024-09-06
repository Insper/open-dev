# Running Guide for Quiz SoftDes 2018.2

### Group Members: André Brito (andreb10)

## How to run this project

### Prerequisites

- Install [Python 3](https://www.python.org/downloads/)
- Install [PIP](https://pip.pypa.io/en/stable/installing/)

### Libraries

```py
pip install flask flask_httpauth
```

### Creating user account

To create a user account, create a `users.csv` file on the root directory of the project with the following format:

```
admin,admin
andre,admin
```

The first column is the username and the second column is the password.

By default the username and password are the same.

### Seeding the database

To seed database create database_seed.py file on the root directory with the following code:

```py
import sqlite3
import hashlib

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

with open('quiz.sql', 'r') as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()
```

The quiz.sql file already exists on the root directory.

Now run the following command:

```py
python database_seed.py
```

This will create the database and seed it with the data from the quiz.sql file.

Also create user account by running the following command:

```py
python create_user.py
```

### Running the server

To run the server, run the following command:

```py
python softdes.py
```

Now you can access the server at IP address of your machine on port 80
