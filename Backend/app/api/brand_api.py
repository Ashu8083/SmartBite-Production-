from fastapi import APIRouter,Depends
from uuid import UUID
from fastapi.responses import JSONResponse

from app.schema.brand_schema import CreateBrandSchema,BrandResponse
from app.dependency.service_dependency import get_brand_service
from app.service.brand_service import BrandService

brand_router=APIRouter(
    prefix="/brands",
    tags=["Brands"]
)

@brand_router.post("/create-brand")
def create_brand(brand_schema:CreateBrandSchema,brand_service:BrandService=Depends(get_brand_service)):
    brand=brand_service.create_brand(brand_schema)
    brand_response=BrandResponse(
            name=brand.name,
            description=brand.description,
            country_name=brand.country_name

    )
    return  JSONResponse(
        status_code=200,
        content={
            "message":"Brand created successfully",
            "status_code":200,
            "content":brand_response.model_dump()
        }
    )

@brand_router.get("/get-all-brand")
def get_all_brand(brand_service:BrandService=Depends(get_brand_service)):
    brand=brand_service.get_all_brand()
    return brand

@brand_router.get("/get-brand-by-id")
def get_brand_by_id(id:int,brand_service:BrandService=Depends(get_brand_service)):
    brand=brand_service.get_brand_by_id(id)
    return brand

@brand_router.get("/get-brand-by-name")
def get_brand_by_name(name:str,brand_service:BrandService=Depends(get_brand_service)):
    brand=brand_service.get_brand_by_name(name)
    return brand

@brand_router.delete("/delete-brand")
def delete_brand(brand_id:int,brand_service:BrandService=Depends(get_brand_service)):
    brand=brand_service.delete_brand(brand_id)
    return brand