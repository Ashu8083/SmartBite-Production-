from uuid import UUID
from fastapi import APIRouter
from app.schema.user_schema import UserCreateSchema
from app.service.user_service import UserService
from fastapi import Depends
from app.dependency.service_dependency import get_user_service

user_router=APIRouter(
    tags=["Users"]
)
 
@user_router.post("/users")
def create_user(user_schema:UserCreateSchema,user_service:UserService=Depends(get_user_service)):
    user=user_service.create_user(user_schema)
    return user

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
