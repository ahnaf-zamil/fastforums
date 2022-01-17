from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from fastapi import Depends

from .config import config

engine = create_engine(config.database_uri, echo=True)
local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    session_db: Session = local_session()
    try:
        yield session_db
    finally:
        session_db.close()


class DatabaseContext:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


from ..models import User
