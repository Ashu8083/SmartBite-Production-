from sqlalchemy.orm import Session
from Backend.app.repo.user_repo import Users
class UserRepository:
    def _init_(self,db:Session):
        self.db=db
    def create_user(self,user:Users):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user