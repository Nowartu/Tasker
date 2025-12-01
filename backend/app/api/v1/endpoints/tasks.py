from fastapi import APIRouter, HTTPException
from schemas.task import CreateTask, TaskSimple, TaskDetails
from typing import List

api_router = APIRouter(
    prefix="/tasks",
    tags=['tasks']
)

@api_router.get("/tasks/", response_model=List[TaskSimple])
def get_tasks():
    raise HTTPException(501, "Not implemented")


@api_router.get("/tasks/{task_id}/", response_model=TaskDetails)
def get_task(task_id: int):
    raise HTTPException(501, "Not implemented")


@api_router.post("/tasks/")
def create_task(task: CreateTask):
    raise HTTPException(501, "Not implemented")


@api_router.put("/tasks/{task_id}")
def update_task(task_id: int):
    raise HTTPException(501, "Not implemented")


@api_router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    raise HTTPException(501, "Not implemented")