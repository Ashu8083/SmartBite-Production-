from pydantic import BaseModel

class PackageFoodAllergenschema(BaseModel):
    package_food_id : int
    allergen_id :int
    
class UpdatePackageFoodAllergen(BaseModel):
    package_food_id:int
    allergen_id : int 
    
class PackageFoodAllergenResponse(BaseModel):
    id : int
    package_food_id : int 
    allergen_id : int