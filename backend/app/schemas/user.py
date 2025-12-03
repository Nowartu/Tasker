from pydantic import BaseModel

class CreateUser(BaseModel):
    login: str
    password: str


class UpdateUser(CreateUser):
    pass


class User(BaseModel):
    id: int
    login: str