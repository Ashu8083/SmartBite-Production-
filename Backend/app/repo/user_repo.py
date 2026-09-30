from sqlalchemy.orm import Session
from uuid import UUID
from app.model.user_model import Users
from app.schema.user_schema import UserUpdate

class UserRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_user(self,user:Users):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    def get_all_user(self):
        user=self.db.query(Users).filter().all()
        return user
    
    def get_user_by_id(self,user_id:UUID):
        user=self.db.query(Users).filter(Users.id==user_id).first()
        return user

    def get_user_by_email(self,email:str):
        user=self.db.query(Users).filter(Users.email==email).first()
        return user

    def get_user_by_username(self,username:str):
        user=self.db.query(Users).filter(Users.username==username).first()
        return user

    def update_user(self,users:Users,user_update:UserUpdate):
        for field , value in user_update.model_dump(exclude_unset=True).items():
            setattr(users,field,value)
        self.db.add(users)   
        self.db.flush()
        self.db.refresh(users)
        return users
    
    def delete_user(self,user:Users):
        self.db.delete(user)
        self.db.commit()
        return True
    
    