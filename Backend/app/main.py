from fastapi import FastAPI
from fastapi import Request, Response,APIRouter
from app.api.user_api import user_router
from app.api.user_device_api import user_device_router
app = FastAPI()

app.include_router(user_router)
app.include_router(user_device_router)

@app.get("/")
def read_hello():
    return {"message": "SmartBite!"}
