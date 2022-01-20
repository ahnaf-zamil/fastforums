from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content={"description": exc.detail},
        status_code=exc.status_code,
        headers=exc.headers,
    )
