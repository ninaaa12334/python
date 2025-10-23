from fastapi import FastAPI, HTTPException
from typing import List
import database
from models import Task, TaskCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tasks API!"}

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    """Add a new task"""
    task_id = database.create_task(task)
    return Task(id=task_id, **task.dict())

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """Read one task"""
    task = database.read_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    """Update a task"""
    updated = database.update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task(id=task_id, **task.dict())

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task"""
    deleted = database.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
