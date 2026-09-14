from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.repo.user_device_repo import UserDeviceRepo
from app.service.user_service import UserService 
from app.service.user_device_service import UserDeviceService
from app.core.database import get_db


def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_user_device_service(db=Depends(get_db)):
    user_device_repository = UserDeviceRepo(db)
    user_service = UserDeviceService(user_device_repository)
    return user_service
    