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


class TaskDetails(TaskSimple):
    created_at: datetime
    created_by: str

    done: bool
    done_at: datetime
    done_by: str

    comments: List[Comment]


class CompleteTask(BaseModel):
    id: int


class DeleteTask(BaseModel):
    id: int
