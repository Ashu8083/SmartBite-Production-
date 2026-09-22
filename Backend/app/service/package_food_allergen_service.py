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
    
    def get_package_food_allergen_by_package_food_id(self,package_food_id:int):
        package_food_allergen=self.package_food_allergen.get_package_food_allergen_by_package_food_id(package_food_id)
        if package_food_allergen is None:
            raise HTTPException(
                status_code=404,
                detail="allergen are not found by this package food id"
            )
            
        return package_food_allergen
    
    def get_package_food_allergen_by_allergen_id(self,allergen_id:int):
        package_food_allergen=self.package_food_allergen.get_package_food_allergen_by_allergen_id(allergen_id)
        if package_food_allergen is None:
            raise HTTPException(
                status_code=404,
                detail="package food not found bu allergen id"
            )
        return package_food_allergen
    
    def update_package_food_allergen(self,package_food_allergen_id:int,package_food_allergen:UpdatePackageFoodAllergen):
        exisiting_allergen=self.package_food_allergen.get_package_food_allergen_by_id(package_food_allergen_id)
        if exisiting_allergen is None:
            raise HTTPException(
                status_code=404,
                detail="package food allergen not found"
            )
        update_allergen=self.package_food_allergen.update_package_food_allergen(package_food_allergen_id,package_food_allergen)
        return update_allergen
    
    def delete_package_food_allergen(self,package_food_allergen_id:int):
        exsiting_allergen=self.package_food_allergen.get_package_food_allergen_by_id(package_food_allergen_id)
        if exsiting_allergen is None:
            raise HTTPException(
                status_code=404,
                detail="package food allergen not found"
            )
        delete_allergen=self.package_food_allergen.delete_package_food_allergen(package_food_allergen_id)
        return delete_allergen