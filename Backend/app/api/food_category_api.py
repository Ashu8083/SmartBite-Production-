from fastapi import APIRouter,Depends
from app.schema.food_category_schema import FoodCategorySchema,UpadteFoodCategory,FoodCategoryResponse
from app.service.food_category_service import FoodCategoryService
from app.dependency.service_dependency import get_food_category_service

food_category_router=APIRouter(prefix="/food-category",tags=["food category"])

@food_category_router.post("/create",response_model=FoodCategoryResponse)
def create_food_category(create_food_category:FoodCategorySchema,service:FoodCategoryService=Depends(get_food_category_service)):
    return service.create_food_category_service(create_food_category)

@food_category_router.get("/get-food-category-by-id",response_model=FoodCategoryResponse)
def get_food_category_by_id(category_id:int,service:FoodCategoryService=Depends(get_food_category_service)):
    return service.get_food_category_by_id(category_id)

@food_category_router.get("/get-food-category-by-name",response_model=FoodCategoryResponse)
def get_food_category_by_name(name:str,service:FoodCategoryService=Depends(get_food_category_service)):
    return service.get_food_category_by_name(name)

@food_category_router.get("/get-all-food-category",response_model=list[FoodCategoryResponse])
def get_all_food_category(service:FoodCategoryService=Depends(get_food_category_service)):
    return service.get_all_food_category

@food_category_router.put("/update-food-category",response_model=FoodCategoryResponse)
def update_food_category(category_id:int,food_category:UpadteFoodCategory,service:FoodCategoryService=Depends(get_food_category_service)):
    return service.update_food_category(category_id,food_category)

@food_category_router.delete("/delete-food-category",response_model=FoodCategoryResponse)
def delete_food_category(category_id:int,service:FoodCategoryService=Depends(get_food_category_service)):
    return service.delete_food_category(category_id)