from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db.session import get_db
from schemas.user import UpdateUser
from services import users_services
from services import utils
from schemas import user
from typing import List


api_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@api_router.get("/", response_model=List[user.User])
def get_users(db = Depends(get_db), current_user = Depends(utils.get_current_user)):
    return users_services.get_users(db)


@api_router.get("/{username}", response_model=user.User)
def get_user_details(username: str, db=Depends(get_db), current_user = Depends(utils.get_current_user)):
    user = users_services.get_user_details(db, username)
    if user is None:
        raise HTTPException(404, "User not found.")
    else:
        return user


@api_router.post("/")
def create_user(user_data: user.CreateUser, db=Depends(get_db), current_user = Depends(utils.get_current_user)):
    user_id = users_services.create_user(db, user_data)
    return user_id


@api_router.put("/")
def update_user(user_data: UpdateUser, db=Depends(get_db), current_user = Depends(utils.get_current_user)):
    user = users_services.update_user(db, user_data)
    if user is None:
        raise HTTPException(404, "User not found.")
    else:
        return user


@api_router.delete("/{user_id}")
def delete_user(user_id: int, db = Depends(get_db), current_user = Depends(utils.get_current_user)):
    if users_services.delete_user(db, user_id):
        return "OK"
    else:
        raise HTTPException(404, "User not found.")


@api_router.post("/token/")
def login_user(form_data=Depends(OAuth2PasswordRequestForm), db=Depends(get_db)):
    user = users_services.authenticate_user(db, form_data.username, form_data.password)
    token = users_services.create_access_token(
        data={
            "sub": user.login
        }
    )
    return {"access_token": token, "token_type": "bearer"}
