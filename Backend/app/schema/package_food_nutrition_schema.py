from pydantic import BaseModel

class PackageFoodNutritionSchema(BaseModel):
    
    package_id:int
    nutrient_id:int
    amount:float
    
class UpdatePackageFoodNutrition(BaseModel):
    
    package_id:int | None=None
    nutrient_id:int | None=None
    amount:float  | None=None
    
class PackageFoodNutritionResponse(BaseModel):
    
    id:str
    package_id:int
    nutrient_id:int
    amount:float