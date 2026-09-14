from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schema.packaged_food_schema import PackagedFoodSchema, UpdatePackageFood,PackageFoodResponse
from app.service.package_food_service import PackagedFoodService
from app.dependency.service_dependency import get_package_food_service

packaged_food_router=APIRouter(prefix="/packaged-food",tags=["Packaged Food"])

@packaged_food_router.post("/create",response_model=PackageFoodResponse)
def create_packaged_food(create_packaged_food:PackagedFoodSchema,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.create_packaged_food_service(create_packaged_food)

@packaged_food_router.get("/get-packaged-food-by-id",response_model=PackageFoodResponse)
def get_packaged_food_by_id(package_food_id:int,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.get_package_food_by_id(package_food_id)

@packaged_food_router.get("/get-packaged-food-by-barcode",response_model=PackageFoodResponse)
def get_packaged_food_by_barcode(barcode:str,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.get_package_food_by_barcode(barcode)

@packaged_food_router.get("/get-packaged-food-by-brand-id",response_model=PackageFoodResponse)
def get_packaged_food_by_brand_id(brand_id:int,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.get_package_food_by_barand_id(brand_id)

@packaged_food_router.get("/get-packaged-food-by-category-id",response_model=PackageFoodResponse)
def get_packaged_food_by_category_id(category_id:int,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.get_package_food_by_category_id(category_id)


@packaged_food_router.put("/update-packaged-food",response_model=PackageFoodResponse)
def update_packaged_food(package_food_id:int,package_food:UpdatePackageFood,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.update_package_food(package_food_id,package_food)

@packaged_food_router.delete("/delete-packaged-food",response_model=PackageFoodResponse)
def delete_packaged_food(package_food_id:int,service:PackagedFoodService=Depends(get_package_food_service)):
    return service.delete_package_food(package_food_id)