from uuid import UUID
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse

from app.schema.user_schema import UserCreateSchema
from app.service.user_service import UserService
from app.dependency.service_dependency import get_user_service
from app.schema.user_schema import UserUpdate,UserResponse




user_router=APIRouter(
    tags=["Users"]
)
 
@user_router.post("/users",response_model=UserResponse)
def create_user(user_schema:UserCreateSchema,user_service:UserService=Depends(get_user_service)):
    user=user_service.create_user(user_schema)
    user_response=UserResponse(
        username=user.username,
        email=user.email,
        gender=user.gender,
        
       
    )
    return JSONResponse(
        status_code=200,
        content={
            "message":"User created successfully",
            "status_code":200,
            "content":user_response.model_dump()
        }

    )

@user_router.get("/get-all-user")
def get_all_user(user_service:UserService=Depends(get_user_service)):
    user=user_service.get_all_user()
    return user

@user_router.get("/get-user-by-id")
def get_user_by_id(user_id:UUID,user_service:UserService=Depends(get_user_service)):
    user=user_service.get_user_by_id(user_id)
    return user

@user_router.get("/get-user-by-email")
def get_user_by_email(email:str,user_service:UserService=Depends(get_user_service)):
    user=user_service.get_user_by_email(email)
    return user

@user_router.put("/update-user")
def update_user(user_id:UUID,request:UserUpdate,user_service:UserService=Depends(get_user_service)):
    user=user_service.update_user(user_id,request)
    return user

@user_router.delete("/delete-user")
def delete_user(user_id:UUID,user_service:UserService=Depends(get_user_service)):
    user=user_service.delete_user(user_id)
    return user
