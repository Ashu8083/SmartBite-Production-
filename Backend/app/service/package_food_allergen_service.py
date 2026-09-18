from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.packaged_food_allergen_repo import PackageFoodAllergenRepository
from app.schema.packaged_food_allergen_schema import PackageFoodAllergenSchema,UpdatePackageFoodAllergen

class PackageFoodAllergenService:
    def __init__(self,package_food_allergen:PackageFoodAllergenRepository):
        self.package_food_allergen=package_food_allergen
        
        
    def create_package_food_allergen_service(self,create_package_food_allergen:PackageFoodAllergenSchema):
        package_food_allergen=self.package_food_allergen.create_packagefood_allergen(create_package_food_allergen)
        return package_food_allergen
        
    def get_package_food_allergen_by_id(self,package_food_allergen_id:int):
        package_food_allergen=self.package_food_allergen.get_package_food_allergen_by_id(package_food_allergen_id)
        if package_food_allergen is None:
            raise HTTPException(
                status_code=404,
                detail="package food allergen not found"
            )
            
        return package_food_allergen