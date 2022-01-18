from fastapi import APIRouter, Depends, Response

from ..utils.auth import auth_required
from ..services.jwt import JWTService
from ..utils.service import handle_result
from ..schemas.users import CreateUserBody, LoginUserBody
from ..services.hash import HashService
from ..services.user import UserService
from ..models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/@me")
async def get_logged_in_user(
    user: User = Depends(auth_required),
):
    return user.get_json(include_email=True)


@router.post("/create")
async def create_user(
    payload: CreateUserBody,
    hash_service: HashService = Depends(),
    user_service: UserService = Depends(),
):
    """Register a user on the application"""
    hashed_pw = hash_service.get_password_hash(payload.password)
    result = user_service.create_user(payload, hashed_pw)

    return handle_result(result)


@router.post("/login")
async def login_user(
    payload: LoginUserBody,
    res: Response,
    hash_service: HashService = Depends(),
    user_service: UserService = Depends(),
    jwt_service: JWTService = Depends(),
):
    """Authenticate a pre-existing user"""
    result = user_service.login_user(payload, res, hash_service, jwt_service)
    return handle_result(result)
