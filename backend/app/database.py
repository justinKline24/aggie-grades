from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#postgresql://postgres:password@localhost/grades
SQLALCHEMY_DATABASE_URL = 'postgresql://justin:aggiegradedata@gradedata.cgvbm0h9cyvd.us-east-2.rds.amazonaws.com/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()