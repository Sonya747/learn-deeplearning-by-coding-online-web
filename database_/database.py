from sqlalchemy import create_engine
from sqlmodel import SQLModel
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlite_file_path = project_path+f'\database.db'
sqlite_url = 'sqlite:///' + sqlite_file_path
engine = create_engine(sqlite_url)
from database_.model import User,Student,Teacher,Class,Quiz,Record

def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_db_and_tables(engine)

