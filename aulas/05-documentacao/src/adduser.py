import sqlite3
import hashlib

def addUser(user, pwd, type):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(user, pwd, type))
    conn.commit()
    conn.close()  

with open('users.csv','r') as file:
  lines = file.read().splitlines()

for users in lines:
  (user, type) = users.split(',')
  print(user)
  print(type)
  addUser(user, hashlib.md5(user.encode()).hexdigest(), type)
