import sqlite3
from models import Task, TaskCreate

def create_connection():
    """Connect to SQLite database"""
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create the tasks table"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Create the table automatically on import
create_table()

def create_task(task: TaskCreate) -> int:
    """Add a new task to the database"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)",
                   (task.title, task.description))
    connection.commit()
    task_id = cursor.lastrowid
    connection.close()
    return task_id

def read_task(task_id: int):
    """Retrieve one task by id"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Task(id=row["id"], title=row["title"], description=row["description"])

def update_task(task_id: int, task: TaskCreate) -> bool:
    """Update an existing task"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
        (task.title, task.description, task_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0

def delete_task(task_id: int) -> bool:
    """Delete a task"""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0
