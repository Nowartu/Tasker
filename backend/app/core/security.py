from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from core.config import ROOT_PATH

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{ROOT_PATH}/v1/users/token/")


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)