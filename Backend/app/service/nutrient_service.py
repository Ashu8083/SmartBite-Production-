from fastapi import HTTPException
from app.repo.nutrient_repo import NutrientRepository
from app.schema.nutrient_schema import NutrientSchema,UpdateNutrient

class NutrientService:
    def __init__(self,nutrient_repo:NutrientRepository):
        self.nutrient_repo=nutrient_repo
        
    def create_nutrient_service(self,create_nutrient:NutrientSchema):
        nutrient=self.nutrient_repo.create_nutrient_repo(create_nutrient)
        return nutrient
    
    def get_nutrient_by_id(self,nutrient_id:int):
        nutrient=self.nutrient_repo.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found"
            )
        return nutrient
    
    def update_nutrient(self,nutrient_id:int,nutrients:UpdateNutrient):
        nutrient=self.nutrient_repo.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="not found"
            )
        update_nutrient=self.nutrient_repo.update_nutrient(nutrient,nutrients)
        return update_nutrient
    
    def delete_nutrient(self,nutrient_id:int):
        nutrient=self.nutrient_repo.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found"
            )    
        delete_nutrient=self.nutrient_repo.delete_nutrient(nutrient_id)
        return delete_nutrient
        
            