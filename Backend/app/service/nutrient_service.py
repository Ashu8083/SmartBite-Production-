from fastapi import HTTPException
from app.repo.nutrient_repo import NutrientRepository
from app.schema.nutrient_schema import NutrientSchema,UpdateNutrient

class NutrientService:
    def __init__(self,nutrient:NutrientRepository):
        self.nutrient=nutrient
        
    def create_nutrient_service(self,create_nutrient:NutrientSchema):
        nutrient=self.nutrient.create_nutrient_repo(create_nutrient)
        return nutrient
    
    def get_nutrient_by_id(self,nutrient_id:int):
        nutrient=self.nutrient.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found"
            )
        return nutrient
            
    def get_nutrient_by_name(self,name:str):
        nutrient=self.nutrient.get_nutrient_by_name(name)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found in this name"
            )
        return nutrient
    
    def get_nutrient_by_category(self,category:str):
        nutrient=self.nutrient.get_nutrient_by_category(category)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found for this category"
            )
        return nutrient
    
    def update_nutrient(self,nutrient_id:int,nutrients:UpdateNutrient):
        nutrient=self.nutrient.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="not found"
            )
        update_nutrient=self.nutrient.update_nutrient(nutrient_id,nutrients)
        return update_nutrient
    
    def delete_nutrient(self,nutrient_id:int):
        nutrient=self.nutrient.get_nutrient_by_id(nutrient_id)
        if nutrient is None:
            raise HTTPException(
                status_code=404,
                detail="nutrient not found"
            )
            
        delete_nutrient=self.nutrient.delete_nutrient(nutrient_id)
        return delete_nutrient
        
            