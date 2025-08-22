
import models, schemas
from sqlalchemy.orm import Session

#Функция для создания задания
def create_task(db:Session, task:schemas.CreateTaskModel):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#Функция для вывода одного задания
def get_task(db:Session, task_id:str):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

#Функция для вывода всех заданий
def get_tasks(db:Session, skip: int=0, limit: int=10):
    return db.query(models.Task).offset(skip).limit(limit).all()

#Функция для обновления задания
def update_task(db:Session, task_id:str, task_data:schemas.TaskBase):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        for key, value in task_data.dict().items(): setattr(task, key, value)
    db.add(task)
    db.commit()   
    db.refresh(task)
    return task

#Функция для удаления задания
def delete_task(db:Session, task_id:str):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task