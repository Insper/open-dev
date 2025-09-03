# How to run

1. Install all dependencies from requirements.txt 

```bash
pip install -r ericalp_requirements.txt
```

2. Create `users.csv` with the desired user values

3. Run the following code to execute `quiz.sql` and create `quiz.db`
```python
import sqlite3

#run quiz.sql to create the database
with open('quiz.sql', 'r') as f:
    sql = f.read()
    conn = sqlite3.connect('quiz.db')
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print("Database initialized")
```

4. Execute `adduser.py` to add the users in `users.csv` to the database

5. Execute `softdes.py` to run the website

6. Log in using your credentials, your password is the same as your username

