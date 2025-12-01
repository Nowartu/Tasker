from fastapi import APIRouter, HTTPException, Body
from schemas.comment import CreateComment, CommentDetails
from typing import List, Annotated

api_router = APIRouter(
    prefix="/comments",
    tags=['comments']
)

@api_router.get("/comments/", response_model=List[CommentDetails])
def get_comments():
    raise HTTPException(501, "Not implemented")


@api_router.get("/comments/{comment_id}/", response_model=CommentDetails)
def get_task(comment_id: int):
    raise HTTPException(501, "Not implemented")


@api_router.post("/comments/")
def create_comment(comment: Annotated[CreateComment, Body()]):
    raise HTTPException(501, "Not implemented")


@api_router.delete("/comments/{comment_id}/")
def create_comment(comment_id: int):
    raise HTTPException(501, "Not implemented")
