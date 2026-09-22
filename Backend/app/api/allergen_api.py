from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse
from uuid import UUID

from app.dependency.service_dependency import get_allergen_service
from app.schema.allergen_schema import CreateAllergenSchema,AllergenResponse,AllergenUpdate
from app.service.allergen_service import AllergenService


allergen_router=APIRouter(
    prefix="/allergen",
    tags=["Allergen"]
)

@allergen_router.post("/create-allergen")
def create_allergen(allergen_schema:CreateAllergenSchema,allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.create_allergen(allergen_schema)
    allergen_response=AllergenResponse(
        name=allergen.name,
        description=allergen.description
    )

    return JSONResponse(
        status_code=200,
        content={
            "message":"allergen created successfully.",
            "status_code":200,
            "content":allergen_response.model_dump()
        }
    )

@allergen_router.get("/get-all-allergen")
def get_all_allergen(allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.get_all_allergen()
    return allergen

@allergen_router.get("/get-allergen-by-id")
def get_allergen_by_id(id:UUID,allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.get_allergen_by_id(id)
    return allergen

@allergen_router.get("/get-allergen-by-name")
def get_allergen_by_name(name:str,allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.get_allergen_by_name(name)
    return allergen

@allergen_router.put("/update-allergen")
def update_allergen(id:UUID,request:AllergenUpdate,allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.update_allergen(id,request)
    return allergen

@allergen_router.delete("/delete-allergen")
def delete_allergen(id:UUID,allergen_service:AllergenService=Depends(get_allergen_service)):
    allergen=allergen_service.delete_allergen(id)
    return allergen