from fastapi import APIRouter, HTTPException, Body, Depends
from schemas.comment import CreateComment, CommentDetails
from typing import List, Annotated
from sqlalchemy.orm import Session
from db.session import get_db
from services import comments_services

api_router = APIRouter(
    prefix="/comments",
    tags=['comments']
)

@api_router.get("/", response_model=List[CommentDetails])
def get_comments(db: Session = Depends(get_db)):
    return comments_services.get_comments(db)


@api_router.get("/{comment_id}/", response_model=CommentDetails)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = comments_services.get_comment_details(db, comment_id)
    if comment is None:
        raise HTTPException(404, "Comment not found.")
    else:
        return comment


@api_router.post("/")
def create_comment(comment: Annotated[CreateComment, Body()], db: Session = Depends(get_db)):
    comment_id = comments_services.create_comment(db, comment)
    if comment_id is not None:
        return comment_id
    else:
        return HTTPException(404, "Task does not exist")

@api_router.delete("/{comment_id}/")
def create_comment(comment_id: int, db: Session = Depends(get_db)):
    if comments_services.delete_comment(db, comment_id):
        return "OK"
    else:
        raise HTTPException(404, "Comment not found")
