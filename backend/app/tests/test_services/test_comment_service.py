from services.comments_services import (
    get_comments,
    create_comment,
    get_comment_details,
    delete_comment
)
from backend.app.services.tasks_service import create_task
from schemas.comment import CreateComment
from schemas.task import CreateTask

def test_create_comment(db_session):
    task_id = create_task(db_session, CreateTask(title="Task"))
    comment_id = create_comment(db_session, CreateComment(task_id=task_id, description="C"))
    assert isinstance(comment_id, int)

def test_comment_details(db_session):
    task_id = create_task(db_session, CreateTask(title="Task"))
    comment_id = create_comment(db_session, CreateComment(task_id=task_id, description="C"))
    comment = get_comment_details(db_session, comment_id)
    assert comment['id'] == comment_id
    assert comment['task_id'] == task_id


def test_get_comment(db_session):
    task_id = create_task(db_session, CreateTask(title="Task"))
    comment_id = create_comment(db_session, CreateComment(task_id=task_id, description="C"))
    comments = get_comments(db_session)
    assert isinstance(comments, list)
    assert comments[0]["id"] == comment_id

def test_get_comment_not_found(db_session):
    comment = get_comment_details(db_session, 999)
    assert comment is None

def test_delete_comment(db_session):
    task_id = create_task(db_session, CreateTask(title="Task"))
    comment_id = create_comment(db_session, CreateComment(task_id=task_id, description="C"))
    delete_comment(db_session, comment_id)
    comment = get_comment_details(db_session, comment_id)
    assert comment is None
