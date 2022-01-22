from fastapi import APIRouter, Depends

from ..utils.auth import auth_required
from ..utils.service import handle_result
from ..schemas.users import CreateUserBody, LoginUserBody
from ..services.hash import HashService
from ..services.user import UserService
from ..utils.session import session_manager, Session
from ..models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/@me")
async def get_logged_in_user(user: User = Depends(auth_required)):
    return user.get_json(include_email=True)


@router.post("/create")
async def create_user(
    payload: CreateUserBody,
    hash_service: HashService = Depends(),
    user_service: UserService = Depends(),
    session: Session = Depends(session_manager.use_session),
):
    """Register a user on the application"""
    hashed_pw = hash_service.get_password_hash(payload.password)
    result = user_service.create_user(payload, hashed_pw, session)

    return handle_result(result)


@router.post("/login")
async def login_user(
    payload: LoginUserBody,
    hash_service: HashService = Depends(),
    user_service: UserService = Depends(),
    session: Session = Depends(session_manager.use_session),
):
    """Authenticate a pre-existing user"""
    result = user_service.login_user(payload, hash_service, session)
    return handle_result(result)
