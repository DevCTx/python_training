import os
import sqlite3


class Todo :

    def __init__(self):
        # Creation de la base
        self.todo_db = sqlite3.connect("todo.db")
        # Creation du curseur dans la base
        self.todo_cursor = self.todo_db.cursor()
        # Creation d'une table tasks
        self.create_task_table()

    def create_task_table(self):
        self.todo_cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            name TEXTE NOT NULL, 
            priority INTEGER NOT NULL
        );
        ''')

    def add_task(self):
        name = None
        priority = 0
        while name == None or len(name) == 0 or not name.isascii():
            name = input("Enter the task name : ")
            if len(name) == 0 or not name.isascii() :
                print("> Please enter an alpha string...")

        # Verifie si la tache est existante
        if self.find_task(name) is None:
            while priority <= 0:
                try :
                    priority = int(input("Enter the priority : "))
                except:
                    print("> Please enter an integer...")
            self.todo_cursor.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
            self.todo_db.commit()

        self.read_table_all_in_memory()

    def find_task(self, name):
        # REtourne l'enregistrement trouvé ou None
        if len(name) > 0 :
            self.todo_cursor.execute("SELECT * FROM tasks WHERE name = ?",(name,))  # ATTENTION TUPPLE UNIQUEMENT !!!
            return self.todo_cursor.fetchone()
        else :
            return None

    def delete_task(self):
        id = 0
        while id <= 0:
            try:
                id = int(input("Enter the id : "))
            except:
                print("> Please enter a valid id...")

        self.todo_cursor.execute('DELETE FROM tasks WHERE id =?', (id,))
        self.todo_db.commit()
        self.read_table_all_in_memory()

    def change_priority(self):
        name = None
        priority = 0
        while name == None or len(name) == 0 or not name.isalnum():
            name = input("Enter the task name : ")
            if len(name) == 0 or not name.isalnum() :
                print("> Please enter an alpha string...")

        # Verifie si la tache est existante
        found = self.find_task(name)
        if found is None:
            print("Sorry, not in the table")
        else:
            while priority <= 0:
                print("Current priority is", found[2])      # TUPPLE : Utiliser index et non string !!!
                try :
                    priority = int(input("Enter the new priority : "))
                except:
                    print("> Please enter an integer...")
            self.todo_cursor.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, found[0]))
            self.todo_db.commit()

        self.read_table_all_in_memory()

    def read_table_by_iterator(self):
        # lit les elements avec le curseur en tant qu'iterateur
        for row in self.todo_cursor.execute('SELECT * from tasks'):
            print( row )

    def read_table_all_in_memory(self):
        # lit les elements et met tout en memoire (attention si grande quantité de données)
        self.todo_cursor.execute('SELECT * from tasks')
        rows = self.todo_cursor.fetchall()
        for row in rows:
            print(row)

    def read_table_2_first_only(self):
        # lit l'element suivant uniquement
        self.todo_cursor.execute('SELECT * from tasks')
        print(self.todo_cursor.fetchone())
        print(self.todo_cursor.fetchone())

app = Todo()
choice = -13

while choice != 0 :
    # Clearing the Screen
    # posix is os name for Linux or mac
    if (os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')
    print("#"*40)

    print("TODO :")
    app.read_table_by_iterator()
    print("#" * 40)
    print("MENU :")
    print("1. Add Task")
    print("2. Change priority")
    print("3. Delete Task")
    print("0. Exit")
    try:
        choice = int(input("Your choice : "))
    except:
        pass
    else:
        if choice == 0:
            break
        elif choice == 1:
            app.add_task()
        elif choice == 2:
            app.change_priority()
        elif choice == 3 :
            app.delete_task()
        else:
            pass
