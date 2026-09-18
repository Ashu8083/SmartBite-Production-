from fastapi import FastAPI
from fastapi import Request, Response,APIRouter
from app.api.package_food_api import packaged_food_router


app = FastAPI()

app.include_router(packaged_food_router)


@app.get("/hello")
def read_hello():
    return {"message": "SmartBite!"}
