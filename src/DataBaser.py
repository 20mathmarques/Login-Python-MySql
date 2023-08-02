import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

if cursor != '':
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Users(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        User TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    """)
    
    print ("Conectado com o banco de Dados")