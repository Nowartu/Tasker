from pydantic import BaseModel

class CreateUser(BaseModel):
    login: str
    password: str


class UpdateUser(BaseModel):
    password: str


class User(BaseModel):
    id: int
    login: str