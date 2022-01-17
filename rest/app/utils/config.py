from pydantic import BaseSettings


class AppConfig(BaseSettings):
    database_uri: str
    debug: bool
    secret_key: str


config = AppConfig(_env_file=".env")
