import bcrypt


class HashService:
    salt = bcrypt.gensalt()

    def verify_password(self, plain_password: str, hashed_password: bytes):
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)

    def get_password_hash(self, plain_password: str):
        return bcrypt.hashpw(plain_password.encode("utf-8"), self.salt)
