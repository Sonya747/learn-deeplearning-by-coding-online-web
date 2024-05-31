from sqlalchemy import create_engine
from sqlmodel import SQLModel

sqlite_file_name = 'database.db'
sqlite_url = 'sqlite:///' + sqlite_file_name
engine = create_engine(sqlite_url)

def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)




