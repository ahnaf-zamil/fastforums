from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from .utils.error import http_exception_handler
from .routers import users

app = FastAPI()


app.include_router(users.router)
app.add_exception_handler(HTTPException, http_exception_handler)
