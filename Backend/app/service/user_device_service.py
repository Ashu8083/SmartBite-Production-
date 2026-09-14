from app.repo.user_device_repo import UserDeviceRepo
from app.schema.userDevice_schema import UserDeviceCreate
from app.model.user_device_model import UserDevice
from uuid import UUID
from datetime import datetime
class UserDeviceService:
    def __init__(self,user_device_repository:UserDeviceRepo):
        self.user_device_repo:UserDeviceRepo=user_device_repository

    def create_user_device(self,user_device_schema:UserDeviceCreate):

        user_device = UserDevice(
            user_id = user_device_schema.user_id,
            device_id = user_device_schema.device_id,
            device_type = user_device_schema.device_type,
            firebase_fcm_token = user_device_schema.firebase_fcm_token,
            last_login=datetime.utcnow()
        )
        return self.user_device_repo.create_user_device(user_device)
    
    def get_user_device_by_id(self,id:UUID):
        user_device=self.user_device_repo.get_user_device_by_id(id)
        return self.user_device_repo.get_user_device_by_id(user_device)