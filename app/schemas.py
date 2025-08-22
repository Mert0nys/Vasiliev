from pydantic import BaseModel

class TaskBase(BaseModel):
    title:str
    description:str
    status:str

class CreateTaskModel(TaskBase):
    pass

class Task(TaskBase):
    id:str
