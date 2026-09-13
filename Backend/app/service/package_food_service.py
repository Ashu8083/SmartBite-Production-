from sqlalchemy.orm import Session
from fastapi import HTTPException
from Backend.app.repo.packaged_food_repo import PackagedFoodRepository
from Backend.app.schema.packaged_food_schema import PackagedFoodSchema,UpdatePackageFood

class PackagedFoodService:
    def __init__(self,packaged_food:PackagedFoodRepository):
        self.packaged_food = packaged_food
        
    def create_packaged_food_service(self,create_packaged_food:PackagedFoodSchema,id:int):
        existing_food=self.packaged_food.get_package_food_barcode(create_packaged_food.barcode)
        if existing_food:
            raise HTTPException(
                status_code=400,
                detail="packaged food with this barcode already exists"
            )
        packaged_food=self.packaged_food.create_packaged_food_repo(create_packaged_food,id)
        return packaged_food
    
    def get_package_food_by_id(self,package_food_id:int):
        packaged_food=self.packaged_food.get_package_food_by_id(package_food_id)
        if packaged_food is None:
            raise HTTPException(
                status_code=404,
                detail="package food not found"
            )
        return packaged_food
    
    def get_package_food_by_barcode(self,barcode:str):
        packaged_food=self.packaged_food.get_package_food_barcode(barcode)
        if packaged_food is None:
            raise HTTPException(
                status_code=404,
                detail="package food not found"
            )
        return packaged_food
    
    def get_package_food_by_barand_id(self,brand_id:int):
        packaged_food=self.packaged_food.get_package_food_by_brand_id(brand_id)
        if packaged_food is None:
            raise HTTPException(
                status_code=404,
                detail="package food not found for this brand"
            )
        return packaged_food
    
    
