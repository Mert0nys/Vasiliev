from fastapi import FastAPI, Depends, HTTPException
import models, schemas, crud
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

#Ручка для создания
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.CreateTaskModel, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

#Ручка для вывода по id
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id:str, db: Session = Depends(get_db)):
    task = crud.get_task(db=db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

#Ручка для для вывода 10 последних заданий
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int=0, limit: int=10, db:Session = Depends(get_db)):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    return tasks

#Ручка для изменений
@app.put("/tasks/{task_id}", response_model=schemas.Task)
def updata_task(task_id: str, task: schemas.TaskBase, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db=db, task_id=task_id, task_data=task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

#Ручка для удаления
@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: str, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db=db, task_id=task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
