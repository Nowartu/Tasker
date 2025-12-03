import datetime

from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import CreateTask, UpdateTask


def get_tasks(db: Session, only_undone):
    """
    Returns all tasks in database.
    :param db: database Session
    :param only_undone: Whether return only undone tasks
    :return: List of tasks.
    """
    results = db.query(Task)
    if only_undone:
        results = results.filter(Task.done == False)
    return results.all()


def get_task_details(db: Session, task_id: int):
    """
    Returns details of a task.
    :param db: database Session
    :param task_id: Id of a task
    :return: Dict with data of task
    """
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task_data: CreateTask, user: str = "unknown") -> int:
    """
    Creates new task in database.
    :param db: database Session
    :param task_data: Dict with task data
    :param user: User who is adding new task
    :return: Id of newly created task
    """
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
    """
    Deletes task.
    :param db: database Session
    :param task_id: Id of a task to be deleted
    :return: Bool based on result
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is not None:
        db.delete(task)
        db.commit()
        return True
    else:
        return False


def update_task(db: Session, task_data: UpdateTask, user: str = "unknown") -> bool:
    """
    Changes task done attribute
    :param db: database Session
    :param task_data: Dict with new task data
    :param user: User who is performing changes
    :return: Bool based on result
    """
    task = db.query(Task).filter(Task.id == task_data.id).first()
    if task is not None:
        task.done = task_data.done
        task.done_at = datetime.datetime.now()
        task.done_by = user
        db.commit()
        return True
    else:
        return False