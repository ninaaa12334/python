import sqlite3

connection =sqlite3.connect('example.db')

cursor =connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
    )''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS workPlace(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         position TEXT NOT NULL,
#         department TEXT NOT NULL,
#         salary REAL
#     )''')

connection.commit()

cursor.execute('''
  INSERT INTO emplyess(name, position, department, salary)
  VALUES(?,?,?,?)
  '''        ,  ('John Doe', 'Software Engineer', 'IT', 70000))

connection.commit()

# cursor.execute("SELECT * FROM employess")
# rows = cursor.fetchball()
# for now in rows:
#     print(f'emplyess:{rows[0]}, WorkPlace: {row[1]}')

