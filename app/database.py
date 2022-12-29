from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

from .config import Settings
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

print("with type")

print(type(settings.database_port))

print("without type")
settings.database_port

#****srror *****#
engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# try:
#     conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='123',
#                             cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("database connected")
# except Exception as error:
#     print("not connect")
#     print('Error', error)
