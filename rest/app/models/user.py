from ..utils.database import Base
from sqlalchemy import Column, String, LargeBinary
from uuid import uuid4


class User(Base):
    """An object referring to a user in the application"""

    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True, default=lambda x: str(uuid4()))
    username = Column(String(30), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(LargeBinary, nullable=False)

    def get_json(self, include_email=False):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email if include_email else None,
        }
