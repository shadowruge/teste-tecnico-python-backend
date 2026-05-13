from sqlalchemy.orm import Session
from app.repositories import task_repository
from app.core.exceptions import not_found


def create_task(db: Session, title: str, description: str):
    return task_repository.create_task(db, title, description)


def get_tasks(db: Session):
    return task_repository.get_tasks(db)


def get_task(db: Session, task_id: int):
    task = task_repository.get_task_by_id(db, task_id)

    if not task:
        not_found("Task")

    return task


def update_task(db: Session, task_id: int, data):
    task = get_task(db, task_id)

    if data.title is not None:
        task.title = data.title

    if data.description is not None:
        task.description = data.description

    if data.completed is not None:
        task.completed = data.completed

    return task_repository.update_task(db, task)


def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    task_repository.delete_task(db, task)