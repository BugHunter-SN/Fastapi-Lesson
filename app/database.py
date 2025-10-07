from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB connection string
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost/fastapi'

# establish db conection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session for b communication
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

