from jwt.exceptions import PyJWTError, InvalidTokenError
from fastapi import Request
from fastapi.responses import JSONResponse


async def jwt_exception_handler(request: Request, exc: PyJWTError):
    if isinstance(exc, InvalidTokenError):
        return JSONResponse(content={"description": "Unauthorized"}, status_code=401)
    else:
        return JSONResponse(
            content={"description": "Internal Server Error: JWT Exception"},
            status_code=500,
        )
