from fastapi import APIRouter
from api.v1.endpoints import tasks, comments

api_router = APIRouter()
api_router.include_router(tasks.api_router)
api_router.include_router(comments.api_router)