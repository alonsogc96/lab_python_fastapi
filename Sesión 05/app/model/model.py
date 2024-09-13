from sqlalchemy import Column, String, Integer, create_engine
#from uuid import UUID, uuid4
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__="users"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    city = Column(String, nullable=False)

SQLACHEMY_DATABASE_URL = 'postgresql://postgres:280396@localhost:5432/fast_api'
engine = create_engine(SQLACHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)