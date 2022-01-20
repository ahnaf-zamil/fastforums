from fastapi import Depends
from fastapi.exceptions import HTTPException
from ..services.user import UserService
from ..utils.session import session_manager, Session


async def auth_required(
    user_service: UserService = Depends(),
    session: Session = Depends(session_manager.use_session),
):
    """Dependency for getting authenticated users on required routes"""
    user_id = session.get("user_id")
    user = user_service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(401, "Unauthorized")
    return user
