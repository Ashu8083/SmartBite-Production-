from pydantic import BaseModel

class PackagedFoodSchema(BaseModel):
    
    id : int
    name : str
    description : str
    price : float