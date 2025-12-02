from fastapi import APIRouter, HTTPException, Depends, Body
from db.session import get_db
from schemas.task import CreateTask, TaskSimple, TaskDetails, UpdateTask
from typing import List, Annotated
from sqlalchemy.orm import Session
from services import tasks_service

api_router = APIRouter(
    prefix="/tasks",
    tags=['tasks']
)

@api_router.get("/", response_model=List[TaskSimple])
def get_tasks(db: Session = Depends(get_db), only_undone: bool = True):
    return tasks_service.get_tasks(db, only_undone)


@api_router.get("/{task_id}/", response_model=TaskDetails)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = tasks_service.get_task_details(db, task_id)
    if task is None:
        raise HTTPException(404, "Task not found.")
    else:
        return task


@api_router.post("/")
def create_task(task: Annotated[CreateTask, Body], db: Session = Depends(get_db)):
    task_id = tasks_service.create_task(db, task)
    return task_id


@api_router.put("/{task_id}")
def update_task(task: Annotated[UpdateTask, Body], db: Session = Depends(get_db)):
    if tasks_service.update_task(db, task):
        return "OK"
    else:
        raise HTTPException(404, "Task not found")


@api_router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if tasks_service.delete_task(db, task_id):
        return "OK"
    else:
        raise HTTPException(404, "Task not found.")