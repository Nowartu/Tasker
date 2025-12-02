from fastapi import APIRouter, HTTPException, Depends
from db.session import get_db
from schemas.task import CreateTask, TaskSimple, TaskDetails
from typing import List

api_router = APIRouter(
    prefix="/tasks",
    tags=['tasks']
)

@api_router.get("/", response_model=List[TaskSimple])
def get_tasks():
    raise HTTPException(501, "Not implemented")


@api_router.get("/{task_id}/", response_model=TaskDetails)
def get_task(task_id: int):
    raise HTTPException(501, "Not implemented")


@api_router.post("/")
def create_task(task: CreateTask):
    raise HTTPException(501, "Not implemented")


@api_router.put("/{task_id}")
def update_task(task_id: int):
    raise HTTPException(501, "Not implemented")


@api_router.delete("/{task_id}")
def delete_task(task_id: int):
    raise HTTPException(501, "Not implemented")