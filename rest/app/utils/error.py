from jwt.exceptions import PyJWTError, InvalidTokenError
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


async def jwt_exception_handler(request: Request, exc: PyJWTError):
    if isinstance(exc, InvalidTokenError):
        return JSONResponse(content={"description": "Unauthorized"}, status_code=401)
    else:
        return JSONResponse(
            content={"description": "Internal Server Error: JWT Exception"},
            status_code=500,
        )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        content={"description": exc.detail},
        status_code=exc.status_code,
        headers=exc.headers,
    )
