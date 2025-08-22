from uuid import uuid4
from sqlalchemy import Column, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#Создание модели для базы данных
class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum("created", "in_progress", "completed"), default="created")
