from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task.title, task.description)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get(task_id: int, db: Session = Depends(get_db)):
    return task_service.get_task(db, task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    return task_service.update_task(db, task_id, data)


@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    task_service.delete_task(db, task_id)
    return {"message": "Task deleted"}