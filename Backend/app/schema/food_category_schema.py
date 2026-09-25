from pydantic import BaseModel

class FoodCategorySchema(BaseModel):
    name:str
    description:str | None=None
    
class UpadteFoodCategory(BaseModel):
    name:str | None=None
    description: str | None=None
    
class FoodCategoryResponse(BaseModel):
    id:int
    name:str
    description: str | None=None
    