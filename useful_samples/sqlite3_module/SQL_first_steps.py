import sqlite3

# Creation de la base
hello_db = sqlite3.connect("hello.db")

# Creation du curseur dans la base
hello_cursor = hello_db.cursor()

# Creation d'une table
hello_cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, 
    name TEXTE NOT NULL, 
    priority INTEGER NOT NULL
);
''')

# insertion d'un element dans cette table avec 'execute'
hello_db.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My First task', 1))
hello_db.commit()

#insertion de plusieurs elements simultanément avec 'executemany'
tasks = [
    ('My First task', 1),
    ('My Second task', 5),
    ('My Third task', 10),
]
hello_db.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
hello_db.commit()
hello_db.close()
