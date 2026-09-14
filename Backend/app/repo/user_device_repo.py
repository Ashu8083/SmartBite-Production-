from sqlalchemy.orm import Session
from app.model.user_device_model import UserDevice
from uuid import UUID

class UserDeviceRepo:
    def __init__(self,db:Session):
        self.db=db

    def create_user_device(self,user_device:UserDevice):
        self.db.add(user_device)
        self.db.commit()
        self.db.refresh(user_device)
        return user_device 
    
    def get_user_device_by_id(self,id:UUID):
        user_device=self.db.query(UserDevice).filter(UserDevice.id==id).first()
        return user_device
    