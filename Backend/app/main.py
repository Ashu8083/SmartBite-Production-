from fastapi import FastAPI
from fastapi import Request, Response,APIRouter
from app.api.package_food_api import packaged_food_router
from app.api.package_food_allergen_api import package_food_allergen_router
from app.api.package_food_nutrition_api import package_food_nutrition_router


app = FastAPI()

app.include_router(packaged_food_router)
app.include_router(package_food_allergen_router)
app.include_router(package_food_nutrition_router)


@app.get("/hello")
def read_hello():
    return {"message": "SmartBite!"}
