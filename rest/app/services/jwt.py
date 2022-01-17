from ..utils.config import config
from datetime import datetime, timedelta
import jwt


class JWTService:
    @staticmethod
    def generate_jwt(user_id: str):
        return jwt.encode(
            {
                "sub": user_id,
                "exp": datetime.utcnow() + timedelta(days=7),
                "iat": datetime.utcnow(),
            },
            config.secret_key,
            algorithm="HS256",
        ).decode(
            "UTF-8"
        )  # Wrong typehint in lib, it's actually a byte obj that's why decoding it

    @staticmethod
    def verify_and_return_id(encoded_jwt: str):
        return jwt.decode(encoded_jwt, config.secret_key, algorithms="HS256")["sub"]
