from pydantic import BaseModel, Field
from datetime import datetime


class CreateComment(BaseModel):
    task_id: int
    description: str


class Comment(CreateComment):
    id: int


class CommentDetails(Comment):
    task_title: str
    description: str
    created_at: datetime
    created_by: str