from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from fastapi import Depends
from types import GeneratorType

from .config import config

engine = create_engine(
    config.database_uri,
    connect_args={"check_same_thread": False}
    if config.database_uri.startswith("sqlite://")
    else {},
)
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
        self.db = next(get_db()) if isinstance(db, GeneratorType) else db

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


from ..models import User
