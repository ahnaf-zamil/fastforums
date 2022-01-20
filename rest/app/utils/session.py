from sessions.manager import SessionManager, Session  # noqa

import redis

session_manager = SessionManager(redis_client=redis.from_url("redis://localhost"))
