from sqlalchemy.orm import Session
from uuid import UUID
from Backend.app.model.user_model import Users
class UserRepository:
    def _init_(self,db:Session):
        self.db=db
    def create_user(self,user:Users):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    def get_user_by_id(self,user_id:UUID):
        user=self.db.query(Users).filter(Users.id==user_id).first()
        return user