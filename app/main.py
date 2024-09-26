from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.api_v1 import router as api_v1_router
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(api_v1_router)


@main_app.get("/")
async def read_root():
    return {"Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True, port=8888)
