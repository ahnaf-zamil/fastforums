"""Custom server-sided session management feature using Redis

Usage Example:

session_manager = SessionManager(redis.from_url('redis://localhost'))

@app.get("/@me")
async def get_me(session: Session = Depends(session_manager.use_session)):
    session.set("user_id", "someid")
    
    ....

    print(session.get("user_id"))
"""

from typing import Optional
from fastapi import Request, Depends, Response
from collections.abc import MutableMapping

import redis
import uuid
import json


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


class Session(MutableMapping):
    """A dictionary-like object that represents a server-sided session"""

    def __init__(
        self,
        response: Response,
        request: Request,
        redis: redis.Redis,
        session_id: Optional[str] = None,
    ):
        self.response = response
        self.request = request
        self.session_id = session_id
        self.redis = redis

    def _session_check(self) -> None:
        if not self.session_id or not self.redis.get(str(self.session_id)):
            self._initiate_session(str(uuid.uuid4()))

    def _initiate_session(self, session_id: str) -> None:
        self.session_id = session_id
        self.redis.set(session_id, json.dumps({}))
        self.response.set_cookie("session", session_id)

    def _get_session_data(self) -> dict:
        self._session_check()
        try:
            return json.loads(self.redis.get(self.session_id))
        except:
            return {}

    def _set_session_data(self, data: dict):
        self.redis.set(self.session_id, json.dumps(data))

    def __getitem__(self, key) -> Optional[any]:
        self._session_check()
        try:
            return self._get_session_data().get(key)
        except:
            return None

    def __setitem__(self, key, value) -> None:
        self._session_check()
        data = self._get_session_data()
        data[key] = value
        self._set_session_data(data)

    def __delitem__(self, key) -> None:
        self._session_check()
        data = self._get_session_data()
        del data[key]
        self._set_session_data(data)

    def __iter__(self):
        return iter(self._get_session_data())

    def __len__(self):
        return len(self._get_session_data())

    def set(self, key, value):
        """Sets an item in the session"""
        return self.__setitem__(key, value)

    def remove(self, key):
        """Removes an item from the session"""
        return self.__delitem__(key)

    def clear(self) -> None:
        """Deletes the whole session, as well as the cookie"""
        self.redis.delete(self.session_id)
        self.response.delete_cookie("session", httponly=True)

    def __str__(self):
        return str(self._get_session_data())

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.session_id}>"


class SessionManager:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def use_session(
        self,
        request: Request,
        response: Response,
    ) -> Session:
        """Dependency to be used for accessing server-sided session in the specific request context"""

        session_id = str(request.cookies.get("session"))
        if not is_valid_uuid(session_id):
            return Session(response=response, request=request, redis=self.redis_client)

        return Session(
            response=response,
            request=request,
            session_id=session_id,
            redis=self.redis_client,
        )
