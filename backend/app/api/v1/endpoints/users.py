from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from db.session import get_db
from services import users_services
from services import utils


api_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@api_router.get("/")
def get_users(current_user = Depends(utils.get_current_user)):
    return "OK"


@api_router.get("/{user_id}")
def get_user_details(current_user = Depends(utils.get_current_user)):
    pass


@api_router.post("/")
def create_user(current_user = Depends(utils.get_current_user)):
    pass


@api_router.put("/{user_id}/")
def update_user(current_user = Depends(utils.get_current_user)):
    pass


@api_router.delete("/{user_id}")
def delete_user(current_user = Depends(utils.get_current_user)):
    pass


@api_router.post("/token/")
def login_user(form_data=Depends(OAuth2PasswordRequestForm), db=Depends(get_db)):
    user = users_services.authenticate_user(db, form_data.username, form_data.password)
    token = users_services.create_access_token(
        data={
            "sub": user.login
        }
    )
    return {"access_token": token, "token_type": "bearer"}
