from pydantic import BaseModel

class NutrientSchema:
    name:str
    category:str
    unit:str
    
class UpdateNutrient:
    name:str|None=None
    category:str|None=None
    unit:str|None=None
    
class NutrientResponse:
    id:int
    name:str
    category:str
    unit : str
    