from sqlalchemy.orm import Session
from Backend.app.model.user_device_model import UserDevice
from uuid import UUID

class UserDeviceRepo:
    def __init__(self,db:Session):
        self.db=db

    def create_user_device(self,user_device:UserDevice):
        self.db.add(user_device)
        self.db.commit()
        self.db.refresh(user_device)
        return user_device 
    
    def get_userdevice_by_id(self,id:UUID):
        return self.db.query(UserDevice).filter(UserDevice.id==id).first()
    