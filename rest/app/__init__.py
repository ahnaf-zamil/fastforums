from fastapi import FastAPI
from jwt.exceptions import PyJWTError

from .utils.error import jwt_exception_handler
from .routers import users

app = FastAPI()

app.include_router(users.router)
app.add_exception_handler(PyJWTError, jwt_exception_handler)
