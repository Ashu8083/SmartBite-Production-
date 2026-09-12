from fastapi import FastAPI
from fastapi import Request, Response,APIRouter
from app.api.user_api import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def read_hello():
    return {"message": "SmartBite!"}
