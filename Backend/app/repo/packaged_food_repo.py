from sqlalchemy.orm import Session
from Backend.app.model.user_model import Users

class PackagedFoodRepository:
    def __init__(self,db:Session):
        self.db=db