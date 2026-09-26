from sqlalchemy.orm import Session
from app.model.food_category_model import FoodCategory
from app.schema.food_category_schema import FoodCategorySchema,UpadteFoodCategory

class FoodCategoryRepository:
    def __init__(self,db:Session):
        self.db=db
    
    def create_food_category_service(self,food_category:FoodCategorySchema):
        category=FoodCategory(
            name=food_category.name,
            description=food_category.description
        )
        
        self.db.add(category)
        self.db.flush()
        return category