from ..services.jwt import JWTService
from ..services.hash import HashService
from ..utils.service import ServiceResult
from ..schemas.users import CreateUserBody, LoginUserBody
from ..utils.database import DatabaseContext
from ..models import User
from fastapi import Response, Header
from fastapi.exceptions import HTTPException


class UserService(DatabaseContext):
    def get_user_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def create_user(
        self,
        payload: CreateUserBody,
        hashed_pw: bytes,
    ):
        result = ServiceResult()

        try:
            user_exists = bool(
                self.db.query(User).filter(User.email == payload.email).count() > 0
            )

            if user_exists:
                result.set_err_description("User already exists")
                raise HTTPException(status_code=429)

            new_user = User(
                username=payload.username, email=payload.email, password=hashed_pw
            )
            self.db.add(new_user)
            self.db.commit()

            result.set_value(new_user.get_json(include_email=True))
        except Exception as e:
            result.set_exception(e)

        return result

    def login_user(
        self,
        payload: LoginUserBody,
        resp: Response,
        hash_service: HashService,
        jwt_service: JWTService,
    ):
        result = ServiceResult()
        try:
            user = self.db.query(User).filter(User.email == payload.email).first()
            if not user:
                result.set_err_description("Invalid email/password")
                raise HTTPException(status_code=401)

            if not hash_service.verify_password(payload.password, user.password):
                result.set_err_description("Invalid email/password")
                raise HTTPException(status_code=401)

            access_token = jwt_service.generate_jwt(user.id)
            resp.set_cookie(key="token", value=access_token, httponly=True)

            result.set_value(user.get_json(include_email=True))
        except Exception as e:
            result.set_exception(e)

        return result
