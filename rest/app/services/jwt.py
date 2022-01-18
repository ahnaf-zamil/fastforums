from ..utils.config import config
from datetime import datetime, timedelta
import jwt


class JWTService:
    @staticmethod
    def generate_jwt(user_id: str):
        token = jwt.encode(
            {
                "sub": user_id,
                "exp": datetime.utcnow() + timedelta(days=7),
                "iat": datetime.utcnow(),
            },
            config.secret_key,
            algorithm="HS256",
        )
        # During tests, the token is string. While running server, its a bytes obj...... strange
        return token.decode("utf-8") if isinstance(token, bytes) else token

    @staticmethod
    def verify_and_return_id(encoded_jwt: str):
        return jwt.decode(encoded_jwt, config.secret_key, algorithms="HS256")["sub"]
