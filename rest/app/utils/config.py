from pydantic import BaseSettings, validator
from typing import Optional


class AppConfig(BaseSettings):
    database_uri: Optional[str]
    debug: Optional[bool]
    secret_key: Optional[str]


config = AppConfig(_env_file=".env")
