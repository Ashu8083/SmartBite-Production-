from fastapi import FastAPI
from fastapi import Request, Response,APIRouter
from app.api.user_api import user_router
from app.api.user_device_api import user_device_router
from app.api.package_food_api import packaged_food_router
from app.api.package_food_allergen_api import package_food_allergen_router
from app.api.package_food_nutrition_api import package_food_nutrition_router
from app.api.nutrient_api import nutrient_router
from app.api.allergen_api import allergen_router
from app.api.brand_api import brand_router

from app.exception.exception_handler import app_exception_handler
from app.exception.app_exception import AppException


app = FastAPI()


app.include_router(user_router)
app.include_router(user_device_router)
app.include_router(packaged_food_router)
app.include_router(package_food_allergen_router)
app.include_router(package_food_nutrition_router)
app.include_router(nutrient_router)
app.include_router(allergen_router)
app.include_router(brand_router)


app.add_exception_handler(
    AppException,
    app_exception_handler
)


@app.get("/")
def read_hello():
    return {"message": "SmartBite!"}

