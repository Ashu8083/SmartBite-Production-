from pydantic import BaseModel

class NutrientSchema(BaseModel):
    name:str
    category:str
    unit:str
    
class UpdateNutrient(BaseModel):
    name:str|None=None
    category:str|None=None
    unit:str|None=None
    
class NutrientResponse(BaseModel):
    id:int
    name:str
    category:str
    unit : str
    