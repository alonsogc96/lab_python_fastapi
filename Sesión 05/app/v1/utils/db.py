from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLACHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/fastapi'
engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

