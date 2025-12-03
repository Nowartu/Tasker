from fastapi import FastAPI
from api.v1.router import api_router as api_router_v1
import uvicorn
from contextlib import asynccontextmanager
from core.config import ROOT_PATH
from db.init_db import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_database()
    yield

app = FastAPI(root_path=ROOT_PATH, lifespan=lifespan)

app.include_router(api_router_v1, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run(app)