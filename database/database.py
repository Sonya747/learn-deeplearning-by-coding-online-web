from sqlalchemy import create_engine
from sqlmodel import SQLModel
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlite_file_path = project_path+f'\database.db'
sqlite_url = 'sqlite:///' + sqlite_file_path
engine = create_engine(sqlite_url)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)




