from fastapi import Request, Depends
from ..services.jwt import JWTService
from ..services.user import UserService


async def auth_required(request: Request, user_service: UserService = Depends()):
    """Dependency for getting authenticated users on required routes"""
    token = str(
        request.cookies.get("token")
    )  # Stringyfy-ing because pyjwt might cry if it gets NoneType

    user_id = JWTService.verify_and_return_id(token)
    request.state.user_id = user_id

    return user_service.get_user_by_id(user_id)
