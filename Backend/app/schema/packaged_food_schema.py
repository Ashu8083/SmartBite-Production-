from pydantic import BaseModel

class PackagedFoodSchema(BaseModel):
    brand_id : int
    barcode : str
    image_url : str |None=None
    price : float
    category_id:int
    allergens_id : int
    serving_size : float
    serving_unit : str | None=None
    quantity : float
    quantity_unit : str | None=None
    food_claims : str | None = None
    
class UpdatePackageFood(BaseModel):
    brand_id : int
    barcode : str
    image_url : str |None=None
    price : float
    category_id:int
    allergens_id : int
    serving_size : float
    serving_unit : str | None=None
    quantity : float
    quantity_unit : str | None=None
    food_claims : str | None = None
    
class PackageFoodResponse(BaseModel):
    brand_id : int
    barcode : str
    image_url : str |None=None
    price : float
    category_id:int
    allergens_id : int
    serving_size : float
    serving_unit : str | None=None
    quantity : float
    quantity_unit : str | None=None
    food_claims : str | None = None
    