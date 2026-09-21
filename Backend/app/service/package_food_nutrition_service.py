from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.package_food_nutrition_repo import PackageFoodNutritionRepository
from app.schema.package_food_nutrition_schema import PackageFoodNutritionSchema,UpdatePackageFoodNutrition

class PackageFoodNutritionService:
    def __init__(self,package_food_nutrient:PackageFoodNutritionRepository):
        self.package_food_nutrient=package_food_nutrient
        
    def create_package_food_nutrient_service(self,create_package_food_nutrient:PackageFoodNutritionSchema):
        package_food_nutrient=self.package_food_nutrient.create_package_food_nutrition(create_package_food_nutrient)
        return package_food_nutrient
        