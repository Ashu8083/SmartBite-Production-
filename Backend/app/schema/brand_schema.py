from pydantic import BaseModel

class CreateBrandSchema(BaseModel):
    name:str
    logo_url:str
    website_url:str
    description:str
    country_name:str

class BrandResponse(BaseModel):
    name:str
    description:str
    country_name:str