from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevOps Task API")


class Task(BaseModel):
    title: str
    completed: bool = False

tasks = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task