from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB = "sqlite:///./task.db"
engine = create_engine(SQL_DB)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()