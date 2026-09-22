from pydantic import BaseModel


class CreateAllergenSchema(BaseModel):
    name:str
    description:str

class AllergenResponse(BaseModel):
    name:str
    description:str

class AllergenUpdate(BaseModel):
    name:str 
    description:str | None = None