from app.utils.config import config
from app.utils.session import session_manager

import os
import fakeredis


def pytest_sessionstart(session):
    # Mocking config values
    config.secret_key = "asecretkey"
    config.database_uri = "sqlite:///./test.db"
    config.debug = False

    # Mocking redis client
    session_manager.redis_client = fakeredis.FakeStrictRedis()

    from app.utils.database import Base, engine

    Base.metadata.create_all(bind=engine)


def pytest_sessionfinish(session, exitstatus):
    os.remove("./test.db")  # Removes test.db after finishing tests
