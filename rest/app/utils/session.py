from sessions.manager import SessionManager, Session

import redis

session_manager = SessionManager(redis_client=redis.from_url("redis://localhost"))
