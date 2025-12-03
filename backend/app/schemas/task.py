from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from schemas.comment import Comment


class CreateTask(BaseModel):
    title: str

    title: str
    description: str | None = None


class TaskSimple(CreateTask):
    id: int
    done: bool


class TaskDetails(TaskSimple):
    created_at: datetime
    created_by: str

    done_at: datetime | None = None
    done_by: str | None = None

    comments: List[Comment]


class CompleteTask(BaseModel):
    id: int


class DeleteTask(BaseModel):
    id: int


class UpdateTask(BaseModel):
    id: int

    done: bool