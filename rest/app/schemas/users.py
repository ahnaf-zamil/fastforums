from pydantic import BaseModel, constr


class UserAuthBase(BaseModel):
    email: constr(
        regex=r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"  # noqa: F722
    )
    password: constr(min_length=8)


class LoginUserBody(UserAuthBase):
    pass


class CreateUserBody(UserAuthBase):
    username: constr(to_lower=True, min_length=3, max_length=30, strip_whitespace=True)
