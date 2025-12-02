import datetime

from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import CreateTask, UpdateTask


def get_tasks(db: Session, only_undone):
    results = db.query(Task)
    if only_undone:
        results = results.filter(Task.done == False)
    return results.all()


def get_task_details(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task_data: CreateTask, user: str = "unknown") -> int:
    task = Task(
        created_by=user,
        title=task_data.title,
        description=task_data.description
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task.id


def delete_task(db: Session, task_id: int) -> bool:
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is not None:
        db.delete(task)
        db.commit()
        return True
    else:
        return False


def update_task(db: Session, task_data: UpdateTask, user: str = "unknown") -> bool:
    task = db.query(Task).filter(Task.id == task_data.id).first()
    if task is not None:
        task.done = True
        task.done_at = datetime.datetime.now()
        task.done_by = user
        db.commit()
        return True
    else:
        return False