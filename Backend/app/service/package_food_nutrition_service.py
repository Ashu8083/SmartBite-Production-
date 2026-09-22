from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.package_food_nutrition_repo import PackageFoodNutritionRepository
from app.schema.package_food_nutrition_schema import PackageFoodNutritionSchema,UpdatePackageFoodNutrition

class PackageFoodNutritionService:
    def __init__(self,package_food_nutrient:PackageFoodNutritionRepository):
        self.package_food_nutrient=package_food_nutrient
        
    def create_package_food_nutrition_service(self,create_package_food_nutrient:PackageFoodNutritionSchema):
        package_food_nutrient=self.package_food_nutrient.create_package_food_nutrition(create_package_food_nutrient)
        return package_food_nutrient
        
    def get_package_food_nutrition_by_id(self,package_food_nutrient_id:str):
        package_food_nutrient=self.package_food_nutrient.get_package_food_nutrition_by_nutrient_id(package_food_nutrient_id)
        if package_food_nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="package food nutrient not found"
            )
        return package_food_nutrient
    
    def get_package_food_nutrition_by_package_id(self,package_id:int):
        package_food_nutrient = self.package_food_nutrient.get_package_food_nutrition_by_package_id(package_id)
        if package_food_nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found in this package food"
            )
        return package_food_nutrient
            
    def get_package_food_nutrition_by_nutrient_id(self,nutrient_id:int):
        package_food_nutrient=self.package_food_nutrient.get_package_food_nutrition_by_nutrient_id(nutrient_id)
        if package_food_nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="package food not found for nutrient"
            )
        return package_food_nutrient
    
    def update_package_food_nutrient(self,package_food_nutrient_id:int,package_food_nutrient:UpdatePackageFoodNutrition):
        existing_nutrient=self.package_food_nutrient.update_package_food_nutrient(package_food_nutrient_id)
        if existing_nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="package food nutrient not found"
            )
            
        updated_nutrieent=self.package_food_nutrient.update_package_food_nutrient(package_food_nutrient_id,package_food_nutrient)
        return updated_nutrieent
    
    def delete_package_food_nutrient(self,package_food_nutrient_id:str):
        existing_nutrient=self.package_food_nutrient.get_package_food_nutrition_by_id(package_food_nutrient_id)
        if existing_nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="package food nutrient not found"
            )
            
        deleted_nutrient=self.package_food_nutrient.delete_package_food_nutrient(package_food_nutrient_id)
        return deleted_nutrient