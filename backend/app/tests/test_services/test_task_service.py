import pytest
from services.tasks_service import (
    get_tasks,
    get_task_details,
    create_task,
    update_task,
    delete_task
)
from schemas.task import CreateTask, UpdateTask


def test_create_task(db_session):
    task_data = {"title": "Test title", "description": "Test desc"}
    task_id = create_task(db_session, task_data=CreateTask(**task_data))
    assert task_id is not None

def test_get_task(db_session):
    task_id = create_task(db_session, task_data=CreateTask(title="Test title"))
    fetched = get_task_details(db_session, task_id)
    assert fetched.id == task_id

def test_get_tasks(db_session):
    tasks = get_tasks(db_session, only_undone=False)
    assert isinstance(tasks, list)

def test_get_task_not_found(db_session):
    task = get_task_details(db_session, 999)
    assert task is None

def test_update_task(db_session):
    task_id = create_task(db_session, task_data=CreateTask(title="Test"))
    updated = update_task(db_session, task_data=UpdateTask(id=task_id, done=True), user="user1")
    assert updated is True
    task = get_task_details(db_session, task_id=task_id)
    assert task.done is True
    assert task.done_by == "user1"

def test_get_undone_tasks(db_session):
    task_data = {"title": "Test title", "description": "Test desc"}
    task_id1 = create_task(db_session, task_data=CreateTask(**task_data))
    create_task(db_session, task_data=CreateTask(**task_data))
    update_task(db_session, task_data=UpdateTask(id=task_id1, done=True), user="user1")
    tasks = get_tasks(db_session, only_undone=True)
    assert len(tasks) == 1

def test_delete_task(db_session):
    task_id = create_task(db_session, task_data=CreateTask(title="Test"))
    delete_task(db_session, task_id)
    assert get_task_details(db_session, task_id) is None
