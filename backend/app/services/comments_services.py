from sqlalchemy.orm import Session
from models.comment import Comment
from models.task import Task
from schemas.comment import CreateComment


def get_comments(db: Session):
    """
    Returns all comments in database.
    :param db: database Session
    :return: List with comments.
    """
    return [{
        "id": comment.id,
        "task_id": comment.task.id,
        "task_title": comment.task.title,
        "task_description": comment.task.description,
        "description": comment.description,
        "created_at": comment.created_at,
        "created_by": comment.created_by
    } for comment in db.query(Comment).join(Task).all()]


def get_comment_details(db: Session, comment_id: int):
    """
    Returns details of a comment.
    :param db: database Session
    :param comment_id: Id of a comment.
    :return: Dictionary with data of a comment or None if not found.
    """
    comment = db.query(Comment).join(Task).filter(Comment.id == comment_id).first()
    if comment is not None:
        return {
            "id": comment.id,
            "task_id": comment.task.id,
            "task_title": comment.task.title,
            "task_description": comment.task.description,
            "description": comment.description,
            "created_at": comment.created_at,
            "created_by": comment.created_by
        }
    else:
        return None


def create_comment(db: Session, comment_data: CreateComment, user: str = "unknown") -> int | None:
    """
    Creates new comment.
    :param db: database Session
    :param comment_data: Dict with comment info.
    :param user: User who is adding comment.
    :return: Id of new comment or None if task not exists.
    """

    # Get task from database and check if it exists.
    task = db.query(Task).filter(Task.id == comment_data.task_id).first()
    if task is None:
        return None

    comment = Comment(
        task_id=comment_data.task_id,
        created_by=user,
        description=comment_data.description
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment.id


def delete_comment(db: Session, comment_id: int) -> bool:
    """
    Deletes comment.
    :param db: database Session
    :param comment_id: Id of a comment to be deleted
    :return: Bool based on result
    """
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is not None:
        db.delete(comment)
        db.commit()
        return True
    else:
        return False