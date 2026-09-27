from fastapi import APIRouter,Depends
from app.schema.nutrient_schema import NutrientSchema,UpdateNutrient,NutrientResponse
from app.service.nutrient_service import NutrientService
from app.dependency.service_dependency import get_nutrient_service

nutrient_router=APIRouter(prefix="/nutrient",tags=["nutrient"])

@nutrient_router.post("/create",response_model=NutrientResponse)
def create_nutrient(create_nutrient:NutrientSchema,service:NutrientService=Depends(get_nutrient_service)):
    return service.create_nutrient_service(create_nutrient)

@nutrient_router.get("/get-nutrient-by-id",response_model=NutrientResponse)
def get_nutrient_by_id(nutrient_id:int,service:NutrientService=Depends(get_nutrient_service)):
    return service.get_nutrient_by_id(nutrient_id)

@nutrient_router.get("/get-nutrient-by-name",response_model=NutrientResponse)
def get_nutrient_by_name(name:str,service:NutrientService=Depends(get_nutrient_service)):
    return service.get_nutrient_by_name(name)

@nutrient_router.get("/get-nutrient-by-category",response_model=NutrientResponse)
def get_nutrient_by_category(category:str,service:NutrientService=Depends(get_nutrient_service)):
    return service.get_nutrient_by_category(category)

@nutrient_router.put("update-nutrient",response_model=NutrientResponse)
def update_nutrient(nutrient_id:int,nutrient:UpdateNutrient,service:NutrientService=Depends(get_nutrient_service)):
    return service.update_nutrient(nutrient_id,nutrient)

@nutrient_router.delete("delete-nutrient",response_model=NutrientResponse)
def delete_nutrient(nutrient_id:int,service:NutrientService=Depends(get_nutrient_service)):
    return service.delete_nutrient(nutrient_id)